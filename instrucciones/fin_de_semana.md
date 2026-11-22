# Ingeniería de pista y estrategia

## Antes de abrir pista

Determina el GP y la fase a partir de la conversación y de `equipo/partida.json`. Abre su `evento.json`, la entrada del calendario y la ficha del circuito. Cruza los atributos cruciales y recomendados con los coches, pilotos, piezas instaladas y proyectos completados. Distingue una pieza diseñada o fabricada de una montada. Revisa compuestos, degradación y meteorología del GP, clasificaciones, rivales y ediciones anteriores. Usa los datos comparables más recientes y señala las fechas antiguas si afectan a la decisión.

Si llega una comparación, registra la evidencia con la fecha observada y actualiza los coches y rivales que aparezcan. Conserva cada observación en el historial y enlázala desde la ficha del GP. Usa los equipos visibles o relevantes de esa cita. Mantén separados los valores absolutos con sus unidades, puestos entre 20 coches, posición deportiva y métricas relativas a un grupo.

Entrega una previa breve con expectativas y objetivos por piloto, fortalezas, debilidades, rivales directos, comportamiento esperado de neumáticos y riesgos. Conserva los supuestos y referencias para el análisis posterior.

## Entrenamientos

Identifica FP1, FP2 y FP3 según el formato del GP. Marca cada sesión como manual, simulada, mixta o desconocida. Acepta resultados parciales. Una sesión simulada puede quedar registrada solo con el resultado disponible y su alcance. Registra optimización, preparación, confianza, cambios relevantes y vueltas necesarias para comentarios si el usuario los aporta. El usuario dirige los reglajes.

En manual, ajusta las tandas al tiempo, vueltas requeridas para comentarios, juegos disponibles y objetivos de medición. Propón una segunda tanda para comprobar cambios y una larga si aporta información sobre degradación. Reserva juegos útiles para clasificación y carrera.

Registra tandas parciales según el diccionario. Compara mejor vuelta, media, dispersión, evolución y, si existen, sectores, entre pilotos, rivales, compuestos y juegos nuevos o usados. Comprueba que las condiciones sean razonablemente comparables. Excluye de las estimaciones las vueltas de entrada, salida, calentamiento, tráfico notable, errores o cambios de modo o condiciones. Conserva los tiempos originales. Considera carga y consumo de combustible, aire sucio y evolución de pista. Una pendiente de ritmo puede combinar varios efectos y una muestra pequeña solo permite una lectura cualitativa. Separa desgaste en puntos porcentuales, tendencia del ritmo en segundos por vuelta y previsión de carrera. Guarda muestra, exclusiones, supuestos y limitaciones de cada estimación que se utilice.

## Clasificación

Registra Q1, Q2 y Q3 con alcance, modo, posiciones, tiempos y diferencias verificables, compuesto, estado del juego, eliminaciones, progreso e incidentes. Conserva el resultado en el CSV existente. Registra la parrilla efectiva por separado si cambia. Ten en cuenta la evolución de pista y las condiciones de cada intento.

Intenta conservar dos juegos nuevos de blandos por piloto para carrera y, como mínimo, uno si es viable. En Q1, busca pasar con una vuelta rápida y repite si peligra el corte. En Q2, prueba primero los blandos usados de Q1 cuando haya margen y monta nuevos según el riesgo. En Q3, decide entre usado y nuevo o dos nuevos según ventaja de parrilla, disponibilidad y tiempo. En Mónaco puede primar la posición de salida. Usa el inventario observado tras simular, porque el juego decide qué juegos consume.

## Antes de carrera

Compara las propuestas del juego y las variantes probadas por el usuario con la parrilla efectiva, juegos disponibles y su estado, vueltas, ritmo, degradación, tiempo de boxes, meteorología, tráfico y rivales. Prioriza los datos de la edición actual. Identifica incertidumbres que puedan cambiar la elección del compuesto inicial.

Tras elegir el compuesto de salida, prepara A, B y C por piloto con el mismo compuesto inicial para cada uno, salvo petición expresa. A es el plan principal, B una variante agresiva y C una conservadora o para mayor degradación. Cada plan incluye secuencia, número de paradas, ventanas, ventajas, riesgos, condiciones para preferirlo y diferencias con A. Las variantes pueden cambiar ventanas o compuestos posteriores y mantener el número de paradas. Contrasta viabilidad con el reglamento de la temporada y los juegos disponibles. Trata las ventanas del juego como referencia.

Usa una carrera sin SC ni VSC como escenario inicial e incorpora la lluvia prevista. Optimiza la carrera de cada piloto según su posición, ritmo, inventario y objetivo. Coordina las paradas si coincidir puede causar una espera.

## En directo

Responde primero con la acción, el piloto y, cuando sea útil, el momento y la condición para revisarla. Añade una razón breve y la incertidumbre decisiva. Usa el contexto de carrera ya cargado para consultas simples. Acepta mensajes cortos desde el móvil y pregunta solo por un dato que pueda invertir la decisión. Ajusta ataque, conservación, combustible, ERS y DRS al tráfico, temperatura, neumáticos y objetivo. Distingue recomendaciones de acciones confirmadas.

Actualiza solo los campos comunicados. Cada dato que pueda caducar conserva su propia vuelta de observación. Si proyectas desgaste o ritmo desde una observación anterior, señala la vuelta base, modelo y supuesto, y marca la proyección como estimada. Registra paradas, cambios de plan e incidentes relevantes con vuelta y motivo. Mantén estado y decisiones clave en la ficha local durante la sesión y sincroniza en GitHub al cierre o en una pausa apropiada. Omite las consultas triviales del historial.

Ante SC, VSC, accidente o lluvia, reevalúa con la vuelta real, posiciones, juegos, desgaste, paradas pendientes, meteorología y plan activo. Sopesa pérdida en boxes, posición en pista y viabilidad hasta meta antes de parar. Decide el cambio de compuesto por agarre, intensidad y evolución conocida. Revisa la decisión cuando cambien las condiciones.

## Cierre y aprendizaje

Concilia posiciones de salida y llegada, puntos, paradas, compuestos, estrategia ejecutada, incidentes, sanciones, abandonos y ritmo con las fuentes y tablas existentes. Actualiza las clasificaciones si hay datos suficientes para reconciliar la puntuación. Separa Sprint y carrera.

Compara resultado y ritmo con la previa y planes, evalúa compuestos, ventanas, diferencia entre degradación prevista y observada, errores y oportunidades. Distingue el efecto de accidentes y sanciones del efecto de las decisiones. Registra lecciones concretas sobre piloto, coche, rivales, circuito, neumáticos, ritmo, combustible y ERS cuando haya evidencia. Al consultar otra edición, ajusta la confianza por cambios de coche, reglamento, compuestos y condiciones.

Aplica el [diccionario](../esquemas/DICCIONARIO.md), registra las fuentes, revisa cambios y valida antes de sincronizar.
