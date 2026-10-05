# Session 0 · Martes 6 de octubre
# Assessment y revisión

**Cómo usar este guion:** lo que sigue a **DI** se lee tal cual. Lo que sigue a
**HAZ** lo haces tú.

| Min | Bloque |
|---|---|
| 0–5 | Opening |
| 5–27 | Diagnóstico en Pear Deck |
| 27–40 | Revisión de 5 preguntas |
| 40–45 | Preparación para el jueves y cierre |

## Antes de que llegue la gente

1. Abre el deck y comprueba que las preguntas con código se leen bien y conservan
   la sangría.
2. Ponlo en **modo a ritmo del estudiante**, para que cada uno avance a su
   velocidad y nadie quede expuesto por ir lento.
3. Comprueba que las respuestas **no se proyectan con nombres**.
4. Comprueba que al terminar puedes **guardar o exportar las respuestas por
   persona**. Las necesitas para armar parejas y para comparar el día 29.
5. Ten VS Code abierto con la letra grande, para la revisión.

---

## 1. Opening (0–5)

**DI:**
> Bienvenidos. Este programa se llama Frostbite Technical Foundations. Nos vamos
> a ver martes y jueves, 45 minutos, hasta el 29 de octubre.
>
> Quiero ser claro con lo que es y lo que no es. No van a salir de aquí siendo
> Technical Testers de Frostbite; eso toma mucho más que un mes. Lo que sí van a
> tener es la base sobre la que se construye ese trabajo: programación, lógica y
> saber leer lo que una máquina les dice.
>
> Ustedes van a escribir Python en Visual Studio Code, y yo les voy a mostrar la
> misma idea dentro de Frostbite. El mismo concepto en dos lugares.
>
> Hoy no hay clase todavía. Hoy quiero saber desde dónde partimos.

---

## 2. Diagnóstico (5–27)

**DI:**
> Vamos a hacer un cuestionario de 16 preguntas. Tienen 20 minutos.
>
> Tres cosas importantes. No es un examen y no afecta a nadie. Los resultados
> individuales solo los veo yo. Y si no saben una respuesta, marquen "No lo sé":
> adivinar me da información falsa y terminaría armando el curso mal.
>
> Las preguntas van de menos a más. Es normal no saber las últimas; están ahí
> precisamente para ver hasta dónde llega cada uno. Cada quien a su ritmo.

**HAZ:** comparte el código o enlace de acceso. Avisa cuando falten 5 minutos y
cuando falte 1. No ayudes con las respuestas; sí con problemas de acceso.

---

## 3. Revisión (27–40)

No revises las 16: no hay tiempo y además conviene no gastar todas las respuestas.
Revisa estas cinco, una por idea. No muestres quién acertó.

**DI:**
> No vamos a ver todas. Voy a mostrar cinco, porque cada una representa algo que
> vamos a aprender en este mes.

### A1 — seguir instrucciones

**DI:**
> Empieza en 3, súmale 2, y si es mayor que 4 multiplícalo por 2. Da 10. Aquí no
> hay código, pero esto ya es programar: una secuencia de pasos y una decisión.
> Quien resolvió esta ya tiene la forma de pensar. Lo demás es aprender a
> escribirlo.

### C3 — tipos de datos

**HAZ:** en VS Code, escribe y ejecuta `print("5" + "5")`. Sale `55`.

**DI:**
> Muchos esperaban 10. Sale 55 porque entre comillas no son números: son textos,
> y sumar textos los pega. El computador hace exactamente lo que le escribimos,
> no lo que queríamos decir. Esto lo vemos el jueves.

### D2 — leer un loop

**DI:**
> Este código recorre cinco resultados y cuenta cuántos son "fail". Son tres. Es
> una revisión repetida con un contador: la base de casi cualquier herramienta de
> validación. Llegamos a esto la próxima semana.

### E2 — el bug silencioso

**HAZ:** en VS Code, ejecuta `print(10 + 20 + 30 / 3)`. Sale `40.0`.

**DI:**
> Debería dar 20 y da 40. No hay ningún mensaje de error. El programa corre
> perfecto y da un resultado equivocado, porque la división se hace antes que la
> suma y faltan los paréntesis. Estos son los bugs más difíciles: los que no
> avisan. Encontrarlos es trabajo de QA técnico.

### F2 — el assertion

**DI:**
> Aparece "Assertion failed: player_health mayor o igual a 0" y el juego sigue.
> No es ruido. Alguien escribió en el código "la vida nunca debería ser negativa",
> y lo fue. Entender qué es un assertion lo vamos a lograr en este programa.
> Saber qué lo causó dentro del engine es otro nivel, y toma más tiempo. Esa
> diferencia la van a ver varias veces este mes.

---

## 4. Preparación y cierre (40–45)

**DI:**
> Para el jueves necesito que cada uno llegue con dos cosas instaladas: Python 3
> y Visual Studio Code. Vamos a comprobarlo ahora, toma un minuto.
>
> Abran una terminal: tecla Windows, escriban cmd, Enter. Escriban python, espacio,
> guion guion version, y Enter.

**HAZ:** escríbelo tú en pantalla: `python --version`

**DI:**
> Si les sale Python y un número que empieza por 3, están listos. Si sale un
> error, prueben con py en lugar de python. Si tampoco, escríbanme hoy y lo
> resolvemos antes del jueves.
>
> Les voy a compartir un archivo que se llama sesion1_ejercicios.py. Guárdenlo en
> una carpeta que puedan encontrar. No lo tienen que abrir todavía.
>
> El jueves empezamos a escribir código. Nadie se va a ir sin que algo le funcione.

---

## Después de la sesión

1. **Guarda las respuestas** del deck con nombre de cada persona.
2. **Calcula el nivel** de cada uno con la tabla de `diagnostico.md` (0 a 4, 5 a
   8, 9 a 12, 13 a 16).
3. **Arma las parejas** para el jueves: Level 0 con Level 1 o 2.
4. **Comparte `sesion1_ejercicios.py`.**
5. **Atiende a quien no le funcionó Python** antes del jueves.

## Si vas mal de tiempo

- Si el diagnóstico se alarga, revisa solo C3, E2 y F2.
- No recortes la comprobación de Python: te ahorra el problema más común de la
  primera clase.
