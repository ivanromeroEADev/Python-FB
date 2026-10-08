# Session 5 · Jueves 22 de octubre
# Reading Logs: Root Cause and Symptom

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

La pregunta del log fue la más difícil del diagnóstico: 2 aciertos de 9, y 5
personas no la respondieron. La dificultad no es técnica. Es de lectura: ante
varias líneas de error, la tendencia es quedarse con la última, que es la más
visible y casi siempre la menos útil. Hoy se lee un log primero a ojo y después
con un programa, y se ve que el programa comete el mismo error que una persona
si se le escribe mal.

**Al terminar, el participante puede:** identificar las tres partes de una línea
de log, clasificar las líneas en causa raíz, síntoma y ruido, leer un archivo
con Python y contar por nivel, y explicar por qué el primer error orienta más
que el último.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–4 | 1. Apertura y repaso | | Una pregunta al grupo |
| 4–13 | 2. Leer un log a ojo | 1 | Lectura en parejas, debate |
| 13–19 | 3. Abrir el archivo | 2 | Predicción |
| 19–24 | 4. Contar por nivel | 3 | Predicción, escriben un contador |
| 24–31 | 5. La primera, no la última | 4 | Caza de un bug |
| 31–39 | 6. Una función, dos logs | 5 | Trabajo en parejas, debate final |
| 39–45 | 7. Frostbite y cierre | | Demostración guiada |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `semana3`, con la terminal abierta y la letra
   grande.
2. Ejecuta `python sesion5_ejercicios.py`. Debe mostrar `Session 5 ready` y
   `Root cause: [09:24:09] ERROR Job 5120 finished with exit code 1`.
3. **Elige un log real** que se pueda mostrar al grupo: el de un proceso que haya
   fallado, con al menos un error y algunas líneas antes. Léelo tú primero y ten
   clara la causa. Escribe su ruta en `LOG_PATH`, al inicio del script
   `PyQV_S5_ReadingLogs`, con `/` en lugar de `\`.
4. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S5_ReadingLogs` listo y la ventana de
   salida limpia. **Ejecútalo una vez antes de la clase** y comprueba que la
   sección 5 encuentra el error que esperabas. Si tu log escribe los niveles de
   otra forma, ajusta `ERROR_WORD` y `WARN_WORD`.
5. Ese mismo log abierto en un editor de texto, para mostrarlo completo.
6. Los tres archivos publicados en el canal: `sesion5_ejercicios.py`,
   `build_5120.log` y `nightly_5121.log`. **Los tres van en la misma carpeta.**
7. La lista de parejas a mano.

---

# Bloque 1 · Apertura y repaso (0–4)

**Propósito:** recuperar la idea del martes sobre la que se construye hoy: donde
revienta no es donde se origina.

**DI:**
> Buenos días. Gracias por estar aquí.
>
> Una pregunta sobre el martes. Vimos un rastro de error con tres niveles: una
> línea llamaba a report, report llamaba a pass rate, y pass rate dividía entre
> cero.

**PREGUNTA:**
> El programa reventó dentro de pass rate. ¿Ahí estaba el problema?

**ESPERAS:** no. Ahí estaba el síntoma. El origen era la llamada que entregó un
total de cero.

**SI NO RESPONDEN:**
> La línea que reventó había funcionado bien con otros datos. ¿Qué había
> cambiado?

**DI:**
> Eso. El lugar donde algo falla y el lugar donde se origina no son el mismo.
>
> Hoy aplicamos esa idea a algo que ven todos los días: un log. Un traceback
> describe un solo error. Un log describe un proceso completo, que puede durar
> minutos u horas, y cuando ese proceso falla suele dejar varios errores
> seguidos. La pregunta de hoy es cuál de ellos importa.
>
> Esta fue la pregunta más difícil del diagnóstico. La mayoría del grupo no la
> respondió. No es porque sea complicada: es porque nadie nos enseña a leer un
> log. Se aprende mirando a otros. Hoy lo hacemos con método.
>
> Necesitan tres archivos en la misma carpeta: el de ejercicios y dos que
> terminan en punto log. Abran sesion5 ejercicios y ejecútenlo.

**PREGUNTA:**
> ¿Todos ven Session 5 ready, y debajo una línea que empieza con Root cause?

**SI ALGUIEN VE `FileNotFoundError`:**
> Lean la última línea del mensaje, con el método del martes. ¿Qué archivo no
> encontró? Ese archivo tiene que estar en la misma carpeta que el de ejercicios,
> y la terminal tiene que estar abierta en esa carpeta.

---

# Bloque 2 · Leer un log a ojo (4–13)

**Propósito:** clasificar las líneas en causa raíz, síntoma y ruido, sin código.
Es el bloque más importante de hoy. Si este queda claro, el resto es mecánica.

## Ejercicio 1

**HAZ:** abre `build_5120.log` en VS Code. Que ellos también lo abran.

```
[09:14:02] INFO  Job 5120 started
[09:14:03] INFO  Syncing workspace
[09:14:41] WARN  Shader cache is 3 days old, rebuilding
[09:16:10] INFO  Step 'compile_code' started
[09:19:55] INFO  Step 'compile_code' finished
[09:19:56] INFO  Step 'build_assets' started
[09:21:30] ERROR Texture 'props/crate_02' has no source file
[09:21:30] ERROR Asset 'props/crate_02' could not be built
[09:21:31] WARN  Skipping 3 assets that depend on 'props/crate_02'
[09:24:08] ERROR Step 'build_assets' failed with 1 error
[09:24:08] INFO  Step 'package' skipped
[09:24:09] ERROR Job 5120 finished with exit code 1
```

**DI:**
> Antes de escribir una línea de código, vamos a leer. En el panel izquierdo
> abran el archivo build 5120 punto log. Es inventado, pero tiene la forma de los
> que van a encontrar.
>
> Cada línea tiene tres partes. Entre corchetes, la hora. Después, una palabra
> en mayúsculas: el nivel. Y después, el mensaje.
>
> Hay tres niveles. INFO informa: el proceso cuenta lo que está haciendo. WARN
> advierte: algo no es ideal, pero el proceso sigue. ERROR: algo falló.

**PREGUNTA:**
> Una pregunta rápida para ubicarnos. ¿Qué hizo este proceso entre las 9:16 y las
> 9:19?

**ESPERAS:** compiló el código. El paso `compile_code` empezó y terminó.

**DI:**
> Bien. Un log se lee como una historia, de arriba hacia abajo, en orden de
> tiempo. Ahora la pregunta de fondo. Este proceso falló. En el archivo de
> ejercicios hay cinco preguntas. Respóndanlas con su pareja, contando a mano.
> Tres minutos.

**HAZ:** circula. Escucha qué línea señalan como causa. No intervengas.

**PREGUNTA:**
> ¿Cuántas líneas tiene, y cuántas son ERROR?

**ESPERAS:** 12 líneas, 4 de ERROR.

**PREGUNTA:**
> ¿Cuál es la causa raíz? Quiero oír a dos parejas antes de decir nada.

**HAZ:** escucha. Es probable que alguna diga la última línea, o la del paso
`build_assets`.

**ESPERAS:** la de las 9:21:30: la textura `props/crate_02` no tiene archivo
fuente.

**SI FALLAN (dirán "el job terminó con código 1" o "falló build_assets"):**
> Veamos por qué. Hagamos una prueba con esa línea. Si alguien arreglara
> solamente eso, ¿el problema desaparecería? ¿Se puede "arreglar" que el job
> haya terminado con código 1?

**DI:**
> No se puede. Esa línea no describe un problema: describe el final de uno.
>
> Les propongo una pregunta para aplicar a cada línea de error: ¿esto pasó por
> algo que está más arriba? Vamos de abajo hacia arriba.

**PREGUNTA:**
> El job terminó con código 1. ¿Por algo de más arriba?

**ESPERAS:** sí, porque falló el paso `build_assets`.

**PREGUNTA:**
> Falló build assets. ¿Por algo de más arriba?

**ESPERAS:** sí, porque no se pudo construir el asset `crate_02`.

**PREGUNTA:**
> No se pudo construir el asset. ¿Por algo de más arriba?

**ESPERAS:** sí, porque su textura no tiene archivo fuente.

**PREGUNTA:**
> La textura no tiene archivo fuente. ¿Por algo de más arriba, dentro de este
> log?

**ESPERAS:** no. Arriba no hay nada que lo explique.

**DI:**
> Ahí se detiene la cadena. Esa es la causa raíz: el primer error, el que no
> tiene explicación más arriba. Los otros tres son síntomas: consecuencias, una
> detrás de otra.

**PREGUNTA:**
> Quedan dos advertencias. La de las 9:21:31, que dice que se saltaron tres
> assets: ¿causa, síntoma o ruido?

**ESPERAS:** síntoma. Es otra consecuencia, aunque diga WARN y no ERROR.

**PREGUNTA:**
> ¿Y la de las 9:14:41, la de la caché de shaders?

**ESPERAS:** ruido. Ocurrió siete minutos antes, el proceso siguió, y no tiene
relación con la textura.

**DI:**
> Ruido. Es verdadera, está en el log, y no tiene nada que ver con el fallo. Los
> logs reales están llenos de líneas así, y parte del trabajo es no perseguirlas.

**PREGUNTA:**
> Si tuvieran que escribir el título de un bug con este log, ¿cuál de estos dos
> pondrían: "Job 5120 falla con exit code 1", o "La textura props crate 02 no
> tiene archivo fuente"?

**ESPERAS:** el segundo.

**IDEA CLAVE:**
> En un log, el último error es el más fácil de ver y el que menos dice. La causa
> raíz suele ser el primero. Para encontrarla se toma un error y se pregunta: ¿esto
> pasó por algo que está más arriba? Y se sube hasta que la respuesta sea no.

---

# Bloque 3 · Abrir el archivo (13–19)

**Propósito:** que vean que un archivo leído es una lista de textos, y que todo lo
que ya saben de listas se aplica.

## Ejercicio 2

```python
log_file = open("build_5120.log")
lines = log_file.readlines()
log_file.close()
```

**DI:**
> Lo que hicieron a mano con doce líneas no se puede hacer a mano con cuarenta
> mil. Un log real de un build tiene ese tamaño. Para eso se le pide ayuda al
> programa.
>
> Tres líneas nuevas. Open abre el archivo. Readlines lo lee completo. Close lo
> cierra. Lo importante es lo que queda guardado en lines.

**PREGUNTA:**
> Readlines entrega una lista, con un elemento por cada línea del archivo.
> Entonces, ¿cuánto vale len de lines?

**ESPERAS:** 12.

**HAZ:** que quiten el `#` y ejecuten. Sale `12`.

**PREGUNTA:**
> ¿Qué hay en lines, corchete, cero?

**ESPERAS:** la primera línea del log: Job 5120 started.

**HAZ:** que quiten el `#` y ejecuten. Sale la línea, y debajo una línea en blanco.

**DI:**
> Notarán una línea en blanco debajo. Cada línea del archivo trae al final un
> salto de línea, invisible, y print agrega el suyo. No afecta nada de lo que
> vamos a hacer.

**PREGUNTA:**
> La siguiente tiene un espacio en blanco para que lo llenen ustedes. Son doce
> líneas. ¿En qué posición está la última?

**ESPERAS:** en la 11.

**SI FALLAN (dirán 12):**
> Pruébenlo con 12 y lean el mensaje. Ya lo conocen.

**HAZ:** si alguien escribe 12, que lo ejecute: sale `IndexError`. Que lo lea en
voz alta y lo corrija a 11.

**PREGUNTA:**
> Y la última predicción. ¿De qué tipo es lines, corchete, cero? Tienen cinco
> opciones.

**ESPERAS:** `str`. Texto.

**HAZ:** que quiten el `#` y ejecuten. Sale `<class 'str'>`.

**PREGUNTA:**
> La hora, 09:14:02, ¿es un número?

**ESPERAS:** no. Es parte de un texto.

**DI:**
> Recuerden lo que dijimos el primer día: casi todo lo que se lee de un archivo
> llega como texto, aunque parezca un número. Para el programa, esa hora y ese
> 5120 son letras. El martes van a necesitar esto.

**IDEA CLAVE:**
> Un archivo leído es una lista de textos. Todo lo que saben de listas sirve
> aquí: posiciones, len, y sobre todo, for.

---

# Bloque 4 · Contar por nivel (19–24)

**Propósito:** aplicar el loop con contador a un caso real. Es rápido porque ya
lo saben hacer.

## Ejercicio 3

```python
errors = 0

for line in lines:
    if "ERROR" in line:
        errors = errors + 1
```

**DI:**
> Este código ya lo saben leer. Es el loop con contador de la sesión 2. Hay una
> sola palabra nueva: in.
>
> Ya la vieron en el for. Dentro de un if hace otra cosa: pregunta si un texto
> está dentro de otro, y responde True o False. Aquí pregunta si la palabra
> ERROR aparece en algún lugar de la línea.

**PREGUNTA:**
> ¿Cuánto vale errors al final? Ya tienen la respuesta: la contaron a mano.

**ESPERAS:** 4.

**HAZ:** que quiten el `#` y ejecuten. Sale `Errors: 4`.

**DI:**
> Coincide con lo que contaron a mano, y por eso podemos confiar en el programa.
> Ese orden importa: primero se comprueba con un caso pequeño que uno puede
> contar, y solo después se usa con uno grande.
>
> Ahora escriban ustedes. Debajo, cuenten también las advertencias, en una
> variable que se llame warnings, y muéstrenla. Un minuto.

**Respuesta:**

```python
warnings = 0

for line in lines:
    if "WARN" in line:
        warnings = warnings + 1

print("Warnings:", warnings)
```

**HAZ:** circula. También es válido agregar el segundo `if` dentro del loop que ya
existe, con el contador creado antes.

**PREGUNTA:**
> El programa dice 4 errores y 2 advertencias. ¿Eso responde la pregunta de qué
> falló?

**ESPERAS:** no. Dice cuántos hay, no cuál importa.

**IDEA CLAVE:**
> Contar errores sirve para saber el tamaño del problema. No dice nada sobre la
> causa. Un log con cuatrocientos errores puede tener una sola causa.

---

# Bloque 5 · La primera, no la última (24–31)

**Propósito:** encontrar un defecto que hace que el programa cometa el mismo error
de lectura que las personas: quedarse con el último error.

## Ejercicio 4

```python
first_error = ""

for line in lines:
    if "ERROR" in line:
        first_error = line

print("Root cause:", first_error)
```

**DI:**
> El siguiente tiene un defecto, y no les voy a decir cuál.
>
> Este código quiere mostrar la causa raíz. La variable se llama first error, y
> la idea es guardar ahí el primer error del log.

**PREGUNTA:**
> Miren la salida. ¿Qué línea muestra como causa raíz?

**ESPERAS:** la última: Job 5120 finished with exit code 1.

**PREGUNTA:**
> ¿Es la que ustedes encontraron a mano?

**ESPERAS:** no. Es el último síntoma.

**DI:**
> El programa hizo lo mismo que hace una persona con prisa: se quedó con el
> último error. Sin ningún mensaje. Encuentren por qué, y corríjanlo. La tabla
> de la sesión 2 sirve. Tres minutos.

**HAZ:** circula en silencio. No des la respuesta.

**PISTA (solo si una pareja se atasca):**
> Hagan la tabla solo con las cuatro líneas que tienen ERROR. ¿Cuánto vale first
> error después de cada una?

**PREGUNTA (cuando la mayoría termine o se acerque):**
> ¿Qué encontraron?

**ESPERAS:** cada vez que aparece un ERROR, la variable se sobrescribe. Al final
queda el último.

**DI:**
> Es la primera idea del programa, la del primer día: una variable no recuerda
> lo que fue, solo sabe lo que es ahora. Guardó el primer error, después lo
> reemplazó por el segundo, por el tercero y por el cuarto.

**PREGUNTA:**
> ¿Cómo le decimos al programa "guárdalo solo si todavía no has guardado
> ninguno"? Miren con qué valor empieza la variable.

**ESPERAS:** agregando una condición: que `first_error` todavía esté vacía.

**Respuesta:**

```python
if "ERROR" in line and first_error == "":
    first_error = line
```

**HAZ:** confirma que a todos les sale
`Root cause: [09:21:30] ERROR Texture 'props/crate_02' has no source file`.

**PREGUNTA:**
> ¿Qué palabra hace que las dos condiciones se tengan que cumplir a la vez? ¿Y
> qué pasaría si en su lugar escribiéramos or?

**ESPERAS:** `and`. Con `or` volvería a guardar el último, porque bastaría con que
la línea tuviera ERROR.

**IDEA CLAVE:**
> El nombre de la variable decía first error y guardaba el último. Un nombre es
> una intención, no una garantía. Y fíjense que el defecto del programa y el
> error de lectura de las personas son el mismo: quedarse con lo último que
> pasó.

---

# Bloque 6 · Una función, dos logs (31–39)

**Propósito:** empaquetar lo anterior en una función y descubrir, con el segundo
log, hasta dónde llega una herramienta y dónde empieza el criterio.

## Ejercicio 5 · Escribir la función (5 minutos)

**DI:**
> Ahora lo escriben ustedes. Cambien de persona en el teclado.
>
> Lo que tienen funciona para un archivo. Hay un segundo log en la carpeta.
> Conviertan lo que ya tienen en una función que reciba el nombre de un archivo y
> devuelva su primer error.
>
> Casi no hay código nuevo: son las tres líneas del ejercicio 2 y el loop del
> ejercicio 4, dentro de un def. Dos cuidados. Donde decía el nombre del archivo
> entre comillas, ahora va lo que la función recibe. Y al final, return, no
> print.

**HAZ:** circula. Observa sin intervenir durante el primer minuto.

**Respuesta:**

```python
def first_error_in(file_name):
    log_file = open(file_name)
    lines = log_file.readlines()
    log_file.close()

    first_error = ""

    for line in lines:
        if "ERROR" in line and first_error == "":
            first_error = line

    return first_error
```

Con las dos líneas sin comentar debe salir:

```
[09:21:30] ERROR Texture 'props/crate_02' has no source file

[02:41:50] ERROR Could not write 'levels/harbor_03.cache': not enough space on disk
```

| Lo que ven | Causa | Pregunta que los lleva a la solución |
|---|---|---|
| Sale el mismo error las dos veces | Dejaron `"build_5120.log"` escrito dentro de la función | "¿Qué archivo abre la función? ¿Y cuál le pidieron?" |
| Sale `None` dos veces | Falta el `return`, o usaron `print` | "¿Qué le faltaba a la función que devolvía None el jueves pasado?" |
| `FileNotFoundError` | Escribieron `open("file_name")`, con comillas | "Con comillas es un texto. ¿Existe un archivo que se llame file_name?" |
| Sale el último error | No copiaron el arreglo del ejercicio 4 | "¿Qué condición agregaron hace cinco minutos?" |
| Sale una línea vacía | El `return` está dentro del `for`, o dentro del `if`, con más espacios de la cuenta | "¿Cuántas vueltas alcanza a dar el loop antes de llegar al return?" |
| `NameError: name 'first_error_in' is not defined` | Quitaron los `#` antes de escribir la función, o la escribieron debajo | "Cuando Python llega a esa línea, ¿ya conoce la función?" |
| `IndentationError` | Las líneas copiadas no tienen los 4 espacios de la función | "¿A quién pertenecen esas líneas ahora?" |

## Ejercicio 5 · El segundo log (3 minutos)

**HAZ:** cuando la mayoría tenga la función, detén al grupo. Abre
`nightly_5121.log` en pantalla.

```
[02:00:01] INFO  Job 5121 started
[02:00:02] INFO  Syncing workspace
[02:03:15] WARN  Disk space low on D: (1.2 GB free)
[02:03:16] INFO  Step 'build_assets' started
[02:41:50] ERROR Could not write 'levels/harbor_03.cache': not enough space on disk
[02:41:50] ERROR Step 'build_assets' failed with 1 error
[02:41:51] INFO  Step 'run_tests' skipped
[02:41:52] ERROR Job 5121 finished with exit code 1
```

**DI:**
> Miren el segundo log. La función encontró el primer error: no pudo escribir un
> archivo porque no había espacio en el disco. Hizo exactamente lo que le
> pedimos.
>
> Ahora lean el log completo, ustedes, y apliquen la pregunta de hoy.

**PREGUNTA:**
> No pudo escribir el archivo porque no había espacio. ¿Eso pasó por algo que
> está más arriba?

**ESPERAS:** sí. A las 2:03 hay un WARN: queda poco espacio en el disco D.

**PREGUNTA:**
> ¿Cuánto tiempo antes del error apareció esa advertencia?

**ESPERAS:** casi cuarenta minutos antes.

**PREGUNTA:**
> En el primer log dijimos que una advertencia era ruido. ¿Esta también?

**ESPERAS:** no. Esta es la explicación.

**DI:**
> En el primer log, la advertencia era ruido. En este, la advertencia es la
> causa. Dicen WARN las dos. Lo que las distingue no es el nivel: es si tienen
> relación con lo que falló. Y eso el programa no lo puede decidir, porque para
> decidirlo hay que entender qué significa cada mensaje.

**PREGUNTA:**
> Entonces, ¿para qué sirve la función, si no encuentra la causa?

**ESPERAS:** para saber dónde empezar a leer. Señala el primer error; desde ahí
una persona lee hacia arriba.

**IDEA CLAVE:**
> Una herramienta señala. Una persona interpreta. La función les dice en qué
> línea de cuarenta mil empezar a mirar, y eso ahorra horas. Decidir cuál es la
> causa sigue siendo trabajo de ustedes.

---

# Bloque 7 · Frostbite y cierre (39–45)

**Propósito:** recorrer un log real con el mismo método, guiado, y dejar clara la
distancia que falta.

**HAZ:** muestra primero el log real completo, en el editor de texto. Desplázate
despacio de arriba hacia abajo para que vean su tamaño. No expliques nada todavía.

**DI:**
> Pasemos a un log real, de un proceso que falló. Mírenlo un momento.

**PREGUNTA:**
> ¿Qué diferencias ven con los dos que leyeron hoy?

**ESPERAS:** es mucho más largo. Las líneas tienen otro formato. Hay palabras y
nombres que no conocen.

**DI:**
> Es más largo, el formato es otro, y está lleno de nombres de sistemas que
> todavía no conocen. Leerlo de arriba hacia abajo no es una opción. Veamos qué
> hace con él el script.

**HAZ:** cambia a FrostEd y ejecuta `PyQV_S5_ReadingLogs`. Muestra brevemente la
sección 3 de la salida.

**DI:**
> La sección 3 es el defecto que corrigieron: sin la segunda condición, el
> último error; con ella, el primero.

**HAZ:** baja a la sección 5. Señala, en este orden: el número de líneas, los
contadores, y la línea del primer error.

**DI:**
> Sección 5: el log real. Tantas líneas, tantos errores, tantas advertencias. Son
> los contadores que escribieron hoy. Y debajo, la posición del primer error.

**PREGUNTA:**
> El script muestra el primer error, y antes de él, las cinco líneas anteriores.
> ¿Por qué creen que las muestra?

**ESPERAS:** para leer hacia arriba. Para ver si algo anterior lo explica, como la
advertencia del disco.

**HAZ:** lee con ellos esas líneas en voz alta. Explica, con tus palabras, cuál
fue la causa real de ese fallo y cómo llegaste a ella. Un minuto, no más. Si la
causa estaba en una de las líneas anteriores, señálala. Si no estaba en el log,
dilo: también es una lección.

**DI:**
> Quiero ser preciso sobre lo que acaban de ver. El script encontró la línea en
> un segundo. Entender qué significa esa línea me tomó bastante más, y fue
> posible porque conozco ese proceso: sé qué hace cada paso y qué necesita para
> funcionar.
>
> Ese conocimiento no sale de este programa. Sale de tiempo trabajando con el
> engine. Lo que sí sale de aquí es el método, y es el mismo para un log de doce
> líneas y para uno de cuarenta mil: buscar el primer error, preguntar si algo
> de más arriba lo explica, y no perseguir el ruido.
>
> Y hay algo que pueden hacer desde hoy, sin saber nada más del engine. Cuando
> reporten un fallo, no copien solo la última línea del log. Busquen el primer
> error, y copien ese junto con las líneas anteriores. Quien reciba el reporte
> va a empezar donde ustedes terminaron, y no desde cero.

**PREGUNTA:**
> Para cerrar: ¿qué línea de un log van a mirar primero a partir de hoy?

**ESPERAS:** el primer error, no el último.

**DI:**
> Gracias. Resumo lo que hicieron hoy: leyeron un log como una historia,
> separaron la causa raíz de los síntomas y del ruido, abrieron un archivo con
> Python, contaron por nivel, corrigieron un programa que se quedaba con el
> último error, y vieron dónde termina el trabajo de una herramienta.
>
> El martes juntamos todo. Van a construir, en parejas, un validador de
> resultados de pruebas: lee un archivo, revisa cada resultado contra una regla
> y entrega un resumen. Usa cada pieza que han visto, desde la primera sesión.
>
> Tarea opcional: los retos al final del archivo.
>
> Buen trabajo. Nos vemos el martes.

**Plan B, si `LOG_PATH` está vacío o el log no se puede leer:** muestra las
secciones 1 a 4 del script. Después abre el log real en el editor de texto, busca
la palabra "error" con `Ctrl+F` y ve a la primera coincidencia: "Esto es lo que
haría el script: ir al primero". Lee hacia arriba con ellos.

**Dato para ti, por si preguntan:**

- La forma habitual de abrir archivos en Python es `with open(...) as f:`, que
  cierra el archivo sola. Aquí se usa `open` y `close` porque se leen sin
  explicar nada nuevo.
- `"ERROR" in line` distingue mayúsculas de minúsculas. La línea
  `failed with 1 error` no cuenta, y está bien: su nivel ya dice ERROR. El script
  del engine sí busca sin distinguir, con `line.lower()`, porque los logs reales
  no son uniformes.
- Buscar la palabra "error" en un log real da falsos positivos: líneas como
  `0 errors found` o un asset que se llama `error_texture`. Si aparece uno en tu
  demostración, úsalo: es otro ejemplo de que la herramienta señala y la persona
  decide.
- No siempre el primer error es la causa raíz. A veces la causa no deja ninguna
  línea en el log, o está en el log de otro proceso. "El primero" es la mejor
  regla para empezar, no una ley.
- El reto b usa `first_error[1:9]`. Se llama *slice*: toma un pedazo de un texto
  o de una lista. El script del engine lo usa para mostrar las líneas anteriores.

---

## Si vas mal de tiempo

Recorta en este orden:

1. Ejercicio 2: omite `lines[0]` y la última posición; deja solo `len` y `type`.
2. Ejercicio 3: muestra el contador de errores y omite el de advertencias.
3. Ejercicio 5, escribir la función: muéstrala tú, que la copien y quiten los `#`.
4. Bloque 7: omite la sección 3 y ve directo a la sección 5.

No recortes el ejercicio 1, el ejercicio 4 ni la discusión del segundo log. Si
el ejercicio 1 necesita más de nueve minutos, dáselos: es la razón de esta
sesión.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Ejercicio 1 | Qué línea señala cada pareja como causa raíz | Es la pregunta 16 del diagnóstico; compara con el resultado del 29 |
| Ejercicio 1 | Quién clasifica como ruido el WARN de las 9:21:31 | No ven que una consecuencia puede no decir ERROR |
| Ejercicio 2 | Quién dice que la última posición es la 12 | El error por uno sigue presente |
| Ejercicio 4 | Quién relaciona el bug con "una variable solo sabe lo que es ahora" | Mide si la idea de la sesión 1 quedó |
| Segundo log | Quién encuentra el WARN del disco sin ayuda | Son quienes ya leen hacia arriba por su cuenta |
