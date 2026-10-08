# Contexto para continuar en otra sesión de Claude

Este archivo resume las decisiones tomadas para que una sesión nueva pueda seguir
el trabajo sin la conversación original.

## Situación

- Iván es Technical QA con experiencia en Frostbite: pipeline de assets,
  automatización del editor, herramientas de build, validación de datos y arreglo
  de jobs. Su contrato termina a finales de octubre de 2026.
- Le pidieron enseñar al equipo de QA/QV antes de irse.
- Quiere material para leer en voz alta, con el mínimo esfuerzo de preparación.

## Decisiones cerradas

- **Programa:** Python QV Foundations (Frostbite Technical Foundations). Ver
  `programa.md`.
- **Calendario:** martes y jueves, 45 minutos, del 6 al 29 de octubre de 2026.
- **Modelo:** participantes en VS Code + Python; el instructor demuestra en
  Frostbite/FrostEd. Los participantes no tocan Frostbite.
- **Objetivo:** fundamentos, no formar Technical Testers. Ningún nivel del
  diagnóstico habilita validaciones independientes.
- **Ejemplos:** de QA (pass/fail, fps, crashes, bugs, logs, assertions), con
  identificadores en inglés y explicaciones en español. Todo inventado: sin código,
  datos ni logs reales del proyecto.
- **Tono de los speech:** serio y directo, con calma, sutileza, dominio y autoridad,
  y que el receptor se sienta comodo. Sin exclamaciones ni efusividad. Evitar
  adjetivos con genero al hablar en primera persona.
- **Formato de los guiones:** interaccion bidireccional. Cada bloque tiene proposito,
  y usa las marcas **DI**, **PREGUNTA**, **ESPERAS**, **SI NO RESPONDEN**,
  **SI FALLAN**, **HAZ** e **IDEA CLAVE**. Incluyen mapa de la sesion, tabla de
  errores con la pregunta que lleva a la solucion, "Si vas mal de tiempo" y "Que
  observar". Modelo a seguir: `semana1/sesion1_guion.md`.
- **Regla didáctica:** predecir antes de ejecutar. Los `print` de comprobación van
  comentados en los archivos de ejercicios.
- **Scripts del engine:** cada sesion tiene un FBScript de solo lectura que repite
  los ejercicios de los participantes y termina con datos reales. Se escriben como
  `.py` en `semanaN/engine/` y se convierten a `.dbx` con
  `herramientas/build_fbscript.py`, hacia
  `D:/dev/dingo/dev/DingoData/Source/ztest/users/ivromero/Scripts`. FrostEd usa
  IronPython 2: sin f-strings, `print("...")` con un solo argumento, solo ASCII y
  division entera (usar `100.0`). No se hace `p4 add` ni submit sin que Ivan lo pida.
- **Canal de Slack:** `python-qv-foundations`, con un canvas del programa.

## Resultados del diagnóstico (6 de octubre)

Aplicado en vivo, 17 preguntas (Q1 es la autoevaluación; Q2 a Q17 son A1 a F2 de
`semana1/diagnostico.md`, en el mismo orden). 9 personas respondieron, 2 ausentes.
Promedio 12,7 de 17 (75 %), mediana 14. Nadie en Level 0.

Aciertos por pregunta, de 9:

| Pregunta | Tema | Aciertos |
|---|---|---|
| Q16 (F1) | Log: causa raíz | 2, con 5 sin responder |
| Q12 (D2) | Loop con contador | 4 |
| Q7 (B3) | Condición con valor límite | 5 |
| Q8 (C1) | `x = x + 2` | 5 |
| Q17 (F2) | Assertion | 5 |
| Q11 (D1) | `if / else` | 6 |
| Q15 (E2) | Bug silencioso | 6 |
| Resto | | 7 a 9 |

Conclusión: reconocen conceptos, pero les cuesta seguir un valor que cambia, los
valores límite, los logs y los assertions. El plan se ajustó a eso.

## Calendario vigente

| # | Fecha | Tema |
|---|---|---|
| 0 | Mar 6 oct | Assessment y revisión (hecha) |
| 1 | Jue 8 oct | Variables, tipos, operadores, condiciones y valores límite |
| 2 | Mar 13 oct | Loops y listas |
| 3 | Jue 15 oct | Funciones y diccionarios |
| 4 | Mar 20 oct | Debugging: tracebacks, `assert`, bugs silenciosos |
| 5 | Jue 22 oct | Archivos y logs: causa raíz y síntoma |
| 6 | Mar 27 oct | Mini-proyecto: validador de resultados de pruebas |
| 7 | Jue 29 oct | Repaso, diagnóstico final y cierre |

## Hecho

- `programa.md`
- `semana1/diagnostico.md`
- `semana1/sesion0_guion.md`
- Sesiones 1 a 7: cada una con `sesionN_guion.md`, `sesionN_ejercicios.py`,
  `sesionN_soluciones.py` y un script en `engine/`.

| Sesión | Carpeta | Script del engine | Archivos de datos |
|---|---|---|---|
| 1 | `semana1` | `PyQV_S1_FollowTheValue` | |
| 2 | `semana2` | `PyQV_S2_Repetition` | |
| 3 | `semana2` | `PyQV_S3_ReusableLogic` | |
| 4 | `semana3` | `PyQV_S4_Debugging` | `sesion4_demo_assert.py` (demo opcional) |
| 5 | `semana3` | `PyQV_S5_ReadingLogs` | `build_5120.log`, `nightly_5121.log` |
| 6 | `semana4` | `PyQV_S6_Validator` | `test_results.txt` |
| 7 | `semana4` | `PyQV_S7_FullPicture` | |

- Los siete `.dbx` están generados en ztest. **Ninguno se ha probado en FrostEd**
  ni tiene `p4 add`. La lógica de las secciones que leen assets se comprobó fuera
  del engine, con los dos `.dbx` de `QV_Ivan_TrickTest` como datos.
- `herramientas/build_fbscript.py`
- `_version_anterior/`: versiones descartadas.

## Notas de las sesiones 2 a 7

- **Hilo conductor:** cada sesión tiene un bug silencioso distinto, y los
  ejercicios siguen el orden predecir, leer, cazar un bug, escribir desde cero.
  Sesión 2: contador que se reinicia dentro del loop. Sesión 3: `or` en lugar de
  `and`. Sesión 4: promedio sin paréntesis. Sesión 5: se guarda el último error
  y no el primero. Sesión 6: números leídos de un archivo y comparados como texto.
- **Assets de las demos:** `QV_Ivan_DetectionTest` (7 líneas de descripción) pasa
  la regla de 5 pasos; `QV_Ivan_Combo01` (1 línea) falla. Los guiones cuentan con
  ese FAIL. Si cambia alguno de los dos assets, cambian las salidas que citan.
- **Sesión 4:** `PyQV_S4_Debugging` termina con un `AssertionError` a propósito
  (`RAISE_AT_END`).
- **Sesión 5:** hay que escribir en `LOG_PATH`, dentro de `PyQV_S5_ReadingLogs`,
  la ruta de un log real que se pueda mostrar, y volver a generar el `.dbx`.
- **Sesión 7:** `PyQV_S7_FullPicture` pide un asset que no existe
  (`INCLUDE_MISSING_ASSET`). Falta comprobar cómo reacciona FrostEd. El guion
  asume que el diagnóstico final (pendiente 1) ya está montado en Pear Deck. El
  párrafo de despedida es un borrador: Iván debe ajustarlo a lo que quiera decir.
- Los números de línea que citan los guiones de las sesiones 2, 3 y 4 son los de
  los archivos de ejercicios sin modificar. Si se edita un archivo, hay que
  revisarlos.

## Pendiente

1. Versión paralela del diagnóstico para el 29 de octubre: misma estructura, otros
   valores. No debe repetir los valores del repaso de `semana4/sesion7_ejercicios.py`
   (job 6033, `docks_02`, `load_times`, `rc_02`).
2. El canvas de Slack tiene el calendario anterior; hay que actualizar la tabla.
3. Probar los siete scripts en FrostEd antes de cada sesión.

## Cómo retomar

Abrir una sesión de Claude en esta carpeta y escribir:
"Lee CONTEXTO.md y programa.md, y continúa con el pendiente 1."
