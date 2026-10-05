# Contexto para continuar en otra sesión de Claude

Este archivo resume las decisiones tomadas para que una sesión nueva pueda seguir
el trabajo sin la conversación original.

## Situación

- Iván es Technical QA con experiencia en Frostbite: pipeline de assets,
  automatización del editor, herramientas de build, validación de datos y arreglo
  de jobs. Su contrato termina a finales de octubre de 2026.
- Le pidieron enseñar al equipo de QA/QV antes de irse. El equipo tiene poca o
  ninguna base de programación.
- Quiere material para leer en voz alta, con el mínimo esfuerzo de preparación.

## Decisiones cerradas

- **Programa:** Frostbite Technical Foundations. Ver `programa.md`.
- **Calendario:** martes y jueves, 45 minutos, del 6 al 29 de octubre de 2026.
- **Modelo:** participantes en VS Code + Python; el instructor demuestra en
  Frostbite/FrostEd. Los participantes no tocan Frostbite.
- **Objetivo:** fundamentos, no formar Technical Testers. Ningún nivel del
  diagnóstico habilita validaciones independientes.
- **Ejemplos:** de QA (pass/fail, fps, crashes, bugs, logs, assertions), con
  identificadores en inglés y explicaciones en español. Todo inventado: sin código,
  datos ni logs reales del proyecto.
- **Diagnóstico:** 16 preguntas, secciones A a F, niveles 0 a 3. Se aplica en vivo
  el 6 de octubre en Pear Deck y se revisan 5 preguntas (A1, C3, D2, E2, F2).
- **Tono de los speech:** cálido, carismático y con frases completas; que se note que disfruta enseñar. Incluyen marcas de *(pausa)*.
- **Formato de los guiones:** bloques **DI** (se lee tal cual) y **HAZ** (acción),
  tabla de tiempos, explicación línea por línea, tabla de errores típicos, demo de
  Frostbite descrita por objetivo y sección "Si vas mal de tiempo".

## Calendario

| # | Fecha | Tema |
|---|---|---|
| 0 | Mar 6 oct | Assessment y revisión |
| 1 | Jue 8 oct | Variables, tipos, operadores |
| 2 | Mar 13 oct | Condiciones y primer error |
| 3 | Jue 15 oct | Loops |
| 4 | Mar 20 oct | Funciones |
| 5 | Jue 22 oct | Listas y diccionarios |
| 6 | Mar 27 oct | Debugging y logs |
| 7 | Jue 29 oct | Repaso, diagnóstico final y cierre |

## Hecho

- `programa.md`
- `semana1/diagnostico.md`
- `semana1/sesion0_guion.md`
- `semana1/sesion1_guion.md`, `sesion1_ejercicios.py`, `sesion1_soluciones.py`
- `semana1/sesion2_guion.md`, `sesion2_ejercicios.py`, `sesion2_soluciones.py`,
  `sesion2_demo_assert.py`
- `_version_anterior/`: primera versión descartada (3 sesiones por semana, ejemplos
  de nombres de assets). Solo referencia.

## Pendiente

1. Guiones, ejercicios y soluciones de las sesiones 3 a 7, en el mismo formato.
2. Versión paralela del diagnóstico para el 29 de octubre: misma estructura, otros
   valores.
3. El documento de diseño original de Iván se cortó en la sección 11 (demo de
   Frostbite de la sesión 1, `player_speed = 5`). Si hay más contenido, integrarlo.

## Cómo retomar

Abrir una sesión de Claude en esta carpeta y escribir:
"Lee CONTEXTO.md y programa.md, y continúa con el pendiente 1."
