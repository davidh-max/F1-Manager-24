"""Validación, calendario y resumen de la trayectoria. Solo librería estándar."""
import argparse
import csv
from datetime import date, timedelta
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def calendar(year, confirmed=False):
    block = load(f'temporadas/{year}/calendario.json')
    if confirmed and block['metadatos']['estado'] != 'CONFIRMADO':
        raise ValueError('El calendario de la partida sigue pendiente de confirmar')
    return block


def calendar_info(day, year, count=5, ready=None, deadline=None):
    block = calendar(year)
    events = block['datos']
    previous = [gp for gp in events if gp['carrera'] < day.isoformat()]
    current = next((gp for gp in events if gp['inicio'] <= day.isoformat() <= gp['carrera']), None)
    future = [gp for gp in events if gp['inicio'] > day.isoformat()]
    following = future[0] if future else None
    # Se informa del hueco de agosto entre citas, sin inferir cierres de fábrica.
    summer = [dict(desde=(date.fromisoformat(a['carrera']) + timedelta(days=1)).isoformat(),
                   hasta=(date.fromisoformat(b['inicio']) - timedelta(days=1)).isoformat())
              for a, b in zip(events, events[1:])
              if a['carrera'][5:7] in ('07', '08') and b['inicio'][5:7] == '08'
              and (date.fromisoformat(b['inicio']) - date.fromisoformat(a['carrera'])).days >= 21]
    result = dict(origen=block['metadatos']['estado'], anterior=previous[-1] if previous else None,
                  actual=current, siguiente=following, proximos=future[:count], pausa_verano=summer,
                  dias_hasta_siguiente=(date.fromisoformat(following['inicio']) - day).days if following else None)
    if ready:
        result['primer_gp_elegible'] = next((gp for gp in events
                                            if gp['inicio'] >= max(day, ready).isoformat()), None)
    if deadline:
        result['carreras_antes_del_vencimiento'] = [gp for gp in events
                                                    if day.isoformat() <= gp['carrera'] < deadline.isoformat()]
    return result


def rows(path):
    with path.open(encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def duplicates(records, keys):
    values = [tuple(record[key] for key in keys) for record in records]
    return len(values) != len(set(values))


def validate():
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    schema = load('esquemas/datos.json')
    sources = {item['id'] for item in load('fuentes/registro.json')}
    partida = load('equipo/partida.json')['datos']
    day = partida['fecha_partida']
    if day:
        date.fromisoformat(day)

    def metadata(block, place):
        m = block['metadatos']
        state = m['estado']
        check(state in schema['estados'], f'{place}: estado inválido')
        for key in ('fecha_partida', 'fecha_registro'):
            if m[key]:
                date.fromisoformat(m[key])
        if state != 'DESCONOCIDO':
            check(bool(m['fecha_registro'] and m['fuente'] and m['fuente'].split('#')[0] in sources),
                  f'{place}: falta fecha de registro o fuente registrada')
        if day and m['fecha_partida'] and state == 'CONFIRMADO':
            check(m['fecha_partida'] <= day, f'{place}: observación posterior a la fecha de partida')

    for folder in ('equipo', 'circuitos', 'temporadas', 'rivales', 'desarrollo', 'finanzas', 'instalaciones'):
        for path in (ROOT / folder).rglob('*.json'):
            metadata(load(path), path.relative_to(ROOT))
    for path in ROOT.rglob('*.jsonl'):
        if '.git' in path.parts:
            continue
        records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        check(not duplicates(records, ['id']), f'{path.name}: ID histórico repetido')
        for record in records:
            metadata(record, record['id'])
            check(record['metadatos']['estado'] != 'DESCONOCIDO', f"{record['id']}: evento sin origen")

    for path in (ROOT / 'temporadas').glob('*/calendario.json'):
        block = load(path)
        events = block['datos']
        year = block['temporada']
        check(not duplicates(events, ['id']), f'{year}: GP duplicado')
        check([gp['ronda'] for gp in events] == list(range(1, len(events) + 1)), f'{year}: rondas discontinuas')
        if year == 2024:
            check(len(events) == 24, '2024: el calendario debe tener 24 rondas')
        last = date.min
        for gp in events:
            begin, race = (date.fromisoformat(gp[k]) for k in ('inicio', 'carrera'))
            check(last < begin <= race and race.year == year and type(gp['sprint']) is bool,
                  f"{gp['id']}: fechas o Sprint inválidos")
            last = race
            check((ROOT / f"circuitos/{gp['circuito']}/ficha.json").is_file(), f"{gp['id']}: falta circuito")
            record = load(path.parent / f"grandes_premios/{gp['id']}/evento.json")
            check((record['id'], record['circuito'], record['temporada']) == (gp['id'], gp['circuito'], year),
                  f"{gp['id']}: ficha de evento incompatible")
        for filename, key in [('clasificacion_pilotos.csv', 'piloto_id'), ('clasificacion_constructores.csv', 'equipo_id')]:
            standings = rows(path.parent / filename)
            snapshot = ['fecha_partida', 'evento', 'sesion']
            check(not duplicates(standings, snapshot + [key]), f'{year}/{filename}: competidor duplicado')
            check(not duplicates([r for r in standings if r['posicion']], snapshot + ['posicion']),
                  f'{year}/{filename}: posición duplicada')
        check(not duplicates(rows(path.parent / 'resultados.csv'), ['evento', 'sesion', 'piloto_id']),
              f'{year}: resultado duplicado')

    inventory = {piece['id']: piece for piece in load('desarrollo/inventario/piezas.json')['datos']}
    assigned = set()
    units = schema['unidades_coche']
    pilots = {path.stem: load(path)['datos'] for path in (ROOT / 'equipo/pilotos').glob('*.json')}
    for path in (ROOT / 'equipo/coches').glob('*.json'):
        data = load(path)['datos']
        pilot = data['piloto']
        if pilot:
            check(pilot in pilots and pilot not in assigned and pilots[pilot]['coche'] == path.stem,
                  f'{path.stem}: asignación de piloto incompatible')
            assigned.add(pilot)
        check(set(data['atributos']) == set(units) == set(data['posiciones_20_coches']),
              f'{path.stem}: atributos incompletos o unidad ajena al esquema')
        for key, value in data['atributos'].items():
            check(value is None or type(value) in (int, float), f'{path.stem}: valor incompatible para {key}')
            if value is not None and units.get(key) == '%' and type(value) in (int, float):
                check(0 <= value <= 100, f'{path.stem}: porcentaje fuera de rango en {key}')
        for position in data['posiciones_20_coches'].values():
            check(position is None or (type(position) is int and 1 <= position <= 20), f'{path.stem}: ranking inválido')
        for piece in data['piezas_instaladas']:
            check(piece in inventory, f'{path.stem}: pieza instalada ausente del inventario: {piece}')
    for path in (ROOT / 'equipo').rglob('*.json'):
        contract = load(path)['datos'].get('contrato') or {}
        start, end = contract.get('inicio'), contract.get('vencimiento')
        if start and end:
            check(date.fromisoformat(start) <= date.fromisoformat(end), f'{path.stem}: contrato incompatible')
        if path.parent.name == 'pilotos':
            pilot = pilots[path.stem]
            check(not pilot['coche'] or path.stem in assigned, f'{path.stem}: coche no recíproco')
            engineer = pilot['ingeniero']
            if engineer:
                engineer_path = ROOT / f'equipo/personal/{engineer}.json'
                check(engineer_path.is_file() and load(engineer_path)['datos'].get('piloto') == path.stem,
                      f'{path.stem}: ingeniero no recíproco')

    for group, name in [('diseno', 'proyectos'), ('investigacion', 'proyectos'), ('fabricacion', 'lotes')]:
        projects = load(f'desarrollo/{group}/{name}.json')['datos']
        check(not duplicates(projects, ['id']), f'{group}: ID de proyecto duplicado')
        for project in projects:
            start = project.get('inicio_real')
            check(project['estado'] in schema['estados_proyecto'], f"{project['id']}: estado de proyecto inválido")
            if start:
                for key in ('fin_estimado', 'fin_real'):
                    if project.get(key):
                        check(date.fromisoformat(start) <= date.fromisoformat(project[key]),
                              f"{project['id']}: {key} anterior al inicio")

    for period in load('desarrollo/atr/periodos.json')['datos']:
        start, end = period.get('inicio'), period.get('fin')
        if start and end:
            check(date.fromisoformat(start) <= date.fromisoformat(end), f"{period['id']}: fechas ATR incoherentes")
        renewal = period.get('renovacion_calculada')
        if renewal:
            observed = date.fromisoformat(period['metadatos']['fecha_partida'])
            days = period['dias_hasta_renovacion_observados']
            check(days >= 0 and date.fromisoformat(renewal) == observed + timedelta(days=days),
                  f"{period['id']}: renovación ATR incoherente")
        for resource in ('cfd_mau', 'tunel_h'):
            amounts = period[resource]
            initial, used, left, reserved = (amounts.get(k) for k in ('inicial', 'consumido', 'restante', 'reservado'))
            check(all(x is None or x >= 0 for x in (initial, used, left, reserved)), f"{period['id']}: ATR negativo")
            if None not in (initial, used, left):
                check(abs(initial - used - left) < 1e-6, f"{period['id']}: ATR no cuadra")
            if None not in (initial, left):
                check(left <= initial, f"{period['id']}: saldo ATR superior a la asignación")
            if None not in (left, reserved):
                check(reserved <= left, f"{period['id']}: reserva ATR superior al saldo")

    finance = load('finanzas/estado.json')['datos']
    limit, spent, remaining = (finance[k] for k in ('limite_usd', 'consumido_limite_usd', 'restante_limite_usd'))
    if None not in (limit, spent, remaining):
        check(limit >= 0 and spent >= 0 and limit - spent == remaining, 'Finanzas: el límite presupuestario no cuadra')
    movements = rows(ROOT / 'finanzas/movimientos.csv')
    check(not duplicates(movements, ['id']), 'Finanzas: movimiento duplicado')
    for movement in movements:
        check(bool(movement['id'] and movement['importe_usd']), 'Finanzas: movimiento sin ID o importe')
        if movement['importe_usd']:
            int(movement['importe_usd'])

    return errors


def display(value):
    if value is None:
        return 'Pendiente'
    if isinstance(value, list):
        return ', '.join(str(x) for x in value) or 'Ninguno registrado'
    return str(value)


def summary():
    current_state = load('equipo/partida.json')
    partida = current_state['datos']
    finance = load('finanzas/estado.json')['datos']
    season, day = partida['temporada'], partida['fecha_partida']
    gp = partida['gran_premio_confirmado']
    day_matches_observation = day and current_state['metadatos']['fecha_partida'] == day
    upcoming = partida.get('proximos_gp_confirmados') if day_matches_observation else None
    remaining = partida.get('dias_hasta_gp_observados') if gp and day_matches_observation else None
    if season and (ROOT / f'temporadas/{season}/calendario.json').is_file():
        schedule = calendar(season)
        names = {event['id']: event['nombre'] for event in schedule['datos']}
        if remaining is None and day and schedule['metadatos']['estado'] == 'CONFIRMADO':
            info = calendar_info(date.fromisoformat(day), season)
            event = info['actual'] or info['siguiente']
            if event and gp in (None, event['id'], event['nombre']):
                gp = event['id']
                remaining = 0 if info['actual'] else info['dias_hasta_siguiente']
        gp = names.get(gp, gp)
        upcoming = [names.get(event_id, event_id) for event_id in upcoming] if upcoming else None

    fields = [('Temporada', season), ('Fecha de partida', day), ('Gran Premio actual o próximo', gp),
              ('Días hasta el inicio', remaining), ('Próximos Grandes Premios comunicados', upcoming),
              ('Presupuesto disponible (USD)', finance['saldo_usd']),
              ('Límite restante (USD)', finance['restante_limite_usd'])]
    if season and (ROOT / f'temporadas/{season}').is_dir():
        for title, filename, key, target in [
            ('Constructores', 'clasificacion_constructores.csv', 'equipo_id', 'aston_martin'),
            ('Fernando Alonso', 'clasificacion_pilotos.csv', 'piloto_id', 'fernando_alonso'),
            ('Lance Stroll', 'clasificacion_pilotos.csv', 'piloto_id', 'lance_stroll'),
        ]:
            matches = [r for r in rows(ROOT / f'temporadas/{season}/{filename}') if r[key] == target and r['estado'] == 'CONFIRMADO']
            latest_row = max(reversed(matches), key=lambda row: row['fecha_partida'], default=None)
            standing = latest_row['posicion'] if latest_row else None
            if standing and latest_row['puntos']:
                standing = f"{standing}.º · {latest_row['puntos']} puntos"
            fields.append((title, standing or None))
    else:
        fields.extend((title, None) for title in ('Constructores', 'Fernando Alonso', 'Lance Stroll'))

    competitions = load('equipo/boxes/estado.json')['datos']['competiciones']
    dhl = next((entry for entry in reversed(competitions) if entry.get('id') == 'dhl_fastest_pit_stop'
                and entry.get('fecha_partida') == day and entry.get('temporada') == season), None)
    if dhl:
        fields.append(('DHL de paradas en boxes', f"{dhl['posicion']}.º · {dhl['puntos']} puntos"))

    contracts = []
    for path in sorted((ROOT / 'equipo/coches').glob('*.json')):
        data = load(path)['datos']
        pilot = load(f"equipo/pilotos/{data['piloto']}.json")['datos'] if data['piloto'] else {}
        fields.extend([(f'{path.stem} · rendimiento general', data['rendimiento_general']),
                       (f'{path.stem} · piloto', data['piloto']),
                       (f'{path.stem} · ingeniero', pilot.get('ingeniero')),
                       (f'{path.stem} · mentalidad', pilot.get('mentalidad')),
                       (f'{path.stem} · confianza por sesión', pilot.get('confianza_por_sesion') or None)])
    for folder in ('pilotos', 'personal'):
        for path in (ROOT / f'equipo/{folder}').glob('*.json'):
            end = load(path)['datos']['contrato']['vencimiento']
            if end and (day is None or end >= day):
                contracts.append((end, path.stem))
    for folder, filename in [('diseno', 'proyectos'), ('investigacion', 'proyectos'), ('fabricacion', 'lotes')]:
        block = load(f'desarrollo/{folder}/{filename}.json')
        active = [p['id'] for p in block['datos'] if p['estado'] in ('iniciado', 'en_curso', 'en_fabricacion')]
        fields.append((f'Proyectos activos · {folder}', active if block['metadatos']['estado'] != 'DESCONOCIDO' else None))
    construction = [p.stem for p in sorted((ROOT / 'instalaciones').rglob('*.json'))
                    if load(p)['datos']['estado_proyecto'] in ('en_construccion', 'en_mejora')]
    fields.append(('Instalaciones en obra', construction or None))
    fields.append(('Próximos vencimientos contractuales', [f'{person} ({end})' for end, person in sorted(contracts)] or None))
    pending = [p.get('version') or 'Diseño por identificar'
               for p in load('desarrollo/diseno/proyectos.json')['datos'] if p['estado'] == 'pendiente_fabricacion']
    if pending:
        fields.append(('Diseños pendientes de fabricar', pending))

    periods = load('desarrollo/atr/periodos.json')['datos']
    end = min((p['fin'] for p in periods if day and p.get('inicio') and p.get('fin')
               and p['inicio'] <= day <= p['fin']), default=None)
    observation = next((p for p in reversed(periods)
                        if day and p.get('metadatos', {}).get('fecha_partida') == day), None)
    fields.append(('Próximo vencimiento ATR', end))
    if observation:
        renewal = observation.get('renovacion_calculada')
        if renewal:
            fields.append(('Renovación ATR calculada', renewal))
        fields.extend([('CFD disponible (MAU)', observation['cfd_mau']['restante']),
                       ('Túnel de viento disponible (h)', observation['tunel_h']['restante'])])
    fields.extend([('Principales problemas', partida['problemas'] or None), ('Decisiones pendientes', partida['decisiones_pendientes'] or None)])

    latest = []
    for directory in ('equipo', 'desarrollo', 'instalaciones', 'finanzas', 'temporadas', 'rivales', 'circuitos'):
        for path in (ROOT / directory).rglob('*.json'):
            metadata = load(path)['metadatos']
            if metadata['estado'] == 'CONFIRMADO' and metadata['fecha_registro']:
                latest.append(metadata['fecha_registro'])
    fields.append(('Última actualización confirmada del estado', max(latest, default=None)))
    lines = ['# Estado actual de Aston Martin Aramco', '',
             'Generado con `python herramientas/gestion.py resumen`.', '',
             'La trayectoria comenzó en 2024. Las observaciones iniciales se conservan en `historial/eventos.jsonl`.', '',
             *[f'- **{label}** · {display(value)}' for label, value in fields], '',
             '## Datos prioritarios para sincronizar', '']
    unresolved = []
    if not day:
        unresolved.append('Fecha dentro del juego')
    if not gp:
        unresolved.append('Gran Premio actual o próximo')
    if finance['saldo_usd'] is None:
        unresolved.append('Presupuesto disponible')
    if finance['restante_limite_usd'] is None:
        unresolved.append('Límite presupuestario restante')
    for title, value in fields:
        if value is None and (title in ('Constructores', 'Lance Stroll', 'Fernando Alonso') or 'rendimiento general' in title):
            unresolved.append(title)
    for folder, filename in [('diseno', 'proyectos'), ('investigacion', 'proyectos'), ('fabricacion', 'lotes')]:
        if load(f'desarrollo/{folder}/{filename}.json')['metadatos']['estado'] == 'DESCONOCIDO':
            unresolved.append(f'Proyectos activos de {folder}')
    lines += [f'- {item}.' for item in unresolved] or ['Los datos prioritarios ya se han incorporado.']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validar')
    sub.add_parser('resumen')
    dates = sub.add_parser('calendario')
    dates.add_argument('fecha', type=date.fromisoformat)
    dates.add_argument('--temporada', type=int)
    dates.add_argument('--cantidad', type=int, default=5)
    dates.add_argument('--fin-diseno', type=date.fromisoformat)
    dates.add_argument('--dias-fabricacion', type=int)
    dates.add_argument('--dias-montaje', type=int, default=0)
    dates.add_argument('--vencimiento', type=date.fromisoformat)
    args = parser.parse_args()
    try:
        if args.command == 'resumen':
            (ROOT / 'ESTADO_ACTUAL.md').write_text(summary(), encoding='utf-8')
        elif args.command == 'validar':
            errors = validate()
            if summary() != (ROOT / 'ESTADO_ACTUAL.md').read_text(encoding='utf-8'):
                errors.append('ESTADO_ACTUAL.md desactualizado. Ejecuta el comando resumen.')
            if errors:
                parser.exit(1, '\n'.join(errors) + '\n')
            print('Validación correcta')
        else:
            if any(x is not None and x < 0 for x in (args.cantidad, args.dias_fabricacion, args.dias_montaje)):
                parser.error('Las cantidades y duraciones deben ser no negativas')
            if (args.fin_diseno is None) != (args.dias_fabricacion is None):
                parser.error('Indica juntos --fin-diseno y --dias-fabricacion')
            if args.dias_montaje and args.fin_diseno is None:
                parser.error('--dias-montaje requiere fechas de diseño y fabricación')
            ready = (args.fin_diseno + timedelta(days=args.dias_fabricacion + args.dias_montaje)
                     if args.fin_diseno else None)
            info = calendar_info(args.fecha, args.temporada or args.fecha.year, args.cantidad, ready, args.vencimiento)
            if ready:
                info['fecha_disponibilidad_estimada'] = ready.isoformat()
            print(json.dumps(info, indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f'Error de datos: {error}\n')


if __name__ == '__main__':
    main()
