# SESSION 7 - Soluciones (solo para el instructor)

# --- 1. Sigue el valor (sesion 1) ----------------------------------
lives = 3
backup = lives               # backup guarda una copia: 3
lives = lives - 3            # lives pasa a 0; backup no se entera

if lives > 0:                # 0 > 0 es False: el limite NO cuenta con >
    status = "playing"
else:
    status = "game over"

print(backup, status)        # 3 game over

# --- 2. Sigue el contador (sesion 2) -------------------------------
load_times = [4, 10, 12, 10, 7]
slow = 0

for seconds in load_times:
    if seconds >= 10:        # 10 >= 10 es True: aqui el limite SI cuenta
        slow = slow + 1

#   vuelta   seconds   seconds >= 10 ?   slow
#     1         4          False           0
#     2        10          True            1
#     3        12          True            2
#     4        10          True            3
#     5         7          False           3
print(slow)                  # 3

# --- 3. Lo que entra y lo que sale (sesion 3) ----------------------
def is_stable(build):
    return build["crashes"] == 0 and build["fps"] >= 30


build = {"name": "rc_02", "crashes": 0, "fps": 29}

print(is_stable(build))      # False
# crashes == 0 es True, pero fps >= 30 es False (29). Con  and  se tienen
# que cumplir las dos.

# --- 4. Leer un error (sesion 4) -----------------------------------
#   Que paso:        KeyError: se pidio la clave 'total' a un diccionario
#                    que no la tiene.
#   Donde revento:   linea 9, dentro de la funcion summary.
#   Esta mal escrita esa linea?  No necesariamente. Es el sintoma.
#   Que mirar:       donde se creo  results  (antes de la linea 14) y que
#                    claves tiene. El origen esta en quien armo el
#                    diccionario sin 'total', o lo escribio de otra forma.

# --- 5. Leer un log (sesion 5) -------------------------------------
#   Causa raiz:  14:05:47  Level 'docks_02' references missing asset
#                'props/barrel_07'   (el primer error; arriba no hay nada
#                que lo explique)
#   Sintomas:    3  (no se pudo cargar el nivel, fallo el paso, termino
#                el job)
#   Ruido:       el WARN de 14:02:11
#   Titulo:      "docks_02 referencia un asset que no existe: props/barrel_07"
#                y no "Job 6033 falla con exit code 1".
