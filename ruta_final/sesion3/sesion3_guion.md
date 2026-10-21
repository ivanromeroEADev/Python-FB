# Session 3 · Jueves 22 de octubre
# Reusable Logic: funciones y diccionarios (nivel 2)

Versión con más nivel que `semana2/sesion3_guion.md`. Las marcas son las mismas
(**DI**, **PREGUNTA**, **ESPERAS**, **SI NO RESPONDEN**, **SI FALLAN**, **HAZ**,
**IDEA CLAVE**) y las tres reglas de interacción también:

1. Pregunta al grupo o a una pareja, nunca a una persona sola.
2. Una respuesta equivocada nunca se corrige con "no". Se responde con "veamos
   por qué" y se traza el código.
3. El silencio es parte de la clase. No lo llenes.

## Qué cambia en esta versión

- **Se escribe en tu pantalla, no en la de ellos.** VS Code abierto en
  `ruta_final` (sin IA ni autocompletado, por `.vscode/settings.json`). Una pareja
  toma el control remoto y escribe; la otra persona de la pareja dicta. El resto
  predice en el chat.
- **Predicción con tiempo.** Cada predicción tiene 60 segundos, con el
  cronómetro a la vista. Se responde en el chat, todos a la vez, cuando dices
  "ahora".
- **"Explícame la línea".** Después de cada ejercicio, una pregunta a la pareja
  que escribió, sobre una línea concreta.
- **Empieza el mini-proyecto.** Los últimos 11 minutos son el hito 1 de
  `proyecto/skate_validator.py`, con un cambio de requisito anunciado en vivo.

## Objetivo de la sesión

En la versión anterior, funciones y diccionarios se veían por separado. Hoy se
juntan: funciones con dos entradas, un `return` que corta un loop y un
diccionario que cuenta. Y se usan para empezar una herramienta que crece hasta la
última sesión.

**Al terminar, el participante puede:** decir qué recibe, qué hace y qué devuelve
una función con dos entradas, predecir dónde sale una función con `return`
dentro de un loop, contar con un diccionario y explicar por qué revienta, y
escribir `check(test)` según una regla que decidió el grupo.

## Mapa de la sesión

| Min | Bloque | Ejercicios | Tipo de interacción |
|---|---|---|---|
| 0–4 | 1. Apertura y reglas nuevas | | Explicación del formato |
| 4–10 | 2. Dos entradas, una salida | 1 | Predicción con tiempo |
| 10–16 | 3. `return` corta la función | 2 | Predicción y tabla de vueltas |
| 16–24 | 4. Un diccionario que cuenta | 3 | Predicción, debate A o B |
| 24–30 | 5. Encuentra el bug | 4 | La pareja elige los valores de prueba |
| 30–41 | 6. Hito 1 del mini-proyecto | Proyecto | Decisión de grupo, control remoto, cambio de requisito |
| 41–45 | 7. Frostbite y cierre | | Demostración |

## Antes de que llegue la gente

1. **VS Code** abierto en la carpeta `ruta_final` (no en `semana2`), para que se
   aplique la configuración sin IA. Comprueba que, al escribir `pri`, no aparece
   ninguna sugerencia. Cierra el panel de chat de Copilot si está abierto.
2. En pestañas: `sesion3/sesion3_ejercicios.py` y
   `proyecto/skate_validator.py`. Las soluciones, **solo** en tu segundo
   monitor.
3. Ejecuta `python sesion3/sesion3_ejercicios.py` en la terminal y confirma que
   sale `Session 3 ready` y `load_park True`.
4. **Control remoto:** prueba antes con alguien cómo se da y se quita el control
   en la herramienta de la llamada (en Teams: "Dar control").
5. **Lista de parejas** con el orden en que pasan al control remoto. Cinco
   turnos: ejercicios 1, 2, 3 y 4, y el hito 1. Que pase primero la pareja más
   segura.
6. Un cronómetro de 60 segundos a la vista al compartir pantalla.
7. **FrostEd** con `PyQV_S3_ReusableLogic` listo (el script de la versión
   anterior; hoy solo se usa la sección 6). Ejecútalo una vez antes.
8. **No publiques** el archivo de ejercicios en el canal antes de la clase. Se
   publica al final.

---

# Bloque 1 · Apertura y reglas nuevas (0–4)

**Propósito:** explicar el formato nuevo sin que suene a desconfianza.

**DI:**
> Buenos días. Gracias por estar aquí.
>
> Hoy cambio un poco la forma de trabajar, y quiero explicar por qué.
>
> Hasta ahora, cada uno resolvía en su editor. Eso está bien, y sé que muchos
> usan IA para programar. Fuera de esta clase es una herramienta legítima. Pero
> aquí el objetivo no es que el código funcione: es que ustedes puedan leerlo,
> predecirlo y explicarlo. Esa parte la IA no la puede hacer por ustedes.
>
> Así que hoy se escribe en mi pantalla. Mi editor no tiene autocompletado ni
> sugerencias de ningún tipo. Una pareja toma el control: una persona escribe y
> la otra le dicta. El resto predice en el chat. Nadie queda expuesto solo, y
> equivocarse sigue siendo parte del trabajo.
>
> Y una regla más. Cuando pregunte, tienen sesenta segundos. Escriben la
> respuesta en el chat, pero no la envían hasta que yo diga "ahora". Así nadie
> copia la respuesta del primero.

**PREGUNTA:**
> ¿Alguna duda con el formato antes de empezar?

**HAZ:** ejecuta el archivo de ejercicios en tu terminal. Sale `Session 3 ready`.

---

# Bloque 2 · Dos entradas, una salida (4–10)

**Propósito:** una función que recibe dos valores, y una que no devuelve nada.

**HAZ:** pasa el control a la primera pareja. Que se ubique en el ejercicio 1.

**DI:**
> Lean la función check fps. Hay dos diferencias con la de la versión anterior.
> Encuéntrenlas sin ejecutar nada.

**ESPERAS:** recibe dos valores, `fps` y `minimum`. No tiene `else`.

**PREGUNTA:**
> Sesenta segundos. ¿Qué devuelve check fps con treinta y treinta? ¿Y con
> cincuenta y nueve y sesenta?

**HAZ:** cronómetro. Di "ahora". Que la pareja quite el `#` y ejecute. Sale
`PASS FAIL`.

**PREGUNTA (a la pareja):**
> Explíquenme la última línea, return FAIL. Si no hay else, ¿cuándo se ejecuta
> esa línea?

**ESPERAS:** solo cuando la condición no se cumplió, porque si se cumple, el
`return "PASS"` ya salió de la función.

**SI FALLAN:**
> Veamos por qué. Sigamos el treinta y treinta, línea por línea. Llegamos a return
> PASS. ¿Qué hace return?

**DI:**
> Ahora la función report. Miren: no tiene return.

**PREGUNTA:**
> Sesenta segundos. Si quitamos el numeral de las dos líneas, ¿qué sale en
> pantalla, y en qué orden?

**HAZ:** "ahora". Que quiten los `#` y ejecuten. Sale `fps: 45` y luego `None`.

**SI FALLAN (dicen 45 dos veces):**
> Veamos por qué. La primera línea la produjo el print de adentro de la función.
> ¿Qué le entregó la función a r?

**IDEA CLAVE:**
> Mostrar no es devolver. Lo que una función muestra se pierde en la pantalla. Lo
> que devuelve, se puede usar.

---

# Bloque 3 · `return` corta la función (10–16)

**Propósito:** que vean que `return` dentro de un loop termina todo. Prepara la
sesión de logs: "el primer error, no el último".

**HAZ:** cambia de pareja. Ejercicio 2.

**PREGUNTA:**
> Sesenta segundos. First fail, con la lista sesenta, cuarenta y cinco, veintiocho
> y doce, y el mínimo treinta. ¿Qué devuelve? Y lo difícil: ¿cuántas vueltas da el
> for?

**ESPERAS:** devuelve 28. Da tres vueltas; el 12 nunca se revisa.

**HAZ:** ejecuta. Si hay dudas con las vueltas, que la pareja escriba la tabla en
un comentario: vuelta, value, `value < minimum`.

| Vuelta | value | `value < 30` | Qué pasa |
|---|---|---|---|
| 1 | 60 | False | sigue |
| 2 | 45 | False | sigue |
| 3 | 28 | True | `return 28`: sale |

**PREGUNTA:**
> El doce también es menor que treinta. ¿Por qué no lo devolvió?

**ESPERAS:** porque el `return` ya salió en la vuelta 3.

**PREGUNTA:**
> Sesenta segundos. ¿Y con sesenta y cuarenta y cinco? ¿Y con una lista vacía?

**ESPERAS:** `None None`. Ninguna vuelta encuentra un fallo, o no hay vueltas, y
se llega al `return None` del final.

**PREGUNTA (a la pareja):**
> Explíquenme la última línea. ¿Qué pasaría si la borramos?

**ESPERAS:** devolvería `None` igual, porque una función sin `return` devuelve
`None`. Es lo del bloque anterior.

**IDEA CLAVE:**
> Return no solo entrega un valor: termina la función en ese momento, aunque esté
> dentro de un loop. Por eso esta función encuentra el primer fallo, no el último.

---

# Bloque 4 · Un diccionario que cuenta (16–24)

**Propósito:** usar un diccionario como contador, leer el `KeyError` como
información, y decidir un arreglo con criterio de QA.

**HAZ:** cambia de pareja. Ejercicio 3. Todavía no quiten los `#`.

**DI:**
> Esto junta el loop con contador del martes y los diccionarios. Counts tiene dos
> contadores, uno por clave. En cada vuelta, el resultado se usa como clave.

**PREGUNTA:**
> Sesenta segundos. ¿El loop termina bien o revienta? Si revienta, ¿en qué vuelta,
> y cuánto vale counts en ese momento?

**HAZ:** "ahora". Que quiten los `#` del loop y ejecuten.

**ESPERAS:** revienta en la vuelta 4, con `KeyError: 'SKIP'`. Antes de reventar,
counts vale `{'PASS': 2, 'FAIL': 1}`.

**DI:**
> Lean el error de abajo hacia arriba. KeyError, y la clave: SKIP. El diccionario
> no tiene esa clave, y no inventa un cero.
>
> Y miren el último print antes del error. El quinto resultado, un PASS, nunca se
> contó. Cuando un programa revienta, todo lo que venía después se pierde.

**PREGUNTA:**
> Hay dos arreglos en el archivo, A y B. Los dos hacen que el programa termine.
> Discútanlo en pareja, un minuto: ¿cuál elegiría QA, y por qué?

**HAZ:** escucha dos o tres parejas. No des tu respuesta hasta el final.

**ESPERAS:** A. Con B el programa no revienta, pero el SKIP desaparece del
reporte: dice 4 resultados cuando hubo 5.

**SI ELIGEN B:**
> Veamos qué muestra el reporte con B. ¿Cuántos resultados suma? ¿Cuántos había?

**IDEA CLAVE:**
> Un arreglo que hace desaparecer el error no siempre arregla el problema. A
> veces lo esconde. Un reporte de QA tiene que contar todo lo que pasó.

---

# Bloque 5 · Encuentra el bug (24–30)

**Propósito:** el bug silencioso de la sesión, `or` en lugar de `and`. La pareja
elige los valores de prueba.

**HAZ:** cambia de pareja. Ejercicio 4. Ejecuta: sale `load_park True`.

**DI:**
> La regla está en el comentario: entre low y high, ambos incluidos. Con doce
> responde bien. Su trabajo como QA: agregar pruebas a load tests hasta encontrar
> una que responda mal.

**PREGUNTA (al grupo, mientras la pareja escribe):**
> ¿Qué valores le dictarían ustedes? Hay cuatro que importan más que todos los
> demás.

**ESPERAS:** 4 y 5 (borde de abajo), 20 y 21 (borde de arriba).

**HAZ:** que la pareja agregue los diccionarios y ejecute. Todo sale `True`.

**PREGUNTA:**
> Cuatro sale True, y veintiuno sale True. ¿Por qué?

**ESPERAS:** con `or` basta que se cumpla una condición, y cualquier número
cumple al menos una.

**HAZ:** que cambien `or` por `and` y ejecuten. Sale `True False True True False`
en el orden en que hayan agregado las pruebas.

**IDEA CLAVE:**
> Si probamos solo con el doce, el bug no aparece nunca. Los bugs viven en los
> bordes, y elegir los valores de prueba es parte del trabajo de QA.

---

# Bloque 6 · Hito 1 del mini-proyecto (30–41)

**Propósito:** escribir la primera pieza de la herramienta, con una regla que
decidió el grupo, y adaptarla a un requisito que cambia en vivo.

**HAZ:** abre `proyecto/skate_validator.py`. Pasa el control a la última pareja,
la que mejor fue en el diagnóstico.

**DI:**
> Desde hoy construimos una herramienta, y va a crecer hasta la última sesión.
> Revisa resultados de pruebas y dice cuáles pasan. Cada prueba es un
> diccionario, con un nombre, un tipo, un límite y un valor real.
>
> Hay dos tipos. Min: el valor tiene que llegar al menos al límite, como los fps.
> Max: el valor no puede pasar del límite, como un tiempo de carga.
>
> En la última sesión, cada pareja va a explicar una de estas funciones y a
> responder una pregunta mía. Así que lo que escriban hoy tiene que poder
> explicarlo.

### Paso 0 · La decisión (2 minutos)

**PREGUNTA:**
> Antes de programar, una decisión de equipo. Fps plaza tiene límite treinta y
> sacó treinta, justo. ¿Pasa o falla? Y load time plaza: límite veinte, sacó
> veinte.

**HAZ:** deja que discutan. Si nadie lo dice, pregunta por `kickflip_detected`:
se pedía detectarlo una vez y se detectó una vez. Que la pareja escriba la
decisión en la línea `Decision:`.

**ESPERAS:** que el límite pasa. Si el grupo decide que falla, acéptalo: los
números cambian (PASS 1, FAIL 6), y las soluciones tienen los dos casos.

**DI:**
> Esa decisión ahora es de ustedes. No está en ningún enunciado de internet.

### Paso 1 · A mano (2 minutos)

**PREGUNTA:**
> Con esa decisión, cuenten a mano las siete pruebas. ¿Cuántas pasan y cuántas
> fallan? Sesenta segundos.

**ESPERAS:** PASS 4, FAIL 3.

### Pasos 2 y 3 · `check` y `summarize` (5 minutos)

**HAZ:** la pareja escribe `check(test)`. El grupo puede dictar. Si se traban,
la pregunta es: "¿qué tiene que mirar primero la función?" (el `kind`).

**HAZ:** cuando salgan las siete líneas, que escriban `summarize`. Si se traban:
"¿qué ejercicio de hoy cuenta con un diccionario?" (el 3). Debe salir
`{'PASS': 4, 'FAIL': 3}`, igual que la cuenta a mano.

**SI NO TERMINAN:** escribe tú `summarize` en voz alta, línea por línea, y que
el grupo te dicte cada una.

### El cambio de requisito (2 minutos)

**DI:**
> Llega un resultado nuevo. Agréguenlo a la lista tal cual.

**HAZ:** dicta, o pega en el chat:

```python
{"name": "manual_balance", "kind": "maximum", "limit": 10, "actual": 40},
```

**PREGUNTA:**
> Sesenta segundos. Antes de ejecutar: ¿qué va a decir su check de esta prueba?

**ESPERAS:** depende de cómo la escribieron. Si usaron `else` para el `max`, dice
`FAIL` y no da ningún error.

**PREGUNTA:**
> Miren el kind. ¿Es min o max?

**ESPERAS:** ninguno de los dos: dice `maximum`, un error de tipeo en el dato.

**DI:**
> Dio FAIL, y parece razonable. Pero es por casualidad. Si el valor real fuera
> cuatro, diría PASS, y nadie se enteraría de que el dato está roto.
>
> Requisito nuevo: si el kind no es min ni max, check devuelve ERROR, y el
> resumen lo cuenta aparte. Un dato roto no es un fallo del juego, y tampoco es un
> éxito.

**HAZ:** si queda tiempo, que la pareja lo implemente. Al ejecutar `summarize`
revienta con `KeyError: 'ERROR'`.

**PREGUNTA:**
> ¿Dónde vimos este error hoy?

**ESPERAS:** en el ejercicio 3. Falta la clave `"ERROR"` en el diccionario.

**SI NO HAY TIEMPO:** deja el requisito anunciado. Es lo primero de la próxima
sesión.

**IDEA CLAVE:**
> La regla la decidieron ustedes, y el requisito cambió a mitad de camino. En el
> trabajo real pasa siempre. Por eso importa entender el código: si no, no se sabe
> dónde tocarlo.

---

# Bloque 7 · Frostbite y cierre (41–45)

**Propósito:** un asset es un conjunto de propiedades con nombre, como los
diccionarios del validador.

**HAZ:** cambia a FrostEd. Muestra el asset `QV_Ivan_DetectionTest` con sus
propiedades.

**PREGUNTA:**
> ¿A qué se parece esto, de lo que hicieron hoy?

**ESPERAS:** a los diccionarios de `RESULTS`: nombres a la izquierda, valores a
la derecha.

**HAZ:** ejecuta `PyQV_S3_ReusableLogic` y ve directo a la sección 6. Muestra
`read_test_case` y `check_steps`, y su salida.

**DI:**
> Este script lee un asset real del engine y lo convierte en un diccionario. Después
> se lo entrega a una función que dice si pasa o no. Es la misma forma que su
> validador: un diccionario entra, un resultado sale. Lo que no hemos visto es
> cómo se le pide el asset al engine, y hoy no hace falta.

**PREGUNTA:**
> Para cerrar: de lo de hoy, ¿qué les quedó menos claro?

**HAZ:** escucha y anótalo.

**DI:**
> Gracias. Hoy subimos el nivel: funciones con dos entradas, un return que corta
> un loop, un diccionario que cuenta y que revienta, y la primera pieza de su
> herramienta, con una regla que decidieron ustedes.
>
> Ahora subo los dos archivos al canal. Si quieren, en casa pueden intentar el
> requisito del ERROR. La próxima sesión empieza por ahí, en esta pantalla y con
> otra pareja.
>
> Buen trabajo. Nos vemos en la próxima.

**HAZ:** publica en el canal `sesion3_ejercicios.py` y `skate_validator.py`
**tal como quedaron en tu pantalla**. Así nadie empieza desde un archivo
distinto.

---

## Errores probables en el hito 1

| Lo que pasa | Pregunta que lleva a la solución |
|---|---|
| `check` usa `print` en lugar de `return` | ¿Qué le entrega la función a quien la llama? (bloque 2) |
| `if test[kind] == min` sin comillas | ¿`kind` es el nombre de una variable o el texto de una clave? |
| `KeyError: 'Kind'` | ¿Cómo está escrita la clave en el diccionario? |
| `summarize` imprime y devuelve `None` | Lo mismo que report en el ejercicio 1 |
| `summarize` reescribe la regla con `>=` en vez de llamar a `check` | Si mañana cambia la regla, ¿en cuántos lugares hay que corregirla? |
| El contador vuelve a cero en cada vuelta | El bug del martes: ¿dónde está la línea que crea el diccionario? |
| Sale PASS 5, FAIL 2 | Comparen prueba por prueba con su cuenta a mano. ¿Cuál no coincide? |

## Si vas mal de tiempo

Recorta en este orden:

1. Bloque 2: haz solo la predicción de `report`; la de `check_fps` dila tú.
2. Bloque 5: da tú los cuatro valores y que la pareja solo los escriba.
3. Bloque 6: escribe tú `summarize` dictado por el grupo.
4. Bloque 7: muestra solo el asset y haz la pregunta del diccionario.

No recortes el paso 0 del hito ni el anuncio del cambio de requisito. Son lo que
hace que la herramienta sea de ellos.

## Qué observar durante la clase

| Momento | Qué mirar | Para qué te sirve |
|---|---|---|
| Bloque 1 | Cómo reciben el formato nuevo | Si hay resistencia, en la próxima sesión parte con predicciones solo por chat |
| Bloque 3 | Quién dice 4 vueltas | Sigue costando seguir un valor; vuelve a la tabla en la sesión 4 |
| Bloque 4 | Quién elige B | Piensan en "que no falle" antes que en "que informe"; es clave para los logs |
| Bloque 5 | Si alguien propone los bordes sin la pista | Mide el pensamiento de QA, no el de Python |
| Hito 1 | Si la pareja usa `else` para el `max` | Es el bug silencioso que abre la sesión siguiente |
| Hito 1 | Quién dicta y quién solo mira | Decide el orden de las parejas para la defensa final |
