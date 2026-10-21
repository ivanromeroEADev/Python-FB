# SESSION 3 (nivel 2) - Soluciones (solo para el instructor)
# Incluye el ejercicio de clase y el Hito 1 del mini-proyecto.

# --- Ejercicio 1 ---------------------------------------------------
def check_fps(fps, minimum):
    if fps >= minimum:
        return "PASS"
    return "FAIL"                    # solo llega aqui si NO hubo return antes


print(check_fps(30, 30), check_fps(59, 60))   # PASS FAIL


def report(fps):
    print("fps:", fps)


r = report(45)                       # en pantalla: fps: 45
print(r)                             # None   (mostrar no es devolver)

# --- Ejercicio 2 ---------------------------------------------------
def first_fail(values, minimum):
    for value in values:
        if value < minimum:
            return value             # return sale de la funcion Y del loop
    return None


print(first_fail([60, 45, 28, 12], 30))       # 28   (3 vueltas; el 12 nunca se mira)
print(first_fail([60, 45], 30), first_fail([], 30))   # None None

# --- Ejercicio 3 ---------------------------------------------------
results = ["PASS", "FAIL", "PASS", "SKIP", "PASS"]
counts = {"PASS": 0, "FAIL": 0}

# El loop revienta en la vuelta 4 (SKIP) con KeyError: 'SKIP'.
# En ese momento counts vale {'PASS': 2, 'FAIL': 1}; el ultimo PASS no se cuenta.
try:
    for result in results:
        counts[result] = counts[result] + 1
        print(counts)
except KeyError as error:
    print("KeyError:", error)

# A es la que elegiria QA: el SKIP queda contado y visible en el reporte.
# B no revienta, pero esconde el SKIP: el reporte dice 4 resultados cuando
# hubo 5. Es un bug silencioso fabricado a proposito para "que no falle".
counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}
for result in results:
    counts[result] = counts[result] + 1
print("Final:", counts)              # Final: {'PASS': 3, 'FAIL': 1, 'SKIP': 1}

# --- Ejercicio 4 ---------------------------------------------------
# El bug: or en lugar de and. Cualquier numero cumple al menos una de las dos
# condiciones, asi que responde siempre True. Los cuatro valores que importan:
# 4 y 5 (borde de abajo), 20 y 21 (borde de arriba).
def in_range(value, low, high):
    return value >= low and value <= high


load_tests = [
    {"name": "load_park", "low": 5, "high": 20, "actual": 12},
    {"name": "below", "low": 5, "high": 20, "actual": 4},
    {"name": "low_edge", "low": 5, "high": 20, "actual": 5},
    {"name": "high_edge", "low": 5, "high": 20, "actual": 20},
    {"name": "above", "low": 5, "high": 20, "actual": 21},
]

for test in load_tests:
    print(test["name"], in_range(test["actual"], test["low"], test["high"]))
# load_park True / below False / low_edge True / high_edge True / above False
# Con el or original, las cinco salen True.


# ===================================================================
# HITO 1 - Skate Test Validator
# ===================================================================
RESULTS = [
    {"name": "kickflip_detected", "kind": "min", "limit": 1, "actual": 1},
    {"name": "fps_park", "kind": "min", "limit": 30, "actual": 28},
    {"name": "load_time_park", "kind": "max", "limit": 20, "actual": 18},
    {"name": "fps_plaza", "kind": "min", "limit": 30, "actual": 30},
    {"name": "load_time_plaza", "kind": "max", "limit": 20, "actual": 20},
    {"name": "combo_score", "kind": "min", "limit": 500, "actual": 430},
    {"name": "respawn_seconds", "kind": "max", "limit": 3, "actual": 5},
]

# Paso 1, con la decision "el limite pasa" (>= y <=):
#   kickflip PASS, fps_park FAIL, load_park PASS, fps_plaza PASS,
#   load_plaza PASS, combo FAIL, respawn FAIL  ->  PASS 4, FAIL 3
# Con la decision "el limite falla" (> y <): fps_plaza y load_plaza tambien
# fallan, y kickflip_detected (1 de 1) tambien ->  PASS 1, FAIL 6.
# Ese 1 de 1 es buen argumento en el debate: un truco detectado UNA vez
# es justo lo que se pide.


# Paso 2. Version que escribe la mayoria:
def check_v1(test):
    if test["kind"] == "min":
        if test["actual"] >= test["limit"]:
            return "PASS"
        return "FAIL"
    else:
        if test["actual"] <= test["limit"]:
            return "PASS"
        return "FAIL"


# Paso 3:
def summarize_v1(results):
    summary = {"PASS": 0, "FAIL": 0}
    for test in results:
        outcome = check_v1(test)
        summary[outcome] = summary[outcome] + 1
    return summary


for test in RESULTS:
    print(test["name"], check_v1(test))
print(summarize_v1(RESULTS))         # {'PASS': 4, 'FAIL': 3}


# --- Cambio de requisito (lo anuncias en vivo, no esta en su archivo) ---
# Llega un resultado nuevo con un error de tipeo en el kind:
NEW_RESULT = {"name": "manual_balance", "kind": "maximum", "limit": 10, "actual": 40}

# Con check_v1, "maximum" cae en el else y se trata como "max": 40 <= 10 es
# False -> FAIL. Parece razonable, pero es por casualidad: el dato esta mal.
# Con actual 4 diria PASS, y nadie se enteraria. Bug silencioso.
print("v1 con el dato malo:", check_v1(NEW_RESULT))   # FAIL

# Requisito nuevo: si kind no es "min" ni "max", check devuelve "ERROR",
# y summarize tiene que contarlo. Un dato roto no es un fallo del juego.
def check(test):
    if test["kind"] == "min":
        if test["actual"] >= test["limit"]:
            return "PASS"
        return "FAIL"
    if test["kind"] == "max":
        if test["actual"] <= test["limit"]:
            return "PASS"
        return "FAIL"
    return "ERROR"


def summarize(results):
    summary = {"PASS": 0, "FAIL": 0, "ERROR": 0}   # sin "ERROR": KeyError, como en el ejercicio 3
    for test in results:
        outcome = check(test)
        summary[outcome] = summary[outcome] + 1
    return summary


print("check con el dato malo:", check(NEW_RESULT))   # ERROR
print(summarize(RESULTS + [NEW_RESULT]))   # {'PASS': 4, 'FAIL': 3, 'ERROR': 1}
