# Session 7 · Jueves 29 de octubre
# The Full Picture: Review, Final Assessment and Closing

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

Tres cosas, en este orden de importancia. Medir: el diagnóstico final, con la
misma estructura del primero y otros valores, para que cada persona vea cuánto
se movió. Ordenar: mostrar una validación completa dentro del engine y ubicar en
ella cada sesión. Y cerrar: decir con precisión qué saben, qué no, y por dónde
seguir sin ti.

**Al terminar, el participante puede:** ubicar cada pieza del programa dentro de
una validación completa, comparar su punto de llegada con su punto de partida, y
nombrar su siguiente paso.

## Mapa de la sesión

| Min | Bloque | Material | Tipo de interacción |
|---|---|---|---|
| 0–3 | 1. Apertura | | Tú expones |
| 3–12 | 2. Repaso: cinco predicciones | `sesion7_ejercicios.py` | Predicción en parejas, rápida |
| 12–14 | 3. Entrar al diagnóstico | Pear Deck | Todos entran |
| 14–34 | 4. Diagnóstico final | Pear Deck | Individual, en silencio |
| 34–40 | 5. El recorrido completo | FrostEd | Demostración y preguntas |
| 40–45 | 6. Lo que sigue, y cierre | | Tú expones, una pregunta final |

Es la sesión con menos margen. El diagnóstico ocupa veinte minutos que no se
pueden recortar. Empieza puntual.

## Antes de que llegue la gente

1. **El diagnóstico final** montado en Pear Deck: la versión paralela, con la
   misma estructura del 6 de octubre y otros valores. En **modo a ritmo del
   estudiante**, sin nombres proyectados, y con las respuestas guardadas por
   persona. Deja visible el código de acceso.
2. **VS Code** abierto en la carpeta `semana4`, con la terminal abierta y la letra
   grande. Ejecuta `python sesion7_ejercicios.py`: debe mostrar solo
   `Session 7 ready`.
3. **FrostEd** abierto con el script
   `ztest/users/ivromero/Scripts/PyQV_S7_FullPicture` listo y la ventana de
   salida limpia. **Ejecútalo una vez antes de la clase.** Este script pide a
   propósito un asset que no existe, para que su log tenga un error. Si FrostEd
   reacciona mal a eso, con un diálogo o un bloqueo, pon `INCLUDE_MISSING_ASSET`
   en `False` y usa el plan B del bloque 5.
4. El archivo `sesion7_ejercicios.py` publicado en el canal.
5. Los resultados del primer diagnóstico a mano: promedio 12,7 de 17, y las tres
   preguntas más falladas (log, loop con contador, valor límite).
6. El mensaje de cierre para el canal, listo para publicar al terminar. Está al
   final de este guion.
7. Hoy no hace falta rotar parejas. Que se sienten como quieran.

---

# Bloque 1 · Apertura (0–3)

**Propósito:** decir qué pasa hoy y por qué el diagnóstico se repite.

**DI:**
> Buenos días. Gracias por estar aquí. Es la última sesión.
>
> Hoy hacemos tres cosas. Primero, un repaso corto: cinco predicciones, una por
> sesión. Después, el diagnóstico del primer día, con otros valores. Y al final
> les muestro una validación completa dentro del engine, para que vean dónde
> encaja cada cosa que hicieron este mes.
>
> Sobre el diagnóstico, dos aclaraciones. La primera: sigue sin ser un examen.
> No va a ninguna evaluación y nadie más ve los resultados. La segunda: su
> propósito cambió. El primer día me servía a mí, para saber por dónde empezar.
> Hoy les sirve a ustedes. Cada persona va a recibir su resultado del primer día
> al lado del de hoy, y va a poder ver, pregunta por pregunta, qué se movió.
>
> Empecemos por el repaso. Abran sesion7 ejercicios y ejecútenlo.

---

# Bloque 2 · Repaso: cinco predicciones (3–12)

**Propósito:** activar las cinco ideas centrales antes del diagnóstico. Es rápido:
menos de dos minutos por predicción. No es momento de enseñar nada nuevo.

**DI:**
> Cinco predicciones. Las tres primeras se ejecutan; las dos últimas se leen.
> Tienen cuatro minutos para las cinco, con su pareja. Después las revisamos
> juntos, rápido.

**HAZ:** deja cuatro minutos. Circula. Después recorre las cinco: para cada una,
pide la respuesta al grupo, y haz una sola pregunta de fondo.

## 1 · Sigue el valor

```python
lives = 3
backup = lives
lives = lives - 3

if lives > 0:
    status = "playing"
else:
    status = "game over"
```

**PREGUNTA:**
> ¿Cuánto vale backup, y qué dice status?

**ESPERAS:** 3, y game over.

**PREGUNTA:**
> ¿Por qué backup no bajó a cero junto con lives?

**ESPERAS:** porque guardó una copia. Una variable solo sabe lo que vale ahora.

**SI FALLAN (dirán "playing"):**
> Lives vale cero. ¿Cero es mayor que cero?

## 2 · Sigue el contador

```python
load_times = [4, 10, 12, 10, 7]
slow = 0

for seconds in load_times:
    if seconds >= 10:
        slow = slow + 1
```

**PREGUNTA:**
> ¿Cuánto vale slow?

**ESPERAS:** 3.

**PREGUNTA:**
> En la predicción anterior el borde no contaba, y en esta sí. ¿Qué cambió?

**ESPERAS:** el símbolo. Antes era mayor; ahora es mayor o igual.

## 3 · Lo que entra y lo que sale

```python
def is_stable(build):
    return build["crashes"] == 0 and build["fps"] >= 30


build = {"name": "rc_02", "crashes": 0, "fps": 29}
```

**PREGUNTA:**
> ¿Qué devuelve is stable?

**ESPERAS:** False.

**PREGUNTA:**
> El build no tiene crashes. ¿Por qué no es estable?

**ESPERAS:** porque con `and` se tienen que cumplir las dos, y 29 no llega a 30.

## 4 · Leer un error

```
Traceback (most recent call last):
  File "nightly.py", line 14, in <module>
    summary(results)
  File "nightly.py", line 9, in summary
    print(results["passed"] / results["total"])
KeyError: 'total'
```

**PREGUNTA:**
> ¿Qué pasó, y dónde reventó?

**ESPERAS:** se pidió una clave, `total`, que el diccionario no tiene. Reventó en
la línea 9, dentro de `summary`.

**PREGUNTA:**
> ¿Qué irían a mirar para encontrar el origen?

**ESPERAS:** dónde se creó `results` y qué claves tiene. La línea 9 es el síntoma.

## 5 · Leer un log

```
[14:02:10] INFO  Job 6033 started
[14:02:11] WARN  Using default settings
[14:05:47] ERROR Level 'docks_02' references missing asset 'props/barrel_07'
[14:05:47] ERROR Could not load level 'docks_02'
[14:05:48] ERROR Step 'smoke_test' failed
[14:05:49] ERROR Job 6033 finished with exit code 1
```

**PREGUNTA:**
> ¿Cuál es la causa raíz?

**ESPERAS:** la de las 14:05:47: el nivel referencia un asset que no existe.

**PREGUNTA:**
> ¿Qué título le pondrían al bug?

**ESPERAS:** uno que nombre el nivel y el asset que falta. No "el job falla con
código 1".

**IDEA CLAVE:**
> Cinco sesiones, cinco ideas. Una variable solo sabe lo que vale ahora. El
> borde depende de un símbolo. A una función los valores entran por los
> paréntesis y salen por el return. Un error se lee de abajo hacia arriba. Y en
> un log, la causa suele ser el primer error, no el último.

---

# Bloque 3 · Entrar al diagnóstico (12–14)

**Propósito:** que todos estén dentro del deck antes de que empiece a correr el
tiempo.

**DI:**
> Ahora el diagnóstico. Es la misma herramienta del primer día. Abran el
> navegador y entren a joinpd punto com. El código es el que está en pantalla.

**HAZ:** señala el código. Léelo en voz alta, letra por letra, dos veces. Espera a
que todos estén dentro. Ayuda a quien no entre.

**DI:**
> Recuerden cómo funciona: cada quien avanza a su ritmo, y en esta pantalla no
> aparecen nombres.

---

# Bloque 4 · Diagnóstico final (14–34)

**Propósito:** medir. Las condiciones tienen que ser las mismas del primer día.

**DI:**
> Son las mismas preguntas del primer día en estructura, con otros valores.
> Tienen veinte minutos.
>
> Les pido lo mismo que la primera vez. Si no saben una respuesta, marquen "No
> lo sé". Una respuesta adivinada me dice que ya lo saben, y hoy eso les quitaría
> a ustedes la posibilidad de ver con claridad dónde están.
>
> Y una diferencia respecto al primer día: hoy tienen un método. Si hay un valor
> que cambia, trácenlo. Si hay un loop, hagan la tabla. Si hay un log, busquen el
> primer error. Pueden usar papel.
>
> Esta parte es individual y en silencio. Cuando quieran, empiecen.

**HAZ:** deja trabajar en silencio. Avisa cuando falten 5 minutos y cuando falte
1. No ayudes con las respuestas; sí con problemas de acceso. No abras VS Code ni
dejes código proyectado.

**DI (al faltar 5 minutos):**
> Quedan cinco minutos.

**DI (al terminar):**
> Tiempo. Gracias. Los resultados se los envío a cada persona por mensaje
> directo, con el del primer día al lado.

**HAZ:** no revises preguntas ahora. No hay tiempo, y la comparación individual
dice más que una revisión en grupo.

---

# Bloque 5 · El recorrido completo (34–40)

**Propósito:** mostrar una validación de principio a fin y ubicar en ella cada
sesión. Es la respuesta a "¿para qué sirvió todo esto?".

**HAZ:** cambia a FrostEd, con el script `PyQV_S7_FullPicture`. Ejecútalo. Recorre
la salida de arriba hacia abajo, despacio.

**DI:**
> Pasemos a Frostbite por última vez.
>
> Durante seis sesiones vieron el final de cada script: una comprobación sobre un
> asset. Hoy el script completo es una sola validación, de principio a fin,
> contada en siete etapas. Cada etapa dice de qué sesión viene.

**HAZ:** señala las etapas 1 y 2 de la salida.

**DI:**
> Etapa 1: las reglas. Cuántos pasos como mínimo, con qué debe empezar el nombre.
> Son variables. Etapa 2: lo que se va a revisar. Es una lista.

**HAZ:** señala la etapa 3, y muestra el código de `read_test_case` y
`check_test_case`.

**PREGUNTA:**
> Etapa 3. Dos funciones. Sin leer el detalle: ¿qué recibe y qué devuelve cada
> una?

**ESPERAS:** la primera recibe una ruta y devuelve un diccionario. La segunda
recibe un diccionario y devuelve los problemas que encontró.

**HAZ:** señala la etapa 4 de la salida: las líneas INFO, WARN y ERROR.

**DI:**
> Etapa 4: el loop. Recorre la lista, convierte cada asset en un diccionario, lo
> revisa y cuenta. Fíjense en la forma de lo que va escribiendo.

**PREGUNTA:**
> ¿A qué se parece esa salida?

**ESPERAS:** a un log. Tiene niveles: INFO, WARN, ERROR.

**DI:**
> Es un log. Los logs que leen todos los días los escribe un programa como este,
> línea por línea, mientras trabaja. Alguien decidió qué nivel poner en cada una.

**HAZ:** señala las etapas 5 y 6.

**DI:**
> Etapa 5: un assert. Lo que pasó, más lo que falló, más lo que no se pudo leer,
> tiene que dar el total. Etapa 6: el resumen.

**HAZ:** señala la etapa 7.

**DI:**
> Y la etapa 7 hace algo que ya saben hacer: lee el log que el propio script
> acaba de escribir. Cuenta los errores y muestra dos líneas: la última del log,
> y el primer error.

**PREGUNTA:**
> La última línea dice que la validación terminó con errores. El primer error
> dice que no se pudo leer un asset. ¿Cuál de las dos pondrían en un reporte?

**ESPERAS:** la segunda. La primera es el síntoma.

**PREGUNTA:**
> Y la advertencia, la que dice que un caso tiene un solo paso: ¿tiene que ver
> con ese error?

**ESPERAS:** no. Es otro hallazgo, independiente. Para ese error, es ruido.

**DI:**
> Ese asset no existe: lo puse en la lista a propósito. Pero la lectura que
> acaban de hacer es la de verdad.
>
> Esto es una validación técnica completa, en pequeño. Reglas, datos, una
> revisión que se repite, algo que siempre debe ser verdad, un resumen y un log.
> Las que corren sobre el juego tienen miles de assets y cientos de reglas. La
> forma es esta.

**IDEA CLAVE:**
> Nada de lo que está en esa pantalla es nuevo para ustedes. Hace cuatro semanas
> era una caja cerrada. Hoy pueden decir qué hace cada parte.

**Plan B, si `INCLUDE_MISSING_ASSET` está en `False`:** el log no tiene ningún
ERROR y la etapa 7 dice "No hubo errores". Haz las preguntas sobre la advertencia:
"¿Esa línea es un error? ¿Qué dice exactamente? ¿Qué haría falta para saber si el
caso está mal o la regla es demasiado simple?". Es la misma conversación de la
sesión 2.

**Plan B, si no se pudieron leer los assets:** la etapa 4 escribe un solo ERROR y
la etapa 7 lo muestra. Recorre el código en lugar de la salida, con las mismas
preguntas.

---

# Bloque 6 · Lo que sigue, y cierre (40–45)

**Propósito:** decir con precisión dónde están, por dónde seguir, y despedirte.

**DI:**
> Para terminar, tres cosas: dónde están, qué falta y por dónde seguir.
>
> Dónde están. El primer día el grupo promedió 75 por ciento, y dije que había
> base. Lo que faltaba no era saber qué es una variable: era seguir un valor que
> cambia, cuidar los bordes, leer un log y entender un assertion. En eso
> trabajamos. Hoy pueden trazar un loop en una tabla, leer un error de abajo
> hacia arriba, encontrar el primer error de un log, y construyeron un validador
> que funciona. Eso es real, y es de ustedes.
>
> Qué falta. Lo dije el primer día y lo repito hoy, porque sigue siendo cierto:
> este programa no forma Technical Testers. Ningún resultado del diagnóstico
> indica que alguien esté en condiciones de hacer validaciones independientes de
> Frostbite. Entre lo que saben y eso hay conocimiento del engine: qué sistemas
> tiene, cómo se le piden los datos, qué significa cada mensaje. Eso se aprende
> trabajando con el engine, al lado de alguien que lo conoce, durante meses.
>
> Por dónde seguir. Tres pasos, en orden.
>
> El primero es no soltar Python. Diez minutos, tres veces por semana, valen más
> que dos horas un sábado. Vuelvan a los retos de cada sesión: quedaron
> pendientes a propósito.
>
> El segundo es aplicarlo a algo suyo. Piensen en esa revisión que hacen a mano
> muchas veces; la mencionaron en la segunda sesión. Escriban un programa
> pequeño que haga una parte. No tiene que ser útil para nadie más.
>
> El tercero es leer. La próxima vez que vean un log, un error o un script de
> otra persona, no lo cierren. Aplíquenle el método: el primer error, la última
> línea del traceback, qué recibe y qué devuelve. Y cuando no entiendan algo,
> hagan una pregunta precisa a quien lo escribió. Una buena pregunta abre más
> puertas que cualquier curso.
>
> En el canal queda todo el material: los guiones, los ejercicios, las
> soluciones y esta ruta por escrito.

**PREGUNTA:**
> Una última pregunta, y me gustaría oír a todos los que quieran responder. De
> todo el programa, ¿qué es lo que van a hacer distinto a partir de mañana?

**HAZ:** escucha todas las respuestas que quepan. No las comentes; solo agradece
cada una. Es el momento de ellos.

**DI:**
> Gracias.
>
> Lo último es personal. Estas son mis últimas semanas en el equipo, y preparar
> este programa ha sido una buena forma de cerrarlas. Lo que sé, lo aprendí
> porque alguien se tomó el tiempo de explicármelo cuando yo no entendía nada de
> lo que veía en pantalla. Esto era lo que me correspondía hacer con eso.
>
> Les pido una sola cosa: cuando alguien del equipo esté donde ustedes estaban
> hace cuatro semanas, tómense el tiempo.
>
> Ha sido un gusto trabajar con ustedes. Gracias por estas ocho sesiones.

---

## Después de la sesión

1. **Guarda las respuestas** del deck con el nombre de cada persona.
2. **Calcula el resultado** de cada uno con la misma tabla del primer día.
3. **Envía a cada persona, por mensaje directo,** sus dos resultados lado a lado,
   y las preguntas en las que cambió. Nunca en el canal.
4. **Publica en el canal** el promedio del grupo de los dos diagnósticos, sin
   nombres, y el mensaje de cierre.
5. **Deja el material ordenado** para quien continúe: la carpeta del programa y
   una nota sobre qué funcionó y qué cambiarías.

**Mensaje de cierre para el canal:**

> Gracias a todos por estas ocho sesiones de Python QV Foundations.
>
> En este canal queda todo el material: guiones, ejercicios y soluciones de cada
> sesión.
>
> **Por dónde seguir**
> 1. No soltar Python: diez minutos, tres veces por semana. Empiecen por los
>    retos que quedaron al final de cada archivo.
> 2. Aplicarlo a algo propio: un programa pequeño que haga parte de una revisión
>    que hoy hacen a mano.
> 3. Leer: ante un log, un error o un script ajeno, aplicar el método antes de
>    cerrarlo, y hacer preguntas precisas.
>
> **El método, en cinco líneas**
> - Una variable solo sabe lo que vale ahora: se traza línea por línea.
> - El borde depende de un símbolo: se prueba el valor límite.
> - A una función los valores entran por los paréntesis y salen por el return.
> - Un error se lee de abajo hacia arriba: qué pasó, dónde, quién llamó.
> - En un log, la causa suele ser el primer error, no el último.
>
> Cada persona recibe por mensaje directo su resultado del primer diagnóstico y
> el del último.

## Si vas mal de tiempo

El diagnóstico no se recorta. Recorta en este orden:

1. Bloque 2: revisa en grupo solo las predicciones 2 y 5, las dos más falladas
   en el primer diagnóstico. Las otras tres quedan con sus soluciones en el
   canal.
2. Bloque 5: señala las siete etapas sin detenerte en el código, y haz solo la
   pregunta de la etapa 7.
3. Bloque 6: omite la pregunta final y pídeles que la respondan en el canal.

Si empezaste tarde, omite el bloque 2 completo antes que quitarle un minuto al
diagnóstico. No recortes la parte de "qué falta" ni la despedida.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Repaso, predicción 2 | Cuántos aciertan sin hacer la tabla | Era la segunda pregunta más fallada; mide lo que dejó la sesión 2 |
| Repaso, predicción 5 | Cuántos señalan el primer error | Era la más fallada: 2 de 9 |
| Diagnóstico | Quién usa papel para trazar | Mide si el método se quedó, más allá del puntaje |
| Diagnóstico | Cuántos "No lo sé" hay en la pregunta del log | El primer día fueron 5 sin responder |
| Pregunta final | Qué dicen que van a hacer distinto | Es el resultado real del programa; anótalo para tu nota de cierre |
