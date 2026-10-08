# Session 2 · Presentación
# Repetition: Loops and Lists

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion2_guion.md`.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–3 | 1. Apertura y repaso | 0–5 |
| 4–7 | 2. Listas | 5–12 |
| 8–10 | 3. Repetir con `for` | 12–18 |
| 11–14 | 4. Seguir el contador | 18–26 |
| 15–17 | 5. El contador que no cuenta | 26–33 |
| 18–19 | 6. Escribir desde cero | 33–40 |
| 20–23 | 7. Frostbite y cierre | 40–45 |

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 2 · Repetition
> Una revisión, muchos datos.

**DI:**
> Buenos días. Gracias por volver. Entren a la lección con el código que ven en
> pantalla. Antes de avanzar, una pregunta sobre el jueves.

### 2 · Repaso — Poll

**En pantalla:** captura de este código, y la pregunta "¿Cuánto vale `y` al final?"

```python
x = 4
y = x
x = x + 1
```

**Opciones:** 4 · 5 · 1 · Da error

**DI:**
> Sin ejecutar nada. ¿Cuánto vale y al final? Respondan en su pantalla.

**Después de ver las respuestas:**
> Vale 4. Cuando escribimos y igual a x, se guardó una copia del valor que x
> tenía en ese momento. Una variable solo sabe lo que vale ahora.

### 3 · El problema de hoy — Diapositiva

**En pantalla:**
> El jueves: un dato.
> Hoy: cuarenta pruebas, doscientos builds, diez mil assets.
>
> **Ahora en VS Code:** abre `sesion2_ejercicios.py` y ejecútalo.

**DI:**
> El jueves cada programa revisaba un solo dato. En nuestro trabajo nunca hay un
> solo dato. Hoy vemos cómo decirle al computador que repita una revisión sobre
> todos, escribiéndola una sola vez. Abran el archivo de hoy y ejecútenlo. Deben
> ver Session 2 ready al inicio.

### 4 · Listas — Poll

**En pantalla:** captura de las dos líneas, y la pregunta "¿Qué es `results[0]`?"

```python
results = ["pass", "fail", "pass", "pass"]
print(len(results))
```

**Opciones:** "pass" · "fail" · La posición 0 no existe · Da error

**DI:**
> Una lista guarda varios valores, en orden, bajo un solo nombre. Len cuenta
> cuántos hay: cuatro. Para pedir uno se escribe el nombre y, entre corchetes,
> la posición. ¿Qué creen que es results, corchete, cero?

**Después:**
> Es pass, el primero. El computador cuenta desde cero. Quiten el numeral de esa
> línea y de la siguiente, y compruébenlo.

### 5 · La última posición — Poll

**En pantalla:** "La lista tiene 4 valores. ¿Qué hace `print(results[4])`?"

**Opciones:** Muestra "pass" · Muestra "fail" · No muestra nada · Da un error

**DI:**
> Queda una línea. Si hay cuatro valores y el primero está en la posición cero,
> ¿qué pasa al pedir la posición cuatro? Respondan antes de ejecutar.

### 6 · Ahora en VS Code — Diapositiva

**En pantalla:**
> **Ahora en VS Code**
> Quita el `#` de `print(results[4])`, ejecuta y lee **la última línea** del
> mensaje. Después vuelve a poner el `#`.

**DI:**
> Compruébenlo. Lean solo la última línea. IndexError: un problema con una
> posición. List index out of range: está fuera del rango. Pedimos la cuatro, y
> la última es la tres. Vuelvan a poner el numeral y guarden.

### 7 · Idea clave — Diapositiva

**En pantalla:**
> Cuatro elementos: posiciones 0, 1, 2 y 3.
> Equivocarse por uno es de los errores más frecuentes que existen.

**DI:**
> Una lista de cuatro elementos tiene las posiciones cero, uno, dos y tres. Ese
> borde es el valor límite de una lista.

### 8 · for — Diapositiva

**En pantalla:** captura de este código.

```python
for r in results:
    print("Checking:", r)
print("Done")
```

**DI:**
> Pedir los valores uno por uno no sirve cuando son doscientos. Para eso existe
> for. Se lee así: por cada r en results, haz lo que está debajo. Las reglas de
> formato son las del if: dos puntos al final, y cuatro espacios en lo que se
> repite. Miren su salida: Checking salió cuatro veces, y Done una sola.

### 9 · Cuatro espacios — Poll

**En pantalla:** "Si le pongo 4 espacios al inicio a `print("Done")`, ¿cuántas veces sale Done?"

**Opciones:** 0 · 1 · 4 · 5

**DI:**
> Predigan. Después háganlo en VS Code, comprueben, y déjenlo como estaba.

**Después:**
> Cuatro, y sale intercalado: Checking, Done, Checking, Done. En cada vuelta se
> ejecutan todas las líneas del loop antes de pasar al siguiente valor.

### 10 · Idea clave — Diapositiva

**En pantalla:**
> Los espacios deciden qué se repite y qué ocurre una sola vez.

**DI:**
> Mover una línea cuatro espacios cambia el programa. En diez minutos van a ver
> un defecto que es exactamente eso.

### 11 · El contador — Dibujo

**En pantalla:** captura del código y, debajo, la tabla vacía para llenar.

```python
fps_samples = [45, 30, 28, 60, 29]
low = 0

for fps in fps_samples:
    if fps < 30:
        low = low + 1
```

| vuelta | fps | fps < 30 ? | low |
|---|---|---|---|
| 1 | 45 | | |
| 2 | 30 | | |
| 3 | 28 | | |
| 4 | 60 | | |
| 5 | 29 | | |

**DI:**
> Este es el ejercicio central de hoy. La regla: contar cuántas muestras están
> por debajo de 30 fps. Una variable que empieza en cero y sube de uno en uno se
> llama contador. No ejecuten. Llenen la tabla con su pareja, una fila por
> vuelta: si la condición es verdadera o falsa, y cuánto vale low al terminar
> esa vuelta. Dos minutos.

### 12 · ¿Cuánto vale low? — Poll

**En pantalla:** "Al terminar el loop, `low` vale…"

**Opciones:** 1 · 2 · 3 · 5

**DI:**
> Antes de ver el resultado, respondan: ¿cuánto vale low al final?

### 13 · La tabla, llena — Diapositiva

**En pantalla:**

| vuelta | fps | fps < 30 ? | low |
|---|---|---|---|
| 1 | 45 | False | 0 |
| 2 | 30 | False | 0 |
| 3 | 28 | True | 1 |
| 4 | 60 | False | 1 |
| 5 | 29 | True | 2 |

**DI:**
> Vamos fila por fila. Vuelta dos, fps vale 30: treinta no está por debajo de
> treinta. Es el borde del jueves, visto desde el otro lado. Vuelta cuatro, la
> condición es falsa: low no vuelve a cero. Conserva lo que tenía. Solo cambia
> cuando una línea lo cambia. Quiten el numeral del print y comprueben: 2.

### 14 · Idea clave — Diapositiva

**En pantalla:**
> Un loop se lee vuelta por vuelta.
> Una fila por vuelta, y se mira en qué fila el valor deja de ser el esperado.

**DI:**
> Esta tabla es lo que hago yo cuando un contador da un número que no cuadra.

### 15 · El bug — Diapositiva

**En pantalla:** captura del código, con el texto "Regla: contar los builds con al menos un crash. A ojo: 3. El programa dice: 1."

```python
crashes_per_build = [0, 3, 0, 1, 2]

for crashes in crashes_per_build:
    builds_with_crashes = 0
    if crashes > 0:
        builds_with_crashes = builds_with_crashes + 1

print("Builds with crashes:", builds_with_crashes)
```

**DI:**
> El siguiente tiene un defecto, y no les voy a decir cuál. A ojo, tres builds
> tuvieron al menos un crash. El programa dice uno, sin ningún error. Y uno es
> un número creíble: con doscientos builds, se iría directo a un reporte.
> Encuéntrenlo y corríjanlo en VS Code. Tienen la tabla. Dos minutos.

### 16 · ¿Dónde está? — Pregunta abierta

**En pantalla:** "En una frase: ¿dónde está el defecto?"

**DI:**
> Cuando lo tengan, escríbanlo en una frase.

**Después:**
> La línea que pone el contador en cero está dentro del loop. Se ejecuta cinco
> veces, y en cada vuelta lo reinicia. El arreglo es moverla cuatro espacios a
> la izquierda, antes del for.

### 17 · Idea clave — Diapositiva

**En pantalla:**
> El defecto no estaba en lo que dice la línea, sino en dónde está.
> Un resultado creíble no es un resultado correcto.

**DI:**
> En un loop, la posición de una línea decide cuántas veces se ejecuta. Por eso
> se comprueba contra un caso que uno pueda contar a mano.

### 18 · Escríbelo tú — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 5 · 5 minutos**
> Cuenta cuántos `"pass"` hay. Debe salir: `Passed: 4`
>
> 1. Un contador en 0, **antes** del loop
> 2. Un `for` con un `if` adentro
> 3. Un `print`, **después** del loop

**DI:**
> Ahora lo escriben ustedes. Cambien de persona en el teclado. Necesitan tres
> piezas, y ya vieron las tres. Fíjense dónde va cada una.

**Mientras trabajan:** la tabla de errores está en el guion, bloque 6.

### 19 · Idea clave — Diapositiva

**En pantalla:**
> Seis resultados o seis mil: las mismas líneas.

**DI:**
> Esa es la razón por la que se automatiza. Lo que cambia es que, con seis mil,
> nadie puede comprobar el resultado a mano. Por eso lo que escribimos tiene que
> estar bien.

### 20 · Frostbite — Diapositiva

**En pantalla:**
> **Frostbite**
> Hoy solo observan.

**DI:**
> Pasemos a Frostbite.

**HAZ:** comparte FrostEd y sigue el bloque 7 del guion: la lista al inicio del
script, las secciones 3 y 4, y la sección 6 con el caso que falla.

### 21 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Un truco, una comprobación.
> ¿Y todos los trucos?

**DI:**
> Aterricemos esto al juego. El caso que vieron comprueba que el juego detecta
> un truco: un 360 flip, en goofy. Es una comprobación. Ahora piensen en cuántos
> trucos tiene el juego, y en que cada uno existe en más de un stance. Nadie
> escribe esa comprobación cien veces. Se escribe una, y se recorre la lista de
> trucos. Es el for de hoy, y el contador dice cuántos se detectaron bien.

### 22 · Cierre — Tablero

**En pantalla:** "¿Qué revisión de tu trabajo actual haces a mano muchas veces?"

**DI:**
> Para cerrar: ¿en qué parte de su trabajo hacen a mano una misma revisión
> muchas veces? Escríbanlo.

**HAZ:** guarda estas respuestas. Sirven para "En Skate" de las sesiones
siguientes y para el mini-proyecto.

### 23 · Resumen — Diapositiva

**En pantalla:**
> **Hoy:** listas y posiciones · lo que se repite y lo que no · un contador,
> vuelta por vuelta · un defecto de posición · un loop escrito por ustedes
>
> **Jueves:** funciones y diccionarios
> **Tarea opcional:** los tres retos al final del archivo

**DI:**
> Gracias. El jueves vemos cómo ponerle nombre a una revisión para usarla muchas
> veces sin copiarla. Lo que no les cuadre, al canal. Buen trabajo.
