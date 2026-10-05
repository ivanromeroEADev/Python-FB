# Session 2 · Martes 13 de octubre
# Decisions and Errors

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual. Lo que sigue a
**HAZ** lo haces tú en pantalla.

**Al terminar, el participante puede:** leer y escribir un `if / else`, combinar
dos condiciones, y leer un mensaje de error identificando dónde, qué tipo y qué
pasó.

| Min | Bloque |
|---|---|
| 0–5 | Repaso |
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

## 1. Repaso (0–5)

**DI:**
> Antes de empezar, tres preguntas rápidas del jueves. Respondan ustedes.
>
> ¿Qué es una variable?
>
> ¿Qué diferencia hay entre el 5 y el "5" entre comillas?
>
> ¿Qué responde siempre una comparación?

**Respuestas que buscas:** un nombre que guarda un valor · uno es número y el otro
texto · True o False.

**DI:**
> Esa última es la clave de hoy. Hasta ahora el programa hacía siempre lo mismo.
> Hoy va a decidir qué hacer según la respuesta sea True o False.

**HAZ:** todos abren `sesion2_ejercicios.py` y lo ejecutan.

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
> Lean conmigo. fps vale 28. Luego: if, que significa "si". Si fps es mayor o
> igual a 30, muestra PASS. Else, que significa "si no", muestra FAIL.
>
> Como 28 no llega a 30, salió FAIL.
>
> Dos detalles que Python exige. Uno: la línea del if termina con dos puntos.
> Dos: las líneas de abajo empiezan con cuatro espacios. Esos espacios le dicen a
> Python qué instrucciones pertenecen al if. No son decoración.
>
> Cambien fps a 60, guarden y ejecuten.

**HAZ:** demuestra la sangría. Borra los 4 espacios de `print("PASS")` y ejecuta.
Sale `IndentationError`.

**DI:**
> Esto pasa si faltan los espacios. Python nos dice la línea exacta. Lo arreglo y
> seguimos.

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
> Cuando hay más de dos caminos se usa elif, que es "si no, prueba esto otro".
> Python revisa de arriba hacia abajo y se queda con el primero que sea verdad.
>
> Con 3 crashes: ¿es igual a 0? No. ¿Es menor o igual a 2? No. Entonces cae en el
> else: Critical.
>
> Prueben con 0. Y luego con 2. Antes de ejecutar el 2, díganle a su pareja qué
> va a salir.

**HAZ:** espera. Con 2 sale `Minor`.

**DI:**
> Salió Minor porque dice menor o igual. Si dijera solo menor, el 2 caería en
> Critical. Los valores límite son donde más se esconden los bugs, y ustedes en
> QA ya lo saben: por eso se prueban los bordes.

---

## 3. El error a propósito (16–23)

**DI:**
> Ahora vamos a romper el programa a propósito. Vayan al ejercicio 3, quiten el
> símbolo numeral del inicio de la línea que empieza con print, guarden y ejecuten.

**HAZ:** hazlo también. Sale:

```
Traceback (most recent call last):
  File "...sesion2_ejercicios.py", line 34, in <module>
    print("Crashes: " + crashes)
TypeError: can only concatenate str (not "int") to str
```

**DI:**
> Que nadie lo arregle todavía. Vamos a leerlo, porque este mensaje tiene tres
> partes y siempre son las mismas.
>
> Primera parte, dónde: dice el archivo y el número de línea.
>
> Segunda parte, la línea exacta que falló: Python nos la copia.
>
> Tercera parte, la última línea, la más importante: el tipo de error y el
> detalle. TypeError: un problema de tipos. Y explica: no puede unir un texto con
> un número entero.
>
> ¿Se acuerdan del jueves, que el 5 y el "5" eran cosas distintas? Aquí está la
> consecuencia. crashes es un número, y lo estamos pegando a un texto.
>
> Quiero que se lleven esto: el error no es el enemigo. Dice dónde, dice qué y
> casi siempre dice por qué. Quien lee esto con calma resuelve; quien se asusta y
> cierra la ventana, no. Leer mensajes como este es una parte grande del trabajo
> técnico.
>
> Vuelvan a poner el símbolo numeral al inicio de esa línea y guarden.

**Nota para ti:** el número de línea puede variar si añadieron o quitaron líneas.
El arreglo, por si preguntan, es `print(f"Crashes: {crashes}")`.

---

## 4. Práctica: test checker (23–37)

**DI:**
> Ahora ustedes. Ejercicio 4: tienen un valor esperado y un valor real. Escriban
> un if else que muestre PASS si son iguales y FAIL si no. Recuerden: dos puntos
> al final del if, cuatro espacios en las líneas de abajo, y doble igual para
> comparar. Cambien de persona en el teclado.

**Respuesta:**

```python
if actual == expected:
    print("PASS")
else:
    print("FAIL")
```

**HAZ:** circula. Cuando la mayoría termine:

**DI:**
> Acaban de escribir la esencia de una prueba automatizada: comparar lo real con
> lo esperado y dar un veredicto. Las herramientas reales hacen esto miles de
> veces, con muchas más reglas, pero el corazón es ese if.
>
> Ejercicio 5: dos condiciones a la vez. La palabra and exige que se cumplan las
> dos. Si fps es mayor o igual a 30 y además crashes es igual a 0, muestren
> Build OK. Si no, Build needs review.

**Respuesta:**

```python
if fps >= 30 and crashes == 0:
    print("Build OK")
else:
    print("Build needs review")
```

**DI:**
> Ahora cambien los valores de fps y crashes, arriba en el archivo, hasta que
> salga Build OK.

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
> Antes de ir a Frostbite, una última cosa en Python. Miren esta línea.

```python
assert player_speed >= 0, "player_speed must not be negative"
```

**DI:**
> assert significa "afirmo". El programador está diciendo: esto siempre tiene que
> ser verdad. La velocidad nunca debería ser negativa. Si alguna vez lo es,
> detente y avisa.
>
> Arriba le puse menos uno a propósito. Lo ejecuto.

**HAZ:** ejecuta `python sesion2_demo_assert.py`. Sale `AssertionError`.

**DI:**
> AssertionError, con el mensaje que escribió el programador. Es un if que, en
> lugar de mostrar FAIL, se detiene y grita.

**HAZ:** cambia a FrostEd, a la ventana de mensajes del engine.

**DI:**
> Aquí es donde el engine nos habla. Lo que para ustedes fue print, aquí son
> estos mensajes. Hay informativos, hay advertencias y hay errores.

**HAZ:** si preparaste un ejemplo de warning o de assertion, muéstralo ahora.

**DI:**
> Cuando en una prueba aparece un assertion, es exactamente lo que acaban de ver:
> alguien escribió en el código "esto siempre debe ser verdad", y dejó de serlo.
> No es ruido. Es el engine diciendo que ocurrió algo que no debía ocurrir.
>
> Y aquí viene la parte honesta. Ustedes ya pueden entender qué es un assertion.
> Pero ver un assertion no es saber qué lo causó. Para eso hay que saber qué
> sistema lo lanzó, qué valor esperaba, qué pasó antes. Eso es interpretar, y
> toma tiempo y experiencia. Lo que sí pueden hacer desde hoy es reportarlo bien:
> el mensaje exacto, copiado tal cual, y los pasos que hicieron antes.
>
> Resumen de estas dos sesiones: variables, tipos, operadores, condiciones, y leyeron su
> primer error sin asustarse. El jueves vemos cómo hacer que el programa repita
> una revisión cien veces sin escribirla cien veces.
>
> Tarea opcional, cinco minutos: en el ejercicio 2, añadan un nivel más. Por
> ejemplo, que con más de 10 crashes diga Blocker.

---

## Si vas mal de tiempo

Recorta en este orden:

1. El ejercicio 5 (`and`) pasa a ser la tarea.
2. En el ejercicio 2, prueba solo con el valor 2.
3. La demo de `assert` en Python: explícala de palabra y ve directo a FrostEd.

No recortes el error a propósito: es el momento más importante de la sesión.
