# Diagnóstico inicial

16 preguntas · 20 minutos · 1 punto por pregunta.
Se responde antes de la sesión 1 y se repite idéntico el 29 de octubre.
No es una prueba de Frostbite. Todo el contenido es inventado.

## Cómo montarlo en Microsoft Forms

1. Crear un **Cuestionario** (se califica solo). Una sección por letra (A a F).
2. Todas las preguntas son de selección única. Añadir en cada una la opción
   **"No lo sé"**.
3. **Las preguntas con código se insertan como imagen.** Forms no respeta la
   sangría ni la letra de ancho fijo. Escribe el código en VS Code, haz una captura
   y añádela a la pregunta.
4. Forms ramifica por respuesta, no por puntaje. Al final de las secciones B y D,
   añadir una pregunta sin puntaje: *"Las siguientes preguntas son más difíciles.
   ¿Quieres continuar?"* → "Sí" sigue; "Prefiero terminar aquí" va al final.
5. Desactivar la opción de mostrar resultados automáticamente.

Texto de introducción:

> Este cuestionario no es un examen y no afecta a nadie. Sirve para saber por dónde
> empezar el programa. Si no sabes una respuesta, marca "No lo sé": adivinar
> estropea el resultado. Los resultados solo los ve el instructor.

Pregunta 0, sin puntaje: *Del 1 al 5, ¿cuánta experiencia tienes programando?*

---

## Section A — Computational Thinking

### A1

Sigue estas instrucciones en orden: empieza con el número 3. Súmale 2. Si el
resultado es mayor que 4, multiplícalo por 2; si no, réstale 1. ¿Qué número queda?

- a) 4
- b) 5
- c) 8
- d) 10 ✔

**Explicación:** 3 + 2 = 5. Como 5 es mayor que 4, se multiplica por 2: 10.
**Competencia:** seguir una secuencia con una decisión.
**Dificultad:** fácil.

### A2

Una regla dice: *"Un ID de caso de prueba es válido si empieza por `TC-` y después
tiene exactamente 4 números"*. ¿Cuál es válido?

- a) `TC-42`
- b) `TC-0042` ✔
- c) `TC_0042`
- d) `0042-TC`

**Explicación:** solo b) empieza por `TC-` y tiene 4 números. a) tiene 2, c) usa
guion bajo y d) está en otro orden.
**Competencia:** aplicar una regla con precisión.
**Dificultad:** fácil.

### A3

Tienes cuatro archivos: `a.png`, `b.wav`, `c.png`, `d.txt`. La instrucción es:
*"Por cada archivo, si termina en `.png`, anota su nombre"*. ¿Qué queda anotado?

- a) `a.png`
- b) `a.png` y `c.png` ✔
- c) Los cuatro
- d) Ninguno

**Explicación:** la instrucción se repite para cada archivo y solo dos cumplen la
condición.
**Competencia:** repetición con condición (la idea de un loop).
**Dificultad:** media.

---

## Section B — Programming Fundamentals

### B1

En programación, ¿qué es una variable?

- a) Un error que aparece a veces
- b) Un nombre que guarda un valor, y ese valor puede cambiar ✔
- c) Un archivo del programa
- d) Una operación matemática

**Explicación:** una variable es una etiqueta asociada a un valor.
**Competencia:** concepto de variable.
**Dificultad:** fácil.

### B2

¿Cuál de estos valores es un **texto** y no un número?

- a) `42`
- b) `"42"` ✔
- c) `4.2`
- d) `True`

**Explicación:** las comillas indican texto. `42` es un entero, `4.2` un decimal y
`True` un valor verdadero/falso.
**Competencia:** tipos de datos.
**Dificultad:** fácil.

### B3

Un programa sigue esta regla: *SI la vida es menor o igual a 0, mostrar "muerto";
SI NO, mostrar "vivo"*. La vida vale exactamente 0. ¿Qué muestra?

- a) vivo
- b) muerto ✔
- c) Las dos cosas
- d) Nada

**Explicación:** "menor o igual" incluye el 0. Los valores límite son donde más
errores aparecen.
**Competencia:** condiciones y valores límite.
**Dificultad:** media.

*Pregunta puente: ¿continuar?*

---

## Section C — Python

### C1

¿Qué muestra en pantalla?

```python
x = 5
x = x + 2
print(x)
```

- a) 5
- b) 7 ✔
- c) x + 2
- d) Da error

**Explicación:** la segunda línea toma el valor actual (5), le suma 2 y guarda 7.
**Competencia:** asignación y actualización de una variable.
**Dificultad:** fácil.

### C2

¿Qué muestra en pantalla?

```python
word = "crash"
print(len(word))
```

- a) crash
- b) 4
- c) 5 ✔
- d) Da error

**Explicación:** `len` cuenta los caracteres del texto: c-r-a-s-h son 5.
**Competencia:** funciones básicas de Python sobre texto.
**Dificultad:** media.

### C3

¿Qué muestra en pantalla?

```python
print("5" + "5")
```

- a) 10
- b) 55 ✔
- c) 5 5
- d) Da error

**Explicación:** entre comillas son textos, y sumar textos los une.
**Competencia:** diferencia entre texto y número en Python.
**Dificultad:** media.

---

## Section D — Code Reading

### D1

¿Qué muestra en pantalla?

```python
fps = 28
if fps >= 30:
    print("PASS")
else:
    print("FAIL")
```

- a) PASS
- b) FAIL ✔
- c) PASS y FAIL
- d) Nada

**Explicación:** 28 no es mayor o igual que 30, así que se ejecuta el `else`.
**Competencia:** leer una condición.
**Dificultad:** media.

### D2

¿Qué muestra en pantalla?

```python
results = ["pass", "fail", "pass", "fail", "fail"]
count = 0
for r in results:
    if r == "fail":
        count = count + 1
print(count)
```

- a) 2
- b) 3 ✔
- c) 5
- d) fail

**Explicación:** el loop recorre los 5 resultados y suma 1 cada vez que encuentra
"fail". Hay 3.
**Competencia:** leer un loop con una condición y un contador.
**Dificultad:** media.

### D3

¿Qué muestra en pantalla?

```python
def is_valid(speed):
    return speed > 0 and speed <= 10

print(is_valid(12))
```

- a) True
- b) False ✔
- c) 12
- d) Da error

**Explicación:** 12 es mayor que 0, pero no es menor o igual que 10. Con `and`,
las dos condiciones deben cumplirse.
**Competencia:** leer una función con una condición compuesta.
**Dificultad:** alta.

*Pregunta puente: ¿continuar?*

---

## Section E — Debugging

### E1

Un script termina con este mensaje. ¿Cuál es el problema?

```
Traceback (most recent call last):
  File "check.py", line 3, in <module>
    print(totl)
NameError: name 'totl' is not defined
```

- a) El archivo `check.py` no existe
- b) En la línea 3 se usa un nombre, `totl`, que no existe; probablemente está mal escrito ✔
- c) `print` no funciona en ese computador
- d) Falta instalar Python

**Explicación:** el mensaje indica el archivo, la línea y el tipo de error.
`NameError` significa que ese nombre no fue definido.
**Competencia:** leer un mensaje de error.
**Dificultad:** media.

### E2

Este código debería mostrar el promedio de 10, 20 y 30, que es 20. Pero muestra
40.0. ¿Por qué?

```python
a = 10
b = 20
c = 30
average = a + b + c / 3
print(average)
```

- a) Python no sabe dividir
- b) La división solo se aplica a `c`; faltan paréntesis ✔
- c) Los valores de las variables están mal
- d) `print` muestra el valor equivocado

**Explicación:** la división se hace antes que la suma: 10 + 20 + (30 / 3) = 40.
Lo correcto es `(a + b + c) / 3`. El programa no falla; da un resultado incorrecto
sin avisar.
**Competencia:** encontrar un error de lógica que no produce mensaje de error.
**Dificultad:** alta.

---

## Section F — Technical Thinking

### F1

Este es el log de un proceso que falló. ¿Cuál es la causa raíz?

```
[10:01:02] INFO  Job 4471 started
[10:01:05] WARN  Cache not found, downloading
[10:03:40] ERROR Could not open 'data/levels/city_01.json': file does not exist
[10:03:40] ERROR Step 'validate_levels' failed
[10:03:41] ERROR Job 4471 finished with exit code 1
```

- a) No se encontró la caché
- b) Falta el archivo `city_01.json` ✔
- c) Falló el paso `validate_levels`
- d) El job terminó con código 1

**Explicación:** el primer error es la causa; los dos siguientes son consecuencias.
La advertencia de la caché no detuvo nada.
**Competencia:** distinguir causa raíz, síntoma y ruido.
**Dificultad:** media.

### F2

Durante una prueba aparece este mensaje y el juego sigue funcionando:

```
Assertion failed: player_health >= 0
```

¿Qué te dice ese mensaje?

- a) Nada importante, porque el juego no se cerró
- b) Que el computador tiene poca memoria
- c) Que una condición que los programadores esperaban siempre verdadera fue falsa: la vida llegó a ser negativa ✔
- d) Que la prueba fue exitosa

**Explicación:** un assertion es una comprobación escrita en el código. Si falla,
algo ocurrió que no debía ocurrir, aunque el juego continúe. Se reporta con el
mensaje exacto y los pasos previos.
**Competencia:** interpretar una señal técnica.
**Dificultad:** alta.

---

## Lectura de resultados

| Puntaje | Nivel | Significado |
|---|---|---|
| 0 a 4 | Level 0 — No Foundation | Empieza desde conceptos computacionales básicos |
| 5 a 8 | Level 1 — Beginner | Comprende algunos conceptos; necesita práctica significativa |
| 9 a 12 | Level 2 — Foundational | Comprende programación básica y resuelve ejercicios sencillos |
| 13 a 16 | Level 3 — Strong Foundation | Lee código básico y razona sobre problemas |

**Ningún nivel habilita a nadie para validar Frostbite de forma independiente.**
El resultado solo indica el punto de partida.

**Parejas:** Level 0 con Level 1 o 2. Si hay algún Level 3, que circule ayudando.

**Clave rápida:** A1 d · A2 b · A3 b · B1 b · B2 b · B3 b · C1 b · C2 c · C3 b ·
D1 b · D2 b · D3 b · E1 b · E2 b · F1 b · F2 c

Antes de publicar, baraja el orden de las opciones en Forms (tiene una opción para
hacerlo): en esta clave casi todas las correctas son la b.
