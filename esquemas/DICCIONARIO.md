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
| `equipo/partida.json` | `gran_premio_confirmado` acepta el ID del evento. `dias_hasta_gp_observados` es la cuenta que muestra el juego en la fecha de observación. `proximos_gp_confirmados` conserva los IDs en el orden comunicado para esa fecha |
| Antigüedad | Fecha actual de la partida menos fecha de observación. Deja pendiente si falta cualquiera |

## Evidencias audiovisuales

- `fuentes/registro.json` identifica cada captura por circuito, tipo de panel y lote. El GP referencia esos IDs desde `datos.evidencias`. En la ficha del circuito, `datos.mapa` referencia la captura del mapa y `datos.secciones_por_velocidad.fuente` la del gráfico de velocidades.
- Cuando el original esté disponible, guárdalo bajo `circuitos/<id>/evidencias/` con un nombre que incluya la temporada y el panel. Usa una ruta relativa al repositorio en `archivo`. Si la captura solo está visible en el chat, conserva su referencia y deja `archivo` en `null` hasta que se pueda archivar.
- Para el vídeo registra el nombre del clip y el minuto y segundo de cada pantalla útil. Un clip pendiente de descarga queda registrado como evidencia pendiente y carece de fecha de consulta hasta que pueda revisarse.

## Entidades, unidades y claves

- Usa identificadores persistentes en minúsculas con guiones bajos. El GP se identifica por temporada y `NN_circuito`. Para Aston Martin usa `aston_martin` en clasificaciones.
- Lee las unidades de los diez atributos en `datos.json`. Los porcentajes están en escala 0 a 100 y las diferencias absolutas entre dos porcentajes se expresan en puntos porcentuales. Los puestos de atributo son de 1 a 20. Las métricas relativas de escuderías y las clasificaciones deportivas tienen sus propios campos.
- Vincula coche y piloto por ID en ambos sentidos. Vincula piloto e ingeniero en ambas fichas. Indexa preparación y confianza por GP y sesión cuando corresponda. Contratos con inicio, vencimiento, dinero en USD y negociaciones separadas.
- Unidades generales: segundos en `_s`, kilómetros en `_km`, días naturales en `_dias`, dólares enteros en `_usd`, porcentaje en `_pct`, puntos porcentuales en `_pp`. Tipifica toda degradación con su unidad observada.
- Para importancia por circuito usa CRUCIAL, RECOMENDADO, SIN MARCA ESPECIAL o DESCONOCIDO. Conserva en el GP los compuestos `C1` a `C5` cuando figuren, ritmo medio, vueltas competitivas, vida útil prevista, degradación y unidad, condiciones, temperaturas y evidencia. Para estrategias registra origen, secuencia, ventanas, duración de tandas y tiempo total previsto.
- Cada fila de clasificación representa un competidor por fecha, evento y sesión. Cada resultado tiene clave evento, sesión y piloto. Mantén resultados Sprint y carrera diferenciados y conserva las instantáneas previas. No sumes puntos automáticamente sin reconciliar resultados, puntuación de temporada y penalizaciones.
- En `resultados.csv`, los tiempos de carrera y de Q1, Q2 y Q3 están en milisegundos. Guarda los doblados en `vueltas_perdidas` y deja el tiempo de diferencia vacío. Un DNF puede tener puesto vacío y conservar los puntos mostrados. Las filas de clasificación y carrera tienen su propia sesión. Un evento puede enlazar el CSV desde `datos.resultados` e indicar el alcance de la captura.
- En una captura de campeonato, `puntos_ultimo_movimiento_mostrado` y `puestos_ganados_mostrados` reproducen los cambios visibles. Un guion se guarda como campo vacío. Las cifras del campeonato DHL se guardan en `clasificacion_dhl_boxes.json` y tienen su propio sistema de puntos.
- Identifica cada movimiento con un ID estable. Usa importe con signo (ingreso positivo, gasto negativo) y registra el saldo posterior si figura. El coste consumido del límite y el saldo disponible son magnitudes independientes. La diferencia entre dos saldos es una observación hasta conciliar su causa.
- Para proyecciones conserva fecha de corte, partidas de ingresos y gastos, supuestos, saldo proyectado y margen. La fórmula básica suma al saldo actual los ingresos previstos y resta gastos pendientes. Separa pagos ya incluidos en el saldo.

## Datos de las pestañas de circuitos

- Usa `metadatos_por_bloque` para conservar la procedencia de cada pestaña. Una transcripción aportada puede incluir marca de tiempo sin que se haya revisado el vídeo directamente.
- Guarda el tiempo medio de vuelta y los récords mostrados por el juego en milisegundos (`_ms`). Los récords históricos mostrados no son resultados de la trayectoria.
- `perdida_boxes_sc_vsc_s` conserva una única estimación cuando el juego agrupa ambas neutralizaciones. Las cifras de `histograma_salidas_por_temporada` cuentan temporadas en cada intervalo de salidas, separadas en SC y VSC.
- En el GP, `inventario_neumaticos` registra los juegos indicados en la previa. `compuestos` guarda el intervalo competitivo y la degradación en segundos por vuelta. Las ventanas de estrategias previstas son intervalos inclusivos de números de vuelta. Los datos de la previa quedan separados de las estrategias ejecutadas.
- `posicion_en_parrilla_mostrada_en_previa` es el indicador de la pestaña de atributos por circuito. El resultado de clasificación y la parrilla efectiva se registran con su propia evidencia. La probabilidad de lluvia y la fecha de disponibilidad de la previsión se registran aunque el pronóstico esté pendiente.

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

### Comparativas de diseño y fabricación

- `desarrollo/diseno/simulaciones.json` registra las previsualizaciones junto con el coche, la base mostrada y el ATR asignado en la pantalla. Los deltas en atributos porcentuales se expresan en puntos porcentuales. `puestos_ganados_mostrados` conserva el signo del juego: positivo es una mejora de ranking. Un cambio de ranking puede aparecer con un delta absoluto que se redondea a cero en pantalla.
- El diseño terminado pendiente de fabricar se registra en `desarrollo/diseno/proyectos.json`. Su `comparacion_fabricacion` conserva la base y los deltas de esa pantalla, que pueden diferir de la base de diseño. Los proyectos confirmados individualmente pueden coexistir con una lista de proyectos activos aún desconocida.
- En ATR, `renovacion_calculada` suma los días observados a la fecha de partida. `inicio` y `fin` quedan pendientes hasta confirmarlos. Saldo disponible, consumo y reserva se registran por separado.
