# Session 4 · Martes 20 de octubre
# Debugging: Tracebacks, Assertions and Silent Bugs

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

En el diagnóstico, la pregunta del assertion la acertaron 5 de 9 y la del bug
silencioso 6 de 9. Hoy no se escribe código nuevo. Se rompe a propósito el que
ya saben leer, y se practica un método para cada una de las tres formas en que
un programa falla: con un mensaje, sin mensaje, y con un assertion.

**Al terminar, el participante puede:** leer un traceback en tres pasos, leerlo de
abajo hacia arriba cuando hay funciones, distinguir el lugar donde algo falla del
lugar donde se origina, encontrar un bug silencioso mostrando valores
intermedios, y explicar qué es un assertion y qué hacer cuando ve uno.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–4 | 1. Apertura | | Tú expones, una pregunta |
| 4–11 | 2. Las tres partes de un error | 1 | Todos provocan el mismo error |
| 11–18 | 3. El tipo de error | 2 | Predicción en parejas |
| 18–26 | 4. Dónde falla y dónde se origina | 3 | Lectura guiada, debate |
| 26–32 | 5. El bug que no avisa | 4 | Caza de un bug sin mensaje |
| 32–39 | 6. Assertions | 5 | Predicción, escriben un assert |
| 39–45 | 7. Frostbite y cierre | | Demostración y preguntas |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana3`, con la terminal abierta y la letra
   grande.
2. Ejecuta `python sesion4_ejercicios.py`. Debe correr sin errores y mostrar
   `Session 4 ready`, `Smoke 85.0`, `Average load time: 33.0` y `Still running`.
3. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S4_Debugging` listo y la ventana de salida
   limpia. **Ejecútalo una vez antes de la clase.** Este script **termina con un
   error a propósito** (sección 7): es lo que quieres mostrar. Si la sección 6
   dice "No se pudieron leer los assets", usa el plan B del bloque 7.
4. Mira cómo muestra tu versión de FrostEd el error final: en qué ventana, de qué
   color, con qué texto. En el bloque 7 lo vas a señalar.
5. El archivo `sesion4_ejercicios.py` publicado en el canal.
6. La lista de parejas a mano, y la respuesta del jueves sobre qué quedó menos
   claro.

---

# Bloque 1 · Apertura (0–4)

**Propósito:** cambiar el marco. Hoy los errores son el material de trabajo.

**DI:**
> Buenos días. Gracias por estar aquí.
>
> Durante tres sesiones construimos: variables, decisiones, loops, funciones. Y
> cada vez que apareció un error en pantalla, lo leímos rápido y seguimos.
>
> Hoy nos detenemos ahí. Esta sesión trata sobre lo que pasa cuando algo falla.
> Es la parte del programa más cercana a su trabajo, y el diagnóstico mostró que
> es donde hay más por ganar.
>
> Un programa puede fallar de tres formas. Puede detenerse y dejar un mensaje.
> Puede no detenerse, no decir nada y entregar un resultado equivocado. O puede
> tener escrito por adelantado qué debe ser siempre verdad, y avisar el día en
> que deja de serlo. Hoy vemos las tres, y para cada una hay un método.

**PREGUNTA:**
> Antes de empezar. Cuando en su trabajo aparece un mensaje de error largo, en
> inglés, ¿qué es lo primero que hacen?

**HAZ:** escucha dos o tres respuestas. No las corrijas. Es probable que digan
"lo copio y lo pego en el bug", "busco a alguien" o "lo cierro".

**DI:**
> Gracias. Todas son respuestas honestas. Al final de la sesión les voy a hacer
> la misma pregunta.
>
> Hoy el archivo de ejercicios se rompe a propósito. Lean las cinco líneas del
> encabezado: se trabaja una línea a la vez. Se predice, se quita el numeral, se
> ejecuta, se lee el mensaje, y se vuelve a poner el numeral. Si no lo vuelven a
> poner, el programa se detiene ahí y no llega a los ejercicios siguientes.
>
> Abran sesion4 ejercicios y ejecútenlo. Debe correr sin errores.

---

# Bloque 2 · Las tres partes de un error (4–11)

**Propósito:** fijar el método de tres pasos: dónde, qué línea, qué pasó.

## Ejercicio 1

```python
tests_total = 40
tests_passed = 34

# print(tests_pased)
```

**DI:**
> Ejercicio 1. Quiten el numeral de la línea del print, guarden y ejecuten. No lo
> arreglen. Lo quiero en todas las pantallas.

**HAZ:** hazlo también. Sale:

```
Traceback (most recent call last):
  File "...sesion4_ejercicios.py", line 20, in <module>
    print(tests_pased)
          ^^^^^^^^^^^
NameError: name 'tests_pased' is not defined. Did you mean: 'tests_passed'?
```

**DI:**
> Esto se llama traceback. Significa rastro. Son cuatro o cinco líneas, y la
> reacción natural es no leerlas. Vamos a leerlas, porque siempre tienen las
> mismas tres partes.

**PREGUNTA:**
> Primera parte: dónde. ¿En qué línea del archivo ocurrió?

**ESPERAS:** en la 20.

**PREGUNTA:**
> Segunda parte: Python copia la línea que falló. ¿Cuál es?

**ESPERAS:** `print(tests_pased)`.

**PREGUNTA:**
> Tercera parte, la última línea del mensaje. Tiene dos pedazos separados por dos
> puntos. ¿Qué dice cada uno?

**ESPERAS:** el tipo, `NameError`, y la explicación: ese nombre no está definido.

**DI:**
> NameError: un problema con un nombre. Y la explicación: ese nombre no existe.
> Le falta una letra.
>
> Fíjense que en muchas de sus pantallas Python incluso propone la corrección.
> No siempre lo hace, y dentro del engine no lo hace nunca. Por eso conviene
> saber leerlo sin esa ayuda.

**PREGUNTA:**
> De las tres partes, ¿cuál leerían primero si tuvieran prisa?

**ESPERAS:** la última línea.

**DI:**
> La última. Ahí está el qué. Después la línea, que dice el dónde. Escriban las
> tres respuestas en el archivo, y ahora sí, arréglenlo.

**HAZ:** confirma que a todos les sale `34` y que el archivo corre completo.

**IDEA CLAVE:**
> Un mensaje de error responde tres preguntas: dónde, qué línea y qué pasó. Quien
> lo lee en ese orden, de la última línea hacia arriba, ya tiene la mitad del
> problema resuelto antes de pedir ayuda.

---

# Bloque 3 · El tipo de error (11–18)

**Propósito:** que el nombre del error les diga algo antes de leer el resto.

## Ejercicio 2

```python
crashes = 3
builds = ["b01", "b02", "b03"]
build = {"name": "b01", "fps": 28}

# print("Crashes: " + crashes)                  # A
# print(builds[3])                              # B
# print(build["crashes"])                       # C
# print(tests_passed / (tests_total - 40))      # D
```

**DI:**
> La primera palabra de la última línea es el tipo de error. Hay decenas, pero
> cinco aparecen casi siempre, y ya han visto tres de ellos.
>
> En el ejercicio 2 hay cuatro líneas. Cada una produce un error distinto. Arriba
> están los cinco nombres posibles. Sin ejecutar nada, decidan con su pareja cuál
> le toca a cada línea. Dos minutos.

**HAZ:** espera. Después recorre las cuatro. Para cada una: pide la predicción al
grupo, y solo entonces que quiten el `#`, ejecuten, lean la última línea y vuelvan
a poner el `#`.

**PREGUNTA:**
> Línea A. ¿Qué error?

**ESPERAS:** TypeError.

**DI:**
> TypeError: un problema de tipos. El mensaje dice que solo puede unir texto con
> texto, y que recibió un entero. Es el cinco con comillas y el cinco sin
> comillas del primer día, ahora con consecuencias.

**PREGUNTA:**
> Línea B.

**ESPERAS:** IndexError. La lista tiene tres valores; la posición 3 no existe.

**PREGUNTA:**
> Línea C.

**ESPERAS:** KeyError. El diccionario no tiene la clave `crashes`.

**SI FALLAN (dirán NameError, porque arriba hay una variable crashes):**
> Buena observación: arriba sí existe una variable crashes. Pero aquí crashes
> está entre comillas, dentro de corchetes. No se busca una variable: se busca
> una clave dentro de build. ¿Qué claves tiene build?

**PREGUNTA:**
> Línea D. Esta no la hemos visto. ¿Cuánto vale lo que está entre paréntesis?

**ESPERAS:** cero. Y no se puede dividir entre cero: ZeroDivisionError.

**PREGUNTA:**
> De los cinco nombres, hay uno que no salió. ¿Cuál, y dónde lo vieron hoy?

**ESPERAS:** NameError, en el ejercicio 1.

**DI:**
> Ahora una pregunta distinta. Estos cinco errores se pueden agrupar por lo que
> están diciendo en el fondo.

**PREGUNTA:**
> ¿Cuáles dicen "me pediste algo que no existe"?

**ESPERAS:** NameError, IndexError y KeyError: un nombre, una posición y una clave
que no existen.

**IDEA CLAVE:**
> El tipo de error es la primera pista. NameError, IndexError y KeyError dicen
> "eso no existe". TypeError dice "eso existe, pero no es lo que esperaba".
> ZeroDivisionError dice "ese valor no puede ser cero". Con solo leer esa palabra
> ya saben qué clase de problema buscar.

---

# Bloque 4 · Dónde falla y dónde se origina (18–26)

**Propósito:** leer un traceback de varios niveles y separar el lugar donde
revienta del lugar donde está la causa. Prepara la sesión de logs.

## Ejercicio 3

```python
def pass_rate(passed, total):
    return passed / total * 100


def report(name, passed, total):
    rate = pass_rate(passed, total)
    print(name, rate)


report("Smoke", 34, 40)
# report("Nightly", 0, 0)
```

**DI:**
> Hasta aquí el error estaba en la misma línea que lo causaba. Casi nunca es así.
>
> Miren el ejercicio 3. Dos funciones del estilo de las del jueves. La primera
> calcula un porcentaje. La segunda usa a la primera y muestra el resultado.

**PREGUNTA:**
> En la salida dice Smoke 85. Síganlo: ¿quién llama a quién?

**ESPERAS:** la última línea llama a `report`, y `report` llama a `pass_rate`.

**PREGUNTA:**
> Ahora la línea comentada: un reporte de Nightly con cero pruebas pasadas, de
> cero pruebas totales. Antes de ejecutar: ¿qué error va a salir?

**ESPERAS:** ZeroDivisionError.

**HAZ:** que quiten el `#` y ejecuten. No lo corrijan. Sale:

```
Traceback (most recent call last):
  File "...sesion4_ejercicios.py", line 63, in <module>
    report("Nightly", 0, 0)
  File "...sesion4_ejercicios.py", line 56, in report
    rate = pass_rate(passed, total)
  File "...sesion4_ejercicios.py", line 52, in pass_rate
    return passed / total * 100
ZeroDivisionError: division by zero
```

**DI:**
> El mensaje creció. Ahora menciona tres líneas del archivo en lugar de una. Es
> el recorrido completo: quién llamó a quién hasta llegar al punto donde se
> detuvo.
>
> La primera línea del mensaje dice cómo leerlo: most recent call last. La
> llamada más reciente está al final. Por eso se lee de abajo hacia arriba.

**PREGUNTA:**
> Empecemos por abajo. ¿Qué pasó?

**ESPERAS:** una división entre cero.

**PREGUNTA:**
> Una línea más arriba. ¿En qué línea reventó, y dentro de qué función?

**ESPERAS:** línea 52, dentro de `pass_rate`.

**PREGUNTA:**
> Siguiente hacia arriba. ¿Quién llamó a pass rate?

**ESPERAS:** `report`, en la línea 56.

**PREGUNTA:**
> Y la de más arriba. ¿Quién llamó a report?

**ESPERAS:** la línea 63, la que acaban de descomentar.

**DI:**
> Ahora la pregunta importante. Miren la línea 52, donde reventó: passed dividido
> entre total, por cien.

**PREGUNTA:**
> ¿Esa línea está mal escrita?

**ESPERAS:** no. Con Smoke funcionó.

**PREGUNTA:**
> Entonces, ¿en cuál de las tres líneas está el origen del problema?

**ESPERAS:** en la 63. Ahí se entregó un total de cero.

**SI FALLAN (dirán la 52):**
> La 52 es donde se detuvo. Pero la misma línea funcionó con 34 y 40. ¿Qué
> cambió entre la llamada que funcionó y la que no?

**DI:**
> El programa reventó en la línea 52, y la causa está once líneas más abajo, en
> un dato. La línea 52 es el síntoma. Si alguien reporta "falla pass rate en la
> línea 52", está reportando el síntoma, y quien reciba ese reporte va a mirar
> una línea que no tiene nada malo.

**HAZ:** que vuelvan a poner el `#` y guarden.

**IDEA CLAVE:**
> El lugar donde algo revienta y el lugar donde se origina casi nunca son el
> mismo. El traceback muestra el camino entre los dos. La última línea dice qué
> pasó; para saber por qué, hay que subir.

---

# Bloque 5 · El bug que no avisa (26–32)

**Propósito:** un método para cuando no hay mensaje: mostrar valores intermedios.
Es la pregunta 15 del diagnóstico.

## Ejercicio 4

```python
load_a = 12
load_b = 15
load_c = 18

average = load_a + load_b + load_c / 3
print("Average load time:", average)
```

**DI:**
> Segunda forma de fallar: sin decir nada.
>
> Tres tiempos de carga: 12, 15 y 18 segundos.

**PREGUNTA:**
> De cabeza: ¿cuál es el promedio?

**ESPERAS:** 15.

**PREGUNTA:**
> ¿Y qué dice el programa?

**ESPERAS:** 33.

**DI:**
> Treinta y tres. No hay traceback, no hay número de línea, no hay tipo de error.
> Las herramientas de los últimos veinte minutos aquí no sirven, porque no hay
> mensaje que leer.
>
> Para estos casos el método es otro. El resultado final está mal, así que algún
> paso intermedio también lo está. Se muestran los pasos intermedios, uno por
> uno, y se compara cada uno con lo que uno espera.
>
> En el archivo hay dos predicciones. Cuánto vale la suma de los tres, y cuánto
> vale load c dividido entre tres. Escríbanlas. Después escriban dos print para
> comprobarlas. Dos minutos.

**HAZ:** circula. Los dos print son:

```python
print(load_a + load_b + load_c)
print(load_c / 3)
```

Salen `45` y `6.0`.

**PREGUNTA:**
> ¿Qué encontraron?

**ESPERAS:** la suma está bien, 45. Pero la división solo se aplica a `load_c`:
18 entre 3 es 6. Y 12 más 15 más 6 es 33.

**PREGUNTA:**
> ¿Por qué el computador divide primero, si la división está escrita al final?

**ESPERAS:** porque la división se hace antes que la suma, igual que en
matemáticas. Faltan paréntesis.

**HAZ:** que lo arreglen. Sale `Average load time: 15.0`.

**PREGUNTA:**
> Si los tres tiempos hubieran sido 0, 0 y 0, ¿este programa habría dado un
> resultado correcto o incorrecto?

**ESPERAS:** correcto: cero. El defecto estaría ahí, sin verse.

**DI:**
> Y alguien lo habría dado por bueno. Un programa que no da error no es un
> programa correcto. Solo es un programa que no se detuvo.

**IDEA CLAVE:**
> Cuando no hay mensaje, se mira adentro. Se muestran los valores intermedios y
> se comparan con lo esperado, hasta encontrar el primero que no coincide. Es lo
> mismo que hicieron con la tabla del loop: buscar el punto exacto donde el valor
> deja de ser el que debía.

---

# Bloque 6 · Assertions (32–39)

**Propósito:** que entiendan un assertion como una expectativa escrita por
adelantado, y que escriban uno. Es la pregunta 17 del diagnóstico.

## Ejercicio 5a y 5b · Leer un assert (4 minutos)

```python
player_health = 20
damage = 35
player_health = player_health - damage

# print(player_health)
# assert player_health >= 0, "player_health must not be negative"
print("Still running")
```

**DI:**
> Tercera forma. El defecto anterior lo encontramos porque sabíamos que el
> promedio debía ser 15. Esa expectativa estaba en nuestra cabeza. La pregunta
> es qué pasaría si estuviera escrita en el código.
>
> Ejercicio 5. Un jugador con 20 de vida recibe 35 de daño.

**PREGUNTA:**
> ¿Cuánto vale player health después de la tercera línea?

**ESPERAS:** menos 15.

**HAZ:** que quiten el `#` del `print` y ejecuten. Sale `-15`, y después
`Still running`.

**PREGUNTA:**
> ¿Tiene sentido una vida de menos quince?

**ESPERAS:** no.

**DI:**
> No. Y sin embargo el programa siguió: dice Still running. Es otro defecto
> silencioso. El valor es imposible y nadie se enteró.
>
> Ahora lean la línea siguiente. Assert significa "afirmo". Es quien programa
> diciendo: afirmo que la vida es mayor o igual a cero; esto tiene que ser verdad
> siempre. Y después de la coma, un mensaje para el caso en que no lo sea.

**PREGUNTA:**
> Predigan. Si activo esa línea, ¿sale Still running?

**HAZ:** pide dos predicciones. Que quiten el `#` y ejecuten. Sale:

```
Traceback (most recent call last):
  File "...sesion4_ejercicios.py", line 99, in <module>
    assert player_health >= 0, "player_health must not be negative"
AssertionError: player_health must not be negative
```

**ESPERAS:** no. El programa se detiene en el assert.

**PREGUNTA:**
> Léanlo con el método de hoy. ¿Qué pasó, y dónde?

**ESPERAS:** AssertionError, con el mensaje que se escribió; en la línea 99.

**DI:**
> Un assert convierte un defecto silencioso en uno que avisa. Si la condición es
> verdadera, no hace nada y nadie lo nota. Si es falsa, detiene el programa en
> ese punto exacto, con el mensaje que dejó escrito quien lo programó.

**HAZ:** que vuelvan a poner el `#` en la línea del assert y guarden.

## Ejercicio 5c · Escribir un assert (3 minutos)

**DI:**
> Ahora escriban uno. Vuelvan al ejercicio 4, el del promedio. Ustedes sabían que
> el resultado debía ser 15. Escriban, en el espacio del 5c, un assert que afirme
> eso, con un mensaje. Cambien de persona en el teclado.

**Respuesta:**

```python
assert average == 15, "average should be 15"
```

**HAZ:** circula. Cuando lo tengan, pídeles que deshagan el arreglo del ejercicio
4, quitando los paréntesis, y ejecuten. El assert debe detener el programa. Luego
que restauren los paréntesis.

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| `SyntaxError` con `assert average = 15` | Un solo igual | "¿Ahí estás guardando o preguntando?" |
| El assert salta aunque el promedio esté bien | Escribieron la condición al revés, por ejemplo `!= 15` | "Un assert afirma lo que debe ser verdad. Léanme lo que afirmaron." |
| El assert no salta con el bug | Lo escribieron antes de calcular `average`, o el ejercicio 4 ya está arreglado | "¿Cuánto vale average en este momento? Muéstrenlo con un print." |
| `NameError: name 'average' is not defined` | Mal escrito | "Compáralo letra por letra con el de arriba." |
| `SyntaxWarning: assertion is always true` | Usaron paréntesis: `assert(average == 15, "...")` | "assert no es una función. Quiten los paréntesis." |

**PREGUNTA (al grupo):**
> En el diagnóstico había una pregunta: aparece Assertion failed, player health
> mayor o igual a cero, y el juego sigue funcionando. ¿Qué les dice ese mensaje
> ahora?

**ESPERAS:** que alguien escribió que la vida nunca debía ser negativa, y lo fue.
Algo que no debía pasar, pasó.

**IDEA CLAVE:**
> Un assertion no es ruido. Es una persona del equipo de desarrollo que dejó
> escrito, a veces años atrás, "esto nunca debería pasar". Cuando aparece, pasó.
> Y trae el dato más valioso que puede tener un reporte: qué se esperaba.

---

# Bloque 7 · Frostbite y cierre (39–45)

**Propósito:** mostrar que el engine habla con los mismos mensajes, y decir con
precisión qué pueden hacer con uno y qué no.

**HAZ:** cambia a FrostEd, con el script `PyQV_S4_Debugging`. Ejecútalo. Muestra
la sección 1 de la salida.

**DI:**
> Pasemos a Frostbite. Este script provoca los mismos errores que provocaron
> ustedes.

**PREGUNTA:**
> Miren la sección 1. Sin que yo diga nada: ¿dónde está el dónde, y dónde está el
> qué pasó?

**ESPERAS:** señalan el número de línea y la última línea, `NameError`.

**DI:**
> Las mismas tres partes. La redacción puede cambiar un poco, porque el engine
> usa una versión anterior de Python, y aquí no aparece la sugerencia de
> corrección. El tipo de error y la forma del mensaje son los mismos.

**HAZ:** baja a la sección 6. Muestra el código: los tres `assert`.

**DI:**
> Sección 6. Tres cosas que siempre deben ser verdad en un caso de prueba: que
> tenga nombre, que tenga autor, y que describa cinco pasos o más. Están escritas
> como tres assert, y se aplican a los dos assets de las sesiones anteriores.

**HAZ:** muestra la salida de la sección 6.

**PREGUNTA:**
> Uno de los dos dice Assertion failed. Lean el mensaje. ¿Qué se esperaba, y qué
> llegó?

**ESPERAS:** se esperaban al menos 5 pasos y llegó 1.

**DI:**
> El mensaje dice las dos cosas, porque quien lo escribió se tomó el trabajo de
> ponerlas. No todos los assertions son así de claros. Algunos solo muestran la
> condición.

**HAZ:** baja a la sección 7. Muestra cómo FrostEd presenta el error final, el que
nadie atrapó. Señala la ventana, el color y el texto.

**DI:**
> Y la última sección. Hasta aquí el script atrapaba cada error y seguía. Este
> último no lo atrapa nadie. Así se ve dentro del editor un assertion sin
> atrapar. Es el mismo AssertionError que vieron en su terminal.
>
> Ahora la parte que más me importa que quede clara.
>
> Ya saben qué es un assertion, y saben leer su mensaje. Eso es más de lo que
> sabe mucha gente que los ve todos los días. Lo que todavía no pueden hacer, y
> no se espera que hagan, es decir qué lo causó. Para eso hay que saber qué
> sistema lo lanzó, qué valor esperaba, y qué ocurrió antes, a veces varios
> minutos antes. Eso se llama interpretar, y se gana con tiempo dentro del
> engine.
>
> Lo que sí pueden hacer desde hoy, y cambia mucho la calidad de un reporte, son
> tres cosas. Copiar el mensaje exacto, completo, sin resumirlo. Anotar los pasos
> que hicieron antes de que apareciera. Y no descartarlo porque el juego siguió
> funcionando.

**PREGUNTA:**
> Vuelvo a la pregunta del inicio. Cuando aparece un mensaje de error largo, en
> inglés, ¿qué es lo primero que van a hacer ahora?

**ESPERAS:** leer la última línea. Después, dónde.

**HAZ:** escucha dos o tres respuestas. Solo agradece.

**DI:**
> Gracias. Resumo lo que hicieron hoy: leyeron un error en tres pasos,
> reconocieron cinco tipos de error por su nombre, leyeron un rastro de abajo
> hacia arriba y separaron el síntoma del origen, encontraron un defecto que no
> dejaba mensaje, y escribieron un assertion.
>
> El jueves aplicamos esto mismo a un log: muchas líneas, varios errores, y una
> sola causa. Era la pregunta más difícil del diagnóstico, y con lo de hoy ya
> tienen la idea que hace falta: el último error casi nunca es la causa.
>
> Tarea opcional: los retos al final del archivo. El reto c es el más
> interesante.
>
> Buen trabajo. Nos vemos el jueves.

**Plan B, si la sección 6 no pudo leer los assets:** muestra las secciones 1, 3 y
5, que no dependen del engine. Después muestra el código de la sección 6 y
pregunta: "Si el caso tuviera un solo paso, ¿cuál de los tres assert saltaría, y
qué diría el mensaje?". La sección 7 funciona siempre.

**Dato para ti, por si preguntan:**

- El script usa `try` y `except` para atrapar cada error y poder seguir. No se
  enseña en este programa. Si preguntan: "es la forma de decirle al programa
  qué hacer si algo falla, en lugar de detenerse".
- Los símbolos `^^^^` y `~~~~` debajo de la línea del error aparecen solo en
  versiones recientes de Python, y señalan el pedazo exacto. Si alguien no los
  ve, su versión es anterior; no cambia nada.
- En FrostEd el mensaje de la división puede decir `integer division or modulo
  by zero` o `float division by zero`. El tipo sigue siendo `ZeroDivisionError`.
- Un assertion del engine no siempre detiene el juego. Depende de cómo esté
  configurado el build: en algunos se registra y continúa, en otros detiene la
  ejecución. Por eso la pregunta del diagnóstico decía "y el juego sigue
  funcionando".
- Si preguntan cuándo usar `if` y cuándo `assert`: `if` es para algo que puede
  pasar y el programa debe manejar. `assert` es para algo que nunca debería
  pasar, y si pasa, alguien tiene que enterarse.
- `semana3/sesion4_demo_assert.py` es una demo de cinco líneas del mismo
  concepto, con `player_speed = -1`. Sirve si recortas el ejercicio 5.

---

## Si vas mal de tiempo

Recorta en este orden:

1. Bloque 1: omite la pregunta inicial, y con ella la pregunta de cierre.
2. Ejercicio 2: ejecuta tú las cuatro líneas en pantalla; ellos solo predicen.
3. Ejercicio 5c: pasa a ser la tarea.
4. Ejercicio 5a y 5b: reemplázalos por `sesion4_demo_assert.py`, ejecutado por
   ti, con la pregunta "¿sale la última línea?".

No recortes el ejercicio 3, el ejercicio 4 ni la parte del bloque 7 sobre qué
pueden hacer con un assertion. El ejercicio 3 es la base de la sesión 5.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Pregunta inicial | Qué hacen hoy ante un error | Línea base; compárala con la respuesta del cierre |
| Ejercicio 2, línea C | Quién dice NameError | Todavía confunden una variable con una clave |
| Ejercicio 3 | Quién señala la línea 52 como origen | Es la confusión entre síntoma y causa; el jueves vuelve con los logs |
| Ejercicio 4 | Quién escribe los print y quién cambia cosas al azar | Mide si adoptaron un método o siguen probando a ciegas |
| Ejercicio 5c | Quién afirma lo contrario de lo que quería | No han entendido que un assert declara lo que debe ser verdad |
