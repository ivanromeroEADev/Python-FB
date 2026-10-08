# SESSION 3 - Soluciones (solo para el instructor)

# --- Ejercicio 1 ---------------------------------------------------
def check_fps(fps):
    if fps >= 30:
        return "PASS"
    else:
        return "FAIL"


print(check_fps(60))                 # PASS
print(check_fps(29), check_fps(30))  # FAIL PASS  (30 >= 30: el limite cuenta)

# --- Ejercicio 2a --------------------------------------------------
def add_bonus(score):
    score = score + 5                # este score es el de ADENTRO de la funcion
    return score


score = 10
new_score = add_bonus(score)         # la funcion recibe una copia del valor: 10
print(score, new_score)              # 10 15  (el score de afuera no cambio)

# --- Ejercicio 2b --------------------------------------------------
def show_bonus(points):
    print(points + 5)                # muestra 15, pero no devuelve nada


result = show_bonus(10)              # aqui aparece 15 en pantalla
print(result)                        # None  (sin return, la funcion no entrega valor)

# --- Ejercicio 3 ---------------------------------------------------
build = {"name": "nightly_0412", "fps": 28, "crashes": 0}

print(build["name"])                          # nightly_0412
print(build["fps"], check_fps(build["fps"]))  # 28 FAIL
build["fps"] = build["fps"] + 2               # 30
print(check_fps(build["fps"]))                # PASS
# print(build["FPS"])                         # KeyError: 'FPS'
#                                               La clave es "fps". Mayusculas y
#                                               minusculas son distintas.

# --- Ejercicio 4 ---------------------------------------------------
# El bug: usa  or  donde la regla necesita  and .
# "Entre 1 y 10" exige las DOS condiciones a la vez. Con  or  basta una, y
# cualquier numero cumple al menos una: la funcion responde siempre True.
#   is_valid(12) -> True   deberia ser False
#   is_valid(0)  -> True   deberia ser False
def is_valid(speed):
    return speed >= 1 and speed <= 10


print(is_valid(5))                   # True
print(is_valid(0), is_valid(1))      # False True   (limite inferior)
print(is_valid(10), is_valid(11))    # True False   (limite superior)

# --- Ejercicio 5 ---------------------------------------------------
tests = [
    {"name": "Player speed", "expected": 5, "actual": 5},
    {"name": "Jump height", "expected": 3, "actual": 4},
    {"name": "Max health", "expected": 100, "actual": 100},
]


def check(test):
    if test["actual"] == test["expected"]:
        return "PASS"
    else:
        return "FAIL"


for test in tests:
    print(test["name"], check(test))
# Player speed PASS
# Jump height FAIL
# Max health PASS

# --- Reto a --------------------------------------------------------
passed = 0

for test in tests:
    if check(test) == "PASS":
        passed = passed + 1

print("Passed:", passed, "of", len(tests))    # Passed: 2 of 3

# --- Reto b --------------------------------------------------------
def check_minimum(value, minimum):
    if value >= minimum:
        return "PASS"
    else:
        return "FAIL"


print(check_minimum(30, 30))         # PASS
print(check_minimum(59, 60))         # FAIL

# --- Reto c --------------------------------------------------------
tests.append({"name": "Respawn time", "expected": 2, "actual": 9})

passed = 0
for test in tests:
    if check(test) == "PASS":
        passed = passed + 1

print("Passed:", passed, "of", len(tests))    # Passed: 2 of 4
