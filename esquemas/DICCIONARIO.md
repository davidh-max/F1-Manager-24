# Diccionario de datos

## Procedencia y fechas

Los JSON de dominio tienen una raíz con `metadatos` y `datos`. Cada ficha identifica su entidad mediante `id` y, cuando convenga, `nombre` y `temporada`. Para observaciones incorporadas en fechas distintas dentro de una misma ficha, conserva metadatos por bloque o por registro y archiva cada observación. El valor `null` es desconocido. Las colecciones vacías con metadatos DESCONOCIDO están pendientes de sincronización. Una colección confirmada y vacía indica ausencia observada.

| Campo | Convención |
| --- | --- |
| `metadatos.estado` | CONFIRMADO (juego o usuario), CALCULADO, ESTIMADO, REFERENCIA EXTERNA, HIPÓTESIS o DESCONOCIDO |
| `fecha_partida` | Fecha de observación en el juego en formato AAAA-MM-DD o null |
| `fecha_registro` | Día real de incorporación, en el mismo formato |
| `temporada` | Año de la trayectoria que corresponde al dato |
| `fuente` | ID de `fuentes/registro.json` con sección opcional tras `#` |
| `historial/eventos.jsonl` | Un evento por línea con `id`, `entidad`, `metadatos` y `datos`. Añade correcciones con su propio ID, indicando qué evento rectifican |
| Antigüedad | Fecha actual de la partida menos fecha de observación. Deja pendiente si falta cualquiera |

## Entidades, unidades y claves

- Usa identificadores persistentes en minúsculas con guiones bajos. El GP se identifica por temporada y `NN_circuito`. Para Aston Martin usa `aston_martin` en clasificaciones.
- Lee las unidades de los diez atributos en `datos.json`. Los porcentajes están en escala 0 a 100 y las diferencias absolutas entre dos porcentajes se expresan en puntos porcentuales. Los puestos de atributo son de 1 a 20. Las métricas relativas de escuderías y las clasificaciones deportivas tienen sus propios campos.
- Vincula coche y piloto por ID en ambos sentidos. Vincula piloto e ingeniero en ambas fichas. Indexa preparación y confianza por GP y sesión cuando corresponda. Contratos con inicio, vencimiento, dinero en USD y negociaciones separadas.
- Unidades generales: segundos en `_s`, kilómetros en `_km`, días naturales en `_dias`, dólares enteros en `_usd`, porcentaje en `_pct`, puntos porcentuales en `_pp`. Tipifica toda degradación con su unidad observada.
- Para importancia por circuito usa CRUCIAL, RECOMENDADO, SIN MARCA ESPECIAL o DESCONOCIDO. Conserva en el GP los compuestos `C1` a `C5` cuando figuren, ritmo medio, vueltas competitivas, vida útil prevista, degradación y unidad, condiciones, temperaturas y evidencia. Para estrategias registra origen, secuencia, ventanas, duración de tandas y tiempo total previsto.
- Cada fila de clasificación representa un competidor por fecha, evento y sesión. Cada resultado tiene clave evento, sesión y piloto. Mantén resultados Sprint y carrera diferenciados y conserva las instantáneas previas. No sumes puntos automáticamente sin reconciliar resultados, puntuación de temporada y penalizaciones.
- Identifica cada movimiento con un ID estable. Usa importe con signo (ingreso positivo, gasto negativo) y registra el saldo posterior si figura. El coste consumido del límite y el saldo disponible son magnitudes independientes. La diferencia entre dos saldos es una observación hasta conciliar su causa.
- Para proyecciones conserva fecha de corte, partidas de ingresos y gastos, supuestos, saldo proyectado y margen. La fórmula básica suma al saldo actual los ingresos previstos y resta gastos pendientes. Separa pagos ya incluidos en el saldo.

## Registros de desarrollo

| Colección | Campos por registro |
| --- | --- |
| Diseño | `id`, temporada, pieza, versión y versión anterior, propuesta, `inicio_real`, objetivo, preajuste, deslizadores, ATR, ingenieros, tipo, costes previsto y confirmado, duración, `fin_estimado`, `fin_real`, `estado`, impacto previsto en pieza y en cada coche, peso, durabilidad, ranking, alternativas y primer GP elegible |
| Investigación | `id`, temporada objetivo, cambio normativo, atributos y piezas afectados, recursos, ingenieros, costes, `inicio_real`, `fin_estimado`, `fin_real`, `estado`, conocimiento previsto y pérdida a compensar |
| Fabricación | `id`, diseño asociado, pieza, cantidad, método, coste, `inicio_real`, `fin_estimado`, `fin_real`, `estado` |
| Inventario | `id` de versión de pieza, categoría, lote, fabricadas, disponibles, instaladas por coche, usadas, retiradas, repuestos y vida restante |
| ATR | `id`, `inicio`, `fin`, proyectos, siguiente renovación, `cfd_mau` y `tunel_h` con claves `inicial`, `consumido`, `restante`, `reservado` |
| Normativa | `id`, temporada objetivo, atributos o piezas, impacto, valores y evidencia |

Usa los estados de proyecto definidos en `datos.json`. En el historial separa una simulación de diseño, el diseño ejecutado, la fabricación y el montaje. El inventario referencia versiones, y cada coche lista los IDs de sus piezas instaladas.
