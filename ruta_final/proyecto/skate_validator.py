# MINI-PROJECT - Skate Test Validator
#
# Una herramienta que revisa resultados de pruebas y dice cuales pasan.
# Se construye en clase, un hito por sesion, siempre sobre este mismo archivo.
# Al final, cada pareja explica una de sus funciones y responde una pregunta.
#
#   Hito 1 (sesion 3): revisar UNA prueba y resumir muchas
#   Hito 2 (sesion 4): que la herramienta se pruebe a si misma (assert)
#   Hito 3 (sesion 5): leer los resultados desde un archivo y un log
#   Hito 4 (sesion 6): reporte final y defensa
#
# Los datos son inventados.

print("Skate Test Validator")


# ===================================================================
# HITO 1 - revisar una prueba y resumir muchas
# ===================================================================

# Cada prueba es un diccionario:
#   "kind": "min"  -> el valor real tiene que llegar AL MENOS al limite (fps, puntaje)
#   "kind": "max"  -> el valor real NO puede pasar del limite (tiempos)
RESULTS = [
    {"name": "kickflip_detected", "kind": "min", "limit": 1, "actual": 1},
    {"name": "fps_park", "kind": "min", "limit": 30, "actual": 28},
    {"name": "load_time_park", "kind": "max", "limit": 20, "actual": 18},
    {"name": "fps_plaza", "kind": "min", "limit": 30, "actual": 30},
    {"name": "load_time_plaza", "kind": "max", "limit": 20, "actual": 20},
    {"name": "combo_score", "kind": "min", "limit": 500, "actual": 430},
    {"name": "respawn_seconds", "kind": "max", "limit": 3, "actual": 5},
]

# --- Paso 0: la decision del equipo --------------------------------
# Un valor que queda JUSTO en el limite, pasa o falla?
# Lo decide el grupo en clase. Escribe aqui lo que se acordo:
#   Decision: ____


# --- Paso 1: a mano, sin codigo ------------------------------------
# Con esa decision, revisa las 7 pruebas a mano.
#   PASS: ____    FAIL: ____
# Esos numeros son tu forma de saber si la herramienta funciona.


# --- Paso 2: check(test) -------------------------------------------
# Recibe UN diccionario de RESULTS y devuelve "PASS" o "FAIL",
# segun su "kind" y la decision del paso 0.



# Cuando la tengas, quita el # de estas lineas. Una linea por prueba.
# for test in RESULTS:
#     print(test["name"], check(test))


# --- Paso 3: summarize(results) ------------------------------------
# Recibe la lista completa y DEVUELVE (no imprime) un diccionario con
# cuantas pasan y cuantas fallan, con esta forma:   {"PASS": __, "FAIL": __}
# Usa check adentro: la regla no se escribe dos veces.



# Cuando la tengas:
# print(summarize(RESULTS))
