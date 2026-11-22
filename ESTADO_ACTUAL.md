# Estado actual de Aston Martin Aramco

Resumen base del proyecto. Campos operativos actualizados a mano con capturas del 26-08-2024; el script de regeneración integral no se ha ejecutado en este turno.

La trayectoria comenzó en 2024. Las observaciones iniciales se conservan en `historial/eventos.jsonl`.

- **Temporada** · 2024
- **Fecha de partida** · 2024-08-26
- **Gran Premio actual o próximo** · Italia (Monza)
- **Días hasta el inicio** · 4
- **Próximos Grandes Premios comunicados** · Italia, Azerbaiyán, Singapur, Estados Unidos (Austin), México, São Paulo
- **Presupuesto disponible (USD)** · 202015 (calculado 26-08-2024 tras gasto confirmado de 1000000 en diseño suspensión)
- **Límite restante (USD)** · Pendiente de verificar tras diseño suspensión (preconfirmación se mostraron 40836004)
- **Constructores** · 4.º · 236 puntos
- **Fernando Alonso** · 4.º · 187 puntos
- **Lance Stroll** · 9.º · 49 puntos
- **DHL de paradas en boxes** · 7.º · 85 puntos
- **coche_1 · rendimiento general** · 8
- **coche_1 · piloto** · lance_stroll
- **coche_1 · ingeniero** · ben_michell
- **coche_1 · mentalidad** · neutral
- **coche_1 · confianza por sesión** · Pendiente
- **coche_2 · rendimiento general** · 7
- **coche_2 · piloto** · fernando_alonso
- **coche_2 · ingeniero** · peter_bonnington
- **coche_2 · mentalidad** · positiva
- **coche_2 · confianza por sesión** · Pendiente
- **Proyectos activos · diseno** · Suspensión iniciada el 26-08-2024: estrategia normal, 3 ingenieros, 1000000 USD abonados, final previsto 21-09-2024. Alerón trasero previo completado 21 agosto, pendiente fabricar. Las otras simulaciones NO ejecutadas.
- **Proyectos activos · investigacion** · Pendiente
- **Proyectos activos · fabricacion** · Pontones AST24 P.-6 ×2 apresurada: 1 unidad instalada en coche 2 al 26 agosto; la segunda prevista 31 agosto para coche 1 (pendiente). Órdenes antiguas A. t.-4, P.-5 y Ch.-3 con fin previsto vencido; estado actual pendiente de verificar
- **Instalaciones en obra** · Centro turístico nivel 3 → 4 (fin previsto 2024-08-15); sala de recuerdos en mejora (fin previsto 2024-08-18, comercialidad +20→+30, mentalidad +4→+6, coste estimado 700000 USD, diferencia de saldo sin conciliar 30000 USD)
- **Próximos vencimientos contractuales** · ben_michell (2024-12-31), fernando_alonso (2024-12-31), jefe_aerodinamica (2024-12-31), jefe_tecnico (2024-12-31), lance_stroll (2024-12-31), director_deportivo (2027-12-31)
- **Diseños pendientes de fabricar** · Nuevo alerón trasero completado el 21 agosto, pendiente de fabricación tras GP
- **Próximo vencimiento ATR** · Pendiente
- **Renovación ATR calculada** · 2024-09-02
- **CFD disponible (MAU)** · No observado el 26 agosto (último dato 2,5 MAU del 29 julio)
- **Túnel de viento disponible (h)** · 7/72 antes del encargo; 7 h configuradas en el diseño de suspensión, saldo final ATR pendiente de verificación.
- **Principales problemas** · El segundo informe muestra el chasis AST24 Ch.-3 de Stroll como fallido. Verificar su estado y buscar un repuesto apto., Helipuerto deteriorado: 68 % de conservación y 80 % de eficacia.
- **Decisiones pendientes** · Ahorrar y financiar fabricación del alerón trasero previamente diseñado; seguir suspensión en desarrollo hasta el 21 septiembre y planificar fabricación posterior. No asignar al coche mejoras de suspensión todavía. Pontones posteriores a P.-6 descartados para el foco probado.
- **Última actualización confirmada del estado** · 2026-11-22

## Datos prioritarios para sincronizar

- Límite presupuestario restante.
- Proyectos activos de investigacion.

## Evaluación técnica vigente · 26 agosto 2024

- Capturas nuevas: 6 simulaciones de diseño sin CFD ni túnel, coche 1 base de 23 agosto. Datos íntegros en `desarrollo/diseno/simulaciones.json` (IDs `simulacion_*_2024_08_26_sin_atr`).
- **Prioridad de evaluación**: pontones, seguida de suspensión y chasis, condicionada a repetir comparativa tras instalar los pontones P.-6 ya fabricándose. Las ganancias mostradas no son incrementos adicionales garantizados frente a P.-6.
- **Horizonte**: Austin, México y São Paulo; México e Interlagos carecen de prioridades de atributos confirmadas en sus fichas del juego. La aptitud se considera estimación hasta nuevas capturas de los circuitos.
- **Saldo observado 26 agosto**: 1.202.015 USD, sin gasto de nuevo diseño confirmado. El límite presupuestario restante y los recursos ATR son observaciones anteriores, no valores verificados al 26 agosto.

## Prueba real sobre coche 2 con pontones P.-6 montados · 26 agosto

- Coche 2: **321,92 km/h**, aceleración **1,855 G**, **2,593 / 3,626 / 4,904 G** en curvas lenta/media/rápida, DRS **62,70 %**, neumáticos **63,23 %**, refrigeración **56,96 %**, peso extra **17,6 kg**. Confirmados por captura del mismo menú; registro en `equipo/coches/coche_2.json`.
- Simulación de siguientes pontones desde P.-6: **+0,10 km/h**, **-0,006 G** curvas medias, **-0,016 G** curvas rápidas, **+4,04 pp** refrigeración, **+1,0 kg** peso; pieza con **-7,51 pp** flujo central. NO ejecutar este diseño.
- **Recomendación actualizada**: explorar suspensión sobre coche 2, priorizando paso por curvas; chasis como alternativa. Ambas simulaciones del 26 agosto mostradas previamente para coche 1 eran con una base diferente, por lo que sus ganancias no están verificadas tras P.-6.
- **Presupuesto**: 1.202.015 USD (26 agosto). Antes de iniciar un diseño, revisar disponibilidad para fabricar el alerón trasero cuyo diseño está terminado y evaluar coste completo, sin atribuir gastos todavía.

## Suspensión: proyecto de diseño iniciado y pagado · 26 agosto 2024

- **Confirmado por usuario tras pulsar Confirmar**: coste 1.000.000 USD, 3 ingenieros, estrategia normal, duración 26 días, fin estimado 21-09-2024. Saldo posterior **202.015 USD** (= 1.202.015 - 1.000.000). El alerón trasero diseñado anteriormente continúa pendiente de fabricar por falta de financiación confirmada.
- Configuración desde **Equilibrado** con **un clic más en velocidad media y alta**; el resto sin cambios. Proyecciones **coche 2**: +0,03 km/h punta; +0,001 G lenta; +0,002 G media; +0,003 G rápida; +0,63 pp preservación neumáticos. Son previsiones, **no instaladas**.
- En pantalla de diseño aparecen **0,4 MAU CFD y 7 h túnel** configurados; consumo final ATR pendiente de verificar en panel de recursos tras confirmar. Fecha de renovación calculada: 02-09-2024.
- Fuente: `confirmacion_diseno_suspension_2024_08_26`; registro de movimiento `gasto_diseno_suspension_2024_08_26`; proyecto `diseno_suspension_2024_08_26`.
