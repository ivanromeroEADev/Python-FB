# Session 3 · Jueves 15 de octubre
# Reusable Logic: Functions and Dictionaries

## Cómo leer este guion

| Marca | Qué es |
|---|---|
| **DI** | Lo dices tal cual. Voz tranquila, sin prisa. |
| **PREGUNTA** | La haces al grupo y esperas en silencio. Cuenta hasta cinco antes de hablar de nuevo. |
| **ESPERAS** | La respuesta que buscas. |
| **SI NO RESPONDEN** | Qué decir tras el silencio. |
| **SI FALLAN** | Qué decir ante una respuesta equivocada. |
| **HAZ** | Lo que haces tú en pantalla. |
| **IDEA CLAVE** | La frase con la que cierras el bloque. Dila despacio. |

**Tres reglas de interacción**

1. Pregunta al grupo o a una pareja, nunca a una persona sola.
2. Una respuesta equivocada nunca se corrige con "no". Se responde con "veamos
   por qué" y se traza el código.
3. El silencio es parte de la clase. No lo llenes.

## Objetivo de la sesión

Dos piezas nuevas en una sesión, así que ninguna se ve a fondo. De las funciones
interesa una sola cosa: saber leerlas, es decir, seguir un valor que entra y otro
que sale. De los diccionarios, que los datos de una misma cosa se guardan juntos
y se piden por nombre. Con eso basta para el mini-proyecto y para reconocer un
asset del engine como lo que es.

**Al terminar, el participante puede:** leer una función y decir qué devuelve,
distinguir `return` de `print`, leer y modificar un diccionario, y escribir una
función corta que recibe un diccionario.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–4 | 1. Apertura y repaso | | Una pregunta al grupo |
| 4–11 | 2. Leer una función | 1 | Predicción, preguntas al grupo |
| 11–19 | 3. Lo que entra y lo que sale | 2a y 2b | Predicción en parejas, debate |
| 19–26 | 4. Diccionarios | 3 | Predicción, un error a propósito |
| 26–32 | 5. Diseñar la prueba | 4 | Caza de un bug eligiendo valores |
| 32–40 | 6. Escribir desde cero | 5 | Trabajo en parejas, tú circulas |
| 40–45 | 7. Frostbite y cierre | | Demostración y preguntas |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana2`, con la terminal abierta y la letra
   grande.
2. Ejecuta `python sesion3_ejercicios.py`. La salida debe ser, en este orden:
   `Session 3 ready`, `PASS`, `15`, `nightly_0412`, `True`.
3. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S3_ReusableLogic` listo y la ventana de
   salida limpia. **Ejecútalo una vez antes de la clase.** Si la sección 6 dice
   "No se pudieron leer los assets", usa el plan B del bloque 7.
4. El asset `QV_Ivan_DetectionTest` abierto en FrostEd, con el panel de
   propiedades visible.
5. El archivo `sesion3_ejercicios.py` publicado en el canal.
6. La lista de parejas a mano.

---

# Bloque 1 · Apertura y repaso (0–4)

**Propósito:** recuperar el loop con contador y plantear el problema que resuelve
una función.

**DI:**
> Buenos días. Gracias por estar aquí.
>
> Una pregunta sobre el martes.

**HAZ:** escribe en un archivo vacío, sin ejecutar:

```python
count = 0
for n in [5, 0, 7]:
    if n > 0:
        count = count + 1
print(count)
```

**PREGUNTA:**
> ¿Qué muestra? Y la segunda parte: ¿cuántas veces se ejecuta la línea count
> igual a cero?

**ESPERAS:** muestra 2. La línea se ejecuta una vez, porque está antes del loop.

**SI FALLAN:**
> Veamos por qué. Hagamos la tabla: tres vueltas, tres filas.

**DI:**
> Bien. Llevamos dos sesiones revisando valores: si los fps alcanzan, si hubo
> crashes. Y cada vez que necesitamos la misma revisión, la escribimos otra vez.
>
> Eso tiene un costo. Si la regla de los 30 fps está copiada en cinco lugares y
> mañana cambia a 60, hay que corregirla en cinco lugares, y alguien va a olvidar
> uno. Hoy vemos cómo escribir una revisión una sola vez, ponerle nombre, y
> usarla donde haga falta.
>
> Abran sesion3 ejercicios y ejecútenlo.

**PREGUNTA:**
> ¿Todos ven Session 3 ready al inicio?

---

# Bloque 2 · Leer una función (4–11)

**Propósito:** que identifiquen las tres partes de una función: lo que recibe, lo
que hace y lo que devuelve.

## Ejercicio 1

```python
def check_fps(fps):
    if fps >= 30:
        return "PASS"
    else:
        return "FAIL"


print(check_fps(60))
```

**DI:**
> Miren el ejercicio 1. Lo de adentro ya lo conocen: es el if del primer día. Lo
> nuevo es la primera línea y la palabra return.
>
> La primera línea se lee así. Def: voy a definir una revisión. Check fps: ese es
> su nombre. Y entre paréntesis, fps: eso es lo que necesita recibir para
> trabajar.
>
> Return significa "devuelve". Es la respuesta que la función entrega a quien la
> usó.
>
> Hay un detalle importante. Escribir el def no ejecuta nada. Solo le enseña al
> computador una revisión nueva. La función trabaja más abajo, cuando alguien la
> llama por su nombre y le entrega un valor.

**PREGUNTA:**
> En la salida, después de Session 3 ready, hay un PASS. ¿Qué línea lo produjo?

**ESPERAS:** `print(check_fps(60))`.

**PREGUNTA:**
> Síganlo conmigo. Cuando se llama a check fps con un 60, ¿cuánto vale fps dentro
> de la función?

**ESPERAS:** 60.

**DI:**
> Sesenta. La función recibe el 60, lo guarda en fps, revisa la condición, y
> devuelve el texto PASS. Ese texto vuelve al lugar desde donde la llamaron, y
> print lo muestra.

**PREGUNTA:**
> Predigan: ¿qué devuelve con 29? ¿Y con 30? Escríbanlo antes de quitar el
> numeral.

**HAZ:** espera. Luego que quiten el `#` y ejecuten. Sale `FAIL PASS`.

**ESPERAS:** FAIL y PASS.

**SI FALLAN (con el 30):**
> Es el borde de siempre. Lean la condición: mayor o igual.

**PREGUNTA:**
> Si mañana la regla cambia a 60 fps, ¿en cuántos lugares hay que corregirla?

**ESPERAS:** en uno, dentro de la función.

**IDEA CLAVE:**
> Una función tiene tres partes: lo que recibe, lo que hace y lo que devuelve.
> Para leer cualquier función, por larga que sea, se buscan esas tres.

---

# Bloque 3 · Lo que entra y lo que sale (11–19)

**Propósito:** seguir un valor a través de una función. Son las dos confusiones
más frecuentes: creer que la función cambia la variable de afuera, y confundir
mostrar con devolver.

## Ejercicio 2a · Lo que entra es una copia (4 minutos)

```python
def add_bonus(score):
    score = score + 5
    return score


score = 10
new_score = add_bonus(score)
```

**DI:**
> El siguiente parece simple y no lo es. Hay una variable score afuera, y otra
> que se llama igual dentro de la función.

**PREGUNTA:**
> Al terminar, ¿cuánto vale score y cuánto vale new score? Discútanlo con su
> pareja. Aquí también es normal no estar de acuerdo.

**HAZ:** deja un minuto. Escucha sin intervenir.

**PREGUNTA:**
> ¿Qué parejas tienen 15 y 15? *(espera)* ¿Quién tiene otra respuesta?

**HAZ:** que quiten el `#` y ejecuten. Sale `10 15`.

**SI FALLAN (lo habitual es 15 y 15):**
> Quince y quince es la respuesta natural. Veamos dónde se separa.

**PREGUNTA:**
> El primer día vimos b igual a a. ¿Qué se guardaba en b: una conexión, o una
> copia del valor?

**ESPERAS:** una copia.

**DI:**
> Aquí pasa lo mismo. Al llamar a la función, se le entrega una copia del valor:
> un 10. Dentro, ese 10 pasa a 15, y el 15 se devuelve. Pero el score de afuera
> nunca se tocó. Se llaman igual, y son dos variables distintas. La de adentro
> existe solo mientras la función trabaja.
>
> El 15 llega afuera por un solo camino: el return. Y se guarda en new score
> porque así lo dice esa línea.

**PREGUNTA:**
> Entonces, si quisiera que el score de afuera quedara en 15, ¿qué tendría que
> escribir en la última línea?

**ESPERAS:** `score = add_bonus(score)`.

## Ejercicio 2b · Mostrar no es devolver (4 minutos)

```python
def show_bonus(points):
    print(points + 5)


result = show_bonus(10)
```

**DI:**
> Esta función es casi igual a la anterior. La diferencia es una palabra: en
> lugar de return, tiene print.

**PREGUNTA:**
> Miren la salida de su programa. Hay un 15 suelto. ¿De dónde salió?

**ESPERAS:** del `print` que está dentro de `show_bonus`.

**PREGUNTA:**
> Bien. La función mostró un 15. Ahora: ¿cuánto vale result?

**HAZ:** pide dos predicciones. La mayoría dirá 15. Que quiten el `#` y ejecuten.
Sale `None`.

**DI:**
> None. Significa "nada". Es el valor que Python usa cuando no hay valor.
>
> La función mostró un 15 en la pantalla, y no devolvió nada. Mostrar es para
> una persona que está mirando. Devolver es para el programa, que puede seguir
> trabajando con ese valor. Son dos cosas distintas, y en la pantalla se ven
> igual.

**PREGUNTA:**
> Si otra parte del programa necesitara sumar ese bono a un total, ¿cuál de las
> dos funciones le sirve: add bonus o show bonus?

**ESPERAS:** `add_bonus`, porque devuelve el valor.

**IDEA CLAVE:**
> A una función los valores entran por los paréntesis y salen por el return. No
> hay otro camino. Cuando vean un None donde esperaban un valor, la primera
> pregunta es: ¿a esta función le falta un return?

---

# Bloque 4 · Diccionarios (19–26)

**Propósito:** que vean un diccionario como los datos de una cosa, pedidos por
nombre. Prepara la demostración del asset.

## Ejercicio 3

```python
build = {"name": "nightly_0412", "fps": 28, "crashes": 0}

print(build["name"])
```

**DI:**
> Segunda pieza de hoy. El martes vimos listas: varios valores en orden, que se
> piden por posición. Sirven para muchas cosas del mismo tipo: muchos resultados,
> muchas muestras.
>
> Pero un build no es eso. Un build tiene un nombre, unos fps y un número de
> crashes. Son datos distintos que pertenecen a una misma cosa. Para eso existe
> el diccionario.
>
> Se escribe entre llaves. Cada dato tiene dos partes separadas por dos puntos:
> un nombre, que se llama clave, y un valor. Y se pide por el nombre, entre
> corchetes.

**PREGUNTA:**
> ¿Cuántos datos tiene este build, y cómo se llaman?

**ESPERAS:** tres: name, fps y crashes.

**PREGUNTA:**
> Predigan la primera línea comentada. ¿Qué es build, corchete, fps? Y si ese
> valor se le entrega a check fps, ¿qué devuelve?

**HAZ:** espera. Que quiten el `#` y ejecuten. Sale `28 FAIL`.

**DI:**
> Fíjense en lo que acaba de pasar: sacamos un valor del diccionario y se lo
> entregamos a la función del ejercicio 1. Las piezas empiezan a encajar.
>
> La línea siguiente cambia un dato del diccionario. Tiene la forma que ya
> conocen: toma lo que hay, súmale dos, guárdalo de nuevo.

**PREGUNTA:**
> Después de esa línea, ¿qué devuelve check fps?

**ESPERAS:** PASS, porque ahora fps vale 30.

**HAZ:** que quiten el `#` y ejecuten. Sale `PASS`.

**PREGUNTA:**
> Queda una. ¿Qué diferencia ven entre esa línea y las anteriores? ¿Qué va a
> pasar?

**ESPERAS:** FPS está en mayúsculas. Va a dar un error.

**HAZ:** que quiten el `#` y ejecuten. Sale:

```
Traceback (most recent call last):
  File "...sesion3_ejercicios.py", line 65, in <module>
    print(build["FPS"])
          ~~~~~^^^^^^^
KeyError: 'FPS'
```

**DI:**
> KeyError: un problema con una clave. Y al lado, la clave que no encontró. Para
> el computador, fps en minúsculas y FPS en mayúsculas son dos nombres distintos.
> No interpreta.
>
> Vuelvan a poner el numeral en esa línea y guarden.

**PREGUNTA:**
> El martes vimos otro error parecido, con una lista. ¿Cuál era?

**ESPERAS:** IndexError, al pedir una posición que no existía.

**IDEA CLAVE:**
> Una lista responde "dame el tercero". Un diccionario responde "dame el nombre".
> Y en los dos casos, si se pide algo que no existe, el computador no adivina:
> se detiene y dice qué fue lo que no encontró.

---

# Bloque 5 · Diseñar la prueba (26–32)

**Propósito:** que encuentren un defecto eligiendo ellos los valores de prueba.
Es el trabajo de QA aplicado a una función: probar los bordes y lo que queda
fuera.

## Ejercicio 4

```python
def is_valid(speed):
    return speed >= 1 or speed <= 10


print(is_valid(5))
```

**DI:**
> El defecto de hoy es distinto a los anteriores. Las otras veces yo les daba el
> valor con el que el programa fallaba. Hoy no.
>
> La regla: una velocidad es válida si está entre 1 y 10, ambos incluidos. La
> función devuelve True o False. Con 5 responde True, y eso es correcto.
>
> Hay un defecto. Para verlo, tienen que elegir ustedes con qué valores probar.
> Antes de tocar el teclado, una pregunta.

**PREGUNTA:**
> Si tuvieran que probar esta regla con solo cuatro valores, ¿cuáles elegirían?

**ESPERAS:** los bordes y sus vecinos: 0, 1, 10 y 11.

**SI NO RESPONDEN:**
> Piensen en dónde vive un defecto de límite. La regla tiene dos bordes. ¿Cuáles
> son?

**DI:**
> Esos. Los dos bordes, y el primer valor que queda fuera de cada lado. Pruébenlos
> cambiando el número dentro del print, y anoten en el archivo qué respondió y
> qué debería responder. Dos minutos.

**HAZ:** circula en silencio.

**PREGUNTA (cuando la mayoría tenga resultados):**
> ¿Qué respondió con 11? ¿Y con 0?

**ESPERAS:** True en los dos. Debería ser False.

**PREGUNTA:**
> ¿Encontraron algún valor con el que responda False?

**ESPERAS:** ninguno.

**DI:**
> Ninguno. Esta función responde True a cualquier número. Y aun así, con 5, con
> 1 y con 10 acierta. Quien la probó solo con valores válidos la dio por buena.

**PREGUNTA:**
> ¿Dónde está el defecto?

**ESPERAS:** dice `or` y debería decir `and`.

**SI NO RESPONDEN:**
> Lean la regla y después lean la línea del return en voz alta, traduciendo cada
> palabra.

**DI:**
> Or significa "o": basta con que se cumpla una de las dos. And significa "y":
> se tienen que cumplir las dos. Tomen el 12. ¿Es mayor o igual que 1? Sí. Con or,
> eso ya es suficiente, y la segunda condición ni importa.

**HAZ:** confirma que, con `and`, a todos les da `False` con 0 y con 11, y `True`
con 1 y con 10.

**IDEA CLAVE:**
> Una prueba que solo usa valores válidos comprueba la mitad de la regla. La otra
> mitad es que lo inválido sea rechazado. Eso ustedes ya lo hacen cuando prueban
> el juego; hoy lo hicieron sobre el código.

---

# Bloque 6 · Escribir desde cero (32–40)

**Propósito:** escribir una función que recibe un diccionario. Une las dos piezas
de hoy con el loop del martes.

## Ejercicio 5

**DI:**
> Ahora la escriben ustedes. Cambien de persona en el teclado.
>
> Miren primero los datos. Hay una lista, y adentro tres diccionarios. Cada
> diccionario es una prueba, con un nombre, un valor esperado y un valor real.
>
> Escriban una función que se llame check, que reciba una de esas pruebas y
> devuelva PASS si el valor real es igual al esperado, y FAIL si no.
>
> Es el if que escribieron el primer día, con dos cambios: los valores salen de
> un diccionario, y en lugar de print usan return. Debajo hay un loop comentado
> que la usa. Cuando tengan la función, le quitan los numerales.

**HAZ:** circula. Observa sin intervenir durante el primer minuto.

**Respuesta:**

```python
def check(test):
    if test["actual"] == test["expected"]:
        return "PASS"
    else:
        return "FAIL"
```

Con el loop sin comentar debe salir:

```
Player speed PASS
Jump height FAIL
Max health PASS
```

**Preguntas para hacer a cada pareja mientras circulas:**

- A quien terminó: "Cambien un valor para que Max health falle. Predigan la
  salida." Y después: "Hagan el reto a."
- A quien se atascó: "Escriban primero la línea del def. ¿Qué recibe la función?"
- A quien no sabe cómo sacar los valores: "Si esa prueba se llama test, ¿cómo le
  piden el valor real? Miren el ejercicio 3."
- A quien tiene un error: "¿Qué línea señala el mensaje? ¿Qué dice la última línea?"

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| Sale `None` tres veces | Escribieron `print` en lugar de `return` | "¿Dónde vieron un None hace veinte minutos? ¿Qué le faltaba a esa función?" |
| `NameError: name 'check' is not defined` | Quitaron los `#` del loop antes de escribir la función, o la escribieron debajo del loop | "Python lee de arriba hacia abajo. Cuando llega al loop, ¿ya conoce a check?" |
| `KeyError: 'Actual'` u otra clave | La clave no coincide con la del diccionario | "Compárala letra por letra con la que está en la lista." |
| `NameError: name 'actual' is not defined` | Escribieron `actual` en lugar de `test["actual"]` | "¿Dónde vive ese valor? ¿Quién lo tiene?" |
| `TypeError: list indices must be integers` | Usaron `tests["actual"]`, la lista, en lugar de `test` | "¿Eso es una prueba o son las tres?" |
| `IndentationError` | El `if` no tiene los 4 espacios, o los `return` no tienen 8 | "¿A quién pertenece esa línea: a la función o al if?" |
| Sale PASS tres veces | Compararon un valor consigo mismo | "Léanme la condición en voz alta." |

**PREGUNTA (al grupo, cuando la mayoría termine):**
> El loop tiene dos líneas. ¿Dónde está el if?

**ESPERAS:** dentro de la función. El loop ya no lo necesita.

**IDEA CLAVE:**
> Eso es lo que da una función. Quien lee el loop no necesita saber cómo se
> revisa una prueba: le basta leer la palabra check. Las herramientas grandes
> están hechas así, con funciones que usan otras funciones. Para entender una
> herramienta se empieza por los nombres.

---

# Bloque 7 · Frostbite y cierre (40–45)

**Propósito:** mostrar que un asset del engine es un conjunto de propiedades con
nombre, igual que un diccionario, y dejar clara la distancia que falta.

**HAZ:** cambia a FrostEd. Muestra primero el asset `QV_Ivan_DetectionTest`
abierto, con sus propiedades a la vista. Todavía no muestres el script.

**DI:**
> Pasemos a Frostbite. Hoy empiezo por el asset, no por el script.
>
> Este es el caso de prueba que hemos visto las dos sesiones anteriores. Miren el
> panel de propiedades.

**PREGUNTA:**
> ¿A qué se parece esto, de lo que vieron hoy?

**ESPERAS:** a un diccionario. Cada propiedad tiene un nombre y un valor.

**SI NO RESPONDEN:**
> A la izquierda hay nombres. A la derecha, valores. ¿Qué vimos hoy con esa forma?

**DI:**
> Un asset es eso: un conjunto de propiedades, cada una con su nombre, su tipo y
> su valor. Casi todo lo que hay dentro del engine tiene esa forma. Un personaje,
> una luz, un nivel.

**HAZ:** cambia al script `PyQV_S3_ReusableLogic`. Ejecútalo. Muestra brevemente
las secciones 2 y 4 de la salida.

**DI:**
> Score vale 10 y new score vale 15. Result vale None. Y la tabla del defecto:
> con or, todo es True; con and, el 0 y el 11 quedan fuera. Lo mismo que
> obtuvieron ustedes.

**HAZ:** baja a la sección 6. Muestra primero el código: las funciones
`read_test_case` y `check_steps`.

**PREGUNTA:**
> Miren la función read test case. Sin entender cada línea: ¿qué recibe y qué
> devuelve?

**ESPERAS:** recibe la ruta de un asset. Devuelve un diccionario con el nombre,
el autor, los pasos y el mensaje de fallo.

**DI:**
> Eso es leer una función: lo que recibe, y lo que devuelve. Lo de en medio, cómo
> se le pide un asset al engine, no lo hemos visto y hoy no hace falta. Les basta
> saber que entra una ruta y sale un diccionario.
>
> La segunda función, check steps, sí la pueden leer completa. Es la de ustedes.

**HAZ:** muestra la salida de la sección 6: las propiedades de los dos assets y el
resultado de cada uno.

**DI:**
> Dos assets. Para cada uno, el script arma un diccionario y se lo entrega a la
> función. Uno pasa y el otro no, por la misma razón del martes.
>
> Y aquí la precisión de siempre. Hoy leyeron una función de seis líneas. Una
> herramienta real tiene cientos de funciones, escritas por muchas personas
> durante años, que se llaman unas a otras. Leerla exige saber qué hace cada
> sistema del engine, y eso toma tiempo. Lo que ya tienen es el método: ante
> cualquier función, qué recibe, qué hace, qué devuelve.

**PREGUNTA:**
> Para cerrar: de las dos piezas de hoy, funciones y diccionarios, ¿cuál les
> quedó menos clara?

**HAZ:** escucha. Anota la respuesta: decide qué repasar al inicio de la sesión 4.

**DI:**
> Gracias, eso me sirve para el martes. Resumo lo que hicieron hoy: leyeron una
> función, siguieron un valor que entra y otro que sale, distinguieron mostrar de
> devolver, leyeron y cambiaron un diccionario, encontraron un defecto eligiendo
> ustedes los valores de prueba, y escribieron una función.
>
> Con esto termina la parte de construir. Ya tienen todas las piezas: variables,
> decisiones, loops, listas, funciones y diccionarios.
>
> La próxima semana cambia el enfoque. Dejamos de escribir código nuevo y nos
> dedicamos a lo que pasa cuando algo falla: leer un error completo, entender un
> assertion, y encontrar la causa en un log. Es la parte más cercana a su trabajo.
>
> Tarea opcional: los retos al final del archivo. Lo que no les cuadre, al canal.
>
> Buen trabajo. Nos vemos el martes.

**Plan B, si la sección 6 no pudo leer los assets:** ejecuta el script igual y
muestra las secciones 2 y 4. Después muestra el código de `read_test_case` y haz
la misma pregunta: "¿Qué recibe y qué devuelve?". Vuelve al asset abierto y
señala, propiedad por propiedad, cuál iría a cada clave del diccionario.

**Dato para ti, por si preguntan:**

- Si preguntan por qué `read_test_case` recibe dos cosas: una función puede
  recibir varios valores, separados por comas. Es el reto b.
- Si preguntan por qué la variable de adentro y la de afuera pueden llamarse
  igual: cada función tiene su propio espacio de nombres. Se llama *scope*. No
  uses la palabra si no la piden.
- Si preguntan si una función puede cambiar un diccionario o una lista que
  recibe: sí puede, a diferencia de un número o un texto. No lo abras en clase;
  responde que es cierto y que se ve más adelante.
- `None` aparece mucho en los logs y en los mensajes del engine, a veces escrito
  como `null`. Significa lo mismo: aquí no hay valor.

---

## Si vas mal de tiempo

Esta es la sesión más cargada del programa. Recorta en este orden:

1. Bloque 1: omite el repaso y empieza por el problema de la regla copiada.
2. Ejercicio 3: omite el error de `build["FPS"]` y menciónalo de palabra.
3. Ejercicio 4: da tú los cuatro valores (0, 1, 10, 11) en lugar de preguntarlos.
4. Ejercicio 5: muestra la respuesta, que la copien y quiten los `#` del loop.
   Escribirla sin ayuda pasa a ser la tarea.

No recortes el ejercicio 2a, el ejercicio 2b ni el bloque 7. El `None` del 2b
vuelve a aparecer en la sesión 4.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Ejercicio 2a | Qué parejas dicen 15 y 15 | No han fijado la idea de copia; vuelve a trazarla en la sesión 4 |
| Ejercicio 2b | Quién predice 15 para `result` | Confunden mostrar con devolver; es el error más probable en el mini-proyecto |
| Ejercicio 4 | Qué valores eligen para probar | Mide si ya piensan en bordes sin que se lo pidan |
| Ejercicio 5 | Cuántas parejas escriben `print` en lugar de `return` | Decide cuánto del mini-proyecto das ya escrito |
| Cierre | Cuál de las dos piezas dicen que quedó menos clara | Repaso de cinco minutos al abrir la sesión 4 |
