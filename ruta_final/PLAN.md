# Ruta final: 4 sesiones, del 22 al 30 de octubre

Reemplaza las sesiones 3 a 7 del calendario original, que se corrió. El material
anterior (`semana2` a `semana4`) queda como banco de ejercicios y no se borra.

## Calendario

| # | Fecha | Sesión | Python | Hito del mini-proyecto |
|---|---|---|---|---|
| 3 | Jue 22 oct | Reusable Logic (nivel 2) | Funciones con dos entradas, `return` en un loop, diccionario contador | 1: `check` y `summarize`, regla decidida por el grupo |
| 4 | Por definir | Debugging | Tracebacks, `assert`, bug silencioso | 2: el requisito del `ERROR`, y asserts que prueban la herramienta |
| 5 | Por definir | Archivos y logs | Leer un archivo, texto contra número, primer error | 3: leer los resultados desde un archivo y encontrar la causa en un log |
| 6 | Por definir, antes del 30 | Cierre | Integración y diagnóstico final | 4: reporte final y defensa oral por parejas |

La sesión 7 original (repaso y diagnóstico final) se une a la 6.

## Cómo se trabaja: menos IA, más aprendizaje

Usar IA fuera de clase no se puede impedir, y no hace falta perseguirlo. Lo que
sí se controla es que **los momentos en que se aprende y se evalúa ocurran en
vivo**.

1. **Se escribe en la pantalla del instructor.** VS Code abierto en
   `ruta_final`. El archivo `.vscode/settings.json` apaga Copilot, el chat, el
   autocompletado, las pistas y el subrayado de errores, solo en esa carpeta. Una
   pareja toma el control remoto: una persona escribe y la otra dicta.
2. **Predicción con 60 segundos.** Todos responden en el chat al mismo tiempo,
   cuando el instructor dice "ahora". No alcanza para copiar el código a una IA,
   y sí para pensarlo.
3. **"Explícame la línea".** Después de cada ejercicio, una pregunta a la pareja
   sobre una línea concreta. No se acusa a nadie: si lo entendieron, sirvió.
4. **El proyecto avanza solo en clase.** El archivo se publica al final de cada
   sesión, tal como quedó en pantalla. La próxima sesión parte de ese archivo,
   no del que cada uno tenga en casa.
5. **Reglas que decide el grupo.** Por ejemplo, si un valor justo en el límite
   pasa o falla. No están en ningún enunciado que se pueda pegar en un chat.
6. **Requisitos que cambian en vivo.** En cada hito se anuncia un cambio que no
   está en el archivo. Si no entienden su código, no saben dónde tocarlo.
7. **Defensa final.** En la sesión 6, cada pareja explica una función suya en 2
   minutos y responde una pregunta: "¿qué pasa si cambio esta línea?" o "¿con qué
   dato fallaría?". Esa es la evaluación real del curso.

## Hitos, en detalle

**Hito 1 (sesión 3), hecho.** `proyecto/skate_validator.py`, pasos 0 a 3.
Cambio en vivo: un resultado con `"kind": "maximum"` (error de tipeo). Con `else`
se trata como `max` sin avisar. Requisito: devolver `"ERROR"` y contarlo aparte.

**Hito 2 (sesión 4), por escribir.**
- Abre con el requisito del `ERROR`, si no quedó hecho, y el `KeyError: 'ERROR'`.
- Asserts que prueban `check` en los bordes: `assert check({... "actual": 30, "limit": 30}) == "PASS"`.
- Bug sembrado: un promedio sin paréntesis (el de la sesión 4 original), ahora
  como función `pass_rate(summary)`.
- Cambio en vivo: un tipo nuevo, `"exact"`, para pruebas que deben dar el valor
  justo (un replay guardado: 1 de 1).

**Hito 3 (sesión 5), por escribir.**
- `RESULTS` pasa a un archivo de texto. `parse_line` devuelve un diccionario.
- El bug silencioso: los números leídos del archivo son texto, y `"9" >= "30"` da
  `True`.
- Un log inventado con varios errores: encontrar el primero, no el último (se
  conecta con `first_fail`).
- Cambio en vivo: una línea con `n/a` en lugar de un número.

**Hito 4 (sesión 6), por escribir.**
- `validate(file_name)` junta todo y devuelve el resumen.
- Reporte final por consola, con el porqué de cada FAIL.
- Defensa oral por parejas (20 min) y diagnóstico final paralelo (15 min).
- Demo en FrostEd: la misma lógica sobre los dos casos de prueba de Skate.

## Pendiente

- Fijar las fechas de las sesiones 4, 5 y 6.
- Escribir los guiones y archivos de las sesiones 4, 5 y 6.
- Los scripts de FrostEd de esta ruta: por ahora se reutilizan los de
  `semanaN/engine`. Ninguno se ha probado en FrostEd.
- Diagnóstico final paralelo (pendiente 1 de `CONTEXTO.md`).
