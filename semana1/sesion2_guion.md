# Session 2 · Martes 13 de octubre
# Decisions and Errors

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual, con calma y
sonriendo. Lo que sigue a **HAZ** lo haces tú en pantalla. *(pausa)* es para
respirar y mirar al grupo.

**Al terminar, el participante puede:** leer y escribir un `if / else`, combinar
dos condiciones, y leer un mensaje de error identificando dónde, qué tipo y qué
pasó.

| Min | Bloque |
|---|---|
| 0–5 | Bienvenida y repaso |
| 5–16 | Condiciones: `if`, `else`, `elif` |
| 16–23 | El error a propósito |
| 23–37 | Práctica: test checker |
| 37–45 | Frostbite connection y cierre |

## Antes de que llegue la gente

1. VS Code abierto en la carpeta `semana1`, terminal abierta, letra grande.
2. Prueba `python sesion2_ejercicios.py`: deben salir `FAIL` y `Critical`.
3. Prueba `python sesion2_demo_assert.py`: debe terminar con `AssertionError`.
4. En FrostEd, ten a la vista la ventana donde el engine muestra sus mensajes
   (output o log). Si tienes a mano un ejemplo de warning o de assertion que
   puedas mostrar sin exponer nada sensible, déjalo preparado.
5. Confirma que los participantes tienen `sesion2_ejercicios.py`.

---

## 1. Bienvenida y repaso (0–5)

**DI:**
> ¡Buenas! ¿Cómo están? Qué gusto verlos otra vez. Les confieso que la clase del
> jueves me dejó de muy buen humor; hicieron un trabajo buenísimo.
>
> Antes de arrancar, calentemos con tres preguntas rápidas. No son examen, son
> para despertar la memoria. Respondan en voz alta, sin pena.
>
> ¿Qué es una variable?

**HAZ:** espera respuestas. Buscas: un nombre que guarda un valor.

**DI:**
> ¡Eso! Una caja con etiqueta. Segunda: ¿qué diferencia hay entre el 5 y el 5
> entre comillas?

**HAZ:** espera. Buscas: uno es número y el otro texto.

**DI:**
> Perfecto. Y la última: ¿qué responde siempre una comparación?

**HAZ:** espera. Buscas: True o False.

**DI:**
> Exacto, True o False. Y guárdense esa respuesta, porque es la llave de todo lo
> de hoy. Hasta ahora nuestros programas hacían siempre lo mismo, de arriba hacia
> abajo, sin pensar. Hoy les vamos a enseñar a decidir.
>
> Abran el archivo sesion2 ejercicios y ejecútenlo, igual que la vez pasada.

---

## 2. Condiciones (5–16)

### Ejercicio 1

```python
fps = 28

if fps >= 30:
    print("PASS")
else:
    print("FAIL")
```

**DI:**
> Lean conmigo, que esto se lee casi como una frase normal. fps vale 28. Luego
> viene la palabra if, que significa "si". Si fps es mayor o igual a 30, muestra
> PASS. Y else, que significa "si no", muestra FAIL.
>
> Como 28 no llega a 30, salió FAIL. El programa acaba de tomar su primera
> decisión.
>
> Ahora, Python es un poquito quisquilloso con dos cosas, y es mejor que se las
> presente yo antes de que se las encuentren solos. *(pausa)*
>
> Una: la línea del if termina con dos puntos. Siempre.
>
> Y dos: las líneas de abajo empiezan con cuatro espacios. Esos espacios no son
> decoración; le dicen a Python "esto de aquí pertenece al if".
>
> Cambien fps a 60, guarden y ejecuten, a ver qué pasa.

**HAZ:** cuando lo vean, demuestra la sangría. Borra los 4 espacios de
`print("PASS")` y ejecuta. Sale `IndentationError`.

**DI:**
> Miren lo que pasa si me como los espacios. Python se queja, pero se queja con
> educación: me dice exactamente en qué línea. Lo arreglo y seguimos como si nada.

### Ejercicio 2

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
> ¿Y si hay más de dos caminos? Para eso existe elif, que es una mezcla de else
> e if: "si no, prueba con esto otro". Python va preguntando de arriba hacia
> abajo y se queda con la primera respuesta que sea verdad.
>
> Con 3 crashes: ¿es igual a cero? No. ¿Es menor o igual a 2? Tampoco. Entonces
> cae en el else: Critical.
>
> Prueben con 0. Y después con 2. Pero antes de ejecutar el 2, apuesten con su
> pareja qué va a salir.

**HAZ:** espera. Con 2 sale `Minor`.

**DI:**
> ¿Quién ganó la apuesta? Salió Minor, porque dice menor o igual. Si dijera
> solamente menor, el 2 se nos iría a Critical. Un símbolo de diferencia.
>
> Y esto ustedes lo conocen mejor que nadie: los bugs viven en los bordes. Por
> eso en QA se prueban los valores límite. Ahora ya saben cómo se ven esos bordes
> desde adentro.

---

## 3. El error a propósito (16–23)

**DI:**
> Bueno, llegó el momento que les prometí. Vamos a romper el programa. A
> propósito, y con alegría. *(pausa)*
>
> Vayan al ejercicio 3. Hay una línea que empieza con numeral y luego print.
> Quítenle el numeral, guarden y ejecuten. Sin miedo.

**HAZ:** hazlo también. Sale:

```
Traceback (most recent call last):
  File "...sesion2_ejercicios.py", line 34, in <module>
    print("Crashes: " + crashes)
TypeError: can only concatenate str (not "int") to str
```

**DI:**
> ¡Ahí está! Qué belleza. Que nadie lo arregle todavía, déjenlo en pantalla.
>
> Sé que la primera reacción es de susto: mucho texto, palabras raras, todo en
> inglés. Yo también sentía eso. Pero les voy a mostrar que este mensaje tiene
> tres partes, y que son siempre las mismas tres. Cuando uno aprende a verlas,
> el miedo se va. *(pausa)*
>
> Primera parte, el dónde: nos dice el archivo y el número de línea.
>
> Segunda parte, la línea exacta que falló. Python nos la copia, por si acaso.
>
> Y tercera parte, la última línea, que es la más importante: el tipo de error y
> la explicación. TypeError: un problema de tipos. Y nos dice que no puede unir
> un texto con un número entero.
>
> ¿Se acuerdan del 5 y el 5 entre comillas? Aquí está la consecuencia en vivo.
> crashes es un número, y lo estamos pegando a un texto. El computador, que es
> literal, nos dice: eso no lo sé hacer.
>
> Quiero que se lleven esto para siempre: el error no es el enemigo. El error es
> el compañero más honesto que van a tener. Les dice dónde, les dice qué y casi
> siempre les dice por qué. Quien lo lee con calma, resuelve. Y les cuento que
> leer mensajes como este es una parte enorme de mi trabajo de todos los días.
>
> Ahora sí: vuelvan a ponerle el numeral a esa línea y guarden. Ya nos sirvió.

**Nota para ti:** el número de línea puede variar si añadieron o quitaron líneas.
El arreglo, por si preguntan, es `print(f"Crashes: {crashes}")`.

---

## 4. Práctica: test checker (23–37)

**DI:**
> Ahora les toca a ustedes, y este ejercicio me gusta mucho porque van a
> construir algo que se parece a una herramienta de verdad.
>
> Ejercicio 4: tienen un valor esperado y un valor real. Escriban un if else que
> muestre PASS si son iguales y FAIL si no lo son.
>
> Tres recordatorios cariñosos: dos puntos al final del if, cuatro espacios en
> las líneas de abajo, y doble igual para comparar. Cambien de persona en el
> teclado, y yo voy pasando.

**Respuesta:**

```python
if actual == expected:
    print("PASS")
else:
    print("FAIL")
```

**HAZ:** circula. Celebra los aciertos en voz alta. Cuando la mayoría termine:

**DI:**
> Paren un segundo y miren lo que tienen en pantalla. *(pausa)* Eso que acaban de
> escribir es la esencia de una prueba automatizada: comparar lo real con lo
> esperado y dar un veredicto. Las herramientas con las que trabajamos hacen eso
> miles de veces, con muchas más reglas. Pero el corazón es ese if que ustedes
> acaban de escribir. Y lo escribieron en su segunda clase.
>
> Vamos con el ejercicio 5, que le sube un poquito. Ahora son dos condiciones a
> la vez. La palabra and significa "y": exige que se cumplan las dos. Si fps es
> mayor o igual a 30 y además crashes es igual a 0, muestren Build OK. Si no,
> Build needs review.

**Respuesta:**

```python
if fps >= 30 and crashes == 0:
    print("Build OK")
else:
    print("Build needs review")
```

**DI:**
> Y ahora el reto: cambien los valores de fps y de crashes, arriba en el archivo,
> hasta lograr que salga Build OK.

**Errores típicos:**

| Lo que ven | Causa | Qué decir |
|---|---|---|
| `IndentationError` | Faltan los 4 espacios | "Mira la línea que dice el mensaje." |
| `SyntaxError: expected ':'` | Faltan los dos puntos | "¿Cómo termina la línea del if?" |
| `SyntaxError` con `if actual = expected` | Un solo igual | "Uno guarda, dos comparan." |
| Siempre sale lo mismo | No guardaron, o cambiaron el valor más abajo del `if` | "Guardar primero. Y Python lee de arriba hacia abajo." |

Quien termine antes hace el reto: el mensaje de FAIL con los dos valores.

---

## 5. Frostbite connection y cierre (37–45)

**HAZ:** en VS Code, abre `sesion2_demo_assert.py`.

**DI:**
> Antes de irnos a Frostbite quiero mostrarles una última línea de Python. Es
> cortita, pero es de las más importantes que van a ver en este programa.

```python
assert player_speed >= 0, "player_speed must not be negative"
```

**DI:**
> assert significa "afirmo". Es el programador diciendo: esto tiene que ser
> verdad siempre. La velocidad nunca debería ser negativa. Y si algún día lo es,
> detente y avísame.
>
> Arriba le puse menos uno, a propósito. Miren lo que pasa.

**HAZ:** ejecuta `python sesion2_demo_assert.py`. Sale `AssertionError`.

**DI:**
> AssertionError, y al lado el mensaje que dejó escrito el programador. Es como
> un if, pero con carácter: en lugar de mostrar FAIL, se detiene y grita.

**HAZ:** cambia a FrostEd, a la ventana de mensajes del engine.

**DI:**
> Y ahora sí, vengan conmigo a Frostbite. Aquí, en esta ventana, es donde el
> engine nos habla. Lo que para ustedes fue print, aquí son estos mensajes. Hay
> informativos, hay advertencias y hay errores.

**HAZ:** si preparaste un ejemplo de warning o de assertion, muéstralo ahora.

**DI:**
> ¿Se acuerdan de la última pregunta del diagnóstico, la del assertion? Ya la
> pueden responder. Cuando aparece uno durante una prueba, es exactamente lo que
> acabamos de ver: alguien escribió "esto siempre debe ser verdad", y dejó de
> serlo. No es ruido. Es el engine levantando la mano para avisarnos.
>
> Y ahora la parte sincera, como siempre. Ustedes ya entienden qué es un
> assertion, y eso es un montón. Pero ver uno no es lo mismo que saber qué lo
> causó. Para eso hay que saber qué sistema lo lanzó, qué valor esperaba y qué
> pasó antes. Eso se llama interpretar, y se gana con tiempo y experiencia.
>
> Lo que sí pueden hacer desde hoy, y marca una diferencia enorme, es reportarlo
> bien: el mensaje exacto, copiado tal cual, y los pasos que hicieron antes. Un
> reporte así le ahorra horas a quien lo recibe.
>
> Miren todo lo que llevan en dos clases: variables, tipos, operadores,
> condiciones, y leyeron su primer error sin salir corriendo. Siento mucho orgullo
> por este grupo, se los digo de corazón.
>
> El jueves vamos a ver cómo hacer que el programa repita una revisión cien veces
> sin tener que escribirla cien veces. Ahí es donde esto se empieza a sentir como
> un superpoder.
>
> Tarea opcional de cinco minutos: en el ejercicio 2, agreguen un nivel más. Por
> ejemplo, que con más de 10 crashes diga Blocker.
>
> Gracias por la energía de hoy. Nos vemos el jueves.

---

## Si vas mal de tiempo

Los textos son más largos que en la versión anterior, así que vigila el reloj.
Recorta en este orden:

1. El ejercicio 5 (`and`) pasa a ser la tarea.
2. En el ejercicio 2, prueba solo con el valor 2.
3. La demo de `assert` en Python: explícala de palabra y ve directo a FrostEd.

No recortes el error a propósito: es el momento más importante de la sesión.
