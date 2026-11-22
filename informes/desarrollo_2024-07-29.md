# Opciones de desarrollo del 29 de julio de 2024

Las seis simulaciones corresponden al coche 1 con 0 MAU y 0 h de túnel asignados. Son simulaciones individuales de la pantalla de diseño. Los deltas porcentuales están en puntos porcentuales.

| Diseño | Curvas lentas (G) | Medias (G) | Rápidas (G) | Otro cambio destacado en el coche 1 |
| --- | ---: | ---: | ---: | --- |
| Fondo plano | +0,007 | −0,006 | +0,003 | +1,25 pp de tolerancia al aire sucio |
| Suspensión | +0,005 | +0,003 | +0,004 | +2,75 pp de preservación de neumáticos |
| Pontones | +0,002 | +0,005 | +0,009 | +2,82 pp de refrigeración |
| Alerón trasero | −0,001 | −0,001 | +0,004 | +0,15 km/h y +3,26 pp de DRS, con +1,2 kg |
| Alerón delantero | +0,014 | +0,003 | −0,004 | +1,51 pp de tolerancia al aire sucio, con +0,8 kg |
| Chasis | 0 | +0,003 | +0,007 | +0,34 pp de DRS y +1,73 pp de refrigeración |

## Decisión de desarrollo

- **Zandvoort.** Comprobar primero el coste y el plazo de fabricación de los pontones **AST24 P.-5**. Ya están diseñados y quedan 25 días. En su propia pantalla de fabricación muestran **+0,008 G en curvas medias y +0,013 G en rápidas**, ambos atributos cruciales. A cambio ceden **0,07 km/h** y **3,55 pp de refrigeración**. Hay cero unidades y el conocimiento figura en 0 %. Comparar con la vista de fabricación del alerón trasero A. t.-4 antes de comprometer el saldo de 2.625.344 USD.
- **Desarrollo posterior.** Probar el chasis con ATR si interesa ganar en curvas medias y rápidas sin añadir peso visible en la simulación base. El alerón trasero tiene el mayor salto de DRS y velocidad para evaluar con vistas a Monza. El delantero destaca en curvas lentas para Bakú. La suspensión es la candidata para preservación si los datos de tandas muestran que la degradación limita la estrategia.
- **ATR.** Quedan 2,5 de 5,4 MAU de CFD y 33 de 72 h de túnel. El siguiente periodo comienza en 35 días según el mensaje, lo que corresponde al 2 de septiembre al contar desde el 29 de julio. Comparar el diseño ajustado con y sin esos recursos, junto con coste y fecha de entrega, antes de repartirlos.

## Actualización con el segundo informe técnico

1. **Antes de destinar presupuesto a mejoras**, verificar la indicación de chasis fallido en el AST24 Ch.-3 de Stroll y localizar un repuesto apto. El total de seis chasis de todas las versiones no confirma cuántos repuestos están utilizables. Los dos alerones traseros A. t.-3 instalados figuran con riesgo alto.
2. **Piezas listas para fabricar.** AST24 P.-5 y AST24 A. t.-4 tienen cero unidades. El efecto específico de A. t.-4 y el coste y plazo de fabricación de ambas piezas siguen pendientes. Los deltas de fabricación de P.-5 conservan la referencia de ese menú. Las previsualizaciones de nuevo diseño corresponden a otras configuraciones.
3. **Diseño nuevo.** Chasis, pontones, fondo plano y suspensión cuestan 1.000.000 USD y tardan 31 días cada uno. Cada alerón cuesta 1.800.000 USD y tarda 41 días. Diseñar las seis piezas suma 7.600.000 USD antes de fabricación. Empezando el 29 de julio, las fechas de fin de diseño serían el 29 de agosto y el 8 de septiembre, respectivamente. Con los plazos mostrados, un diseño nuevo no llega a Zandvoort y los de 31 días terminarían un día antes de empezar Monza, con fabricación aún por contar.
4. **Conciliación.** El puesto de peso del coche 1 se conserva en 18.º para la pantalla de diseño, frente al 17.º del informe. La base de fabricación de P.-5 conserva su propio 19.º. Los valores de piezas instaladas se guardan con la procedencia del informe y las simulaciones conservan las bases de sus capturas.

[Simulaciones](../desarrollo/diseno/simulaciones.json) · [Proyectos](../desarrollo/diseno/proyectos.json) · [ATR](../desarrollo/atr/periodos.json)
