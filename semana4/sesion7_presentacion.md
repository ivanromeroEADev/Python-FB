# Session 7 · Presentación
# The Full Picture: Review, Final Assessment and Closing

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion7_guion.md`.

Hoy hay **dos lecciones distintas**: esta, y la del diagnóstico final, que va
aparte, a ritmo del estudiante y con las respuestas guardadas por persona. En
la pantalla 9 se cambia de una a otra.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–2 | 1. Apertura | 0–3 |
| 3–8 | 2. Repaso: cinco predicciones | 3–12 |
| 9 | 3 y 4. Diagnóstico final (otra lección) | 12–34 |
| 10–12 | 5. El recorrido completo | 34–40 |
| 13–16 | 6. Lo que sigue, y cierre | 40–45 |

Es la sesión con menos margen. Empieza puntual.

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 7 · The Full Picture
> Repaso · Diagnóstico · El recorrido completo

**DI:**
> Buenos días. Gracias por estar aquí. Es la última sesión. Entren a la lección.
> Hoy hacemos tres cosas: un repaso corto, el diagnóstico del primer día con
> otros valores, y una validación completa dentro del engine.

### 2 · Sobre el diagnóstico — Diapositiva

**En pantalla:**
> Sigue sin ser un examen.
> El primer día me servía a mí, para saber por dónde empezar.
> Hoy les sirve a ustedes: su resultado del primer día, al lado del de hoy.
>
> **Ahora en VS Code:** abre `sesion7_ejercicios.py` y ejecútalo.

**DI:**
> Dos aclaraciones. No va a ninguna evaluación y nadie más ve los resultados. Y
> su propósito cambió: cada persona va a poder ver, pregunta por pregunta, qué
> se movió. Empecemos por el repaso. Cinco predicciones, una por sesión.

### 3 · 1 · Sigue el valor — Poll

**En pantalla:** captura del código, y la pregunta "¿Cuánto vale `backup`, y qué dice `status`?"

```python
lives = 3
backup = lives
lives = lives - 3

if lives > 0:
    status = "playing"
else:
    status = "game over"
```

**Opciones:** 3 y game over · 0 y game over · 3 y playing · 0 y playing

**DI:**
> Primera. Respondan sin ejecutar.

**Después:**
> Tres, y game over. Backup guardó una copia. Y cero no es mayor que cero.

### 4 · 2 · Sigue el contador — Poll

**En pantalla:** captura del código, y la pregunta "¿Cuánto vale `slow`?"

```python
load_times = [4, 10, 12, 10, 7]
slow = 0

for seconds in load_times:
    if seconds >= 10:
        slow = slow + 1
```

**Opciones:** 1 · 2 · 3 · 5

**DI:**
> Segunda. Si hace falta, hagan la tabla.

**Después:**
> Tres. En la anterior el borde no contaba y en esta sí: cambió el símbolo.

### 5 · 3 · Lo que entra y lo que sale — Poll

**En pantalla:** captura del código, y la pregunta "¿Qué devuelve `is_stable(build)`?"

```python
def is_stable(build):
    return build["crashes"] == 0 and build["fps"] >= 30


build = {"name": "rc_02", "crashes": 0, "fps": 29}
```

**Opciones:** True · False · None · Da error

**DI:**
> Tercera.

**Después:**
> False. No tiene crashes, pero con and se tienen que cumplir las dos, y 29 no
> llega a 30.

### 6 · 4 · Leer un error — Poll

**En pantalla:** el traceback, y la pregunta "¿Qué irías a mirar para encontrar el origen?"

```
Traceback (most recent call last):
  File "nightly.py", line 14, in <module>
    summary(results)
  File "nightly.py", line 9, in summary
    print(results["passed"] / results["total"])
KeyError: 'total'
```

**Opciones:** La línea 9, que está mal escrita · Dónde se creó `results` y qué claves tiene · Si Python está bien instalado · La división

**DI:**
> Cuarta. Esta no se ejecuta: se lee, de abajo hacia arriba.

**Después:**
> Se pidió una clave que el diccionario no tiene. Reventó en la línea 9, y esa
> línea es el síntoma. El origen está donde se armó results.

### 7 · 5 · Leer un log — Dibujo

**En pantalla:** el log, con la instrucción "Encierra en un círculo la causa raíz."

```
[14:02:10] INFO  Job 6033 started
[14:02:11] WARN  Using default settings
[14:05:47] ERROR Level 'docks_02' references missing asset 'props/barrel_07'
[14:05:47] ERROR Could not load level 'docks_02'
[14:05:48] ERROR Step 'smoke_test' failed
[14:05:49] ERROR Job 6033 finished with exit code 1
```

**DI:**
> Quinta. Marquen la causa raíz.

**Después:**
> La primera línea de error: el nivel referencia un asset que no existe. Las
> otras tres son síntomas, y la advertencia es ruido. El título del bug nombra
> el nivel y el asset que falta.

### 8 · Cinco ideas — Diapositiva

**En pantalla:**
> 1. Una variable solo sabe lo que vale ahora.
> 2. El borde depende de un símbolo.
> 3. Los valores entran por los paréntesis y salen por el `return`.
> 4. Un error se lee de abajo hacia arriba.
> 5. En un log, la causa suele ser el primer error, no el último.

**DI:**
> Cinco sesiones, cinco ideas. Llévenlas al diagnóstico.

### 9 · Diagnóstico final — Diapositiva

**En pantalla:**
> **Diagnóstico final · 20 minutos**
> Individual y en silencio. Puedes usar papel.
>
> Si no sabes una respuesta: "No lo sé".
> Hoy tienes un método: traza el valor · haz la tabla · busca el primer error.
>
> Código de acceso: ______

**DI:**
> Ahora el diagnóstico. Salgan de esta lección y entren a la otra, con el código
> que ven en pantalla. Les pido lo mismo que la primera vez: si no saben una
> respuesta, marquen "No lo sé". Una respuesta adivinada hoy les quitaría a
> ustedes la posibilidad de ver con claridad dónde están. Cuando quieran,
> empiecen.

**HAZ:** lanza la lección del diagnóstico. Avisa cuando falten 5 minutos y cuando
falte 1. No dejes código proyectado. Al terminar:

> Tiempo. Gracias. Los resultados se los envío a cada persona por mensaje
> directo, con el del primer día al lado.

### 10 · Frostbite — Diapositiva

**En pantalla:**
> **Frostbite**
> Una validación completa, en siete etapas.

**DI:**
> Pasemos a Frostbite por última vez.

**HAZ:** comparte FrostEd y sigue el bloque 5 del guion: las siete etapas de
arriba hacia abajo, y las dos preguntas de la etapa 7.

### 11 · El recorrido — Diapositiva

**En pantalla:**

| Etapa | Qué es | Sesión |
|---|---|---|
| 1 | Las reglas son variables | 1 |
| 2 | Lo que se revisa es una lista | 2 |
| 3 | Cada cosa es un diccionario; cada regla, una función | 3 |
| 4 | La misma revisión, para todos | 2 y 3 |
| 5 | Lo que siempre debe ser verdad | 4 |
| 6 | El resumen | 6 |
| 7 | Leer el log | 5 |

**DI:**
> Esto es lo que acaban de ver, en una tabla. Una validación técnica completa,
> en pequeño. Las que corren sobre el juego tienen miles de assets y cientos de
> reglas. La forma es esta. Hace cuatro semanas era una caja cerrada. Hoy pueden
> decir qué hace cada parte.

### 12 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Un test de combo, de principio a fin.

**DI:**
> Y por última vez, aterricémoslo al juego. Tomen un test de combo. Tiene
> reglas: qué trucos, en qué orden, en cuánto tiempo. Eso son variables. Tiene
> una lista de trucos, y cada truco es un conjunto de datos con nombre. Hay una
> comprobación, "¿se detectó este truco?", que se repite para cada uno. Hay
> cosas que siempre deben ser verdad mientras corre. Al final hay un veredicto,
> y queda un log. Y cuando falla, lo que ustedes buscan no es la última línea,
> sino el primer truco que no se detectó. Todo lo que hicieron este mes está
> ahí.

### 13 · Dónde están y qué falta — Diapositiva

**En pantalla:**
> **Lo que pueden hacer hoy**
> Trazar un loop · leer un error de abajo hacia arriba · encontrar el primer
> error de un log · construir un validador
>
> **Lo que falta**
> Conocimiento del engine: qué sistemas tiene, cómo se le piden los datos, qué
> significa cada mensaje.

**DI:**
> Para terminar, dónde están y qué falta. El primer día dije que había base, y
> que lo que faltaba era seguir un valor que cambia, cuidar los bordes, leer un
> log y entender un assertion. En eso trabajamos, y lo que ven arriba es real y
> es de ustedes. Lo que falta lo repito porque sigue siendo cierto: este
> programa no forma Technical Testers, y ningún resultado del diagnóstico indica
> que alguien esté en condiciones de hacer validaciones independientes de
> Frostbite. Eso se aprende trabajando con el engine, al lado de alguien que lo
> conoce, durante meses.

### 14 · Por dónde seguir — Diapositiva

**En pantalla:**
> 1. **No soltar Python.** Diez minutos, tres veces por semana. Los retos de
>    cada sesión.
> 2. **Aplicarlo a algo propio.** Un programa pequeño para una revisión que hoy
>    hacen a mano.
> 3. **Leer.** Ante un log, un error o un script ajeno: aplicar el método, y
>    hacer una pregunta precisa.

**DI:**
> Tres pasos, en orden. Diez minutos tres veces por semana valen más que dos
> horas un sábado. Escriban algo pequeño para ustedes, aunque no le sirva a
> nadie más. Y la próxima vez que vean un log o un script de otra persona, no lo
> cierren: aplíquenle el método, y hagan una pregunta precisa a quien lo
> escribió. Una buena pregunta abre más puertas que cualquier curso. En el canal
> queda todo el material.

### 15 · La última pregunta — Tablero

**En pantalla:** "De todo el programa, ¿qué vas a hacer distinto a partir de mañana?"

**DI:**
> Una última pregunta, y me gustaría leer a todos los que quieran responder.

**HAZ:** deja que escriban. Lee algunas en voz alta, sin comentarlas. Solo
agradece. Guarda las respuestas: son el resultado real del programa.

### 16 · Gracias — Diapositiva

**En pantalla:**
> Gracias.

**DI:**
> Lo último es personal.

**HAZ:** di la despedida del guion, bloque 6, con tus palabras. No la leas.
