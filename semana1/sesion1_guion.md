# Session 1 · Jueves 8 de octubre
# Thinking Like a Programmer: Follow the Value

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual, con calma y
sonriendo. Lo que sigue a **HAZ** lo haces tú en pantalla. *(pausa)* es para
respirar y mirar al grupo. Los tiempos son una guía.

**Por qué esta sesión es así:** el diagnóstico mostró que el grupo reconoce los
conceptos básicos, pero falla al seguir un valor que cambia (Q8, Q12) y en los
valores límite (Q7). Por eso hoy se explica poco y se predice mucho.

**Al terminar, el participante puede:** seguir el valor de una variable línea por
línea, distinguir un texto de un número, leer y escribir un `if / else`, y
detectar un error de valor límite.

| Min | Bloque | Ejercicios |
|---|---|---|
| 0–4 | Bienvenida y resultados | |
| 4–9 | Setup: ejecutar el archivo | |
| 9–18 | Variables y seguir el valor | 1 y 2 |
| 18–25 | Operadores y comparaciones | 3 |
| 25–34 | Decisiones y valores límite | 4 y 5 |
| 34–40 | Escribir desde cero | 6 |
| 40–45 | Frostbite connection y cierre | |

## Antes de que llegue la gente

1. Abre **VS Code**. **File > Open Folder** → carpeta `semana1`.
2. **Terminal > New Terminal**. Escribe `python sesion1_ejercicios.py` y Enter.
   Deben salir 9 líneas: `Hello, QA team`, cuatro tipos, `6`, `85.0`, `Critical`
   y `FAIL`. Escribe `cls` para limpiar.
3. Sube la letra: `Ctrl` y `+`, tres o cuatro veces.
4. En otra ventana, deja **FrostEd** abierto con un objeto seleccionado que tenga
   una propiedad numérica fácil de entender. Si esa propiedad tiene un mínimo y un
   máximo permitidos, mejor: te sirve para hablar de valores límite.
5. Confirma que el archivo `sesion1_ejercicios.py` está en el canal.
6. Ten a mano la lista de parejas. Las dos personas que faltaron el martes entran
   en una pareja con alguien de puntaje alto.

---

## 1. Bienvenida y resultados (0–4)

**DI:**
> ¡Hola, hola! Qué bueno verlos de nuevo. Y bienvenidos a quienes no pudieron
> estar el martes; no se perdieron nada que no podamos recuperar hoy.
>
> Les traigo noticias del diagnóstico, y son buenas. *(pausa)* Al grupo le fue
> bastante mejor de lo que yo esperaba: el promedio estuvo en 75 por ciento. Así
> que hice lo que hace cualquier buen tester cuando los datos contradicen el
> plan: cambié el plan.
>
> ¿Qué significa eso? Que no voy a gastarles dos clases explicando qué es una
> variable, porque ya lo saben. Vamos a ir más rápido en lo básico y vamos a
> usar ese tiempo en lo que de verdad cuesta.
>
> Y los datos también me dijeron qué es lo que cuesta, y me pareció fascinante.
> Tres cosas. Una: seguirle la pista a un valor cuando va cambiando. Dos: los
> valores límite, ese "menor o igual" que nos traiciona. Y tres: la pregunta del
> log, que más de la mitad prefirió saltarse. *(pausa)* Y está perfecto, porque
> justamente para eso estamos aquí. Hoy atacamos las dos primeras.
>
> Tres acuerdos para todo el mes. Un error en pantalla es una pista, no un
> regaño. Trabajamos en parejas y se turnan el teclado. Y nadie se va sin que
> algo le haya funcionado.

**HAZ:** anuncia las parejas con buen ánimo y dales unos segundos para acomodarse.

---

## 2. Setup (4–9)

**DI:**
> Manos al teclado. Lo hacemos todos juntos; si alguien se pierde en un paso,
> levanta la mano y lo esperamos.
>
> Paso uno: abran Visual Studio Code.
>
> Paso dos: arriba a la izquierda, File, Open Folder, y elijan la carpeta donde
> guardaron el archivo de ejercicios.
>
> Paso tres: a la izquierda, clic en sesion1 ejercicios.
>
> Paso cuatro: arriba, Terminal, New Terminal. Abajo se abre un panel; ahí es
> donde le hablamos directamente al computador.
>
> Paso cinco: en ese panel escriban python, espacio, sesion1 guion bajo
> ejercicios punto py. Y Enter.

**HAZ:** hazlo tú también, despacio.

**DI:**
> Si la primera línea dice Hello, QA team, ¡felicitaciones!, acaban de ejecutar
> un programa. Y un consejo que les va a ahorrar disgustos: cada vez que cambien
> algo, primero guardan con Control S y después ejecutan. La flecha hacia arriba
> en el panel les devuelve el último comando.

**Si a alguien le falla:**

| Lo que le sale | Qué hacer |
|---|---|
| "python no se reconoce" | Que escriba `py` en vez de `python` |
| "No such file or directory" | No abrió la carpeta correcta: repetir el paso dos |
| No pasa nada | Escribió en el archivo y no en el panel de abajo, o no pulsó Enter |

---

## 3. Variables y seguir el valor (9–18)

### Ejercicio 1

```python
player_name = "Alex"      # str
player_speed = 5          # int
player_health = 87.5      # float
is_alive = True           # bool
```

**DI:**
> Esto lo vamos a pasar rápido, porque el diagnóstico me dijo que ya lo tienen.
> Una variable es un nombre que guarda un valor: una caja con etiqueta. Y cada
> valor tiene un tipo. Texto entre comillas, número entero, número con decimales,
> y verdadero o falso. Son los cuatro que salieron en pantalla: str, int, float
> y bool.
>
> ¿Todos de acuerdo hasta aquí? Perfecto. Ahora viene lo interesante.

### Ejercicio 2a

```python
score = 10
score = score + 5
score = score * 2
```

**DI:**
> Hoy tenemos una regla de oro, y es la más importante del día: antes de
> ejecutar, predecimos. *(pausa)* Les explico por qué. Cualquiera puede darle a
> Enter y ver qué sale. Lo que distingue a alguien que entiende el código es
> poder decir qué va a salir antes de que salga.
>
> Miren el ejercicio 2a. Sin ejecutar nada: ¿cuánto vale score al final?
> Escriban su predicción donde están las rayitas, y pónganse de acuerdo con su
> pareja. Medio minuto.

**HAZ:** pide dos respuestas en voz alta, sin decir cuál es correcta. Luego quitan
el `#` de `print(score)`, guardan y ejecutan. Sale `30`.

**DI:**
> ¡Treinta! Vamos despacio, porque aquí está el truco de todo. El signo igual no
> significa "es igual a", como en matemáticas. Significa "guarda esto aquí".
>
> Entonces: la primera línea guarda un 10. La segunda dice: toma lo que hay en
> score, que es 10, súmale 5, y guarda el resultado otra vez en score. Ahora hay
> un 15, y el 10 desapareció. La tercera: toma el 15, multiplícalo por 2, guarda
> 30.
>
> En el diagnóstico había una pregunta igualita a esta, y a casi la mitad se le
> escapó. Así que si hace un momento dudaron, están en muy buena compañía.

### Ejercicio 2b

```python
a = 3
b = a
a = a + 4
b = b * 2
```

**DI:**
> Ahora una con trampa, y les aviso que es de mis favoritas. Dos variables. ¿Cuánto
> vale a y cuánto vale b al final? Discútanlo, que aquí suele haber debate.

**HAZ:** deja un minuto. Pide respuestas; es normal que alguien diga `7` y `14`.
Luego quitan el `#` y ejecutan. Sale `7 6`.

**DI:**
> Siete y seis. *(pausa)* ¿Quién pensó que b iba a ser catorce? Es la respuesta
> más natural del mundo, y es justo la que nos enseña algo.
>
> Cuando escribimos b igual a a, no los amarramos para siempre. Le dijimos al
> computador: mira qué hay en a ahora mismo, un 3, y guarda una copia en b. A
> partir de ahí cada uno hace su vida. Cuando a cambia a 7, b ni se entera: sigue
> con su 3. Y por eso al final b es 3 por 2, seis.
>
> Lo que acaban de hacer se llama trazar: seguir cada valor, línea por línea. Les
> confieso que así es como yo encuentro la mayoría de los problemas: no con
> magia, sino siguiendo un valor con paciencia hasta ver dónde se tuerce.

---

## 4. Operadores y comparaciones (18–25)

### Ejercicio 3

```python
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100
```

**DI:**
> Vamos con algo de nuestro mundo. Hay 40 pruebas y pasaron 34. El computador
> calcula cuántas fallaron, que son 6, y el porcentaje de éxito, que es 85. Esos
> son los dos números que vieron en pantalla.
>
> Debajo hay cinco líneas con comparaciones. Una comparación siempre responde lo
> mismo: True o False. Antes de quitarles el numeral, predigan las cinco con su
> pareja. Les doy un minuto, y ojo, que hay dos trampas.

**HAZ:** deja un minuto. Luego quitan los `#` de las cinco líneas y ejecutan. Sale:

```
False
True
10
55
False
```

**DI:**
> Veamos cuántas acertaron. Las dos primeras van juntas. ¿85 es mayor que 85?
> No: es igual, no mayor. False. ¿85 es mayor o igual que 85? Sí. True.
>
> Un solo símbolo de diferencia y el resultado se voltea. *(pausa)* Quédense con
> esa imagen, porque en cinco minutos nos vamos a encontrar un bug hecho
> exactamente de eso.
>
> Las dos siguientes: 5 más 5 da 10, porque son números. Pero "5" más "5", entre
> comillas, da 55, porque son textos, y los textos se pegan. Es la del martes.
>
> Y la última: ¿el texto "5" es igual al número 5? Para nosotros, obvio que sí.
> Para el computador, jamás: son tan distintos como una manzana y la foto de una
> manzana. Y fíjense en ese doble igual. Un solo igual guarda; dos iguales
> preguntan.

---

## 5. Decisiones y valores límite (25–34)

### Ejercicio 4

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
> Hasta ahora nuestros programas hacían siempre lo mismo. Ahora van a decidir.
>
> Se lee casi como una frase: if es "si"; elif es "si no, prueba esto otro"; y
> else es "en cualquier otro caso". Python pregunta de arriba hacia abajo y se
> queda con la primera que sea verdad.
>
> Dos cosas con las que Python es quisquilloso: la línea del if termina con dos
> puntos, y las líneas de abajo empiezan con cuatro espacios. Esos espacios le
> dicen qué instrucciones pertenecen a cada decisión.
>
> Con 3 crashes salió Critical. Ahora predigan: ¿qué sale con 0? ¿Y con 2?
> Escríbanlo, y después cambian el valor y comprueban.

**HAZ:** espera. Con 0 sale `No issues`; con 2 sale `Minor`.

**DI:**
> Con 2 sale Minor, porque dice menor o igual. Si dijera solo menor, el 2 se nos
> iría a Critical. Otra vez: un símbolo.

### Ejercicio 5

```python
fps = 30

if fps > 30:
    print("PASS")
else:
    print("FAIL")
```

**DI:**
> Y ahora sí, el momento que más me gusta de hoy. Les tengo un bug. *(pausa)*
>
> Lean la regla que está en el comentario: la prueba pasa si el juego corre a 30
> fps o más. El juego corre a 30. Y el programa dice FAIL.
>
> Fíjense que no hay ningún mensaje de error. El programa corre perfecto, muy
> tranquilo, y nos da un veredicto equivocado. Estos son los bugs más peligrosos,
> los que no avisan.
>
> Ustedes son QA. Encuéntrenlo y arréglenlo. Dos minutos.

**HAZ:** circula. La solución es cambiar `>` por `>=`. Cuando la mayoría lo tenga:

**DI:**
> ¡Exacto! La regla decía "30 o más" y el código decía "más de 30". Faltaba el
> igual. Un carácter.
>
> Y piensen en esto: este bug solo aparece cuando el valor es exactamente 30.
> Con 29 falla bien, con 60 pasa bien. Si nadie prueba justo el borde, este error
> llega a producción y vive ahí durante meses. Por eso en QA probamos los valores
> límite. Hoy lo vieron desde adentro: así se ve un bug de borde en el código.

---

## 6. Escribir desde cero (34–40)

### Ejercicio 6

**DI:**
> Hasta aquí han leído y corregido código. Ahora van a escribirlo ustedes, con
> la pantalla en blanco. Y les aviso algo con cariño: leer es una cosa y escribir
> es otra muy distinta. Es normal que cueste más, y es normal que salga un error.
> Cambien de persona en el teclado.
>
> Tienen un valor esperado y un valor real. Escriban un if else que muestre PASS
> si son iguales y FAIL si no lo son. Acuérdense: dos puntos, cuatro espacios y
> doble igual. Yo voy pasando.

**Respuesta:**

```python
if actual == expected:
    print("PASS")
else:
    print("FAIL")
```

**HAZ:** circula y celebra los aciertos en voz alta. Quien termine sigue con el reto.

**Si aparece un error, léelo con ellos en tres partes:** dónde (archivo y línea),
qué línea falló, y la última línea, que dice el tipo de error y el detalle.

| Lo que ven | Causa | Qué decir |
|---|---|---|
| `IndentationError` | Faltan los 4 espacios | "Mira la línea que dice el mensaje." |
| `SyntaxError: expected ':'` | Faltan los dos puntos | "¿Cómo termina la línea del if?" |
| `SyntaxError` con `if actual = expected` | Un solo igual | "Uno guarda, dos preguntan." |
| `NameError` | Un nombre mal escrito | "Compáralo letra por letra con el de arriba." |

**DI (si a alguien le sale un error):**
> ¡Un error! Qué bien, vengan a verlo. Miren: nos dice en qué línea está y qué
> pasó. Es una pista, y la vamos a seguir.

**DI (cuando la mayoría termine):**
> Paren un segundo y miren su pantalla. *(pausa)* Eso que escribieron es el
> corazón de una prueba automatizada: comparar lo real con lo esperado y dar un
> veredicto. Las herramientas con las que trabajamos hacen eso miles de veces,
> con muchas más reglas alrededor. Pero el centro es ese if. Y lo escribieron
> ustedes, en su primera clase.

---

## 7. Frostbite connection y cierre (40–45)

**HAZ:** cambia a FrostEd, con el objeto seleccionado y sus propiedades a la vista.

**DI:**
> Y ahora, mi parte favorita. Les presento a Frostbite. Hoy no lo van a tocar;
> solo quiero mostrarles una cosa.
>
> Este objeto tiene propiedades. Miren esta.

**HAZ:** señala la propiedad numérica que elegiste.

**DI:**
> Tiene un nombre, tiene un valor y tiene un tipo: es un número. *(pausa)* ¿A qué
> se parece? Exacto: a player_speed igual a 5. Es una variable. Un engine entero,
> con toda su complejidad, está construido con las mismas piezas que usaron hoy.

**HAZ:** cambia el valor. Si la propiedad tiene mínimo y máximo, muéstralos.

**DI:**
> Cuando alguien reporta "el jugador se mueve demasiado rápido", en algún lugar
> hay un valor como este que no es el esperado. Y en algún lugar hay una
> condición, un if, que decide qué pasa con ese valor. Y si esa condición tiene
> un mayor donde debía ir un mayor o igual, tenemos el bug que encontraron hace
> diez minutos, pero dentro de un juego.
>
> Ahora les soy sincero, como siempre. Encontrar ese bug en seis líneas no es lo
> mismo que encontrarlo dentro del engine, donde hay que saber dónde vive el
> valor, quién lo cambió y por qué. Entre una cosa y otra hay muchos escalones.
> Pero la forma de pensar es exactamente la misma, y hoy la practicaron de verdad.
>
> Miren lo que hicieron en 45 minutos: siguieron valores línea por línea,
> distinguieron textos de números, tomaron decisiones, cazaron un bug de valor
> límite y escribieron su primera comprobación desde cero.
>
> El martes le vamos a enseñar al programa a repetir: revisar cien resultados sin
> escribir cien líneas. Ahí esto se empieza a sentir como un superpoder.
>
> Tarea opcional de cinco minutos: hagan el reto del final del archivo. Y si algo
> les sale raro, péguenlo en el canal; me encanta que pregunten.
>
> Gracias por hoy, de verdad. Me voy feliz. Nos vemos el martes.

---

## Si vas mal de tiempo

La sesión está cargada. Recorta en este orden:

1. El ejercicio 1: dilo en dos frases, sin detenerte en los tipos.
2. El ejercicio 4: que solo prueben con el valor 2.
3. El ejercicio 6 pasa a ser la tarea, junto con el reto.

No recortes el ejercicio 2b ni el 5: son los dos que atacan lo que falló en el
diagnóstico. Tampoco la parte de Frostbite.

## Qué observar durante la clase

- **Quién duda en el 2b.** Son los que necesitan más práctica de trazado.
- **Quién no encuentra el bug del 5 en dos minutos.**
- **Cuántas parejas terminan el 6.** Mide la distancia entre leer y escribir, y te
  dice si el ritmo del martes puede mantenerse.
