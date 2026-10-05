# Semana 1: guía del instructor

Tres sesiones de 45 minutos. La convención de nombres usada en los ejercicios es
inventada (`<tipo>_<nombre>_<variante>`, por ejemplo `tex_roca_01`). Si prefieres
la real del proyecto, cámbiala en los `.py` antes de repartirlos.

Los momentos "en el editor" están descritos por objetivo: tú eliges qué carpeta y
qué assets mostrar.

**Archivos que reciben los alumnos:** `sesion1_ejercicios.py`, `sesion2_ejercicios.py`,
`sesion3_ejercicios.py`.
**Archivos solo tuyos:** esta guía, `diagnostico.md`, `sesion1_demo_validador.py` y
los dos `_soluciones.py`.

---

## Sesión 1 · Lunes 5 de octubre · Mi primer script

**Al terminar, cada persona:** ejecutó un script, cambió algo y vio el resultado
cambiar; sabe qué es una variable.

| Min | Qué pasa |
|---|---|
| 0–5 | Bienvenida y reglas |
| 5–13 | Demo: a mano contra script |
| 13–20 | Qué es un script y cómo se ejecuta |
| 20–38 | Práctica en parejas: ejercicios 1 a 5 |
| 38–45 | En el editor: observar nombres. Cierre |

### 0–5 · Bienvenida y reglas

Qué decir, en tus palabras:

- "En cuatro semanas no van a hacer mi trabajo, pero van a entender de qué está
  hecho, y van a escribir cosas que funcionan desde hoy."
- Las cuatro reglas: nadie toca producción, un error es información, se trabaja en
  parejas, cada sesión termina con algo funcionando.
- Sobre el diagnóstico: "Solo lo veo yo y sirve para armar las parejas."

Anuncia las parejas (ver tabla de perfiles en `diagnostico.md`).

### 5–13 · Demo: a mano contra script

1. Muestra en pantalla una lista de nombres de assets y pregunta: "¿Cuáles están
   mal?" Deja que encuentren dos o tres a ojo. Pregunta cuánto tardarían con 200.
2. Ejecuta `python sesion1_demo_validador.py`. Revisa 200 nombres, encuentra 31 con
   problemas y dice por qué falla cada uno, en una fracción de segundo.
3. Abre el archivo y enséñalo sin explicarlo: "Son 60 líneas. El viernes van a
   escribir ustedes la parte central de esto."

No expliques el código de la demo. Su función es mostrar el destino.

### 13–20 · Qué es un script y cómo se ejecuta

Escribe en vivo, con ellos mirando:

```python
print("Hola")
```

Ideas a transmitir:

- Un script es una lista de instrucciones que Python ejecuta de arriba hacia abajo.
- `print()` muestra algo en pantalla. Es la herramienta más usada para entender qué
  está haciendo un script.
- Guardar el archivo y ejecutar son dos pasos distintos. Si no guardan, ejecutan la
  versión anterior.

Ejecuta con todos a la vez `python sesion1_ejercicios.py` y confirma que a todo el
mundo le sale el mismo resultado antes de seguir.

### 20–38 · Práctica en parejas

Ejercicios 1 a 5 de `sesion1_ejercicios.py`. Una persona escribe, la otra lee y
opina; a los 9 minutos cambian.

Explica "variable" solo cuando lleguen al ejercicio 3: "Es una etiqueta pegada a un
valor. Si cambio el valor, todo lo que usa la etiqueta cambia."

Errores típicos y qué decir:

| Lo que ven | Causa | Qué decir |
|---|---|---|
| `SyntaxError: unterminated string literal` | Falta cerrar una comilla | "Python te dice la línea. Mira las comillas." |
| `NameError: name 'x' is not defined` | Variable mal escrita | "Las mayúsculas cuentan: `Ancho` no es `ancho`." |
| No cambia nada al ejecutar | No guardaron | "Guardar primero, ejecutar después." |
| `python` no se reconoce | Python no está en el PATH | Probar con `py` en lugar de `python` |

### 38–45 · En el editor: observar

Abre el editor en una carpeta de assets que elijas. Pide a cada pareja que anote tres
nombres y responda: "¿Qué patrón se repite?" Dos o tres parejas lo dicen en voz alta.

Cierre: "El miércoles vamos a construir y limpiar nombres como esos con Python."

**Señal de que salió bien:** todos completaron el ejercicio 4. Si la mayoría no
llegó, la sesión 2 empieza con 10 minutos para terminarlo.

---

## Sesión 2 · Miércoles 7 de octubre · Tipos y texto

**Al terminar, cada persona:** distingue texto de número, construye un nombre con
variables y limpia un nombre mal escrito.

| Min | Qué pasa |
|---|---|
| 0–5 | Repaso |
| 5–15 | Concepto: los cuatro tipos y las f-strings |
| 15–20 | El primer error a propósito |
| 20–38 | Práctica en parejas: ejercicios 4 a 6 |
| 38–45 | En el editor: comparar con la convención. Cierre |

### 0–5 · Repaso

Pregunta al grupo: "¿Qué es una variable?" y "¿Qué hace `print`?". Que respondan
ellos. Si alguien quedó atrás el lunes, su pareja le enseña el ejercicio 4.

### 5–15 · Concepto

Los cuatro tipos, con ejemplos de tu mundo:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| `str` | Texto, siempre entre comillas | `"tex_roca_01"` |
| `int` | Número entero | `512` |
| `float` | Número con decimales | `0.5` |
| `bool` | Verdadero o falso | `True` |

Hagan juntos los ejercicios 1 y 2. Para la f-string: "La `f` antes de las comillas
permite meter variables dentro del texto, entre llaves."

Frase clave: "`"512"` con comillas es texto; `512` sin comillas es un número. Para
Python son cosas distintas, y esa diferencia causa muchos errores reales."

### 15–20 · El primer error a propósito

Ejercicio 3: todos quitan el `#` y ejecutan. Sale:

```
TypeError: can only concatenate str (not "int") to str
```

Léanlo juntos en tres partes:

1. **Dónde:** el archivo y el número de línea.
2. **Qué tipo de error:** `TypeError`, un problema de tipos.
3. **El detalle:** no se puede unir un texto con un número.

Di: "El mensaje dice exactamente qué pasó y dónde. Leer esto con calma es una parte
grande de mi trabajo." Luego vuelven a poner el `#`.

Este momento importa más que cualquier ejercicio de la sesión: es la primera vez que
ven un error como algo que se lee y no como algo que asusta.

### 20–38 · Práctica en parejas

Ejercicios 4, 5 y 6. Soluciones en `sesion2_soluciones.py`.

- **Ejercicio 4:** la clave es encadenar: `sucio.lower().replace(" ", "_")`.
  Si se atascan: "Primero haz una cosa y guarda el resultado; luego la otra."
- **Ejercicio 5:** explica que se cuenta desde 0 y que `-1` es "el último".
  Es contraintuitivo; dedica un minuto a toda la clase.
- **Ejercicio 6:** introduce `True` y `False`. Di: "Estas preguntas de sí o no son
  lo que el viernes va a usar el script para decidir."

Errores típicos:

| Lo que ven | Causa |
|---|---|
| El nombre sale igual que antes | Llamaron a `.lower()` pero no guardaron el resultado en una variable |
| `IndexError: list index out of range` | Pidieron `partes[3]` cuando solo hay 3 partes (0, 1 y 2) |
| `AttributeError: 'str' object has no attribute 'lowr'` | Método mal escrito |

Quien termine antes hace el reto con `input()`.

### 38–45 · En el editor: comparar

Vuelve a los nombres que anotaron el lunes. Pregunta: "Si partimos este nombre con
`split`, ¿qué partes saldrían? ¿Qué significa cada una?" Hazlo en vivo con uno de
esos nombres.

Cierre: "Ya sabemos hacerle preguntas a un nombre. El viernes el script va a tomar
decisiones con las respuestas."

**Señal de que salió bien:** todos resolvieron el ejercicio 4 y nadie se alarmó con
el error del ejercicio 3.

---

## Sesión 3 · Viernes 9 de octubre · Condicionales: el validador

**Al terminar, cada persona:** escribió un validador que revisa un nombre contra
cuatro reglas y explica qué está mal.

| Min | Qué pasa |
|---|---|
| 0–5 | Repaso |
| 5–15 | Concepto: `if`, `elif`, `else` y la sangría |
| 15–37 | Práctica en parejas: el validador |
| 37–45 | En el editor: probar nombres reales. Cierre de semana |

### 0–5 · Repaso

Escribe en pantalla `"tex_roca_01".startswith("tex_")` y pregunta qué responde.
Luego `" " in "tex roca"`. Son las dos piezas que van a usar hoy.

### 5–15 · Concepto

Hagan juntos los ejercicios 1 y 2. Ideas a transmitir:

- `if` significa "si esto es verdad, haz lo de abajo".
- **La sangría es obligatoria.** Los 4 espacios le dicen a Python qué líneas
  pertenecen al `if`. Demuéstralo: quita la sangría de una línea y ejecuta para que
  vean el `IndentationError`.
- Los dos puntos `:` al final de la línea del `if` también son obligatorios.
- `elif` es "si no, prueba esta otra condición". `else` es "en cualquier otro caso".
- Comparaciones: `>`, `<`, `==` (igual), `!=` (distinto).
  Aviso: `=` guarda un valor; `==` pregunta si dos valores son iguales.
- `and`, `or`, `not` combinan condiciones.

### 15–37 · Práctica: el validador

Ejercicio 3. La regla 1 ya está escrita y sirve de modelo. Soluciones en
`sesion3_soluciones.py`.

Orden recomendado: que escriban la regla 2, ejecuten y comprueben; luego la 3; luego
la 4. Una regla a la vez, ejecutando entre cada una.

Dificultad de cada regla:

- **Regla 2 (minúsculas):** fácil. `if nombre != nombre.lower():`
- **Regla 3 (tipo):** la más difícil por el `not (... or ... or ...)`. Si la clase se
  atasca, escríbela tú en pantalla y explícala; no gastes más de 5 minutos aquí.
- **Regla 4 (variante):** media. Recuérdales `[-1]` de la sesión 2.

Resultados esperados al probar:

| Nombre | Resultado |
|---|---|
| `tex_roca_01` | OK |
| `tex_Roca_01` | 1 error (mayúsculas) |
| `roca_tex_01` | 1 error (tipo) |
| `mesh_arbol_3` | 1 error (variante) |
| `Tex_roca 1` | 4 errores |

Errores típicos:

| Lo que ven | Causa |
|---|---|
| `IndentationError` | Falta la sangría o mezclaron espacios y tabulador |
| `SyntaxError` en la línea del `if` | Faltan los dos puntos al final |
| Siempre dice OK | Olvidaron `errores = errores + 1` dentro del `if` |
| `SyntaxError` con `if nombre = ...` | Usaron `=` en lugar de `==` |

Si una pareja no termina las cuatro reglas, no pasa nada: con la 1 y la 2
funcionando ya tienen un validador. Que lo digan así.

### 37–45 · En el editor y cierre de semana

1. Cada pareja prueba su validador con dos o tres nombres reales del editor
   (los escriben a mano en la variable `nombre`, o con `input()` si hicieron el reto).
2. Pregunta al grupo: "¿Alguno salió con error? ¿El error es del asset o de nuestra
   regla?" Como la convención del curso es inventada, es normal que nombres reales
   fallen. Aprovecha: "Un validador solo es tan bueno como las reglas que le
   escribimos. Definir bien las reglas es la parte difícil."
3. Vuelve a ejecutar `sesion1_demo_validador.py` y di: "El lunes esto parecía magia.
   Hoy escribieron la parte que decide. La semana que viene le enseñamos a revisar
   200 nombres de una vez."

**Señal de que salió bien:** cada pareja tiene un validador con al menos dos reglas
funcionando y lo probó con un nombre real.

---

## Si el tiempo no alcanza

45 minutos es justo. Orden de lo que se puede recortar sin dañar la semana:

1. Los retos con `input()` (son opcionales).
2. El ejercicio 6 de la sesión 2 (se puede ver como repaso al inicio de la sesión 3).
3. La regla 3 del validador (la escribes tú en pantalla).

Lo que no se recorta: el error a propósito de la sesión 2 y el momento en el editor
de cada día.
