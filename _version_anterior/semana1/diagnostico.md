# Diagnóstico inicial (15 a 20 minutos)

Se responde antes de la sesión 1 y se repite, idéntico, el 30 de octubre.
Todo el contenido es inventado: no hay código, rutas ni logs reales.

## Cómo montarlo en Microsoft Forms

1. Crear un formulario de tipo **Cuestionario** (así se califica solo).
2. Una **sección** por nivel. 1 punto por pregunta.
3. Añadir en todas las preguntas la opción **"No lo sé"**. Decirles que la usen:
   adivinar estropea el resultado.
4. Forms ramifica según la respuesta a una pregunta, no según el puntaje. Por eso,
   al final de cada nivel va una pregunta puente:
   *"El siguiente nivel es más difícil. ¿Quieres continuar?"*
   - "Sí" → siguiente sección
   - "Prefiero terminar aquí" → fin del formulario
5. Desactivar "mostrar resultados automáticamente". Los resultados los ves solo tú.

Texto de introducción sugerido:

> Este cuestionario no es un examen y no afecta a nadie. Sirve para saber por dónde
> empezar el curso. Si no sabes una respuesta, marca "No lo sé". Puedes terminar
> cuando quieras.

## Pregunta inicial (sin puntaje)

**0.** Del 1 al 5, ¿cuánta experiencia tienes programando?
(1 = ninguna, 5 = programo con frecuencia)

---

## Nivel 0: lógica (sin código)

**1.** Una regla dice: *"Un nombre es válido si empieza por `tex_` y no tiene
espacios"*. ¿Cuál de estos nombres es válido?

- a) `textura_roca`
- b) `tex_roca 01`
- c) `tex_roca_01` ✔
- d) `roca_tex_01`

**2.** Sigue estas instrucciones en orden: empieza con el número 3. Súmale 2.
Si el resultado es mayor que 4, multiplícalo por 2; si no, réstale 1.
¿Qué número queda?

- a) 4
- b) 5
- c) 8
- d) 10 ✔

**3.** Tienes cuatro archivos: `a.png`, `b.wav`, `c.png`, `d.txt`. La instrucción
es: *"Por cada archivo, si termina en `.png`, anota su nombre"*. ¿Qué queda anotado?

- a) `a.png`
- b) `a.png` y `c.png` ✔
- c) Los cuatro
- d) Ninguno

*Pregunta puente → Nivel 1 o fin.*

---

## Nivel 1: leer código básico

**4.** ¿Qué muestra en pantalla este código?

```python
x = 5
x = x + 2
print(x)
```

- a) 5
- b) 7 ✔
- c) x + 2
- d) Da error

**5.** ¿Qué muestra en pantalla?

```python
nombre = "tex_roca"
print(len(nombre))
```

- a) 7
- b) 8 ✔
- c) tex_roca
- d) 2

**6.** ¿Qué muestra en pantalla?

```python
tam = 300
if tam > 256:
    print("grande")
else:
    print("ok")
```

- a) grande ✔
- b) ok
- c) grande y ok
- d) Nada

*Pregunta puente → Nivel 2 o fin.*

---

## Nivel 2: listas, diccionarios y funciones

**7.** ¿Qué muestra en pantalla?

```python
assets = ["tex_a", "mesh_b", "tex_c"]
total = 0
for a in assets:
    if a.startswith("tex_"):
        total = total + 1
print(total)
```

- a) 0
- b) 1
- c) 2 ✔
- d) 3

**8.** ¿Qué muestra en pantalla?

```python
asset = {"nombre": "tex_roca", "tam": 512}
print(asset["tam"])
```

- a) tam
- b) 512 ✔
- c) tex_roca
- d) Da error

**9.** ¿Qué muestra en pantalla?

```python
def doble(n):
    return n * 2

print(doble(3) + 1)
```

- a) 6
- b) 7 ✔
- c) 8
- d) Da error

*Pregunta puente → Nivel 3 o fin.*

---

## Nivel 3: errores, bugs y logs

**10.** Un script termina con este mensaje. ¿Qué pasó?

```
Traceback (most recent call last):
  File "validar.py", line 4, in <module>
    print(asset["tipo"])
KeyError: 'tipo'
```

- a) El archivo `validar.py` no existe
- b) El diccionario `asset` no tiene la clave `"tipo"` ✔
- c) `print` está mal escrito
- d) Falta instalar un módulo

**11.** ¿Qué muestra en pantalla este código?

```python
def es_valido(nombre):
    if nombre.startswith("tex_"):
        return True

print(es_valido("mesh_roca"))
```

- a) True
- b) False
- c) None ✔
- d) Da error

**12.** Este es el log de un job que falló. ¿Cuál es la causa raíz?

```
[10:01:02] INFO  Job 4471 iniciado
[10:01:05] WARN  Cache no encontrada, descargando
[10:03:40] ERROR No se pudo abrir 'data/levels/city_01.json': el archivo no existe
[10:03:40] ERROR El paso 'validar_niveles' fallo
[10:03:41] ERROR Job 4471 terminado con codigo 1
```

- a) No se encontró la caché
- b) Falta el archivo `city_01.json` ✔
- c) Falló el paso `validar_niveles`
- d) El job terminó con código 1

---

## Cómo leer los resultados

| Puntaje | Perfil | Qué significa |
|---|---|---|
| 0 a 3 | A: desde cero | Sigue instrucciones lógicas, nunca ha leído código |
| 4 a 6 | B: lee código simple | Entiende variables y condiciones |
| 7 a 9 | C: usa estructuras | Puede seguir bucles, diccionarios y funciones |
| 10 a 12 | D: empieza a depurar | Lee errores y logs; puede ayudarte como apoyo en clase |

**Parejas:** junta un perfil A con un B o C. Evita A con D: la distancia es tanta
que el D termina haciendo todo. Si hay algún D, pídele que circule ayudando.

**Dato a guardar:** compara la pregunta 0 (cuánto creen saber) con el puntaje real.
No lo muestres al grupo; te sirve a ti para calibrar el ritmo.

**El 30 de octubre:** mismo cuestionario. Al grupo solo se le muestra el promedio
de antes y el de después.
