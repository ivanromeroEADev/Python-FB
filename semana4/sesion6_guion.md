# Session 6 · Martes 27 de octubre
# Mini-project: Test Results Validator

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

No hay concepto nuevo. Hoy se juntan las piezas de cinco sesiones en una sola
herramienta: lee un archivo de resultados, revisa cada prueba contra una regla y
entrega un resumen. Tú hablas menos que en cualquier otra sesión; ellos escriben
más. El proyecto tiene un defecto que aparece solo, sin que nadie lo ponga: los
números leídos de un archivo son texto. Encontrarlo es la mitad del valor de la
sesión.

**Al terminar, el participante puede:** construir, con ayuda, un programa de unas
veinte líneas que combina archivo, lista, diccionario, función, loop, condición
y assert; comprobar una herramienta contra un caso contado a mano; y reconocer
esa misma estructura en una herramienta del engine.

## Mapa de la sesión

| Min | Bloque | Paso | Viene de | Tipo de interacción |
|---|---|---|---|---|
| 0–4 | 1. Apertura | | | Tú muestras el resultado final |
| 4–8 | 2. Los datos y la cuenta a mano | 1 | Sesión 5 | Conteo en parejas |
| 8–13 | 3. De texto a diccionario | 2 | Sesiones 3 y 5 | Predicción |
| 13–19 | 4. La revisión | 3 | Sesiones 1 y 3 | Escriben, tú circulas |
| 19–27 | 5. El loop y el resumen | 4 | Sesión 2 | Escriben, tú circulas |
| 27–35 | 6. La herramienta contra la cuenta a mano | 5 | Sesiones 1 y 4 | Caza de un bug |
| 35–39 | 7. La herramienta se revisa a sí misma | 6 | Sesión 4 | Escriben un assert |
| 39–45 | 8. Frostbite y cierre | | | Demostración y preguntas |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana4`, con la terminal abierta y la letra
   grande.
2. Ejecuta `python sesion6_ejercicios.py`. Debe mostrar `Session 6 ready` y
   `Lines: 8`.
3. Ejecuta `python sesion6_soluciones.py` y deja esa salida a mano, en otra
   ventana: es lo que muestras en la apertura. **No muestres el código.**
4. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S6_Validator` listo y la ventana de salida
   limpia. **Ejecútalo una vez antes de la clase.** Si la sección 4 dice "No se
   pudieron leer los assets", usa el plan B del bloque 8.
5. Opcional: una herramienta real de validación que puedas mostrar, abierta en
   una pestaña. Sirve `ztest/users/ivromero/Scripts/ReadOnlyDuplicateAssets`.
6. Los dos archivos publicados en el canal: `sesion6_ejercicios.py` y
   `test_results.txt`. **Van en la misma carpeta.**
7. **Parejas nuevas:** junta a quien escribe con soltura con quien todavía lee
   mejor de lo que escribe. Hoy el teclado lo lleva la segunda persona.

---

# Bloque 1 · Apertura (0–4)

**Propósito:** mostrar a dónde van a llegar, y dejar claro que hoy construyen
ellos.

**DI:**
> Buenos días. Gracias por estar aquí.
>
> Hoy no hay tema nuevo. Hoy construyen una herramienta. En parejas, paso a paso,
> con lo que ya saben.
>
> Empiezo por el final, para que sepan a dónde van.

**HAZ:** muestra la salida de `sesion6_soluciones.py`, la parte final: la lista de
pruebas con PASS y FAIL, `Passed: 5  Failed: 3` y `Pass rate: 62.5`. No muestres
el código.

**DI:**
> Esto es lo que va a mostrar su programa en cuarenta minutos. Lee un archivo con
> resultados de pruebas, revisa cada uno contra una regla, dice cuáles pasan y
> cuáles fallan, y entrega un resumen.
>
> Es un validador. Es pequeño, pero tiene la misma estructura que las
> herramientas de validación que corren sobre el juego. Al final les muestro una
> de verdad para que las comparen.

**PREGUNTA:**
> Mirando solo esa salida: ¿qué piezas de las que hemos visto creen que hay
> dentro?

**ESPERAS:** un loop, porque hay una línea por prueba. Un if, porque hay PASS y
FAIL. Contadores, por el resumen. Un archivo.

**HAZ:** anota en pantalla lo que digan. Vuelves a esa lista en el cierre.

**DI:**
> Bien. Hoy cambia la forma de trabajo. Yo voy a hablar poco. El archivo tiene
> seis pasos, y cada uno dice de qué sesión viene y qué debe salir cuando está
> bien. No pasen al siguiente hasta que el actual muestre lo que dice.
>
> Si se atascan, el orden es este: primero lean el mensaje de error, con el
> método de la sesión 4. Después pregúntenle a su pareja. Después, a mí.
>
> Hoy lleva el teclado quien menos lo ha llevado. Necesitan dos archivos en la
> misma carpeta. Abran sesion6 ejercicios y ejecútenlo.

**PREGUNTA:**
> ¿Todos ven Session 6 ready y Lines 8?

---

# Bloque 2 · Los datos y la cuenta a mano (4–8)

**Propósito:** que tengan un resultado contado a mano antes de escribir nada. Sin
esto, el bloque 6 no funciona.

## Paso 1

**HAZ:** abre `test_results.txt` en pantalla.

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

**DI:**
> Abran el archivo test results punto txt. Cada línea es una prueba y tiene tres
> datos separados por comas: el nombre, el mínimo exigido y el valor real que se
> midió.
>
> La regla de hoy es una sola: una prueba pasa si su valor real es mayor o igual
> que su mínimo.

**PREGUNTA:**
> La segunda línea: mínimo 30, valor real 30. ¿Pasa o falla?

**ESPERAS:** pasa. Mayor o igual.

**DI:**
> Pasa. Ahora apliquen la regla a mano a las ocho líneas, y anoten en el archivo
> cuántas pasan y cuántas fallan. Dos minutos. No se salten este paso: es lo que
> les va a permitir saber si su herramienta funciona.

**HAZ:** circula. Confirma que cada pareja escribió sus números. No los digas en
voz alta todavía.

**PREGUNTA:**
> ¿Qué números tienen?

**ESPERAS:** 8 líneas, 5 pasan, 3 fallan.

**SI FALLAN:**
> Revisemos las que tienen el valor real igual al mínimo. ¿Cuántas hay, y qué
> dice la regla sobre ellas?

**IDEA CLAVE:**
> Antes de construir una herramienta, se resuelve a mano un caso pequeño. Ese
> caso es la única forma de saber, después, si la herramienta dice la verdad.

---

# Bloque 3 · De texto a diccionario (8–13)

**Propósito:** que entiendan la única función que reciben hecha, y que noten, sin
que se lo digas, de qué tipo son los valores.

## Paso 2

```python
def parse_line(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": parts[1], "actual": parts[2]}
```

**DI:**
> Paso 2. Leer el archivo ya lo saben hacer; son las tres líneas del jueves, y
> ya están escritas.
>
> El problema es que cada línea llega como un solo texto, con todo pegado. Para
> trabajar con ella hay que separarla. Esta función ya está escrita, y la van a
> leer con el método de la sesión 3.

**PREGUNTA:**
> ¿Qué recibe y qué devuelve?

**ESPERAS:** recibe una línea de texto. Devuelve un diccionario con tres claves.

**DI:**
> Lo de en medio tiene dos palabras nuevas. Strip le quita al texto el salto de
> línea del final, el que el jueves dejaba una línea en blanco. Split corta el
> texto por las comas y entrega una lista con los pedazos.

**PREGUNTA:**
> La primera línea del archivo es fps main menu, coma, 30, coma, 60. Si split la
> corta por las comas, ¿qué hay en parts, corchete, cero? ¿Y en parts, corchete,
> dos?

**ESPERAS:** el nombre, y el 60.

**PREGUNTA:**
> Entonces, ¿qué devuelve parse line para esa primera línea? Escríbanlo antes de
> quitar el numeral.

**HAZ:** espera. Que quiten el `#` y ejecuten. Sale:

```
{'name': 'fps_main_menu', 'minimum': '30', 'actual': '60'}
```

**PREGUNTA:**
> Y la segunda predicción: ¿de qué tipo es el valor de minimum?

**HAZ:** pide dos predicciones. No comentes ninguna. Que quiten el `#` y ejecuten.
Sale `<class 'str'>`.

**HAZ:** **no expliques qué implica.** Solo di:

**DI:**
> Anótenlo. Sigamos.

**IDEA CLAVE:**
> Una línea de un archivo es un texto. Para trabajar con ella hay que
> convertirla en algo con nombres: un diccionario. Eso se llama parsear, y casi
> toda herramienta empieza haciéndolo.

---

# Bloque 4 · La revisión (13–19)

**Propósito:** escribir la función que aplica la regla. Es la del ejercicio 5 de
la sesión 3, con otra condición.

## Paso 3

**DI:**
> Paso 3. Ahora escriben ustedes.
>
> Una función que se llame check. Recibe un diccionario como el que acaban de
> ver, aplica la regla, y devuelve PASS o FAIL. Ya escribieron una casi igual en
> la sesión 3. Cambia la condición: la regla de hoy no es "igual"; es "mayor o
> igual".

**HAZ:** circula. Observa sin intervenir durante el primer minuto.

**Respuesta:**

```python
def check(test):
    if test["actual"] >= test["minimum"]:
        return "PASS"
    else:
        return "FAIL"
```

Con la línea de comprobación sin comentar debe salir `PASS`.

**Preguntas para hacer a cada pareja mientras circulas:**

- A quien se atascó: "Escriban primero la línea del def. ¿Qué recibe?"
- A quien no sabe sacar los valores: "Si la prueba se llama test, ¿cómo le piden
  su valor real? Miren las claves que mostró el paso 2."
- A quien tiene un error: "¿Qué dice la última línea del mensaje? ¿En qué línea?"
- A quien terminó: "¿Con qué línea del archivo probarían el borde de la regla?"

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| Sale `None` | Escribieron `print` en lugar de `return` | "¿Qué le falta a una función que devuelve None?" |
| `KeyError: 'min'` u otra clave | La clave no coincide con la de `parse_line` | "Compárenla letra por letra con las del paso 2." |
| `NameError: name 'actual' is not defined` | Escribieron `actual` en lugar de `test["actual"]` | "¿Dónde vive ese valor? ¿Quién lo tiene?" |
| `NameError: name 'check' is not defined` | Quitaron el `#` antes de escribir la función, o la escribieron debajo | "Cuando Python llega a esa línea, ¿ya conoce a check?" |
| Sale `FAIL` con la primera línea | La condición está al revés, o usaron `>` con los valores cambiados | "Léanme la regla. Ahora léanme la condición." |
| `IndentationError` | Faltan los 4 u 8 espacios | "¿A quién pertenece esa línea: a la función o al if?" |

**NO corrijas** a quien use `>` en lugar de `>=`: lo va a descubrir en el bloque 6
con `fps_city_level`. Sí toma nota de quién fue.

---

# Bloque 5 · El loop y el resumen (19–27)

**Propósito:** recorrer todas las líneas usando las dos funciones, contar y
resumir. Es el bloque donde más ayuda van a necesitar.

## Paso 4

**DI:**
> Paso 4. Tienen una función que convierte una línea en un diccionario, y otra
> que revisa un diccionario. Falta aplicarlas a todas las líneas.
>
> Escriban un loop que recorra lines. En cada vuelta: convierte la línea, la
> revisa, muestra el nombre y el resultado, y cuenta. Y después del loop, el
> resumen.
>
> Les recomiendo hacerlo en dos partes. Primero, solo el loop que muestra el
> nombre y el resultado. Ejecuten y comprueben que salen ocho líneas. Después
> agreguen los contadores.

**HAZ:** circula. Este es el momento de más trabajo para ti. Deja que cada pareja
llegue lo más lejos posible sola.

**Respuesta, primera parte:**

```python
for line in lines:
    test = parse_line(line)
    result = check(test)
    print(test["name"], result)
```

**Respuesta completa:**

```python
passed = 0
failed = 0

for line in lines:
    test = parse_line(line)
    result = check(test)
    print(test["name"], result)

    if result == "PASS":
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed:", passed, " Failed:", failed)
```

**Preguntas para hacer a cada pareja mientras circulas:**

- A quien no sabe cómo empezar: "¿Qué quieren recorrer? Escriban solo la línea
  del for."
- A quien no sabe qué va dentro: "En una vuelta tienen una línea de texto. ¿Qué
  función la convierte? Guarden lo que devuelve en una variable."
- A quien tiene el loop y no los contadores: "¿Dónde vio un contador que sube
  solo cuando se cumple una condición?"
- A quien terminó: "No me digan todavía si coincide con su cuenta a mano.
  Guárdenlo para el siguiente paso."

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| `TypeError: string indices must be integers` | Le pasaron la línea a `check` sin convertirla con `parse_line` | "¿Qué recibe check: un texto o un diccionario? ¿Qué le están entregando?" |
| `TypeError: list indices must be integers` | Usaron `lines["name"]` en lugar de `test["name"]` | "¿Eso es una prueba, o son todas?" |
| Sale el resumen ocho veces | El `print` del resumen está dentro del loop | "¿Cuántas veces quieren que se ejecute ese print?" |
| `Passed: 1  Failed: 0` o parecido | Los contadores se reinician dentro del loop | "¿Dónde vieron ese defecto? Sesión 2." |
| `NameError: name 'passed' is not defined` | No crearon los contadores antes del loop | "¿Cuánto vale passed antes de la primera vuelta?" |
| Todas dicen PASS, o `Passed: 8` | Compararon con `"pass"` en minúsculas, o usaron `=` | "Léanme la condición que decide a qué contador se suma." |
| Sale `<function check at 0x...>` | Escribieron `check` sin paréntesis | "¿La están llamando, o solo la están nombrando?" |

**HAZ:** cuando la mayoría tenga el resumen, detén al grupo. Las parejas que no
hayan llegado copian la respuesta completa de tu pantalla: lo importante ahora es
que todos tengan un resumen para el bloque siguiente.

---

# Bloque 6 · La herramienta contra la cuenta a mano (27–35)

**Propósito:** descubrir, comparando con la cuenta a mano, que la herramienta
miente. Es el bloque central de la sesión.

## Paso 5

**PREGUNTA:**
> Su herramienta ya entrega un resumen. ¿Qué dice?

**ESPERAS:** Passed 6, Failed 2.

**PREGUNTA:**
> ¿Y qué habían contado a mano?

**ESPERAS:** 5 y 3.

**DI:**
> No coincide. Antes de buscar nada, una pregunta.

**PREGUNTA:**
> ¿Cuál de los dos está mal: la herramienta, o su cuenta a mano? ¿Cómo lo
> sabrían?

**ESPERAS:** hay que revisar. Se compara prueba por prueba hasta encontrar la que
difiere.

**DI:**
> Esa es la actitud correcta: no asumir. Puede estar mal la cuenta a mano. Se
> comprueba prueba por prueba. Comparen la lista de su programa con el archivo, y
> encuentren cuál tiene un resultado distinto al de ustedes. Un minuto.

**PREGUNTA:**
> ¿Cuál es?

**ESPERAS:** `fps_boss_fight`. Mínimo 30, valor real 9. El programa dice PASS.

**DI:**
> Nueve fps en una pelea, y la herramienta dice que pasa. Sin ningún mensaje de
> error.
>
> Piensen en lo que eso significa. Si no hubieran contado a mano, este resumen,
> seis de ocho, se habría ido a un reporte. Y el nivel con peor rendimiento del
> juego habría quedado marcado como aprobado.
>
> Ahora hay que encontrar por qué. En el archivo hay dos predicciones.

**PREGUNTA:**
> ¿Nueve es mayor o igual que 30? ¿Y el texto "9" es mayor o igual que el texto
> "30"? Escriban las dos antes de ejecutar.

**HAZ:** pide predicciones. Casi todos dirán False y False. Que quiten el `#` y
ejecuten. Sale `False True`.

**DI:**
> El número 9 no es mayor que el número 30. Pero el texto 9 sí es "mayor" que el
> texto 30.
>
> Los textos no se comparan por su valor: se comparan como en un diccionario,
> letra por letra. La primera letra de uno es un 9; la del otro, un 3. El 9 va
> después. Fin de la comparación. Es la misma razón por la que, en una lista
> ordenada alfabéticamente, el archivo 9 queda después del archivo 30.

**PREGUNTA:**
> ¿En qué paso de hoy vieron que estos valores eran texto?

**ESPERAS:** en el paso 2. El tipo de `minimum` era `str`. Y la salida mostraba
`'30'` entre comillas.

**PREGUNTA:**
> ¿Y en qué sesión vimos por primera vez que un texto y un número no son lo
> mismo?

**ESPERAS:** en la primera. El 5 con comillas y el 5 sin comillas.

**DI:**
> En la primera sesión, y ese día pregunté dónde podría un dato llegar como
> texto cuando esperábamos un número. Aquí está: en cualquier cosa que se lea de
> un archivo.
>
> El arreglo es una instrucción nueva: int. Recibe un texto y devuelve el número
> entero. Decidan con su pareja dónde hay que ponerla, y corrijan.

**HAZ:** circula. Hay dos lugares válidos. No impongas uno.

**Respuesta (en `parse_line`, la más limpia):**

```python
return {"name": parts[0], "minimum": int(parts[1]), "actual": int(parts[2])}
```

**Respuesta alternativa (en `check`, también correcta):**

```python
if int(test["actual"]) >= int(test["minimum"]):
```

**HAZ:** confirma que a todos les sale `fps_boss_fight FAIL` y
`Passed: 5  Failed: 3`.

**PREGUNTA (si hubo parejas con cada solución):**
> Hay dos formas de arreglarlo. Unas parejas convirtieron los valores al leerlos;
> otras, al compararlos. ¿Qué ventaja tiene convertirlos al leerlos?

**ESPERAS:** que quedan como números para todo lo que venga después. Cualquier
otra revisión ya los recibe bien.

**SI ALGUIEN USÓ `>` EN EL PASO 3:** su resumen dice 3 y 5. Pregunta: "¿Cuáles dos
pruebas difieren ahora? ¿Qué tienen en común?". Son `fps_city_level` y
`tricks_detected`, las dos del valor límite.

**IDEA CLAVE:**
> La herramienta no dio error, entregó un resumen creíble, y estaba equivocada.
> Lo que la delató no fue leer el código: fue compararla con un caso contado a
> mano. Una herramienta de validación también se valida.

---

# Bloque 7 · La herramienta se revisa a sí misma (35–39)

**Propósito:** usar un assert como red de seguridad dentro de una herramienta
propia.

## Paso 6

**DI:**
> Último paso. En la sesión 4 vimos que un assert convierte un defecto silencioso
> en uno que avisa. Su herramienta tiene algo que siempre debe ser verdad.

**PREGUNTA:**
> Si el archivo tiene ocho líneas, ¿cuánto tienen que sumar las que pasan y las
> que fallan?

**ESPERAS:** ocho. El total de líneas.

**DI:**
> Escriban un assert que afirme eso, después del loop. Y debajo, muestren el
> porcentaje de éxito. Tres minutos.

**Respuesta:**

```python
assert passed + failed == len(lines), "every line must be counted exactly once"

pass_rate = passed / len(lines) * 100
print("Pass rate:", pass_rate)
```

Debe salir `Pass rate: 62.5`.

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| `SyntaxError` con un solo `=` | Un solo igual | "¿Ahí estás guardando o preguntando?" |
| `AssertionError` | Escribieron `8` y su archivo tiene otra cantidad de líneas, o un contador está mal | "¿Cuánto vale cada lado? Muéstrenlos con un print." |
| `Pass rate: 500.0` u otro número raro | Dividieron al revés, o faltan paréntesis | "¿Cómo encontraron el defecto del promedio en la sesión 4?" |

**PREGUNTA:**
> Ahora mismo ese assert no dice nada, porque se cumple. ¿En qué situación
> saltaría?

**ESPERAS:** si alguien cambia el loop y una línea deja de contarse, o se cuenta
dos veces.

**IDEA CLAVE:**
> Un assert protege a la herramienta de los cambios futuros. Hoy no hace nada. El
> día que alguien modifique el loop y rompa la cuenta, va a avisar en el momento,
> y no tres semanas después en un reporte.

---

# Bloque 8 · Frostbite y cierre (39–45)

**Propósito:** mostrar que una herramienta de validación del engine tiene las
mismas cinco partes, y decir con precisión qué les falta para escribir una.

**HAZ:** vuelve a la lista de piezas que anotaste en la apertura.

**DI:**
> Al empezar les pregunté qué piezas creían que había dentro. Dijeron estas.
> Ahora saben que hay más: un archivo, una lista, dos funciones, un diccionario,
> un loop, una decisión, dos contadores y un assert. Unas veinte líneas.
>
> Si lo miran desde lejos, su herramienta hace cinco cosas en orden: lee,
> convierte, revisa, cuenta y resume. Veamos una del engine.

**HAZ:** cambia a FrostEd, con el script `PyQV_S6_Validator`. Ejecútalo. Muestra
brevemente las secciones 2 y 3 de la salida.

**DI:**
> Las secciones 2 y 3 son su proyecto: con el defecto, seis y dos; arreglado,
> cinco y tres.

**HAZ:** baja a la sección 4. Muestra primero el código.

**PREGUNTA:**
> Miren el código de la sección 4, sin leer cada línea. Busquen las cinco partes.
> ¿Dónde lee y convierte?

**ESPERAS:** en `read_test_case`: recibe una ruta y devuelve un diccionario.

**PREGUNTA:**
> ¿Dónde revisa?

**ESPERAS:** en `check_test_case`.

**PREGUNTA:**
> ¿Dónde cuenta, y dónde resume?

**ESPERAS:** en el loop, con `passed` y `failed`. El resumen está después del
loop.

**PREGUNTA:**
> ¿Y hay un assert?

**ESPERAS:** sí, el mismo: que las que pasan más las que fallan sean todas.

**HAZ:** muestra la salida de la sección 4.

**DI:**
> La misma estructura, sobre assets en lugar de líneas de un archivo. Esta revisa
> cinco reglas en lugar de una, y en lugar de decir solo FAIL, dice por qué.

**HAZ (opcional, si tienes una herramienta real a mano):** abre
`ReadOnlyDuplicateAssets` y muestra su código, sin ejecutarlo.

**DI (opcional):**
> Y esta es una herramienta que uso en mi trabajo. Busca claves duplicadas en una
> colección de items. No la van a entender completa, y no hace falta.

**PREGUNTA (opcional):**
> ¿Qué reconocen?

**ESPERAS:** hay dos `for`, uno dentro de otro. Un diccionario. Un `if` con `in`.
Una lista donde se guardan los duplicados. Un resumen al final.

**DI:**
> Ahora la precisión de siempre, y hoy importa más que nunca, porque acaban de
> construir algo que funciona.
>
> Lo que les falta para escribir una herramienta como esa no es Python. El Python
> de esa herramienta es el que ya saben leer. Lo que falta está en la primera
> parte: leer. Saber qué hay dentro del engine, cómo se le piden los datos, qué
> forma tienen, y sobre todo, qué reglas vale la pena revisar. Eso es
> conocimiento del engine y del proyecto, y toma tiempo.
>
> Pero hay una diferencia entre el primer día y hoy. El primer día, una
> herramienta como esta era una caja cerrada. Hoy pueden abrirla, encontrar el
> loop, encontrar la regla, y hacerle a quien la escribió una pregunta precisa.

**PREGUNTA:**
> Para cerrar: de los seis pasos de hoy, ¿cuál les costó más?

**HAZ:** escucha tres o cuatro respuestas. Anótalas: es lo que repasas el jueves.

**DI:**
> Gracias, eso decide el repaso del jueves. Resumo lo que hicieron hoy:
> resolvieron un caso a mano, convirtieron texto en datos con nombre,
> escribieron una regla como función, la aplicaron a todo un archivo,
> descubrieron que su herramienta mentía y la corrigieron, y la dejaron
> protegida con un assert.
>
> El jueves es la última sesión. Hacemos un repaso corto, repetimos el
> diagnóstico del primer día con otros valores, para que cada quien vea cuánto
> se movió, y les muestro el recorrido completo de una validación dentro del
> engine.
>
> Tarea opcional: los retos al final del archivo. El reto b une esta sesión con
> la del traceback.
>
> Buen trabajo. Hoy construyeron una herramienta. Nos vemos el jueves.

**Plan B, si la sección 4 no pudo leer los assets:** muestra las secciones 2 y 3,
y después el código de la sección 4 sin su salida. Las cuatro preguntas sobre
dónde lee, revisa, cuenta y resume funcionan igual con el código solo.

**Dato para ti, por si preguntan:**

- Este formato de archivo, valores separados por comas, se llama CSV. Python
  tiene un módulo para leerlo. Aquí se usa `split` porque se entiende sin
  explicar nada más.
- `int("n/a")` da `ValueError`. Es el reto b: el traceback revienta dentro de
  `parse_line`, pero el origen está en el archivo de datos. Es la misma lección
  de la sesión 4.
- `int("28.5")` también da `ValueError`. Para decimales se usa `float`.
- `check_test_case`, en el script del engine, usa tres cosas que no se vieron:
  `append` agrega un elemento al final de una lista, `not` invierte un True o un
  False, y `startswith` pregunta si un texto empieza por otro.
- `ReadOnlyDuplicateAssets` usa `print "texto"`, sin paréntesis. Es la forma de
  la versión anterior de Python que usa FrostEd. Hace lo mismo.
- Si alguien pregunta por qué `"9" >= "30"` no da un error como
  `"Crashes: " + crashes`: porque comparar dos textos es una operación válida.
  El computador no sabe que queríamos números. No interpreta.

---

## Si vas mal de tiempo

El riesgo de hoy es que los bloques 4 y 5 se alarguen. Recorta en este orden:

1. Bloque 7: muestra tú el assert y el porcentaje; ellos lo copian.
2. Bloque 5: a los 25 minutos, pon la respuesta completa en pantalla para quien
   no haya terminado. No esperes a todas las parejas.
3. Bloque 3: omite la primera predicción y deja solo la del tipo.
4. Bloque 8: omite `ReadOnlyDuplicateAssets` y las secciones 2 y 3 del script.

No recortes el paso 1, el bloque 6 ni la parte del bloque 8 sobre qué les falta.
Si tienes que elegir entre que escriban el loop solos o llegar al bloque 6 con
tiempo, elige el bloque 6.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Paso 1 | Quién cuenta mal las dos pruebas del valor límite | Compáralo con la pregunta 7 del diagnóstico final |
| Paso 2 | Quién nota por su cuenta las comillas en `'30'` | Son quienes ya leen los tipos en una salida |
| Paso 3 | Quién escribe `>` en lugar de `>=`, y quién `print` en lugar de `return` | Los dos errores más repetidos del programa |
| Paso 4 | Cuántas parejas llegan al resumen sin tu ayuda | La medida más honesta de lo que pueden escribir hoy |
| Paso 5 | Quién sospecha primero de su cuenta a mano y quién del programa | Ninguna es incorrecta; lo que importa es que comprueben |
| Cierre | Qué paso dicen que les costó más | El repaso de la sesión 7 |
