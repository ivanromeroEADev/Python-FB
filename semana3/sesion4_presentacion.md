# Session 4 · Presentación
# Debugging: Tracebacks, Assertions and Silent Bugs

Se lee de arriba hacia abajo: una pantalla, un speech. Cómo montarla:
`presentacion.md`. Si algo se sale del camino: `sesion4_guion.md`.

| Pantallas | Bloque del guion | Min |
|---|---|---|
| 1–4 | 1. Apertura | 0–4 |
| 5–7 | 2. Las tres partes de un error | 4–11 |
| 8–10 | 3. El tipo de error | 11–18 |
| 11–14 | 4. Dónde falla y dónde se origina | 18–26 |
| 15–17 | 5. El bug que no avisa | 26–32 |
| 18–21 | 6. Assertions | 32–39 |
| 22–25 | 7. Frostbite y cierre | 39–45 |

Los tracebacks de las pantallas 5 y 11 son texto de ejemplo: escríbelos o
captúralos de tu propia terminal. Son de un archivo inventado.

---

### 1 · Portada — Diapositiva

**En pantalla:**
> Session 4 · Debugging
> Lo que pasa cuando algo falla.

**DI:**
> Buenos días. Gracias por estar aquí. Entren a la lección. Durante tres
> sesiones construimos, y cada vez que apareció un error lo leímos rápido y
> seguimos. Hoy nos detenemos ahí.

### 2 · Antes de empezar — Pregunta abierta

**En pantalla:** "Cuando aparece un mensaje de error largo, en inglés, ¿qué es lo primero que haces?"

**DI:**
> Antes de empezar, una pregunta honesta. Cuando en su trabajo aparece un
> mensaje de error largo, en inglés, ¿qué es lo primero que hacen? Al final de
> la sesión les voy a hacer la misma pregunta.

**HAZ:** no comentes las respuestas. Solo agradece.

### 3 · Tres formas de fallar — Diapositiva

**En pantalla:**
> Un programa puede fallar de tres formas:
> 1. Se detiene y deja un mensaje.
> 2. No se detiene, no dice nada, y entrega un resultado equivocado.
> 3. Tiene escrito qué debe ser siempre verdad, y avisa cuando deja de serlo.

**DI:**
> Hoy vemos las tres, y para cada una hay un método.

### 4 · Cómo se trabaja hoy — Diapositiva

**En pantalla:**
> **Hoy el archivo se rompe a propósito.** Una línea a la vez:
> 1. Predice · 2. Quita el `#` · 3. Ejecuta · 4. **Lee** el mensaje ·
> 5. Vuelve a poner el `#`
>
> **Ahora en VS Code:** abre `sesion4_ejercicios.py` y ejecútalo.

**DI:**
> Si no vuelven a poner el numeral, el programa se detiene ahí y no llega a los
> ejercicios siguientes. Abran el archivo y ejecútenlo: debe correr sin errores.

### 5 · Un traceback — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 1**
> Quita el `#` de `print(tests_pased)`, ejecuta y **no lo arregles**.

```
Traceback (most recent call last):
  File "sesion4_ejercicios.py", line 20, in <module>
    print(tests_pased)
NameError: name 'tests_pased' is not defined
```

**DI:**
> Esto se llama traceback. Significa rastro. La reacción natural es no leerlo.
> Vamos a leerlo, porque siempre tiene las mismas tres partes.

### 6 · Las tres partes — Poll

**En pantalla:** "Si tuvieras prisa, ¿qué parte del mensaje leerías primero?"

**Opciones:** La primera línea · El nombre del archivo · La línea de código copiada · La última línea

**DI:**
> Primera parte, el dónde: la línea 20. Segunda, la línea que falló: Python la
> copia. Tercera, la última línea: el tipo de error y la explicación. NameError,
> ese nombre no existe; le falta una letra. Ahora respondan: con prisa, ¿cuál
> leerían primero?

**Después:**
> La última. Ahí está el qué. Escriban las tres respuestas en el archivo, y
> ahora sí, arréglenlo.

### 7 · Idea clave — Diapositiva

**En pantalla:**
> Un mensaje de error responde tres preguntas:
> **dónde**, **qué línea**, **qué pasó**.
> Se lee desde la última línea hacia arriba.

**DI:**
> Quien lo lee en ese orden ya tiene la mitad del problema resuelto antes de
> pedir ayuda.

### 8 · ¿Qué error va a salir? — Diapositiva

**En pantalla:** captura del ejercicio 2, con los cinco nombres.

```python
crashes = 3
builds = ["b01", "b02", "b03"]
build = {"name": "b01", "fps": 28}

# A) print("Crashes: " + crashes)
# B) print(builds[3])
# C) print(build["crashes"])
# D) print(tests_passed / (tests_total - 40))
```

> NameError · TypeError · IndexError · KeyError · ZeroDivisionError

**DI:**
> La primera palabra de la última línea es el tipo de error. Cinco aparecen casi
> siempre, y ya han visto tres. Aquí hay cuatro líneas, y cada una produce un
> error distinto. Sin ejecutar, decidan con su pareja cuál le toca a cada una.
> Dos minutos. Después las comprobamos una por una.

**Al revisar:** A es TypeError, B es IndexError, C es KeyError, D es
ZeroDivisionError. Para cada una: quitan el `#`, ejecutan, leen la última línea
y vuelven a poner el `#`.

### 9 · La línea C — Poll

**En pantalla:** "Línea C: `print(build["crashes"])`. ¿Qué error?"

**Opciones:** NameError · KeyError · TypeError · IndexError

**DI:**
> Esta es la que más divide. Respondan antes de ejecutarla.

**Después:**
> KeyError. Arriba sí existe una variable crashes, pero aquí crashes está entre
> comillas, dentro de corchetes. No se busca una variable: se busca una clave
> dentro de build, y build no la tiene.

### 10 · Idea clave — Diapositiva

**En pantalla:**
> **NameError · IndexError · KeyError** → "eso no existe"
> **TypeError** → "existe, pero no es lo que esperaba"
> **ZeroDivisionError** → "ese valor no puede ser cero"

**DI:**
> El tipo de error es la primera pista. Con solo leer esa palabra ya saben qué
> clase de problema buscar.

### 11 · Un rastro más largo — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 3**
> Quita el `#` de `report("Nightly", 0, 0)`, ejecuta y **no lo arregles**.

```
Traceback (most recent call last):
  File "sesion4_ejercicios.py", line 63, in <module>
    report("Nightly", 0, 0)
  File "sesion4_ejercicios.py", line 56, in report
    rate = pass_rate(passed, total)
  File "sesion4_ejercicios.py", line 52, in pass_rate
    return passed / total * 100
ZeroDivisionError: division by zero
```

**DI:**
> Hasta aquí el error estaba en la misma línea que lo causaba. Casi nunca es
> así. Este mensaje menciona tres líneas: es el recorrido completo, quién llamó
> a quién. La primera línea dice cómo leerlo: most recent call last. La llamada
> más reciente está al final. Se lee de abajo hacia arriba. Abajo: división
> entre cero. Una más arriba: reventó en la línea 52, dentro de pass rate. Más
> arriba: la llamó report. Y arriba del todo: la línea 63.

### 12 · ¿Dónde está el origen? — Poll

**En pantalla:** "La línea 52 funcionó bien con Smoke. ¿En qué línea está el origen del problema?"

**Opciones:** Línea 52 · Línea 56 · Línea 63 · En ninguna de las tres

**DI:**
> Miren la línea 52: passed dividido entre total, por cien. Esa misma línea
> funcionó con 34 y 40. Entonces, ¿dónde está el origen?

### 13 · Síntoma y origen — Diapositiva

**En pantalla:**
> Línea 52: donde **revienta**. Es el síntoma.
> Línea 63: donde se **origina**. Ahí se entregó un total de 0.

**DI:**
> La causa está once líneas más abajo, en un dato. Si alguien reporta "falla
> pass rate en la línea 52", está reportando el síntoma, y quien reciba ese
> reporte va a mirar una línea que no tiene nada malo. Vuelvan a poner el
> numeral y guarden.

### 14 · Idea clave — Diapositiva

**En pantalla:**
> Donde algo revienta y donde se origina casi nunca son el mismo lugar.
> La última línea dice **qué** pasó. Para saber **por qué**, hay que subir.

**DI:**
> El traceback muestra el camino entre los dos.

### 15 · El bug que no avisa — Poll

**En pantalla:** captura del código, y la pregunta "El promedio de 12, 15 y 18 es 15. ¿Qué muestra este programa?"

```python
load_a = 12
load_b = 15
load_c = 18

average = load_a + load_b + load_c / 3
print("Average load time:", average)
```

**Opciones:** 15.0 · 33.0 · 45 · Da error

**DI:**
> Segunda forma de fallar: sin decir nada. Tres tiempos de carga. De cabeza, el
> promedio es 15. ¿Qué muestra el programa? Respondan y miren su salida.

### 16 · Mirar adentro — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 4 · 2 minutos**
> No hay mensaje que leer. Se muestran los pasos intermedios.
> 1. Predice `load_a + load_b + load_c` y `load_c / 3`
> 2. Escribe dos `print` para comprobarlo
> 3. Arréglalo

**DI:**
> Treinta y tres, sin traceback, sin número de línea, sin tipo de error. El
> método es otro: el resultado final está mal, así que algún paso intermedio
> también lo está. Se muestran los pasos, uno por uno, y se comparan con lo
> esperado.

**Después:**
> La suma está bien: 45. Pero la división solo se aplica al último: 18 entre 3
> es 6. La división se hace antes que la suma. Faltan paréntesis.

### 17 · Idea clave — Diapositiva

**En pantalla:**
> Un programa que no da error no es un programa correcto.
> Solo es un programa que no se detuvo.

**DI:**
> Cuando no hay mensaje, se mira adentro, hasta encontrar el primer valor que no
> coincide con lo esperado. Es lo mismo que hicieron con la tabla del loop.

### 18 · assert — Poll

**En pantalla:** captura del código, y la pregunta "Con el `assert` activo, ¿sale `Still running`?"

```python
player_health = 20
damage = 35
player_health = player_health - damage

assert player_health >= 0, "player_health must not be negative"
print("Still running")
```

**Opciones:** Sí · No · Sale dos veces · Depende

**DI:**
> Tercera forma. Un jugador con 20 de vida recibe 35 de daño: queda en menos 15.
> No tiene sentido, y sin embargo el programa sigue. Ahora lean la línea del
> assert. Significa "afirmo": afirmo que la vida es mayor o igual a cero, y esto
> tiene que ser verdad siempre. Después de la coma, un mensaje. Predigan: si
> activo esa línea, ¿sale Still running?

**Después:**
> No. Quiten el numeral y compruébenlo: AssertionError, con el mensaje que se
> dejó escrito. Un assert convierte un defecto silencioso en uno que avisa.
> Vuelvan a poner el numeral.

### 19 · Escribe uno — Diapositiva

**En pantalla:**
> **Ahora en VS Code · Ejercicio 5c · 3 minutos**
> Tú sabías que el promedio debía ser 15.
> Escribe un `assert` que lo afirme, con un mensaje.

**DI:**
> Ahora escriban uno. Cambien de persona en el teclado. Cuando lo tengan, quiten
> los paréntesis del ejercicio 4 para comprobar que su assert detiene el
> programa, y vuelvan a ponerlos.

**Mientras trabajan:** la tabla de errores está en el guion, bloque 6.

### 20 · La pregunta del diagnóstico — Pregunta abierta

**En pantalla:**
> `Assertion failed: player_health >= 0`
> …y el juego sigue funcionando.
>
> ¿Qué te dice ese mensaje?

**DI:**
> Esta pregunta estaba en el diagnóstico del primer día. ¿Qué les dice ese
> mensaje ahora?

### 21 · Idea clave — Diapositiva

**En pantalla:**
> Un assertion no es ruido.
> Alguien dejó escrito: "esto nunca debería pasar". Y pasó.

**DI:**
> Es una persona del equipo de desarrollo que lo escribió, a veces años atrás.
> Y trae el dato más valioso que puede tener un reporte: qué se esperaba.

### 22 · Frostbite — Diapositiva

**En pantalla:**
> **Frostbite**
> Los mismos mensajes, dentro del engine.

**DI:**
> Pasemos a Frostbite.

**HAZ:** comparte FrostEd y sigue el bloque 7 del guion: sección 1, sección 6 con
el assertion que falla, y sección 7 con el error que nadie atrapa.

### 23 · En Skate — Diapositiva

**En pantalla:**
> **En Skate**
> Un assertion aparece y el juego sigue.
> Tres cosas: el mensaje exacto · los pasos previos · no descartarlo.

**DI:**
> Aterricemos esto al juego. Piensen en el caso de prueba que hemos visto: el
> jugador se monta en la tabla, empuja y hace un truco. Alguien pudo dejar
> escrito en el código "afirmo que el jugador está sobre la tabla antes de
> evaluar un truco". Si un día eso no se cumple, aparece un assertion, y es muy
> posible que el juego siga como si nada. Ustedes no tienen que saber por qué
> pasó. Sí pueden hacer tres cosas desde hoy: copiar el mensaje exacto, completo;
> anotar los pasos que hicieron antes; y no descartarlo porque el juego siguió
> funcionando.

### 24 · Otra vez — Pregunta abierta

**En pantalla:** "Cuando aparece un mensaje de error largo, en inglés, ¿qué es lo primero que vas a hacer ahora?"

**DI:**
> Vuelvo a la pregunta del inicio.

**HAZ:** compara estas respuestas con las de la pantalla 2. Solo agradece.

### 25 · Resumen — Diapositiva

**En pantalla:**
> **Hoy:** un error en tres pasos · cinco tipos de error · síntoma y origen · un
> defecto sin mensaje · un assertion escrito por ustedes
>
> **Jueves:** leer un log
> **Tarea opcional:** los retos al final del archivo. El reto c es el más
> interesante.

**DI:**
> Gracias. El jueves aplicamos esto mismo a un log: muchas líneas, varios
> errores y una sola causa. Con lo de hoy ya tienen la idea que hace falta: el
> último error casi nunca es la causa. Buen trabajo.
