# SESSION 7 - The Full Picture: repaso
#
# Para ejecutar este archivo, en la terminal:
#     python sesion7_ejercicios.py
#
# Cinco predicciones, una por cada sesion. La regla es la de siempre:
# antes de ejecutar, predice. Escribe tu prediccion donde veas ____ y solo
# despues quita el # del print para comprobar.
#
# Las dos ultimas no se ejecutan: se leen.

print("Session 7 ready")


# --- 1. Sigue el valor (sesion 1) ----------------------------------
lives = 3
backup = lives
lives = lives - 3

if lives > 0:
    status = "playing"
else:
    status = "game over"

# Prediccion: backup vale ____   status vale ____
# print(backup, status)


# --- 2. Sigue el contador (sesion 2) -------------------------------
# Regla: "Una carga es lenta si tarda 10 segundos o mas."
load_times = [4, 10, 12, 10, 7]
slow = 0

for seconds in load_times:
    if seconds >= 10:
        slow = slow + 1

# Prediccion: slow vale ____
# print(slow)


# --- 3. Lo que entra y lo que sale (sesion 3) ----------------------
# Regla: "Un build es estable si no tiene crashes Y corre a 30 fps o mas."
def is_stable(build):
    return build["crashes"] == 0 and build["fps"] >= 30


build = {"name": "rc_02", "crashes": 0, "fps": 29}

# Prediccion: is_stable(build) devuelve ____
# print(is_stable(build))


# --- 4. Leer un error (sesion 4) -----------------------------------
# Este mensaje aparecio al ejecutar otro programa. No lo ejecutes: leelo.
#
#   Traceback (most recent call last):
#     File "nightly.py", line 14, in <module>
#       summary(results)
#     File "nightly.py", line 9, in summary
#       print(results["passed"] / results["total"])
#   KeyError: 'total'
#
#   Que paso (con tus palabras):                   ____
#   En que linea revento, y dentro de que funcion: ____
#   Esa linea esta mal escrita?                    ____
#   Que irias a mirar para encontrar el origen?    ____


# --- 5. Leer un log (sesion 5) -------------------------------------
# Este es el log de un proceso que fallo. No hay nada que ejecutar.
#
#   [14:02:10] INFO  Job 6033 started
#   [14:02:11] WARN  Using default settings
#   [14:05:47] ERROR Level 'docks_02' references missing asset 'props/barrel_07'
#   [14:05:47] ERROR Could not load level 'docks_02'
#   [14:05:48] ERROR Step 'smoke_test' failed
#   [14:05:49] ERROR Job 6033 finished with exit code 1
#
#   Cual es la causa raiz (hora y mensaje):   ____
#   Cuantas lineas son sintomas:              ____
#   Que titulo le pondrias al bug:            ____
