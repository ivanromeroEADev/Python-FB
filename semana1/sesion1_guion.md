# Session 1 · Jueves 8 de octubre
# Thinking Like a Programmer: Follow the Value

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

El diagnóstico mostró que el grupo reconoce los conceptos básicos, pero falla al
seguir un valor que cambia y en los valores límite. Hoy se explica poco, se
predice mucho y se conversa todo.

**Al terminar, el participante puede:** seguir el valor de una variable línea por
línea, distinguir un texto de un número, leer y escribir un `if / else`, y
detectar un error de valor límite.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–4 | 1. Apertura | | Tú expones |
| 4–9 | 2. Setup | | Todos ejecutan |
| 9–18 | 3. Seguir el valor | 1 y 2 | Predicción en parejas, debate |
| 18–25 | 4. Operadores y comparaciones | 3 | Predicción, preguntas al grupo |
| 25–34 | 5. Decisiones y valores límite | 4 y 5 | Caza de un bug |
| 34–40 | 6. Escribir desde cero | 6 | Trabajo en parejas, tú circulas |
| 40–45 | 7. Frostbite y cierre | | Demostración y preguntas |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana1`, con la terminal abierta y la letra
   grande (`Ctrl` y `+`).
2. Ejecuta `python sesion1_ejercicios.py` y confirma que corre sin errores.
3. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S1_FollowTheValue` listo y la ventana de
   salida limpia. **Ejecútalo una vez antes de la clase.** Si la sección 6 dice
   "No se pudo leer el asset", usa el plan B del bloque 7.
4. El asset `QV_Ivan_TrickTest/QV_Ivan_DetectionTest` abierto en FrostEd.
5. El archivo `sesion1_ejercicios.py` publicado en el canal.
6. La lista de parejas a mano.

---

# Bloque 1 · Apertura (0–4)

**Propósito:** fijar el marco. Qué mostraron los datos, qué haremos y cómo.

**DI:**
> Buenos días a todos. Gracias por estar aquí.
>
> Empiezo por el diagnóstico del martes. Lo revisé con cuidado, y me dio dos
> informaciones útiles.
>
> La primera: en este grupo hay base. Nadie parte de cero, y eso nos permite
> avanzar más rápido en lo elemental.
>
> La segunda me interesa más. Los resultados señalan con precisión dónde está la
> dificultad, y son tres puntos: seguir un valor cuando cambia, los valores
> límite, y la lectura de un log. *(pausa)* Ninguno de los tres se resuelve
> memorizando. Se resuelven practicando, y eso es lo que vamos a hacer.
>
> Hoy trabajamos los dos primeros.
>
> La forma de trabajo es sencilla. Trabajan en parejas y se turnan el teclado.
> Yo voy a hacer preguntas, muchas, y no busco respuestas correctas: busco ver
> cómo razonan. Una respuesta equivocada bien razonada me sirve más que un
> acierto por intuición.
>
> Y si aparece un error en pantalla, lo leemos juntos. Los errores son
> información. Con el tiempo van a ver que son la información más útil que hay.

**HAZ:** nombra las parejas. Espera a que se acomoden.

**PREGUNTA:**
> Antes de empezar: ¿alguna duda sobre cómo vamos a trabajar?

**SI NO RESPONDEN:**
> Bien. Si surge algo en el camino, me interrumpen. Empecemos.

---

# Bloque 2 · Setup (4–9)

**Propósito:** que todos ejecuten el archivo. Nadie avanza hasta que todos lo logren.

**DI:**
> Vamos a ejecutar el archivo de hoy. Lo hacemos todos al mismo tiempo, paso por
> paso. Si alguien se queda en un paso, me avisa y esperamos. No hay prisa.
>
> Uno. Abran Visual Studio Code.
>
> Dos. Menú File, Open Folder. Elijan la carpeta donde guardaron el archivo.
>
> Tres. En el panel izquierdo, abran sesion1 ejercicios.
>
> Cuatro. Menú Terminal, New Terminal. Se abre un panel en la parte inferior.
> Ahí es donde le damos instrucciones al computador.
>
> Cinco. En ese panel escriban: python, espacio, sesion1 guion bajo ejercicios
> punto py. Y Enter.

**HAZ:** hazlo tú al mismo ritmo.

**PREGUNTA:**
> ¿Todos ven la línea Hello, QA team al inicio de la salida?

**SI ALGUIEN NO:** acércate y resuélvelo con esta tabla. El grupo espera.

| Lo que ve | Qué hacer |
|---|---|
| "python no se reconoce" | Que escriba `py` en lugar de `python` |
| "No such file or directory" | Abrió otra carpeta: repetir el paso dos |
| No pasa nada | Escribió en el archivo y no en el panel inferior, o no pulsó Enter |

**DI:**
> Bien. Dos hábitos que les van a ahorrar tiempo desde hoy. Cada vez que cambien
> algo, guardan con Control S antes de ejecutar; si no, el computador ejecuta la
> versión anterior. Y en la terminal, la flecha hacia arriba recupera el último
> comando.

---

# Bloque 3 · Seguir el valor (9–18)

**Propósito:** que tracen un valor línea por línea. Ataca la pregunta 8 del
diagnóstico, que falló casi la mitad.

## Ejercicio 1 · Variables y tipos (1 minuto)

```python
player_name = "Alex"      # str
player_speed = 5          # int
player_health = 87.5      # float
is_alive = True           # bool
```

**DI:**
> Esto lo vemos rápido, porque el diagnóstico indica que ya lo manejan.

**PREGUNTA:**
> ¿Alguien me dice, en una frase, qué es una variable?

**ESPERAS:** un nombre que guarda un valor.

**SI NO RESPONDEN:**
> Es un nombre que guarda un valor. Una etiqueta sobre una caja.

**DI:**
> Exacto. Y cada valor tiene un tipo. Son los cuatro que ven en la salida: texto,
> entero, decimal, y verdadero o falso. Los vamos a usar todo el mes.

## Ejercicio 2a · La regla de hoy (3 minutos)

```python
score = 10
score = score + 5
score = score * 2
```

**DI:**
> Hoy tenemos una sola regla: antes de ejecutar, se predice.
>
> Ejecutar y mirar el resultado lo hace cualquiera. Lo que distingue a quien
> entiende el código es poder decir qué va a salir antes de que salga.
>
> Miren el ejercicio 2a. No ejecuten nada.

**PREGUNTA:**
> ¿Cuánto vale score al terminar la tercera línea? Acuérdenlo con su pareja y
> escríbanlo en el archivo. Tienen medio minuto.

**HAZ:** espera en silencio. Luego pide la respuesta a dos parejas distintas. No
digas todavía cuál es correcta.

**PREGUNTA (a quien respondió):**
> ¿Cómo llegaron a ese número?

**HAZ:** que quiten el `#` de `print(score)`, guarden y ejecuten. Sale `30`.

**ESPERAS:** 30.

**SI FALLAN (suelen decir 10, 15 o 20):**
> Es una respuesta razonable. Veamos por qué el computador llega a otro número.

**DI:**
> Vamos línea por línea. El signo igual no significa "es igual a". Significa
> "guarda esto aquí".
>
> Primera línea: guarda un 10.
> Segunda: toma lo que hay en score, que es 10, súmale 5 y guárdalo de nuevo en
> score. Ahora hay un 15. El 10 ya no existe.
> Tercera: toma el 15, multiplícalo por 2. Queda 30.

**IDEA CLAVE:**
> Una variable no recuerda lo que fue. Solo sabe lo que es ahora.

## Ejercicio 2b · Dos variables (5 minutos)

```python
a = 3
b = a
a = a + 4
b = b * 2
```

**DI:**
> El siguiente tiene más fondo. Dos variables.

**PREGUNTA:**
> ¿Cuánto vale a y cuánto vale b al final? Discútanlo. En este ejercicio las
> parejas no suelen estar de acuerdo, y eso está bien.

**HAZ:** deja un minuto completo. Escucha las discusiones sin intervenir.

**PREGUNTA:**
> ¿Qué parejas tienen 7 y 14? *(espera)* ¿Y quién tiene otra respuesta?

**HAZ:** que quiten el `#` y ejecuten. Sale `7 6`.

**SI FALLAN (lo habitual es 7 y 14):**
> Siete y catorce es la respuesta más natural, y es la que más enseña. Veamos
> dónde se separa del resultado.

**PREGUNTA:**
> Cuando escribimos b igual a a, ¿qué creen que guardó el computador en b?

**ESPERAS:** el valor que tenía a en ese momento, un 3.

**DI:**
> Eso. No guardó una conexión con a. Guardó una copia de lo que a tenía en ese
> instante: un 3. A partir de ahí son independientes. Cuando a pasa a 7, b no se
> entera. Sigue en 3. Y 3 por 2 es 6.

**PREGUNTA:**
> Entonces, si después de todo esto yo escribiera a igual a 100, ¿cuánto valdría b?

**ESPERAS:** 6. No cambia.

**IDEA CLAVE:**
> Esto que acaban de hacer se llama trazar: seguir cada valor, línea por línea.
> Es la habilidad sobre la que se apoya todo lo demás. Cuando yo busco un
> problema, la mayor parte del tiempo estoy haciendo exactamente esto.

---

# Bloque 4 · Operadores y comparaciones (18–25)

**Propósito:** diferenciar texto de número y `>` de `>=`. Prepara el bug del bloque 5.

## Ejercicio 3

```python
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100
```

**DI:**
> Un ejemplo de nuestro trabajo. Cuarenta pruebas, pasaron treinta y cuatro. El
> programa calcula cuántas fallaron y el porcentaje de éxito. En la salida ven 6
> y 85.
>
> Debajo hay cinco comparaciones. Una comparación siempre responde una de dos
> cosas: True o False.

**PREGUNTA:**
> Predigan las cinco con su pareja antes de ejecutarlas. Les adelanto que dos de
> ellas no son lo que parecen. Un minuto.

**HAZ:** espera. Después recorre las cinco, una por una, preguntando al grupo
antes de mostrar cada resultado.

**PREGUNTA:**
> Primera: ¿85 es mayor que 85?

**ESPERAS:** No. False.

**PREGUNTA:**
> Segunda: ¿85 es mayor o igual que 85?

**ESPERAS:** Sí. True.

**DI:**
> Un solo símbolo de diferencia, y el resultado se invierte. Guarden esa imagen.
> En unos minutos la vamos a necesitar.

**PREGUNTA:**
> Tercera y cuarta. Cinco más cinco, sin comillas. Y cinco más cinco, con
> comillas. ¿Qué da cada una?

**ESPERAS:** 10 y 55.

**SI FALLAN:**
> Veamos qué ve el computador. Sin comillas son números, y los suma. Con
> comillas son textos, y los textos no se suman: se unen.

**PREGUNTA:**
> Y la última: ¿el texto "5" es igual al número 5?

**ESPERAS:** False.

**DI:**
> Para nosotros son lo mismo. Para el computador, no. Y fíjense en el doble
> igual: un signo guarda, dos signos preguntan.

**PREGUNTA:**
> Pensando en su trabajo: ¿dónde podría un dato llegar como texto cuando
> esperábamos un número?

**ESPERAS:** cualquier respuesta razonable: un campo de un formulario, un archivo
de configuración, un dato exportado, un valor leído de un log.

**SI NO RESPONDEN:**
> Un valor leído de un archivo, por ejemplo. Casi todo lo que se lee de un
> archivo llega como texto, aunque parezca un número.

**IDEA CLAVE:**
> El computador no interpreta. Hace exactamente lo que está escrito. La
> diferencia entre lo que escribimos y lo que queríamos decir es el origen de
> buena parte de los bugs.

---

# Bloque 5 · Decisiones y valores límite (25–34)

**Propósito:** leer un `if` y encontrar un bug de borde. Ataca las preguntas 7 y 11.

## Ejercicio 4 · Leer una decisión (4 minutos)

```python
crashes = 3

if crashes == 0:
    print("No issues")
elif crashes <= 2:
    print("Minor")
else:
    print("Critical")
```

**DI:**
> Hasta ahora el programa hacía siempre lo mismo. Ahora decide.
>
> Se lee casi como una frase. If: si. Elif: si no, prueba esto otro. Else: en
> cualquier otro caso. Python revisa de arriba hacia abajo y se queda con la
> primera condición que sea verdadera.
>
> Dos exigencias de formato: la línea del if termina con dos puntos, y las
> líneas que dependen de él empiezan con cuatro espacios. Los espacios indican
> qué pertenece a cada decisión.

**PREGUNTA:**
> Con 3 crashes salió Critical. ¿Qué sale con 0? ¿Y con 2? Predigan las dos y
> después cambien el valor para comprobar.

**HAZ:** espera a que lo prueben.

**PREGUNTA:**
> ¿Por qué con 2 sale Minor y no Critical?

**ESPERAS:** porque la condición dice menor o igual, y 2 es igual a 2.

**PREGUNTA:**
> ¿Y si la condición dijera solo "menor que 2"?

**ESPERAS:** el 2 pasaría a Critical.

## Ejercicio 5 · El bug (5 minutos)

```python
fps = 30

if fps > 30:
    print("PASS")
else:
    print("FAIL")
```

**DI:**
> El siguiente ejercicio es distinto. Tiene un defecto, y no les voy a decir cuál.
>
> Lean la regla del comentario: la prueba pasa si el juego corre a 30 fps o más.
> El juego corre a 30. El programa dice FAIL.

**PREGUNTA:**
> Miren la salida. ¿Aparece algún mensaje de error?

**ESPERAS:** No.

**DI:**
> Ninguno. El programa se ejecuta sin problema y entrega un veredicto incorrecto.
> Ese es el tipo de defecto más difícil: el que no avisa.
>
> Ustedes son QA. Encuéntrenlo y corríjanlo. Dos minutos.

**HAZ:** circula en silencio. Si una pareja se atasca, no des la respuesta.

**PISTA (solo si una pareja se atasca):**
> Lean la regla en voz alta, palabra por palabra, y comparen cada palabra con el
> código.

**PREGUNTA (cuando la mayoría termine):**
> ¿Qué encontraron?

**ESPERAS:** la regla dice "30 o más" y el código dice "más de 30". Falta el igual.

**PREGUNTA:**
> ¿Con qué valores de fps funciona bien este código, aun con el defecto?

**ESPERAS:** con todos menos el 30. Con 29 falla correctamente; con 60 pasa
correctamente.

**PREGUNTA:**
> Entonces, ¿qué tendría que pasar para que alguien detecte este bug?

**ESPERAS:** que alguien pruebe exactamente el valor límite.

**IDEA CLAVE:**
> Por eso en QA se prueban los bordes. Hoy lo vieron desde adentro: así se ve en
> el código un defecto de valor límite. Un carácter.

---

# Bloque 6 · Escribir desde cero (34–40)

**Propósito:** pasar de leer a escribir. Es donde se ve el nivel real de cada pareja.

## Ejercicio 6

**DI:**
> Hasta aquí leyeron y corrigieron código. Ahora lo escriben.
>
> Les anticipo algo para que no los tome por sorpresa: escribir cuesta más que
> leer. Es normal. También es normal que aparezca un error; si aparece, lo leemos.
>
> Cambien de persona en el teclado. Tienen un valor esperado y un valor real.
> Escriban un if else que muestre PASS si son iguales y FAIL si no lo son.
> Recuerden: dos puntos, cuatro espacios, doble igual.

**HAZ:** circula. Observa sin intervenir durante el primer minuto.

**Respuesta:**

```python
if actual == expected:
    print("PASS")
else:
    print("FAIL")
```

**Preguntas para hacer a cada pareja mientras circulas:**

- A quien terminó: "¿Qué pasa si cambio actual a 5? Predíganlo y pruébenlo."
- A quien se atascó: "Léanme en voz alta lo que llevan escrito."
- A quien tiene un error: "¿Qué línea señala el mensaje? ¿Qué dice la última línea?"

**Cómo leer un error con ellos, en tres pasos:**

1. **Dónde:** el archivo y el número de línea.
2. **Qué línea falló:** Python la copia.
3. **Qué pasó:** la última línea, con el tipo de error y el detalle.

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| `IndentationError` | Faltan los 4 espacios | "¿Qué línea señala el mensaje? ¿Cómo empieza?" |
| `SyntaxError: expected ':'` | Faltan los dos puntos | "¿Cómo termina la línea del if?" |
| `SyntaxError` con `if actual = expected` | Un solo igual | "¿Ahí estás guardando o preguntando?" |
| `NameError` | Un nombre mal escrito | "Compáralo letra por letra con el de arriba." |

**PREGUNTA (al grupo, cuando la mayoría termine):**
> ¿Qué les costó más: leer el código de antes o escribir este?

**ESPERAS:** escribir.

**IDEA CLAVE:**
> Lo que tienen en pantalla es el núcleo de una prueba automatizada: comparar lo
> real con lo esperado y emitir un veredicto. Las herramientas que usamos hacen
> eso miles de veces, con muchas más reglas alrededor. El centro es ese if.

---

# Bloque 7 · Frostbite y cierre (40–45)

**Propósito:** mostrar que lo que hicieron es lo mismo que ocurre dentro del
engine, y dejar clara la distancia que falta.

**HAZ:** cambia a FrostEd, con el script `PyQV_S1_FollowTheValue` a la vista.

**DI:**
> Pasemos a Frostbite. Hoy solo observan.
>
> Esto es un script dentro del editor del engine. Mírenlo un momento.

**PREGUNTA:**
> ¿Reconocen algo?

**ESPERAS:** son los mismos ejercicios: score, a y b, el bug de los 30 fps.

**HAZ:** ejecuta el script. Muestra en la salida las secciones 2 y 5.

**DI:**
> Score: 10, 15, 30. A vale 7, b vale 6. Con mayor que, FAIL; con mayor o igual,
> PASS. El mismo resultado que obtuvieron ustedes. El engine entiende el mismo
> lenguaje que escribieron hoy.
>
> Ahora, la última sección hace algo que en su archivo no era posible.

**HAZ:** baja a la sección 6 de la salida. Muestra el asset
`QV_Ivan_DetectionTest` abierto, con sus campos.

**DI:**
> Este es un caso de prueba real. Tiene un nombre, un autor y una lista de pasos.
> El script no tiene esos valores escritos a mano: se los pide al engine. Lee el
> nombre, lee el autor, cuenta los pasos. Son tres variables, con sus tipos,
> pero con datos reales.

**PREGUNTA:**
> ¿Y qué hace el script con esos tres valores?

**ESPERAS:** los compara con lo esperado y dice PASS o FAIL. El mismo `if` del
ejercicio 6.

**DI:**
> Exactamente. El if que escribieron hace cinco minutos, aplicado a un asset del
> juego. Ahora piensen en eso mismo sobre diez mil assets. Eso es validación
> técnica.
>
> Quiero ser preciso con una cosa, para que nadie se lleve una idea equivocada.
> Encontrar un defecto en seis líneas no es lo mismo que encontrarlo dentro del
> engine, donde primero hay que saber dónde vive el valor, quién lo modificó y
> por qué. Entre lo de hoy y eso hay un camino largo. Pero la forma de pensar es
> la misma, y hoy la ejercitaron.

**PREGUNTA:**
> Para cerrar: de todo lo que vimos hoy, ¿qué fue lo que menos esperaban?

**HAZ:** escucha dos o tres respuestas. No las comentes; solo agradece.

**DI:**
> Gracias. Resumo lo que hicieron: trazaron valores línea por línea,
> distinguieron texto de número, leyeron decisiones, encontraron un defecto de
> valor límite y escribieron una comprobación desde cero.
>
> El martes vemos cómo hacer que el programa repita una revisión sobre muchos
> datos sin escribirla muchas veces.
>
> Queda una tarea opcional: el reto al final del archivo. Si algo no les cuadra,
> lo escriben en el canal y lo vemos.
>
> Buen trabajo hoy. Nos vemos el martes.

**Plan B, si la sección 6 no pudo leer el asset:** ejecuta el script igual y
muestra las secciones 2 y 5. Después abre el asset y señala sus campos: "Este
caso de prueba tiene un nombre, un autor y unos pasos. Son variables, con sus
tipos. Un script puede leerlas y compararlas con lo esperado, igual que hicieron
ustedes."

**Dato para ti, por si preguntan:** FrostEd usa una versión de Python anterior a
la de VS Code. Por eso el script no tiene f-strings y `type()` muestra
`<type 'str'>` en lugar de `<class 'str'>`. En esa versión `34 / 40` da `0`, y
por eso el script calcula el porcentaje con `100.0`.

---

## Si vas mal de tiempo

Las preguntas consumen tiempo. Recorta en este orden:

1. Ejercicio 1: omite la pregunta y di las dos frases.
2. Bloque 4: muestra las cinco comparaciones sin la pregunta sobre su trabajo.
3. Ejercicio 4: que prueben solo con el valor 2.
4. Ejercicio 6: pasa a ser la tarea, junto con el reto.

No recortes el ejercicio 2b, el ejercicio 5 ni el bloque 7.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Ejercicio 2b | Qué parejas dicen 7 y 14 | Necesitan más práctica de trazado |
| Ejercicio 5 | Quién no encuentra el bug en dos minutos | Reforzar valores límite el martes |
| Ejercicio 6 | Cuántas parejas lo terminan y quién escribe con soltura | Mide la distancia real entre leer y escribir |
| Toda la sesión | Quién responde preguntas y quién calla | Ajustar las parejas de la próxima sesión |
