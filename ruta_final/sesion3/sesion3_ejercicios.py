# SESSION 3 - Reusable Logic: funciones y diccionarios (nivel 2)
#
# Este archivo se trabaja en la pantalla del instructor, con control remoto.
# Una pareja escribe; el resto predice en el chat antes de ejecutar.
#
# REGLA: antes de ejecutar, predice. Escribe tu prediccion donde
# veas ____ y solo despues quita el # del print para comprobar.

print("Session 3 ready")


# --- Ejercicio 1: dos entradas, una salida -------------------------
# Esta funcion recibe DOS valores. Fijate: no tiene else.
def check_fps(fps, minimum):
    if fps >= minimum:
        return "PASS"
    return "FAIL"


# Prediccion: check_fps(30, 30) -> ____    check_fps(59, 60) -> ____
# print(check_fps(30, 30), check_fps(59, 60))

# Esta otra no tiene return.
def report(fps):
    print("fps:", fps)


# Prediccion: si quitas el # de estas dos lineas, que sale en pantalla, en orden?  ____
# r = report(45)
# print(r)


# --- Ejercicio 2: return corta la funcion --------------------------
def first_fail(values, minimum):
    for value in values:
        if value < minimum:
            return value
    return None


# Prediccion: first_fail([60, 45, 28, 12], 30) -> ____
#             Cuantas vueltas da el for antes de salir? ____
# print(first_fail([60, 45, 28, 12], 30))

# Prediccion: first_fail([60, 45], 30) -> ____    first_fail([], 30) -> ____
# print(first_fail([60, 45], 30), first_fail([], 30))


# --- Ejercicio 3: un diccionario que cuenta ------------------------
results = ["PASS", "FAIL", "PASS", "SKIP", "PASS"]
counts = {"PASS": 0, "FAIL": 0}

# Prediccion: este loop termina bien o revienta? ____
#             Si revienta: en que vuelta, y cuanto vale counts en ese momento? ____
# for result in results:
#     counts[result] = counts[result] + 1
#     print(counts)
# print("Final:", counts)

# Dos formas de arreglarlo. Cual elegiria QA, y por que?
#   A) counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}
#   B) dentro del loop:   if result in counts:
# Respuesta: ____


# --- Ejercicio 4: encuentra el bug ---------------------------------
# La regla: "un tiempo de carga es valido si esta entre low y high, ambos incluidos".
# No da ningun error, y con la primera prueba responde bien.
def in_range(value, low, high):
    return value >= low or value <= high


load_tests = [
    {"name": "load_park", "low": 5, "high": 20, "actual": 12},
]

for test in load_tests:
    print(test["name"], in_range(test["actual"], test["low"], test["high"]))

# Tu trabajo de QA: agrega a load_tests las pruebas que hagan falta hasta
# encontrar una que responda mal. Despues arregla in_range.
# Pista: hay cuatro valores que importan mas que todos los demas.
