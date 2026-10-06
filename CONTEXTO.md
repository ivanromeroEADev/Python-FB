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
- **Tono de los speech:** cálido, carismático y con frases completas; que se note
  que disfruta enseñar. Incluyen marcas de *(pausa)*. Evitar adjetivos con género
  al hablar en primera persona.
- **Formato de los guiones:** bloques **DI** (se lee tal cual) y **HAZ** (acción),
  tabla de tiempos, explicación línea por línea, tabla de errores típicos, demo de
  Frostbite descrita por objetivo y sección "Si vas mal de tiempo".
- **Regla didáctica:** predecir antes de ejecutar. Los `print` de comprobación van
  comentados en los archivos de ejercicios.
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
- `semana1/sesion1_guion.md`, `sesion1_ejercicios.py`, `sesion1_soluciones.py`
- `semana1/sesion2_demo_assert.py` (se usará en la sesión 4)
- `_version_anterior/`: versiones descartadas. `semana1_v2` tiene los guiones
  anteriores de variables y de condiciones con el "error a propósito" y la demo de
  assert; sirven de base para la sesión 4.

## Pendiente

1. Guiones, ejercicios y soluciones de las sesiones 2 a 7, en el mismo formato.
2. Versión paralela del diagnóstico para el 29 de octubre: misma estructura, otros
   valores.
3. El canvas de Slack tiene el calendario anterior; hay que actualizar la tabla.

## Cómo retomar

Abrir una sesión de Claude en esta carpeta y escribir:
"Lee CONTEXTO.md y programa.md, y continúa con el pendiente 1."
