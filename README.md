# Aston Martin Aramco en F1 Manager 2024

Registro de la trayectoria de Aston Martin desde 2024. Abre [Estado actual](ESTADO_ACTUAL.md) para consultar la situación de la partida y los datos pendientes.

| Ruta | Contenido |
| --- | --- |
| `equipo/` | Partida, coches, pilotos, técnicos y boxes |
| `desarrollo/` | Diseño, investigación, fabricación, inventario, ATR y normativa |
| `instalaciones/` y `finanzas/` | Instalaciones, presupuesto, límite y movimientos |
| `temporadas/` | Calendario, clasificaciones, resultados y fichas por GP |
| `circuitos/` y `rivales/` | Referencias por circuito y seguimiento de rivales |
| `historial/` y `fuentes/` | Observaciones archivadas y procedencia |
| `esquemas/` y `herramientas/` | Diccionario de datos, validación y cálculos |
| `informes/` | Análisis y decisiones documentados |

## Uso

Desde la raíz del repositorio, con Python 3.10 o posterior y su biblioteca estándar:

```bash
python herramientas/gestion.py resumen
python herramientas/gestion.py validar
python herramientas/gestion.py calendario 2024-02-18 --cantidad 3
python herramientas/gestion.py calendario 2024-02-18 --fin-diseno 2024-03-03 --dias-fabricacion 4 --dias-montaje 1 --vencimiento 2024-04-01
```

Las fechas de ejemplo son ilustrativas. El calendario de 2024 utiliza las 24 citas y 6 Sprint de la referencia aportada. Los días hasta el siguiente GP se cuentan hasta que comienza el fin de semana. La disponibilidad de una pieza suma días naturales de fabricación y montaje al fin del diseño, y exige que la pieza esté disponible al inicio del GP. Ajusta el cálculo con las fechas observadas del juego y los huecos reales de fabricación. El cálculo de pausa de verano indica el hueco entre rondas. Para otra temporada, da de alta su calendario y sus fichas sin reutilizar fechas reales automáticamente.

## Registrar una actualización

1. Añade la evidencia al registro de fuentes. Anota la fecha de partida si aparece y la fecha real de incorporación.
2. Guarda en el historial el cambio con un ID único y actualiza la ficha correspondiente. Usa los ejemplos del [diccionario](esquemas/DICCIONARIO.md).
3. Reconcilia clasificaciones y movimientos con los registros existentes. Las primeras observaciones y las hipótesis del encargo se encuentran en `historial/eventos.jsonl`.
4. Ejecuta los comandos de resumen y validación y conserva los cambios en Git.
