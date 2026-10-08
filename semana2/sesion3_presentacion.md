# Session 3 · Presentación
# Reusable Logic: Functions and Dictionaries

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion3_guion.md`.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–3 | 1. Apertura y repaso | 0–4 |
| 4–6 | 2. Leer una función | 4–11 |
| 7–10 | 3. Lo que entra y lo que sale | 11–19 |
| 11–14 | 4. Diccionarios | 19–26 |
| 15–18 | 5. Diseñar la prueba | 26–32 |
| 19–20 | 6. Escribir desde cero | 32–40 |
| 21–24 | 7. Frostbite y cierre | 40–45 |

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 3 · Reusable Logic
> Escribir una revisión una sola vez.

**DI:**
> Buenos días. Gracias por estar aquí. Entren a la lección. Una pregunta sobre
> el martes.

### 2 · Repaso — Poll

**En pantalla:** captura del código, y la pregunta "¿Qué muestra?"

```python
count = 0
for n in [5, 0, 7]:
    if n > 0:
        count = count + 1
print(count)
```

**Opciones:** 1 · 2 · 3 · 12

**DI:**
> Sin ejecutar. ¿Qué muestra?

**Después:**
> Dos. Y la línea count igual a cero se ejecuta una sola vez, porque está antes
> del loop.

### 3 · El problema de hoy — Diapositiva

**En pantalla:**
> La regla de los 30 fps, copiada en cinco lugares.
> Mañana cambia a 60.
>
> **Ahora en VS Code:** abre `sesion3_ejercicios.py` y ejecútalo.

**DI:**
> Cada vez que necesitamos la misma revisión, la escribimos otra vez. Si la
> regla está copiada en cinco lugares y mañana cambia, hay que corregirla en
> cinco lugares, y alguien va a olvidar uno. Hoy vemos cómo escribirla una vez,
> ponerle nombre y usarla donde haga falta. Abran el archivo y ejecútenlo.

### 4 · Una función — Diapositiva

**En pantalla:** captura del código.

```python
def check_fps(fps):
    if fps >= 30:
        return "PASS"
    else:
        return "FAIL"


print(check_fps(60))
```

**DI:**
> Lo de adentro ya lo conocen: es el if del primer día. Lo nuevo es la primera
> línea y la palabra return. Def: voy a definir una revisión. Check fps: su
> nombre. Entre paréntesis, lo que necesita recibir. Return es la respuesta que
> entrega. Escribir el def no ejecuta nada: la función trabaja cuando alguien la
> llama. Con 60, fps vale 60 dentro de la función, y devuelve PASS.

### 5 · Predicción — Poll

**En pantalla:** "¿Qué devuelven `check_fps(29)` y `check_fps(30)`?"

**Opciones:** FAIL y FAIL · FAIL y PASS · PASS y PASS · PASS y FAIL

**DI:**
> Predigan las dos. Después quiten el numeral y comprueben.

**Después:**
> FAIL y PASS. El borde de siempre: mayor o igual. Y si mañana la regla cambia a
> 60, se corrige en un solo lugar.

### 6 · Idea clave — Diapositiva

**En pantalla:**
> Una función tiene tres partes:
> lo que **recibe**, lo que **hace**, lo que **devuelve**.

**DI:**
> Para leer cualquier función, por larga que sea, se buscan esas tres.

### 7 · Lo que entra — Poll

**En pantalla:** captura del código, y la pregunta "Al terminar, ¿cuánto valen `score` y `new_score`?"

```python
def add_bonus(score):
    score = score + 5
    return score


score = 10
new_score = add_bonus(score)
```

**Opciones:** 10 y 15 · 15 y 15 · 10 y 10 · 15 y 10

**DI:**
> Este parece simple y no lo es. Hay un score afuera, y otro que se llama igual
> dentro de la función. Discútanlo con su pareja y respondan. Es normal no estar
> de acuerdo.

**Después:**
> Diez y quince. Al llamar a la función se le entrega una copia del valor: un 10.
> Adentro pasa a 15 y se devuelve. El score de afuera nunca se tocó: se llaman
> igual y son dos variables distintas. El 15 llega afuera por un solo camino, el
> return.

### 8 · Mostrar no es devolver — Poll

**En pantalla:** captura del código, y la pregunta "¿Cuánto vale `result`?"

```python
def show_bonus(points):
    print(points + 5)


result = show_bonus(10)
```

**Opciones:** 15 · 10 · 5 · None

**DI:**
> Casi igual a la anterior. La diferencia es una palabra: en lugar de return,
> tiene print. En su salida hay un 15 suelto: lo mostró esta función. Ahora:
> ¿cuánto vale result?

### 9 · None — Diapositiva

**En pantalla:**
> `None` = aquí no hay valor.
>
> **Mostrar** es para una persona que está mirando.
> **Devolver** es para el programa, que sigue trabajando con ese valor.

**DI:**
> Quiten el numeral y comprueben: None. La función mostró un 15 en la pantalla y
> no devolvió nada. Son dos cosas distintas, y en la pantalla se ven igual.

### 10 · Idea clave — Diapositiva

**En pantalla:**
> Los valores entran por los paréntesis y salen por el `return`.
> ¿Ves un `None` donde esperabas un valor? Falta un `return`.

**DI:**
> No hay otro camino. Guarden esa pregunta: la van a necesitar.

### 11 · Diccionarios — Diapositiva

**En pantalla:** captura del código.

```python
build = {"name": "nightly_0412", "fps": 28, "crashes": 0}

print(build["name"])
```

**DI:**
> Segunda pieza de hoy. Una lista sirve para muchas cosas del mismo tipo. Pero
> un build tiene un nombre, unos fps y un número de crashes: datos distintos de
> una misma cosa. Para eso existe el diccionario. Va entre llaves, y cada dato
> tiene un nombre, que se llama clave, y un valor. Se pide por el nombre.

### 12 · Predicción — Poll

**En pantalla:** "Después de `build["fps"] = build["fps"] + 2`, ¿qué devuelve `check_fps(build["fps"])`?"

**Opciones:** PASS · FAIL · 30 · Da error

**DI:**
> Antes de esa línea, fps vale 28 y la función devuelve FAIL; compruébenlo. La
> línea siguiente le suma dos. ¿Qué devuelve ahora?

**Después:**
> PASS: ahora vale 30. Sacamos un valor del diccionario y se lo entregamos a la
> función. Las piezas empiezan a encajar.

### 13 · Una clave que no existe — Poll

**En pantalla:** "¿Qué hace `print(build["FPS"])`?"

**Opciones:** Muestra 30 · Muestra 28 · Muestra None · Da un error

**DI:**
> Queda una. Miren bien cómo está escrita. Respondan, y después ejecútenla, lean
> la última línea del mensaje y vuelvan a poner el numeral.

**Después:**
> KeyError: un problema con una clave, y al lado la clave que no encontró. Para
> el computador, fps y FPS son dos nombres distintos. No interpreta.

### 14 · Idea clave — Diapositiva

**En pantalla:**
> Lista: "dame el tercero".
> Diccionario: "dame el nombre".
> Si pides algo que no existe, el computador no adivina: se detiene y lo dice.

**DI:**
> El martes fue IndexError, con una posición. Hoy, KeyError, con una clave.

### 15 · Diseñar la prueba — Pregunta abierta

**En pantalla:** captura del código, con el texto "Regla: válida si está entre 1 y 10, ambos incluidos. Si solo pudieras probar con 4 valores, ¿cuáles elegirías?"

```python
def is_valid(speed):
    return speed >= 1 or speed <= 10


print(is_valid(5))
```

**DI:**
> El defecto de hoy es distinto: no les doy el valor con el que falla. Con 5
> responde True, y eso es correcto. Antes de tocar el teclado: si tuvieran que
> probar esta regla con solo cuatro valores, ¿cuáles elegirían?

**Después:**
> Los dos bordes y el primer valor que queda fuera de cada lado: cero, uno, diez
> y once.

### 16 · Ahora en VS Code — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 4 · 2 minutos**
> Prueba con 0, 1, 10 y 11.
> Anota qué respondió y qué debería responder.

**DI:**
> Pruébenlos cambiando el número dentro del print.

### 17 · ¿Dónde está? — Pregunta abierta

**En pantalla:** "¿Encontraste algún valor que responda False? ¿Dónde está el defecto?"

**DI:**
> Escriban qué encontraron.

**Después:**
> Ninguno responde False. Dice or y debería decir and. Or: basta con una. And:
> se tienen que cumplir las dos. Corríjanlo y comprueben los cuatro valores.

### 18 · Idea clave — Diapositiva

**En pantalla:**
> Probar solo con valores válidos comprueba la mitad de la regla.
> La otra mitad: que lo inválido sea rechazado.

**DI:**
> Eso ustedes ya lo hacen cuando prueban el juego. Hoy lo hicieron sobre el
> código.

### 19 · Escríbelo tú — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 5 · 6 minutos**
> Escribe `check(test)`: recibe un diccionario, devuelve `"PASS"` o `"FAIL"`.
> `def` · dos puntos · 4 espacios · `return`
>
> Debe salir:
> `Player speed PASS` · `Jump height FAIL` · `Max health PASS`

**DI:**
> Ahora la escriben ustedes. Cambien de persona en el teclado. Es el if del
> primer día, con dos cambios: los valores salen de un diccionario, y en lugar
> de print usan return. Cuando la tengan, quiten los numerales del loop.

**Mientras trabajan:** la tabla de errores está en el guion, bloque 6.

### 20 · Idea clave — Diapositiva

**En pantalla:**
> El loop tiene dos líneas. El `if` está dentro de la función.
> Para entender una herramienta se empieza por los nombres.

**DI:**
> Quien lee el loop no necesita saber cómo se revisa una prueba: le basta leer
> la palabra check. Las herramientas grandes están hechas así.

### 21 · Frostbite — Diapositiva

**En pantalla:**
> **Frostbite**
> Hoy empezamos por el asset.

**DI:**
> Pasemos a Frostbite.

**HAZ:** comparte FrostEd y sigue el bloque 7 del guion: primero el asset y su
panel de propiedades, después las secciones 2, 4 y 6 del script.

### 22 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Un caso de prueba es un conjunto de datos con nombre.
> Un truco, también.

**DI:**
> Aterricemos esto al juego. El caso de prueba que vieron tiene un nombre, un
> autor, una lista de pasos y un mensaje de fallo: es un diccionario. Un truco
> se puede pensar igual: un nombre, un stance, la secuencia que lo dispara. Y la
> comprobación "¿el juego detectó este truco?" es una función: recibe un truco y
> devuelve PASS o FAIL. Cuando alguien dice que un test "valida la detección",
> por dentro hay algo con esa forma.

### 23 · Cierre — Poll

**En pantalla:** "¿Cuál de las dos piezas de hoy te quedó menos clara?"

**Opciones:** Funciones · `return` y `None` · Diccionarios · Las dos por igual · Ninguna

**DI:**
> Para cerrar: ¿cuál les quedó menos clara? Me sirve para el martes.

### 24 · Resumen — Diapositiva

**En pantalla:**
> **Hoy:** leer una función · lo que entra y lo que sale · mostrar no es devolver
> · diccionarios · diseñar valores de prueba · una función escrita por ustedes
>
> **Martes:** lo que pasa cuando algo falla
> **Tarea opcional:** los retos al final del archivo

**DI:**
> Gracias. Con esto termina la parte de construir. La próxima semana cambia el
> enfoque: leer un error completo, entender un assertion y encontrar la causa en
> un log. Es la parte más cercana a su trabajo. Buen trabajo.
