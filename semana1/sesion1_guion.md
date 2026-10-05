# Session 1 · Jueves 8 de octubre
# Programming Foundations: Thinking Like a Programmer

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual. Lo que sigue a
**HAZ** lo haces tú en pantalla. Los tiempos son una guía.

**Al terminar, el participante puede:** explicar qué es una variable, reconocer
los cuatro tipos básicos, usar operadores y predecir el resultado de un programa
pequeño.

| Min | Bloque |
|---|---|
| 0–4 | Opening |
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

---

## 1. Opening (0–4)

**DI:**
> Bienvenidos. Este programa se llama Frostbite Technical Foundations. Hoy empezamos con el código: quedan siete
> sesiones de 45 minutos, martes y jueves.
>
> Quiero ser claro desde el principio con lo que es y lo que no es. No van a salir
> de aquí siendo Technical Testers de Frostbite. Eso toma mucho más que un mes.
> Lo que sí van a tener es la base sobre la que se construye ese trabajo:
> programación, lógica y saber leer lo que una máquina les dice.
>
> Vamos a trabajar así: ustedes escriben Python en Visual Studio Code. Yo les
> muestro la misma idea dentro de Frostbite. El mismo concepto en dos lugares.
>
> Tres reglas. Un error en pantalla es información, no un fracaso. Se trabaja en
> parejas y se turnan el teclado. Y nadie se va sin que algo le funcione.

**HAZ:** anuncia las parejas.

---

## 2. ¿Qué es programar? (4–8)

**DI:**
> Programar es darle instrucciones a un computador. Tiene tres características
> que conviene saber desde hoy.
>
> Primera: el computador hace exactamente lo que le escribimos, no lo que
> queríamos decir. Si la instrucción está mal, la ejecuta mal.
>
> Segunda: las ejecuta en orden, de arriba hacia abajo, una por una.
>
> Tercera: no se cansa. Lo que revisa una vez, lo revisa mil veces igual.
>
> Ustedes en QA ya piensan así. Un caso de prueba es una lista de pasos exactos,
> en orden, con un resultado esperado. Un programa es lo mismo, pero el que sigue
> los pasos es la máquina.

---

## 3. Setup (8–14)

**DI:**
> Ahora lo hacen ustedes. Síganme paso a paso. Si alguien se pierde, levanta la
> mano y esperamos.
>
> Uno: abran Visual Studio Code.
>
> Dos: arriba, File, Open Folder, y elijan la carpeta de ejercicios.
>
> Tres: a la izquierda, clic en sesion1_ejercicios.py.
>
> Cuatro: arriba, Terminal, New Terminal. Abajo aparece un panel. Ahí le damos
> órdenes al computador.
>
> Cinco: en ese panel escriban python, espacio, sesion1_ejercicios.py, y Enter.

**HAZ:** hazlo tú también.

**DI:**
> Si la primera línea dice Hello, QA team, acaban de ejecutar su primer programa.

**Si a alguien le falla:**

| Lo que le sale | Qué hacer |
|---|---|
| "python no se reconoce" | Que escriba `py` en vez de `python` |
| "No such file or directory" | No abrió la carpeta correcta: repetir el paso dos |
| No pasa nada | Escribió en el archivo y no en el panel de abajo, o no pulsó Enter |

---

## 4. Variables y tipos de datos (14–24)

**DI:**
> Vamos a leer el archivo juntos. Las líneas que empiezan con el símbolo numeral
> son comentarios: Python las ignora. Son notas para nosotros.

### Ejercicio 1

```python
print("Hello, QA team")
```

**DI:**
> print significa "muestra esto en pantalla". Lo que está entre comillas es texto
> y sale tal cual.
>
> Cambien el texto por su nombre. Guarden con Control S. En el panel de abajo,
> flecha hacia arriba para recuperar el comando, y Enter.

**HAZ:** espera a que todos lo vean. Recuerda: **guardar primero, ejecutar después.**

### Ejercicio 2

```python
player_name = "Alex"
player_speed = 5
player_health = 87.5
is_alive = True
```

**DI:**
> Esta es la idea más importante de hoy. Una variable es un nombre que guarda un
> valor. A la izquierda, el nombre. A la derecha, el valor. El signo igual no
> significa "es igual a"; significa "guarda esto aquí".
>
> player_speed guarda un 5. Cuando más abajo escribimos print(player_speed), sin
> comillas, Python no muestra la palabra: muestra lo que hay guardado.
>
> Cambien player_speed a 9, guarden y ejecuten.

### Ejercicio 3

```python
print(type(player_name))
```

**DI:**
> Cada valor tiene un tipo. Miren las cuatro líneas que salieron.
>
> str es texto, siempre entre comillas.
> int es un número entero.
> float es un número con decimales.
> bool es verdadero o falso: True o False.
>
> ¿Por qué importa? Porque el número 5 y el texto "5" entre comillas son cosas
> distintas para el computador. Con uno se puede calcular; con el otro no. Muchos
> bugs reales nacen de confundir un tipo con otro.

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
> Los operadores son los símbolos para calcular: más, menos, asterisco para
> multiplicar y barra para dividir.
>
> Aquí hay 40 pruebas y pasaron 34. La tercera variable no la escribimos a mano:
> se calcula restando. La cuarta es el porcentaje de pruebas que pasaron.
>
> Cambien tests_passed a 38. Antes de ejecutar, díganle a su pareja cuánto va a
> dar tests_failed.

**HAZ:** espera. Sale `2` y `95.0`.

**DI:**
> Cambiaron un solo número y los dos resultados se actualizaron solos. Para eso
> sirven las variables.

### Ejercicio 5

```python
expected_speed = 5

print(player_speed == expected_speed)
print(pass_rate >= 90)
print(player_health > 100)
```

**DI:**
> Hay otro grupo de operadores: los que comparan. Mayor, menor, mayor o igual.
> Y uno que confunde a todo el mundo: el doble igual.
>
> Un solo igual guarda un valor. Doble igual pregunta: ¿estos dos valores son
> iguales?
>
> Una comparación siempre responde True o False. Fíjense en la primera:
> player_speed doble igual expected_speed. Eso es exactamente un caso de prueba:
> valor real contra valor esperado.

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
> Sin ejecutar nada: ¿cuánto vale score al final? Acuérdenlo con su pareja.

**HAZ:** pide dos respuestas en voz alta. Luego quitan el `#` de `print(score)` y
ejecutan. Sale `30`.

**DI:**
> Línea por línea: empieza en 10. Luego toma el 10, le suma 5 y guarda 15. Luego
> toma el 15, lo multiplica por 2 y guarda 30. Leer código es esto: seguir el
> valor paso a paso.

### Ejercicio 7

**DI:**
> Ahora sin ayuda, y cambien de persona en el teclado. Creen una variable
> bugs_found con el valor 12, otra bugs_fixed con el valor 7, y una tercera,
> bugs_open, que sea la resta. Muéstrenla con print.

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

---

## 7. Frostbite connection y cierre (39–45)

**HAZ:** cambia a FrostEd, con el objeto seleccionado y sus propiedades a la vista.

**DI:**
> Esto es Frostbite. No lo van a tocar hoy; solo quiero que vean una cosa.
>
> Este objeto tiene propiedades. Miren esta.

**HAZ:** señala la propiedad numérica que elegiste.

**DI:**
> Tiene un nombre, tiene un valor y tiene un tipo. Es un número. Es lo mismo que
> escribieron hace un rato: player_speed igual a 5. Una variable.

**HAZ:** señala, si las hay, una propiedad de texto y una casilla de verdadero/falso.

**DI:**
> Esta otra es texto. Y esta casilla es un bool: verdadero o falso. Los mismos
> tipos que vimos.

**HAZ:** cambia el valor numérico y, si se puede ver el efecto, muéstralo.

**DI:**
> Cuando un bug dice "el jugador se mueve demasiado rápido", en algún lugar del
> engine hay un valor como este que no es el esperado. Valor real contra valor
> esperado: lo mismo que hicieron con el doble igual.
>
> Ahora, una advertencia honesta. Saber qué es una variable no es saber dónde
> vive ese valor en el engine, ni quién lo cambió, ni por qué. Entre lo que
> hicieron hoy y encontrar eso hay muchos escalones. Hoy subieron el primero.
>
> Resumen: hoy ejecutaron un programa, usaron variables, vieron los cuatro tipos
> y compararon valores. El martes el programa va a empezar a tomar decisiones, y
> vamos a romper algo a propósito para aprender a leer un error.
>
> Tarea opcional, cinco minutos: abran el archivo, cambien valores y predigan el
> resultado antes de ejecutar.

---

## Si vas mal de tiempo

Recorta en este orden:

1. El ejercicio 3 (tipos): explícalo tú sin que lo ejecuten.
2. El ejercicio 7 pasa a ser la tarea.
3. En "¿Qué es programar?", di solo las tres características.

No recortes el ejercicio 6 ni la parte de Frostbite.
