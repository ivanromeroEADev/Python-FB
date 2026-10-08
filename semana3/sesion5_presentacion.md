# Session 5 · Presentación
# Reading Logs: Root Cause and Symptom

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion5_guion.md`.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–3 | 1. Apertura y repaso | 0–4 |
| 4–9 | 2. Leer un log a ojo | 4–13 |
| 10–12 | 3. Abrir el archivo | 13–19 |
| 13–14 | 4. Contar por nivel | 19–24 |
| 15–17 | 5. La primera, no la última | 24–31 |
| 18–21 | 6. Una función, dos logs | 31–39 |
| 22–25 | 7. Frostbite y cierre | 39–45 |

Los dos logs de las pantallas son los inventados de la carpeta. **El log real
del bloque 7 no se sube a la presentación:** se muestra en vivo.

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 5 · Reading Logs
> Varios errores, una sola causa.

**DI:**
> Buenos días. Gracias por estar aquí. Entren a la lección. Una pregunta sobre
> el martes.

### 2 · Repaso — Poll

**En pantalla:** "El martes el programa reventó dentro de `pass_rate`. ¿Ahí estaba el problema?"

**Opciones:** Sí, esa línea estaba mal · No, ahí estaba el síntoma · No se puede saber

**DI:**
> Vimos un rastro con tres niveles: una línea llamaba a report, report llamaba a
> pass rate, y pass rate dividía entre cero. ¿Ahí estaba el problema?

**Después:**
> Ahí estaba el síntoma. El origen era la llamada que entregó un total de cero.

### 3 · El tema de hoy — Diapositiva

**En pantalla:**
> Un traceback describe **un** error.
> Un log describe **un proceso completo**, y suele dejar varios errores seguidos.
> ¿Cuál importa?
>
> **Ahora en VS Code:** tres archivos en la misma carpeta. Abre
> `sesion5_ejercicios.py` y ejecútalo.

**DI:**
> Esta fue la pregunta más difícil del diagnóstico; la mayoría no la respondió.
> No es porque sea complicada: es porque nadie nos enseña a leer un log. Hoy lo
> hacemos con método. Necesitan los tres archivos en la misma carpeta. Ejecuten:
> deben ver Session 5 ready, y una línea que empieza con Root cause.

### 4 · Un log — Diapositiva

**En pantalla:** el log completo, como imagen.

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
> Antes de escribir código, vamos a leer. Abran build 5120 punto log en VS Code.
> Cada línea tiene tres partes: entre corchetes, la hora; después el nivel; y
> después el mensaje. INFO informa. WARN advierte, y el proceso sigue. ERROR:
> algo falló. Un log se lee como una historia, de arriba hacia abajo. Respondan
> las cinco preguntas del ejercicio 1 con su pareja, contando a mano. Tres
> minutos.

### 5 · La causa raíz — Dibujo

**En pantalla:** el mismo log, con la instrucción "Encierra en un círculo la línea que es la causa raíz."

**DI:**
> Este proceso falló. Marquen en su pantalla cuál línea es la causa raíz.

**HAZ:** mira cuántos marcan la última línea. No digas todavía cuál es.

### 6 · La pregunta — Diapositiva

**En pantalla:**
> Para cada error, una pregunta:
> **¿Esto pasó por algo que está más arriba?**
>
> Y se sube hasta que la respuesta sea no.

**DI:**
> Probemos con la última línea. ¿Se puede "arreglar" que el job haya terminado
> con código 1? No: esa línea describe el final de un problema. Vamos de abajo
> hacia arriba. El job terminó, ¿por algo de más arriba? Sí: falló build assets.
> ¿Y eso? Porque no se pudo construir el asset. ¿Y eso? Porque su textura no
> tiene archivo fuente. ¿Y eso, por algo de más arriba? No. Ahí se detiene la
> cadena.

### 7 · Causa, síntoma, ruido — Diapositiva

**En pantalla:**
> **Causa raíz** · 09:21:30 · la textura no tiene archivo fuente
> **Síntomas** · el asset no se construyó · se saltaron 3 assets · falló el paso
> · terminó el job
> **Ruido** · 09:14:41 · la caché de shaders

**DI:**
> El primer error es la causa. Los demás son consecuencias, una detrás de otra;
> incluida la advertencia de los tres assets, que dice WARN y no ERROR. Y la
> advertencia de la caché es ruido: es verdadera, está en el log, y no tiene
> nada que ver. Parte del trabajo es no perseguirla.

### 8 · El título del bug — Poll

**En pantalla:** "¿Qué título le pondrías al bug?"

**Opciones:** "Job 5120 falla con exit code 1" · "Falla el paso build_assets" · "La textura props/crate_02 no tiene archivo fuente" · "Caché de shaders desactualizada"

**DI:**
> Si tuvieran que escribir el título de un bug con este log, ¿cuál pondrían?

### 9 · Idea clave — Diapositiva

**En pantalla:**
> El último error es el más fácil de ver y el que menos dice.
> La causa raíz suele ser **el primero**.

**DI:**
> Para encontrarla se toma un error y se pregunta: ¿esto pasó por algo que está
> más arriba?

### 10 · Abrir el archivo — Poll

**En pantalla:** captura del código, y la pregunta "El log tiene 12 líneas. ¿En qué posición de `lines` está la última?"

```python
log_file = open("build_5120.log")
lines = log_file.readlines()
log_file.close()
```

**Opciones:** 10 · 11 · 12 · 13

**DI:**
> Lo que hicieron a mano con doce líneas no se puede hacer con cuarenta mil.
> Open abre el archivo, readlines lo lee y close lo cierra. Lo importante es lo
> que queda en lines: una lista, con un elemento por cada línea. Comprueben len
> y lines corchete cero. Ahora: son doce líneas, ¿en qué posición está la
> última?

**Después:**
> En la once. Quien haya dicho doce, pruébelo y lea el mensaje: ya lo conoce.

### 11 · ¿De qué tipo? — Poll

**En pantalla:** "¿De qué tipo es `lines[0]`? ¿Y la hora, `09:14:02`, es un número?"

**Opciones:** `str`: todo es texto · `int`: la hora es un número · `list` · `float`

**DI:**
> Última predicción de este bloque. Respondan y compruébenlo con type.

**Después:**
> Texto. Casi todo lo que se lee de un archivo llega como texto, aunque parezca
> un número. El martes van a necesitar esto.

### 12 · Idea clave — Diapositiva

**En pantalla:**
> Un archivo leído es una lista de textos.
> Todo lo que saben de listas sirve aquí: posiciones, `len`, y sobre todo, `for`.

**DI:**
> Nada de esto es nuevo. Solo cambió de dónde vienen los datos.

### 13 · Contar por nivel — Diapositiva

**En pantalla:** captura del código, con el texto "Ahora en VS Code · Ejercicio 3: predice `errors`, compruébalo, y después cuenta también los WARN. Debe salir `Warnings: 2`."

```python
errors = 0

for line in lines:
    if "ERROR" in line:
        errors = errors + 1
```

**DI:**
> Este código ya lo saben leer: es el loop con contador. Una palabra nueva: in.
> Dentro de un if, pregunta si un texto está dentro de otro. ¿Cuánto vale errors?
> Ya lo contaron a mano. Compruébenlo, y después cuenten ustedes las
> advertencias. Dos minutos.

**Después:**
> Cuatro, igual que a mano, y por eso podemos confiar en el programa. Primero se
> comprueba con un caso pequeño que uno puede contar.

### 14 · Idea clave — Diapositiva

**En pantalla:**
> Contar errores dice el **tamaño** del problema.
> No dice nada sobre la **causa**.

**DI:**
> Un log con cuatrocientos errores puede tener una sola causa.

### 15 · El bug — Diapositiva

**En pantalla:** captura del código, con el texto "Debería mostrar el primer ERROR. Muestra: `Job 5120 finished with exit code 1`."

```python
first_error = ""

for line in lines:
    if "ERROR" in line:
        first_error = line

print("Root cause:", first_error)
```

**DI:**
> El siguiente tiene un defecto. Quiere mostrar la causa raíz, y muestra el
> último síntoma. Hizo lo mismo que hace una persona con prisa: se quedó con el
> último error, sin ningún mensaje. Encuentren por qué y corríjanlo en VS Code.
> La tabla de la sesión 2 sirve. Tres minutos.

### 16 · ¿Por qué? — Pregunta abierta

**En pantalla:** "En una frase: ¿por qué guarda el último error y no el primero?"

**DI:**
> Cuando lo tengan, escríbanlo.

**Después:**
> Cada vez que aparece un ERROR, la variable se sobrescribe. Es la primera idea
> del programa: una variable no recuerda lo que fue. El arreglo es una segunda
> condición, con and: guárdalo solo si todavía está vacía.

### 17 · Idea clave — Diapositiva

**En pantalla:**
> La variable se llamaba `first_error` y guardaba el último.
> Un nombre es una intención, no una garantía.

**DI:**
> Y fíjense: el defecto del programa y el error de lectura de las personas son
> el mismo. Quedarse con lo último que pasó.

### 18 · Escríbelo tú — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 5 · 5 minutos**
> Escribe `first_error_in(file_name)`
> - Las 3 líneas del ejercicio 2 + el loop del ejercicio 4, dentro de un `def`
> - Donde decía el nombre del archivo, va lo que la función recibe
> - Al final, `return`

**DI:**
> Ahora lo escriben ustedes. Cambien de persona en el teclado. Casi no hay
> código nuevo. Cuando la tengan, quiten los numerales de las dos líneas de
> abajo.

**Mientras trabajan:** la tabla de errores está en el guion, bloque 6.

### 19 · El segundo log — Diapositiva

**En pantalla:** el segundo log, como imagen.

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
> pedimos. Ahora léanlo ustedes, completo.

### 20 · ¿Es la causa? — Poll

**En pantalla:** "Lo que encontró la función, ¿es la causa raíz?"

**Opciones:** Sí, es el primer error · No: la explicación está en el WARN de las 02:03 · No: es la última línea · No se puede saber

**DI:**
> Apliquen la pregunta de hoy: ¿eso pasó por algo que está más arriba?

**Después:**
> Casi cuarenta minutos antes hay una advertencia: queda poco espacio en el
> disco. En el primer log, una advertencia era ruido. En este, es la
> explicación. Dicen WARN las dos. Lo que las distingue no es el nivel: es si
> tienen relación con lo que falló. Y eso el programa no lo puede decidir.

### 21 · Idea clave — Diapositiva

**En pantalla:**
> Una herramienta **señala**.
> Una persona **interpreta**.

**DI:**
> La función les dice en qué línea de cuarenta mil empezar a mirar, y eso ahorra
> horas. Decidir cuál es la causa sigue siendo trabajo de ustedes.

### 22 · Un log real — Diapositiva

**En pantalla:**
> **Un log real**
> Hoy solo observan.

**DI:**
> Pasemos a un log real, de un proceso que falló.

**HAZ:** comparte tu pantalla y sigue el bloque 7 del guion: primero el log
completo en el editor de texto, después el script en FrostEd, sección 5, y lee
con ellos las líneas anteriores al primer error.

### 23 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Un combo de cinco trucos falla.
> ¿Qué dice la última línea? ¿Y la primera que falló?

**DI:**
> Aterricemos esto al juego. Piensen en un test de combo: cinco trucos seguidos,
> y cada uno se valida en orden. Si el segundo truco no se detecta, el tercero,
> el cuarto y el quinto tampoco se van a validar, y al final el test termina con
> un mensaje como "combo failed", o por tiempo. Ese último mensaje es el que
> todos ven, y es el síntoma. La causa está en el primer truco que no se
> detectó. Cuando reporten un fallo así, no copien solo la última línea: busquen
> la primera que falló y cópienla junto con las anteriores.

### 24 · Cierre — Poll

**En pantalla:** "A partir de hoy, ¿qué línea de un log vas a mirar primero?"

**Opciones:** La última · El primer ERROR · El primer WARN · Todas, de arriba hacia abajo

**DI:**
> Para cerrar.

### 25 · Resumen — Diapositiva

**En pantalla:**
> **Hoy:** un log como una historia · causa, síntoma y ruido · un archivo es una
> lista de textos · contar por nivel · el primero, no el último · la herramienta
> señala, la persona interpreta
>
> **Martes:** el mini-proyecto
> **Tarea opcional:** los retos al final del archivo

**DI:**
> Gracias. El martes juntamos todo: van a construir, en parejas, un validador de
> resultados de pruebas. Usa cada pieza que han visto, desde la primera sesión.
> Buen trabajo.
