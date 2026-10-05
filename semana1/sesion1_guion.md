# Session 1 · Jueves 8 de octubre
# Programming Foundations: Thinking Like a Programmer

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual, con calma y
sonriendo. Lo que sigue a **HAZ** lo haces tú en pantalla. *(pausa)* es para
respirar y mirar al grupo. Los tiempos son una guía.

**Al terminar, el participante puede:** explicar qué es una variable, reconocer
los cuatro tipos básicos, usar operadores y predecir el resultado de un programa
pequeño.

| Min | Bloque |
|---|---|
| 0–4 | Bienvenida |
| 4–8 | ¿Qué es programar? |
| 8–14 | Setup: ejecutar el primer archivo |
| 14–24 | Variables y tipos de datos |
| 24–32 | Operadores |
| 32–39 | Ejercicio: predecir y crear |
| 39–45 | Frostbite connection y cierre |

## Antes de que llegue la gente

1. Abre **VS Code**. **File > Open Folder** → carpeta `semana1`.
2. **Terminal > New Terminal**. Escribe `python sesion1_ejercicios.py` y Enter.
   Deben salir 14 líneas, la primera es `Hello, QA team`. Escribe `cls` para limpiar.
3. Sube la letra: `Ctrl` y `+`, tres o cuatro veces.
4. En otra ventana, deja **FrostEd** abierto con un objeto seleccionado que tenga
   una propiedad numérica fácil de entender (una velocidad, una escala, una
   intensidad). La usarás al final.
5. Confirma que los participantes tienen `sesion1_ejercicios.py`.
6. Ten a mano la lista de parejas.

---

## 1. Bienvenida (0–4)

**DI:**
> ¡Hola, hola! Qué bueno verlos de nuevo. Les cuento que llevo desde el martes
> esperando este momento, porque hoy sí: hoy escribimos código.
>
> Primero, gracias por el diagnóstico. Me sirvió muchísimo, y les confirmo lo que
> les dije: nadie tiene de qué preocuparse. Empezamos desde el principio y vamos
> todos juntos.
>
> Tres acuerdos entre nosotros, que valen para todo el mes. *(pausa)*
>
> Uno: un error en pantalla no es un regaño, es una pista. Cuando les salga uno,
> y les va a salir, a mí me salen todos los días, lo vamos a leer con curiosidad.
>
> Dos: trabajamos en parejas y se turnan el teclado. Programar acompañado es más
> fácil y bastante más divertido.
>
> Y tres, que es una promesa mía: nadie se va de aquí hoy sin que algo le haya
> funcionado.

**HAZ:** anuncia las parejas con buen ánimo y dales unos segundos para acomodarse.

---

## 2. ¿Qué es programar? (4–8)

**DI:**
> Antes de tocar el teclado, una pregunta: ¿qué es programar? Suena a algo
> misterioso, de película, con pantallas verdes. Y la verdad es mucho más
> sencilla: programar es darle instrucciones a un computador. Nada más.
>
> Ahora, el computador es un compañero de trabajo muy particular, y tiene tres
> manías que conviene conocer desde hoy. *(pausa)*
>
> La primera: es absolutamente literal. Hace exactamente lo que le escribimos,
> no lo que queríamos decir. Si le damos una instrucción mal, la cumple mal, con
> toda la disciplina del mundo.
>
> La segunda: es ordenado. Lee de arriba hacia abajo, una línea a la vez, sin
> saltarse nada.
>
> Y la tercera, que es su superpoder: no se cansa. Lo que revisa una vez, lo
> revisa un millón de veces exactamente igual, sin aburrirse y sin pedir café.
>
> Y les digo algo: ustedes ya piensan así. Un caso de prueba es una lista de
> pasos exactos, en orden, con un resultado esperado. Un programa es lo mismo.
> La única diferencia es que quien sigue los pasos es la máquina. Así que hoy no
> arrancan de cero: arrancan con ventaja.

---

## 3. Setup (8–14)

**DI:**
> Bueno, manos al teclado. Vamos a hacerlo todos juntos y sin correr. Si alguien
> se pierde en un paso, levanta la mano y lo esperamos; aquí nadie se queda atrás.
>
> Paso uno: abran Visual Studio Code.
>
> Paso dos: arriba a la izquierda, File, y luego Open Folder. Elijan la carpeta
> donde guardaron el archivo de ejercicios.
>
> Paso tres: en el lado izquierdo aparece la lista de archivos. Hagan clic en
> sesion1 ejercicios.
>
> Paso cuatro: arriba, en el menú, Terminal, y luego New Terminal. Abajo se abre
> un panel. Ese panel es donde le hablamos directamente al computador.
>
> Y paso cinco, el momento de la verdad: en ese panel escriban python, espacio,
> sesion1 guion bajo ejercicios punto py. Y Enter.

**HAZ:** hazlo tú también, despacio.

**DI:**
> Si arriba les dice Hello, QA team... *(pausa)* ¡felicitaciones! Acaban de
> ejecutar su primer programa. En serio, ese es un momento que uno recuerda.

**Si a alguien le falla:**

| Lo que le sale | Qué hacer |
|---|---|
| "python no se reconoce" | Que escriba `py` en vez de `python` |
| "No such file or directory" | No abrió la carpeta correcta: repetir el paso dos |
| No pasa nada | Escribió en el archivo y no en el panel de abajo, o no pulsó Enter |

---

## 4. Variables y tipos de datos (14–24)

**DI:**
> Ahora vamos a leer el archivo juntos, con calma. Lo primero que van a notar es
> que hay muchas líneas que empiezan con el símbolo numeral. Esos son
> comentarios. Python los ignora por completo: son notas que nos dejamos entre
> personas, como un post-it pegado al código.

### Ejercicio 1

```python
print("Hello, QA team")
```

**DI:**
> Esta es la primera instrucción de verdad. print significa "muéstrame esto en
> pantalla". Lo que va entre comillas es texto, y sale tal cual.
>
> Hagamos el primer cambio: borren Hello, QA team y pongan su nombre. Guarden
> con Control S. Ahora, en el panel de abajo, presionen la flecha hacia arriba,
> que les trae de vuelta el último comando, y Enter.

**HAZ:** espera a que todos vean su nombre.

**DI:**
> ¿Lo ven? El computador acaba de decir su nombre porque ustedes se lo pidieron.
> Un detalle que les va a salvar la vida: primero se guarda, después se ejecuta.
> Si no guardan, el computador sigue leyendo la versión vieja.

### Ejercicio 2

```python
player_name = "Alex"
player_speed = 5
player_health = 87.5
is_alive = True
```

**DI:**
> Ahora sí, la idea más importante de hoy. Si se llevan una sola cosa de esta
> clase, que sea esta. *(pausa)*
>
> Una variable es un nombre que guarda un valor. Imagínense una caja con una
> etiqueta: a la izquierda está la etiqueta, a la derecha lo que metemos adentro.
>
> Y un detalle que confunde a todos al principio: ese signo igual no significa
> "es igual a", como en matemáticas. Aquí significa "guarda esto aquí".
>
> Entonces player_speed guarda un 5. Y más abajo, cuando escribimos print de
> player_speed, sin comillas, Python no muestra la palabra: abre la caja y
> muestra lo que hay adentro.
>
> Pruébenlo: cambien player_speed a 9, guarden y ejecuten.

### Ejercicio 3

```python
print(type(player_name))
```

**DI:**
> Miren las cuatro líneas siguientes que salieron. Cada valor tiene un tipo, y
> solo hay cuatro que necesitamos por ahora.
>
> str es texto, y siempre va entre comillas.
> int es un número entero.
> float es un número con decimales.
> Y bool es verdadero o falso: True o False. Nada más.
>
> ¿Se acuerdan del martes, del 5 más 5 que daba 55? Aquí está la explicación. El
> 5 solito es un número. El 5 entre comillas es un texto. Para nosotros se ven
> iguales; para el computador son tan distintos como una manzana y la foto de una
> manzana. Con una se puede hacer jugo; con la otra no.

---

## 5. Operadores (24–32)

### Ejercicio 4

```python
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100
```

**DI:**
> Ya sabemos guardar valores. Ahora vamos a hacer algo con ellos. Los operadores
> son los símbolos para calcular: el más, el menos, el asterisco para multiplicar
> y la barra para dividir.
>
> Miren el ejemplo, que es de nuestro mundo: hay 40 pruebas y pasaron 34. La
> tercera variable no la escribimos a mano; le pedimos al computador que haga la
> resta. Y la cuarta calcula el porcentaje de pruebas que pasaron.
>
> Ahora un juego: cambien tests_passed a 38. Pero antes de ejecutar, díganle a su
> pareja cuánto creen que va a dar tests_failed.

**HAZ:** espera. Sale `2` y `95.0`.

**DI:**
> ¿Acertaron? Fíjense en lo bonito de esto: cambiaron un solo número y los dos
> resultados se actualizaron solos. Eso es lo que hace poderosas a las variables.
> Uno cambia el dato en un lugar y todo lo demás se acomoda.

### Ejercicio 5

```python
expected_speed = 5

print(player_speed == expected_speed)
print(pass_rate >= 90)
print(player_health > 100)
```

**DI:**
> Hay otra familia de operadores, y esta les va a encantar porque es puro QA:
> los que comparan. Mayor que, menor que, mayor o igual.
>
> Y uno que hace tropezar a todo el mundo, a mí incluido cuando empecé: el doble
> igual. *(pausa)* Un solo igual guarda. Dos iguales preguntan: ¿estos dos
> valores son iguales?
>
> Una comparación siempre responde lo mismo: True o False. Miren la primera
> línea: player_speed doble igual expected_speed. Valor real contra valor
> esperado. ¿Les suena? Eso es, literalmente, un caso de prueba escrito en una
> línea.

**Nota para ti:** si cambiaron `player_speed` a 9 y `tests_passed` a 38, verán
`False`, `True`, `False`. Con los valores originales, `True`, `False`, `False`.
Las dos son correctas; aprovecha para preguntar por qué les salió distinto.

---

## 6. Ejercicio: predecir y crear (32–39)

### Ejercicio 6

```python
score = 10
score = score + 5
score = score * 2
```

**DI:**
> Ahora les propongo un reto, y este es sin ejecutar nada. Solo leyendo: ¿cuánto
> vale score al final? Pónganse de acuerdo con su pareja. Les doy medio minuto.

**HAZ:** pide dos respuestas en voz alta, sin decir cuál es correcta. Luego quitan
el `#` de `print(score)` y ejecutan. Sale `30`.

**DI:**
> ¡Treinta! Vamos paso a paso. Empieza en 10. La segunda línea toma ese 10, le
> suma 5 y guarda 15. La tercera toma el 15, lo multiplica por 2 y guarda 30.
>
> Lo que acaban de hacer se llama leer código: seguirle la pista a un valor,
> línea por línea. Y les cuento un secreto del oficio: los programadores pasamos
> mucho más tiempo leyendo código que escribiéndolo.

### Ejercicio 7

**DI:**
> Y para cerrar la parte práctica, uno sin ayuda. Cambien de persona en el
> teclado. Quiero que creen una variable llamada bugs_found con el valor 12, otra
> llamada bugs_fixed con el valor 7, y una tercera, bugs_open, que sea la resta
> de las dos. Y la muestran con print. Yo voy pasando por si me necesitan.

**Respuesta:**

```python
bugs_found = 12
bugs_fixed = 7
bugs_open = bugs_found - bugs_fixed
print(bugs_open)
```

Sale `5`.

**Si aparece un error, léelo con ellos:**

| Mensaje | Significa | Arreglo |
|---|---|---|
| `NameError: name 'bugs_fixd' is not defined` | El nombre está escrito distinto en dos sitios | Escribirlo igual; las mayúsculas cuentan |
| `SyntaxError: unterminated string literal` | Falta cerrar una comilla | Revisar las comillas de esa línea |
| `SyntaxError: '(' was never closed` | Falta cerrar un paréntesis | Añadir `)` |

**DI (si a alguien le sale un error):**
> ¡Un error! Qué bien, vengan todos a verlo. Miren: nos dice en qué línea está y
> qué pasó. Es una pista, y vamos a seguirla.

---

## 7. Frostbite connection y cierre (39–45)

**HAZ:** cambia a FrostEd, con el objeto seleccionado y sus propiedades a la vista.

**DI:**
> Ahora viene mi parte favorita de la clase. Les presento a Frostbite. Hoy no lo
> van a tocar; solo quiero mostrarles una cosa, y creo que les va a gustar.
>
> Este objeto que tengo seleccionado tiene propiedades. Miren esta de aquí.

**HAZ:** señala la propiedad numérica que elegiste.

**DI:**
> Tiene un nombre. Tiene un valor. Y tiene un tipo: es un número. *(pausa)* ¿A
> qué se parece? Exacto. Es lo mismo que escribieron hace veinte minutos:
> player_speed igual a 5. Es una variable.

**HAZ:** señala, si las hay, una propiedad de texto y una casilla de verdadero/falso.

**DI:**
> Esta otra es texto. Y esta casilla es un bool: verdadero o falso. Los mismos
> cuatro tipos que vimos hoy. Un engine entero, con toda su complejidad, está
> construido con estas mismas piezas.

**HAZ:** cambia el valor numérico y, si se puede ver el efecto, muéstralo.

**DI:**
> Cuando alguien reporta "el jugador se mueve demasiado rápido", en algún lugar
> del engine hay un valor como este que no es el esperado. Valor real contra
> valor esperado: lo mismo que hicieron hoy con el doble igual.
>
> Ahora, les soy sincero, porque los respeto. Saber qué es una variable no es lo
> mismo que saber dónde vive ese valor dentro del engine, quién lo cambió y por
> qué. Entre lo de hoy y eso hay muchos escalones. Pero hoy subieron el primero,
> y lo subieron bien. Siéntanse orgullosos.
>
> Repasemos lo que lograron en 45 minutos: ejecutaron un programa, usaron
> variables, conocieron los cuatro tipos de datos y compararon valores. Hace una
> hora nada de eso existía para ustedes.
>
> El martes el programa va a aprender a tomar decisiones. Y vamos a hacer algo
> que me divierte mucho: vamos a romperlo a propósito, para aprender a leer un
> error sin miedo.
>
> Les dejo una tarea opcional, de cinco minutos: abran el archivo, cambien
> valores y traten de adivinar el resultado antes de ejecutar. Y si algo les
> sale raro, escríbanlo en el canal; me encanta que pregunten.
>
> Gracias por hoy, de verdad. Me voy feliz. Nos vemos el martes.

---

## Si vas mal de tiempo

Los textos son más largos que en la versión anterior, así que vigila el reloj.
Recorta en este orden:

1. El ejercicio 3 (tipos): explícalo tú sin que lo ejecuten.
2. El ejercicio 7 pasa a ser la tarea.
3. En "¿Qué es programar?", di solo las tres manías del computador.

No recortes el ejercicio 6, la parte de Frostbite ni la despedida.
