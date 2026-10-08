# Session 2 · Martes 13 de octubre
# Repetition: Loops and Lists

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

En el diagnóstico, la pregunta del loop con contador la acertaron 4 de 9. No
falló por el `for`: falló porque dentro del loop hay un valor que cambia en cada
vuelta, y eso es lo mismo que se practicó el jueves. Hoy se traza un contador
vuelta por vuelta hasta que deje de ser un misterio.

**Al terminar, el participante puede:** leer una lista y sus posiciones, decir
cuántas veces se ejecuta cada línea de un `for`, trazar un contador en una tabla,
y escribir un loop que cuente.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–5 | 1. Apertura y repaso | | Dos preguntas al grupo |
| 5–12 | 2. Listas | 1 | Predicción, un error a propósito |
| 12–18 | 3. Repetir con `for` | 2 | Predicción en parejas |
| 18–26 | 4. Seguir el contador | 3 | Tabla de trazado, debate |
| 26–33 | 5. El contador que no cuenta | 4 | Caza de un bug |
| 33–40 | 6. Escribir desde cero | 5 | Trabajo en parejas, tú circulas |
| 40–45 | 7. Frostbite y cierre | | Demostración y preguntas |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana2`, con la terminal abierta y la letra
   grande (`Ctrl` y `+`).
2. Ejecuta `python sesion2_ejercicios.py` y confirma que termina con
   `Builds with crashes: 1`.
3. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S2_Repetition` listo y la ventana de salida
   limpia. **Ejecútalo una vez antes de la clase.** Si la sección 6 dice "No se
   pudieron leer los assets", usa el plan B del bloque 7.
4. Los assets `QV_Ivan_DetectionTest` y `QV_Ivan_Combo01` abiertos en FrostEd.
5. El archivo `sesion2_ejercicios.py` publicado en el canal.
6. La lista de parejas a mano. Si el jueves alguien estuvo callado, cámbiale la
   pareja.

---

# Bloque 1 · Apertura y repaso (0–5)

**Propósito:** recuperar las dos ideas del jueves que hoy se vuelven a usar, y
dejar el archivo ejecutando.

**DI:**
> Buenos días. Gracias por volver.
>
> Antes de avanzar, dos preguntas sobre el jueves. No son un examen; son para
> saber desde dónde partimos hoy.

**HAZ:** escribe en un archivo vacío, sin ejecutar:

```python
x = 4
y = x
x = x + 1
```

**PREGUNTA:**
> ¿Cuánto vale y al final?

**ESPERAS:** 4. `y` guardó una copia; no se entera de que `x` cambió.

**SI FALLAN (dirán 5):**
> Veamos por qué. Cuando escribimos y igual a x, ¿qué se guardó en y: una
> conexión con x, o el valor que x tenía en ese momento?

**PREGUNTA:**
> Segunda. La regla dice "30 fps o más". ¿Qué símbolo va en el código: mayor, o
> mayor o igual?

**ESPERAS:** mayor o igual.

**DI:**
> Bien. Esas dos ideas, que una variable solo sabe lo que vale ahora y que el
> borde importa, van a aparecer hoy otra vez, dentro de algo nuevo.
>
> El jueves cada programa revisaba un solo dato: un valor de fps, un número de
> crashes. En nuestro trabajo nunca hay un solo dato. Hay cuarenta pruebas,
> doscientos builds, diez mil assets. Hoy vemos cómo decirle al computador que
> repita una revisión sobre todos, escribiéndola una sola vez.
>
> Abran el archivo sesion2 ejercicios y ejecútenlo, igual que el jueves.

**PREGUNTA:**
> ¿Todos ven Session 2 ready al inicio de la salida?

**SI ALGUIEN NO:** misma tabla del jueves: `py` en lugar de `python`, carpeta
equivocada, o escribió en el archivo y no en la terminal.

---

# Bloque 2 · Listas (5–12)

**Propósito:** que entiendan que una lista tiene posiciones y que la primera es
la 0. El error de índice es el valor límite de las listas.

## Ejercicio 1

```python
results = ["pass", "fail", "pass", "pass"]

print(len(results))
```

**DI:**
> Hasta ahora una variable guardaba un valor. Una lista guarda varios, en orden,
> bajo un solo nombre. Se escribe entre corchetes, con los valores separados por
> comas.
>
> La instrucción len cuenta cuántos hay. En la salida ven un 4.
>
> Para pedir un valor de la lista se escribe el nombre y, entre corchetes, la
> posición.

**PREGUNTA:**
> Sin ejecutar: ¿qué creen que es results, corchete, cero? ¿Y results, corchete,
> uno? Acuérdenlo con su pareja y escríbanlo.

**HAZ:** espera. Pide la respuesta a dos parejas. Luego que quiten el `#` y
ejecuten. Sale `pass fail`.

**SI FALLAN (dirán que la posición 0 no existe, o que la 1 es "pass"):**
> Es lo que diría cualquiera que cuenta desde uno. El computador cuenta desde
> cero. La primera posición es la cero.

**PREGUNTA:**
> Entonces, si hay cuatro valores y el primero está en la posición cero, ¿en qué
> posición está el último?

**ESPERAS:** en la 3.

**HAZ:** que quiten el `#` de `print(results[3])` y ejecuten. Sale `pass`.

**PREGUNTA:**
> Queda una línea. ¿Qué va a pasar con results, corchete, cuatro? No ejecuten
> todavía. Quiero oír dos predicciones distintas.

**ESPERAS:** que da un error, porque esa posición no existe.

**HAZ:** que quiten el `#` y ejecuten. Sale:

```
Traceback (most recent call last):
  File "...sesion2_ejercicios.py", line 26, in <module>
    print(results[4])
          ~~~~~~~^^^
IndexError: list index out of range
```

**DI:**
> Déjenlo en pantalla un momento. Nadie lo corrija.
>
> Lean solo la última línea. IndexError: un problema con una posición. List index
> out of range: la posición está fuera del rango. El mensaje dice exactamente lo
> que pasó. Pedimos la posición cuatro, y la última es la tres.

**PREGUNTA:**
> El jueves hablamos de valores límite. ¿Cuál es el valor límite de esta lista?

**ESPERAS:** el 3, la última posición válida. O el 4, la primera que ya no existe.

**DI:**
> Las dos respuestas son correctas: el borde está entre el tres y el cuatro.
> Vuelvan a poner el numeral en esa línea, guarden y ejecuten para confirmar que
> el archivo corre completo.

**IDEA CLAVE:**
> Una lista de cuatro elementos tiene las posiciones cero, uno, dos y tres. Quien
> olvida eso se equivoca por uno, y equivocarse por uno es de los errores más
> frecuentes que existen en programación.

---

# Bloque 3 · Repetir con for (12–18)

**Propósito:** que distingan lo que se repite de lo que ocurre una sola vez.

## Ejercicio 2

```python
for r in results:
    print("Checking:", r)
print("Done")
```

**DI:**
> Pedir los valores uno por uno, por posición, no sirve cuando son doscientos.
> Para eso existe for.
>
> Se lee así: por cada r en results, haz lo que está debajo. La variable r la
> crea el propio for. En la primera vuelta guarda el primer valor de la lista; en
> la segunda, el segundo; y así hasta que la lista se acaba.
>
> Las reglas de formato son las del if: la línea termina con dos puntos, y lo que
> se repite empieza con cuatro espacios.

**PREGUNTA:**
> Miren la salida. ¿Cuántas veces salió Checking? ¿Y cuántas veces salió Done?

**ESPERAS:** cuatro y una.

**PREGUNTA:**
> ¿Por qué Done sale una sola vez, si está justo debajo?

**ESPERAS:** porque no tiene los cuatro espacios. No pertenece al loop.

**SI NO RESPONDEN:**
> Comparen cómo empieza la línea de Checking con cómo empieza la línea de Done.

**PREGUNTA:**
> Ahora predigan. Si le pongo cuatro espacios al inicio a la línea de Done,
> ¿cuántas veces sale? Escríbanlo, y después háganlo.

**HAZ:** espera a que lo prueben. Sale `Done` cuatro veces, intercalado.

**PREGUNTA:**
> ¿Y en qué orden salieron? ¿Los cuatro Checking primero y los cuatro Done después?

**ESPERAS:** no. Intercalados: Checking, Done, Checking, Done.

**DI:**
> Porque en cada vuelta el computador ejecuta todas las líneas del loop, de
> arriba hacia abajo, y solo entonces pasa al siguiente valor. Quiten esos cuatro
> espacios y déjenlo como estaba.

**IDEA CLAVE:**
> Los espacios deciden qué se repite y qué ocurre una sola vez. Mover una línea
> cuatro espacios cambia el programa. En diez minutos van a ver un defecto que es
> exactamente eso.

---

# Bloque 4 · Seguir el contador (18–26)

**Propósito:** trazar un valor que cambia dentro de un loop. Es la pregunta 12
del diagnóstico. Es el bloque más importante de hoy.

## Ejercicio 3

```python
fps_samples = [45, 30, 28, 60, 29]
low = 0

for fps in fps_samples:
    if fps < 30:
        low = low + 1
```

**DI:**
> Este es el ejercicio central de hoy. Junta todo lo que han visto: una lista, un
> for, un if, y una variable que cambia.
>
> La regla es: contar cuántas muestras están por debajo de 30 fps.
>
> Una variable que empieza en cero y sube de uno en uno se llama contador. Fíjense
> en la línea low igual a low más uno: es la misma forma de score igual a score
> más cinco, del jueves.
>
> No ejecuten. Debajo del código hay una tabla, con una fila por cada vuelta del
> loop. Llénenla con su pareja: qué vale fps en esa vuelta, si la condición es
> verdadera o falsa, y cuánto vale low al terminar la vuelta. Dos minutos.

**HAZ:** dibuja la misma tabla en pantalla, vacía. Circula. Mira la fila 2 de
cada pareja: es donde se separan.

**PREGUNTA:**
> Antes de ver el resultado: ¿cuánto vale low al final? Levanten la mano quienes
> tienen 2. *(espera)* ¿Quién tiene 3?

**HAZ:** no digas cuál es correcta. Llena la tabla en pantalla con ellos, fila por
fila, preguntando cada casilla al grupo.

| vuelta | fps | fps < 30 ? | low |
|---|---|---|---|
| 1 | 45 | False | 0 |
| 2 | 30 | False | 0 |
| 3 | 28 | True | 1 |
| 4 | 60 | False | 1 |
| 5 | 29 | True | 2 |

**PREGUNTA (al llegar a la fila 2):**
> Vuelta dos, fps vale 30. ¿30 es menor que 30?

**ESPERAS:** no.

**SI FALLAN (quien tenía 3 contó el 30):**
> Es el mismo borde del jueves, visto desde el otro lado. La regla dice "por
> debajo de 30". Treinta no está por debajo de treinta.

**PREGUNTA (al llegar a la fila 4):**
> Vuelta cuatro, fps vale 60. La condición es falsa. ¿Qué pasa con low? ¿Vuelve a
> cero?

**ESPERAS:** no. Se queda en 1. Nadie lo tocó.

**DI:**
> Eso es lo que más cuesta ver. Cuando la condición es falsa, el programa se
> salta esa línea, y low conserva lo que tenía. No se reinicia. Solo cambia
> cuando una línea lo cambia.

**HAZ:** que quiten el `#` de `print(low)` y ejecuten. Sale `2`.

**PREGUNTA:**
> Una más. La línea low igual a cero, la que está antes del for: ¿cuántas veces
> se ejecuta?

**ESPERAS:** una. Está fuera del loop.

**IDEA CLAVE:**
> Un loop no es difícil de leer si se lee vuelta por vuelta. Lo que hicieron en
> esta tabla es lo que hago yo cuando un contador da un número que no cuadra: una
> fila por vuelta, y se mira en qué fila el valor deja de ser el que esperaba.

---

# Bloque 5 · El contador que no cuenta (26–33)

**Propósito:** encontrar un defecto que no da error y que depende de dónde está
una línea. Refuerza la tabla de trazado como herramienta de búsqueda.

## Ejercicio 4

```python
crashes_per_build = [0, 3, 0, 1, 2]

for crashes in crashes_per_build:
    builds_with_crashes = 0
    if crashes > 0:
        builds_with_crashes = builds_with_crashes + 1

print("Builds with crashes:", builds_with_crashes)
```

**DI:**
> El siguiente tiene un defecto, y de nuevo no les voy a decir cuál.
>
> La regla: contar cuántos builds tuvieron al menos un crash. Miren la lista
> antes de mirar el código.

**PREGUNTA:**
> A ojo, sin programa: ¿cuántos builds tuvieron al menos un crash?

**ESPERAS:** tres: los que tienen 3, 1 y 2.

**PREGUNTA:**
> ¿Y qué dice el programa?

**ESPERAS:** 1.

**DI:**
> Uno. Sin ningún mensaje de error. Y fíjense en algo incómodo: uno es un número
> creíble. Si la lista tuviera doscientos builds y nadie los contara a mano, ese
> resultado se iría directo a un reporte.
>
> Encuentren el defecto y corríjanlo. Tienen la herramienta: la tabla de hace
> cinco minutos. Dos minutos.

**HAZ:** circula en silencio. No des la respuesta.

**PISTA (solo si una pareja se atasca):**
> Hagan la tabla. Una fila por vuelta, y anoten cuánto vale el contador al
> empezar cada vuelta.

**PREGUNTA (cuando la mayoría termine):**
> ¿Qué encontraron?

**ESPERAS:** la línea que pone el contador en cero está dentro del loop. En cada
vuelta se reinicia.

**PREGUNTA:**
> ¿Cuántas veces se ejecuta esa línea tal como está?

**ESPERAS:** cinco, una por vuelta.

**PREGUNTA:**
> Entonces, ¿por qué el resultado es 1 y no 0?

**ESPERAS:** porque en la última vuelta se reinicia a 0 y el último build tiene 2
crashes, así que sube a 1. Solo cuenta la última vuelta.

**PREGUNTA:**
> ¿Y si el último build de la lista tuviera cero crashes?

**ESPERAS:** el resultado sería 0.

**DI:**
> Es decir, este programa no cuenta builds con crashes. Responde otra pregunta:
> si el último build tuvo un crash. El arreglo es mover una línea cuatro espacios
> hacia la izquierda y ponerla antes del for.

**HAZ:** confirma que a todos les sale `Builds with crashes: 3`.

**IDEA CLAVE:**
> El defecto no estaba en lo que dice la línea, sino en dónde está. En un loop,
> la posición de una línea decide cuántas veces se ejecuta. Y un resultado
> creíble no es un resultado correcto: por eso se comprueba contra un caso que
> uno pueda contar a mano.

---

# Bloque 6 · Escribir desde cero (33–40)

**Propósito:** pasar de leer a escribir un loop con contador.

## Ejercicio 5

**DI:**
> Ahora lo escriben ustedes. Cambien de persona en el teclado.
>
> Tienen una lista con seis resultados. Escriban un loop que cuente cuántos son
> pass y que al final muestre Passed, dos puntos, 4.
>
> Necesitan tres piezas, y ya vieron las tres: un contador en cero antes del
> loop, un for con un if adentro, y un print después del loop. Fíjense dónde va
> cada una. El ejercicio anterior les mostró qué pasa si una queda en el lugar
> equivocado.

**HAZ:** circula. Observa sin intervenir durante el primer minuto.

**Respuesta:**

```python
passed = 0

for result in test_results:
    if result == "pass":
        passed = passed + 1

print("Passed:", passed)
```

**Preguntas para hacer a cada pareja mientras circulas:**

- A quien terminó: "¿Cómo saben que 4 es correcto? Cuéntenlos a mano." Y después:
  "Hagan el reto a."
- A quien se atascó: "¿Cuál de las tres piezas ya tienen? Léanmela."
- A quien tiene un error: "¿Qué línea señala el mensaje? ¿Qué dice la última línea?"
- A quien le sale un número raro: "Hagan la tabla de las dos primeras vueltas."

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| `IndentationError` | El `if` o la suma no tienen los espacios que les tocan | "¿Qué línea señala? ¿A quién pertenece esa línea: al for o al if?" |
| `SyntaxError: expected ':'` | Faltan los dos puntos en el `for` o en el `if` | "¿Cómo termina esa línea?" |
| `NameError: name 'passed' is not defined` | No crearon el contador antes del loop | "¿Cuánto vale passed antes de la primera vuelta?" |
| Sale `Passed:` seis veces, subiendo | El `print` está dentro del loop | "¿Cuántas veces quieren que se ejecute ese print?" |
| Sale `Passed: 1` o `Passed: 0` | El contador se reinicia dentro del loop | "¿Dónde vieron ese número hace cinco minutos?" |
| Sale `Passed: 0` | Compararon con `"PASS"` o `"Pass"` | "Compárenlo letra por letra con lo que hay en la lista." |
| `SyntaxError` con `if result = "pass"` | Un solo igual | "¿Ahí estás guardando o preguntando?" |

**PREGUNTA (al grupo, cuando la mayoría termine):**
> ¿Cuántas líneas tendría este programa si la lista tuviera seis mil resultados
> en lugar de seis?

**ESPERAS:** las mismas.

**IDEA CLAVE:**
> Esa es la razón por la que se automatiza. El esfuerzo de escribir la revisión
> es el mismo para seis datos que para seis mil. Lo que cambia es que, con seis
> mil, nadie puede comprobar el resultado a mano. Por eso lo que escribimos tiene
> que estar bien.

---

# Bloque 7 · Frostbite y cierre (40–45)

**Propósito:** mostrar el mismo loop recorriendo assets reales, y dejar clara la
distancia que falta.

**HAZ:** cambia a FrostEd, con el script `PyQV_S2_Repetition` a la vista.

**DI:**
> Pasemos a Frostbite. Hoy también solo observan.
>
> El jueves este script revisaba un caso de prueba. Miren el inicio del de hoy.

**HAZ:** señala la lista `TEST_ASSETS` al principio del script.

**PREGUNTA:**
> ¿Qué es eso?

**ESPERAS:** una lista. Con dos elementos, que son rutas de assets.

**HAZ:** ejecuta el script. Muestra en la salida las secciones 3 y 4.

**DI:**
> La tabla que llenaron a mano: vuelta, fps, condición, contador. Termina en 2.
> Y el defecto: con el contador dentro del loop, 1; con el contador antes del
> loop, 3. El engine llega a los mismos números que ustedes.

**HAZ:** baja a la sección 6 de la salida. Muestra el código de esa sección.

**DI:**
> Ahora la última sección. La regla es: un caso de prueba pasa si describe cinco
> pasos o más. Es la comprobación del jueves. Lo que cambió es que ya no está
> escrita para un asset: está dentro de un for que recorre la lista.

**PREGUNTA:**
> Miren el código. ¿Dónde está el contador, y dónde se pone en cero?

**ESPERAS:** `passed`, antes del for.

**PREGUNTA:**
> El resultado dice que pasó uno de dos. ¿Por qué falló el otro?

**ESPERAS:** porque su descripción tiene un solo paso, o una sola línea.

**HAZ:** abre el asset `QV_Ivan_Combo01` y muestra su descripción: una sola línea.

**DI:**
> Aquí hay un punto que quiero que vean. El script dice FAIL, y hace bien su
> trabajo: la regla dice cinco líneas y este caso tiene una. Pero lean la
> descripción. El caso sí describe una secuencia completa; está escrita en una
> sola línea, con flechas.
>
> Entonces, ¿el caso está mal, o la regla es demasiado simple? Eso el script no
> lo puede decidir. Lo decide una persona que entiende qué se quería comprobar.
>
> Hoy la lista tiene dos assets porque los escribí a mano. En una herramienta
> real, esa lista se le pide al engine y puede tener miles. El loop es el mismo.
> Lo que hace falta para llegar ahí es saber pedirle esa lista al engine, y saber
> qué reglas tiene sentido aplicar. Ese es el camino largo. La estructura, un
> contador, un for y un if, es la que escribieron hace cinco minutos.

**PREGUNTA:**
> Para cerrar: ¿en qué parte de su trabajo actual hacen a mano una misma revisión
> muchas veces?

**HAZ:** escucha dos o tres respuestas. No las comentes; solo agradece. Anótalas:
sirven para el mini-proyecto de la sesión 6.

**DI:**
> Gracias. Resumo lo que hicieron hoy: leyeron una lista y sus posiciones,
> distinguieron lo que se repite de lo que ocurre una vez, trazaron un contador
> vuelta por vuelta, encontraron un defecto que dependía de la posición de una
> línea, y escribieron un loop que cuenta.
>
> El jueves vemos cómo ponerle nombre a una revisión para usarla muchas veces sin
> copiarla, y cómo guardar juntos los datos que pertenecen a una misma cosa.
>
> Tarea opcional: los tres retos al final del archivo. Si algo no les cuadra, lo
> escriben en el canal.
>
> Buen trabajo. Nos vemos el jueves.

**Plan B, si la sección 6 no pudo leer los assets:** ejecuta el script igual y
muestra las secciones 3 y 4. Después muestra el código de la sección 6 sin su
salida y pregunta: "¿Dónde está el contador? ¿Qué se repite?". Abre los dos
assets y compara las descripciones a mano: una tiene siete líneas, la otra una.

**Dato para ti, por si preguntan:**

- En FrostEd cada `print` recibe un solo texto, armado con `+` y `str()`. Por eso
  no se ve `print("Passed:", passed)` como en VS Code. Es la misma versión
  anterior de Python del jueves.
- Si preguntan por `range`: sirve para repetir un número fijo de veces o para
  recorrer posiciones. No hace falta en este programa; se recorre la lista
  directamente.
- Si preguntan por `while`: repite mientras una condición sea verdadera. Tampoco
  hace falta aquí.
- El reto b da `66.66666666666666`, con muchos decimales. Es normal: así guarda
  el computador los decimales. Se puede redondear con `round(pass_rate, 1)`.

---

## Si vas mal de tiempo

Recorta en este orden:

1. Bloque 1: haz solo la primera pregunta de repaso.
2. Ejercicio 1: omite `results[3]` y ve directo al error de `results[4]`.
3. Ejercicio 2: omite la pregunta sobre el orden intercalado.
4. Ejercicio 5: pasa a ser la tarea, junto con los retos.

No recortes el ejercicio 3, el ejercicio 4 ni el bloque 7. Si el ejercicio 3
necesita más de ocho minutos, dáselos: es la razón de esta sesión.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Repaso | Cuántos dicen 5 en la primera pregunta | Si son varios, traza más despacio en el bloque 4 |
| Ejercicio 3, fila 2 | Qué parejas cuentan el 30 | Los valores límite siguen flojos; vuelven en las sesiones 3 y 6 |
| Ejercicio 3, fila 4 | Quién cree que `low` vuelve a 0 | No tienen claro que un valor se conserva entre vueltas |
| Ejercicio 4 | Quién usa la tabla y quién prueba cambios al azar | Mide si adoptaron el trazado como método |
| Ejercicio 5 | Cuántas parejas lo terminan sin ayuda | Decide cuánto apoyo dar en el mini-proyecto |
