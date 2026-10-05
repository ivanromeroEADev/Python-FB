# Sesión 1 · Guion para leer en voz alta

**Cómo usarlo:** lo que está tras **DI** se lee tal cual. Lo que está tras **HAZ**
es lo que haces tú en pantalla. Los tiempos son aproximados.

## Antes de que llegue la gente (5 minutos)

1. Abre **VS Code**.
2. **File > Open Folder** y elige `D:\curso-python-frostbite\semana1`.
3. **Terminal > New Terminal**. Aparece un panel abajo.
4. Escribe `python sesion1_demo_validador.py` y pulsa Enter. Si sale una lista de
   errores y un resumen, todo está bien. Escribe `cls` para limpiar.
5. Sube la letra con `Ctrl` y `+` tres o cuatro veces.
6. Deja el editor de Frostbite abierto en una carpeta de assets, en otra ventana.
7. Confirma que los alumnos tienen el archivo `sesion1_ejercicios.py`.

---

## 1. Bienvenida (minuto 0 a 5)

**DI:**
> Bienvenidos. Durante este mes nos vamos a ver 45 minutos por sesión para aprender
> Python desde cero, usando ejemplos del trabajo que hacemos en Frostbite.
>
> Quiero ser claro con el alcance: en un mes nadie va a salir haciendo pipeline o
> arreglando builds. Lo que sí va a pasar es que van a escribir código que funciona
> desde hoy, y van a entender de qué está hecho ese trabajo.
>
> Hay cuatro reglas. Uno: nadie toca producción, todo lo que usamos es de prueba.
> Dos: un error en pantalla no es un fracaso, es información. Tres: trabajamos en
> parejas y se turnan el teclado. Cuatro: nadie se va sin que algo le funcione.

**HAZ:** di las parejas en voz alta.

---

## 2. Demo (minuto 5 a 12)

**HAZ:** abre `sesion1_demo_validador.py` y baja hasta que no se vea el código;
o simplemente muestra la terminal vacía.

**DI:**
> Imaginen que tenemos 200 assets y cada uno debe seguir una regla de nombre: el
> tipo, un guion bajo, el nombre, otro guion bajo y dos números. Por ejemplo,
> tex_roca_01. Si alguien tuviera que revisar los 200 a mano, ¿cuánto tardaría?

**HAZ:** espera dos o tres respuestas. Luego escribe en la terminal:

```
python sesion1_demo_validador.py
```

**DI:**
> Ahí están. Revisó los 200, encontró 31 con problemas y dice qué tiene mal cada
> uno. Miren el tiempo abajo: menos de un segundo.
>
> Esto es lo que hace un script: una tarea repetitiva que a una persona le toma
> una hora y en la que se equivoca, la máquina la hace igual todas las veces.

**HAZ:** muestra el archivo por encima, sin explicarlo.

**DI:**
> Son unas 60 líneas. Hoy no las vamos a entender. Pero en las próximas sesiones
> van a escribir ustedes la parte que decide si un nombre está bien o mal.

---

## 3. Setup con todos (minuto 12 a 18)

**DI:**
> Ahora lo hacen ustedes. Síganme paso a paso; si alguien se pierde, levanta la
> mano y esperamos.
>
> Paso uno: abran Visual Studio Code.
>
> Paso dos: arriba, File, Open Folder, y elijan la carpeta donde guardaron los
> ejercicios.
>
> Paso tres: a la izquierda aparece la lista de archivos. Hagan clic en
> sesion1_ejercicios.py.
>
> Paso cuatro: arriba, Terminal, New Terminal. Abajo aparece un panel negro. Ahí
> es donde le damos órdenes al computador.
>
> Paso cinco: en ese panel escriban: python, espacio, sesion1_ejercicios.py, y
> pulsen Enter.

**HAZ:** hazlo tú también. Deben salir 5 líneas:

```
Hola, este es mi primer script
2048
2.5
tex_roca_01
262144
```

**DI:**
> Si ven esas cinco líneas, acaban de ejecutar su primer script. ¿A alguien le
> salió algo distinto?

**Si a alguien le falla:**

| Lo que le sale | Qué hacer |
|---|---|
| "python no se reconoce" | Que escriba `py` en vez de `python` |
| "No such file" | No abrió la carpeta correcta: repetir el paso dos |
| No pasa nada | No pulsó Enter, o escribió en el archivo y no en el panel de abajo |

---

## 4. Explicación del código y práctica (minuto 18 a 38)

**DI:**
> Vamos a leer el archivo juntos, de arriba hacia abajo. Python siempre ejecuta
> así: una línea, luego la siguiente.

### Los comentarios

**HAZ:** señala las líneas que empiezan con `#`.

**DI:**
> Las líneas que empiezan con el símbolo numeral son comentarios. Python las
> ignora por completo. Son notas para las personas.

### Ejercicio 1: `print`

```python
print("Hola, este es mi primer script")
```

**DI:**
> print significa "muestra esto en pantalla". Lo que va entre comillas es texto, y
> sale tal cual. Los paréntesis encierran lo que queremos mostrar.
>
> Ejercicio: cambien ese texto por su nombre. Guarden con Control S. Vuelvan al
> panel de abajo, pulsen la flecha hacia arriba para recuperar el comando, y Enter.

**HAZ:** espera a que todos vean su nombre. **Recuérdales:** primero guardar,
después ejecutar.

### Ejercicio 2: Python calcula

```python
print(1024 * 2)
print(10 / 4)
```

**DI:**
> Aquí no hay comillas, así que no es texto: son números, y Python hace la cuenta.
> El asterisco es multiplicar y la barra es dividir. Por eso salió 2048 y 2.5.

### Ejercicio 3: variables

```python
nombre_asset = "tex_roca_01"
print(nombre_asset)
```

**DI:**
> Esta es la idea más importante de hoy. Una variable es una etiqueta que le
> ponemos a un valor para usarlo después. Aquí la etiqueta se llama nombre_asset
> y guarda el texto tex_roca_01.
>
> El signo igual no significa "es igual a". Significa "guarda esto aquí".
>
> En la segunda línea, print no lleva comillas, así que no muestra la palabra
> nombre_asset: muestra lo que hay guardado dentro.
>
> Ejercicio: cambien el valor por otro nombre, guarden y ejecuten.

### Ejercicio 4: variables en cálculos

```python
ancho = 512
alto = 512
pixeles = ancho * alto
print(pixeles)
```

**DI:**
> Tres variables. Las dos primeras guardan números. La tercera guarda el
> resultado de multiplicarlas. Es el número de píxeles de una textura de 512
> por 512.
>
> Ejercicio: cambien ancho y alto a 1024. Antes de ejecutar, díganle a su pareja
> cuánto creen que va a salir.

**HAZ:** espera. Sale `1048576`.

**DI:**
> Fíjense: solo cambiaron dos números arriba y el resultado se actualizó solo.
> Para eso sirven las variables.

### Ejercicio 5: una propia

**DI:**
> Último ejercicio, sin ayuda. Al final del archivo, creen una variable llamada
> mi_asset, guárdenle un nombre cualquiera entre comillas, y muéstrenla con print.
> Cambien de persona en el teclado.

**Respuesta:**

```python
mi_asset = "mesh_puerta_02"
print(mi_asset)
```

**Si aparece un error, léelo con ellos:**

| Mensaje | Significa | Arreglo |
|---|---|---|
| `SyntaxError: unterminated string literal` | Falta cerrar una comilla | Revisar las comillas de esa línea |
| `NameError: name 'mi_aset' is not defined` | El nombre está escrito distinto en las dos líneas | Escribirlo igual; las mayúsculas cuentan |
| `SyntaxError: '(' was never closed` | Falta cerrar un paréntesis | Añadir `)` |

**DI (si sale un error):**
> Perfecto, un error. Miren: dice en qué línea está y qué pasó. Leerlos con calma
> es la mitad de este trabajo.

---

## 5. En Frostbite y cierre (minuto 38 a 45)

**HAZ:** cambia a la ventana del editor, en la carpeta de assets.

**DI:**
> Esto es lo mismo que acabamos de escribir, pero de verdad. Cada cosa que ven
> aquí tiene un nombre, y esos nombres siguen reglas. Cada pareja: anoten tres
> nombres y díganme qué patrón se repite.

**HAZ:** deja dos minutos y pide a dos parejas que respondan.

**DI:**
> Para cerrar: hoy ejecutaron un script, lo modificaron y usaron variables. La
> próxima sesión vamos a construir y limpiar nombres como estos con Python.
>
> Tarea opcional, cinco minutos: abran el archivo, cambien cualquier valor y
> ejecuten. Solo para no perder la mano. Nos vemos el [día de la próxima sesión].

---

## Si vas mal de tiempo

- Salta el ejercicio 2 (solo léelo).
- El ejercicio 5 pasa a ser la tarea.
- No saltes la parte de Frostbite: es lo que conecta la clase con el trabajo real.
