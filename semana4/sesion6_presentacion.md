# Session 6 · Presentación
# Mini-project: Test Results Validator

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion6_guion.md`.

Hoy la presentación se usa menos que en cualquier otra sesión: casi todo el
tiempo están en VS Code. Cada pantalla "Paso N" se queda proyectada mientras
trabajan.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–3 | 1. Apertura | 0–4 |
| 4–6 | 2. Los datos y la cuenta a mano | 4–8 |
| 7–9 | 3. De texto a diccionario | 8–13 |
| 10 | 4. La revisión | 13–19 |
| 11 | 5. El loop y el resumen | 19–27 |
| 12–16 | 6. La herramienta contra la cuenta a mano | 27–35 |
| 17–18 | 7. La herramienta se revisa a sí misma | 35–39 |
| 19–23 | 8. Frostbite y cierre | 39–45 |

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 6 · Mini-project
> Hoy construyen una herramienta.

**DI:**
> Buenos días. Gracias por estar aquí. Entren a la lección. Hoy no hay tema
> nuevo. Hoy construyen una herramienta, en parejas, paso a paso, con lo que ya
> saben. Empiezo por el final.

### 2 · A dónde van — Pregunta abierta

**En pantalla:** la salida final, como imagen, y la pregunta "¿Qué piezas de las que hemos visto crees que hay dentro?"

```
fps_main_menu PASS
fps_city_level PASS
fps_harbor_level FAIL
fps_boss_fight FAIL
tricks_detected PASS
session_minutes PASS
saved_replays FAIL
combo_points PASS
Passed: 5  Failed: 3
Pass rate: 62.5
```

**DI:**
> Esto es lo que va a mostrar su programa en cuarenta minutos. Lee un archivo
> con resultados de pruebas, revisa cada uno contra una regla, y entrega un
> resumen. Es un validador. Mirando solo esa salida: ¿qué piezas creen que hay
> dentro?

**HAZ:** guarda estas respuestas. Vuelves a ellas en la pantalla 19.

### 3 · Cómo se trabaja hoy — Diapositiva

**En pantalla:**
> Seis pasos. No pases al siguiente hasta que el actual muestre su "Debe salir".
>
> Si te atascas: 1. Lee el mensaje de error · 2. Pregunta a tu pareja ·
> 3. Pregúntame
>
> Hoy lleva el teclado quien menos lo ha llevado.
>
> **Ahora en VS Code:** dos archivos en la misma carpeta. Abre
> `sesion6_ejercicios.py` y ejecútalo.

**DI:**
> Hoy yo hablo poco. Cada paso dice de qué sesión viene y qué debe salir cuando
> está bien. Ejecuten: deben ver Session 6 ready y Lines 8.

### 4 · Paso 1: los datos — Diapositiva

**En pantalla:** el archivo, como imagen, y la regla.

```
fps_main_menu,30,60
fps_city_level,30,30
fps_harbor_level,30,28
fps_boss_fight,30,9
tricks_detected,5,5
session_minutes,10,12
saved_replays,3,0
combo_points,80,95
```

> `nombre,mínimo,valor_real`
> **La regla:** una prueba pasa si su valor real es **mayor o igual** que su mínimo.

**DI:**
> Abran test results punto txt. Cada línea es una prueba, con tres datos
> separados por comas. La regla de hoy es una sola. Aplíquenla a mano a las ocho
> líneas, y anoten cuántas pasan y cuántas fallan. Dos minutos. No se salten
> este paso: es lo que les va a permitir saber si su herramienta funciona.

### 5 · La cuenta a mano — Poll

**En pantalla:** "A mano: ¿cuántas pasan y cuántas fallan?"

**Opciones:** 6 y 2 · 5 y 3 · 4 y 4 · 3 y 5

**DI:**
> ¿Qué números tienen?

**Después:**
> Cinco y tres. Quien tenga otro número, revise las dos líneas donde el valor
> real es igual al mínimo.

### 6 · Idea clave — Diapositiva

**En pantalla:**
> Antes de construir una herramienta, se resuelve a mano un caso pequeño.
> Es la única forma de saber, después, si la herramienta dice la verdad.

**DI:**
> Guarden ese cinco y ese tres.

### 7 · Paso 2: de texto a diccionario — Diapositiva

**En pantalla:** captura de la función.

```python
def parse_line(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": parts[1], "actual": parts[2]}
```

> `strip` quita el salto de línea del final.
> `split` corta el texto por las comas y entrega una lista.

**DI:**
> Leer el archivo ya lo saben hacer, y ya está escrito. El problema es que cada
> línea llega como un solo texto, con todo pegado. Esta función ya está hecha;
> léanla con el método de la sesión 3. Recibe una línea de texto. Devuelve un
> diccionario con tres claves. En medio hay dos palabras nuevas, y están en
> pantalla. Predigan qué devuelve para la primera línea, y compruébenlo.

### 8 · ¿De qué tipo? — Poll

**En pantalla:** "¿De qué tipo es el valor de `"minimum"` en ese diccionario?"

**Opciones:** `int` · `str` · `float` · `list`

**DI:**
> Segunda predicción. Respondan y compruébenlo.

**HAZ:** **no expliques qué implica.** Solo di: "Anótenlo. Sigamos."

### 9 · Idea clave — Diapositiva

**En pantalla:**
> Una línea de un archivo es un texto.
> Convertirla en algo con nombres se llama **parsear**.

**DI:**
> Casi toda herramienta empieza haciéndolo.

### 10 · Paso 3: la revisión — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Paso 3 · 6 minutos**
> Escribe `check(test)`: recibe un diccionario, aplica la regla, devuelve
> `"PASS"` o `"FAIL"`.
>
> **La regla:** pasa si el valor real es mayor o igual que el mínimo.
> **Debe salir:** `PASS`

**DI:**
> Ahora escriben ustedes. Ya escribieron una casi igual en la sesión 3. Cambia
> la condición: la regla de hoy no es "igual"; es "mayor o igual".

**Mientras trabajan:** la tabla de errores está en el guion, bloque 4. No
corrijas a quien use `>` en lugar de `>=`: lo descubre en el paso 5.

### 11 · Paso 4: el loop y el resumen — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Paso 4 · 8 minutos**
> Por cada línea de `lines`:
> 1. Conviértela con `parse_line`
> 2. Revísala con `check`
> 3. Muestra el nombre y el resultado
> 4. Cuenta las que pasan y las que fallan
>
> Después del loop: `Passed: __  Failed: __`
>
> **Consejo:** primero el loop que muestra las ocho líneas. Después, los
> contadores.

**DI:**
> Tienen una función que convierte una línea y otra que revisa un diccionario.
> Falta aplicarlas a todas las líneas. Háganlo en dos partes.

**Mientras trabajan:** la tabla de errores y la respuesta completa están en el
guion, bloque 5. A los 25 minutos, pon la respuesta en pantalla para quien no
haya terminado: todos necesitan un resumen para el paso siguiente.

### 12 · Paso 5: ¿coincide? — Poll

**En pantalla:** "¿Qué resumen entrega tu herramienta?"

**Opciones:** Passed 5, Failed 3 · Passed 6, Failed 2 · Passed 3, Failed 5 · Otro

**DI:**
> Su herramienta ya entrega un resumen. ¿Qué dice?

**Después:**
> Seis y dos. A mano contaron cinco y tres. No coincide. Y antes de buscar nada:
> puede estar mal la herramienta, o puede estar mal su cuenta. No se asume: se
> compara prueba por prueba.

### 13 · ¿Cuál es? — Pregunta abierta

**En pantalla:** "Compara la lista de tu programa con el archivo. ¿Qué prueba tiene un resultado distinto al tuyo?"

**DI:**
> Un minuto. Encuentren cuál es.

**Después:**
> Fps boss fight. Mínimo 30, valor real 9, y la herramienta dice PASS. Sin
> ningún mensaje de error. Si no hubieran contado a mano, ese seis de ocho se
> habría ido a un reporte, con el nivel de peor rendimiento marcado como
> aprobado.

### 14 · Texto contra número — Poll

**En pantalla:** "¿Qué muestra `print(9 >= 30, "9" >= "30")`?"

**Opciones:** False False · False True · True True · Da error

**DI:**
> Para encontrar por qué, dos predicciones. ¿Nueve es mayor o igual que 30? ¿Y el
> texto "9" es mayor o igual que el texto "30"? Respondan y después ejecútenlo.

### 15 · Por qué — Diapositiva

**En pantalla:**
> `9 >= 30` → `False`
> `"9" >= "30"` → `True`
>
> Los textos se comparan letra por letra, como en un diccionario.
> `"9"` va después de `"3"`.
>
> **El arreglo:** `int("30")` convierte el texto `"30"` en el número `30`.

**DI:**
> Es la misma razón por la que, en una lista ordenada alfabéticamente, el
> archivo 9 queda después del archivo 30. Ustedes ya vieron hoy que estos
> valores eran texto: en el paso 2. Y la primera vez que vimos que un texto y un
> número no son lo mismo fue en la primera sesión. Decidan con su pareja dónde
> poner int, y corrijan. Debe salir cinco y tres.

### 16 · Idea clave — Diapositiva

**En pantalla:**
> No dio error. Entregó un resumen creíble. Estaba equivocada.
> Una herramienta de validación también se valida.

**DI:**
> Lo que la delató no fue leer el código: fue compararla con un caso contado a
> mano.

### 17 · Paso 6: un assert — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Paso 6 · 3 minutos**
> a) Un `assert`: las que pasan más las que fallan son todas las líneas.
> b) El porcentaje de éxito. **Debe salir:** `Pass rate: 62.5`

**DI:**
> Último paso. Su herramienta tiene algo que siempre debe ser verdad: si el
> archivo tiene ocho líneas, las que pasan y las que fallan tienen que sumar
> ocho. Escriban un assert que lo afirme, después del loop.

### 18 · Idea clave — Diapositiva

**En pantalla:**
> Hoy ese `assert` no dice nada.
> El día que alguien cambie el loop y rompa la cuenta, avisa en el momento.

**DI:**
> Un assert protege a la herramienta de los cambios futuros.

### 19 · Cinco partes — Diapositiva

**En pantalla:**
> Tu herramienta, vista desde lejos:
> **Lee → Convierte → Revisa → Cuenta → Resume**
>
> Archivo · lista · dos funciones · diccionario · loop · decisión · contadores ·
> assert

**DI:**
> Al empezar les pregunté qué piezas había dentro. Ahora saben que hay más. Unas
> veinte líneas. Y desde lejos hace cinco cosas en orden. Veamos una del engine.

### 20 · Frostbite — Diapositiva

**En pantalla:**
> **Frostbite**
> Busca las cinco partes.

**DI:**
> Pasemos a Frostbite.

**HAZ:** comparte FrostEd y sigue el bloque 8 del guion: secciones 2 y 3, y
después el código de la sección 4, preguntando dónde lee, revisa, cuenta y
resume. Opcional: `ReadOnlyDuplicateAssets`.

### 21 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Muchos casos de prueba, las mismas reglas.
> ¿Quién las revisa?

**DI:**
> Aterricemos esto al juego. El proyecto tiene muchos casos de prueba, escritos
> por muchas personas. Cada uno debería tener un nombre con el formato acordado,
> un autor, una descripción con sus pasos y un mensaje de fallo. Revisarlos a
> mano, uno por uno, no escala. Un validador hace lo que hicieron hoy: lee cada
> caso, lo convierte en datos con nombre, aplica las reglas, cuenta y resume. Lo
> que les falta para escribir uno no es Python: es saber cómo se le piden esos
> datos al engine, y qué reglas vale la pena revisar.

### 22 · Cierre — Poll

**En pantalla:** "¿Qué paso te costó más?"

**Opciones:**
- Paso 2: entender `parse_line`
- Paso 3: escribir `check`
- Paso 4: el loop y los contadores
- Paso 5: encontrar el bug
- Paso 6: el `assert`

**DI:**
> Para cerrar: de los pasos de hoy, ¿cuál les costó más? Eso decide el repaso
> del jueves.

### 23 · Resumen — Diapositiva

**En pantalla:**
> **Hoy:** un caso a mano · texto convertido en datos · una regla como función ·
> un archivo completo · una herramienta que mentía, corregida · un assert
>
> **Jueves:** última sesión. Repaso, diagnóstico final y el recorrido completo.
> **Tarea opcional:** los retos. El reto b une esta sesión con la del traceback.

**DI:**
> Gracias. El jueves es la última sesión: un repaso corto, el diagnóstico del
> primer día con otros valores, y el recorrido completo de una validación dentro
> del engine. Hoy construyeron una herramienta. Buen trabajo.
