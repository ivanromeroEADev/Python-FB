# SESSION 6 - Soluciones (solo para el instructor)
#
# Necesita test_results.txt en la misma carpeta.
# LA REGLA: una prueba PASA si su valor real es MAYOR O IGUAL que su minimo.

# --- Paso 1 --------------------------------------------------------
#   fps_main_menu,30,60       PASS
#   fps_city_level,30,30      PASS   (30 >= 30: el limite cuenta)
#   fps_harbor_level,30,28    FAIL
#   fps_boss_fight,30,9       FAIL
#   tricks_detected,5,5       PASS   (otro limite)
#   session_minutes,10,12     PASS
#   saved_replays,3,0         FAIL
#   combo_points,80,95        PASS
#
#   Lineas: 8     PASAN: 5     FALLAN: 3

# --- Paso 2 --------------------------------------------------------
results_file = open("test_results.txt")
lines = results_file.readlines()
results_file.close()

print("Lines:", len(lines))          # Lines: 8


# VERSION CON EL BUG (la que reciben los participantes): los numeros
# quedan guardados como texto.
def parse_line_with_bug(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": parts[1], "actual": parts[2]}


print(parse_line_with_bug(lines[0]))
# {'name': 'fps_main_menu', 'minimum': '30', 'actual': '60'}
print(type(parse_line_with_bug(lines[0])["minimum"]))
# <class 'str'>   Las comillas alrededor de '30' ya lo avisaban.


# --- Paso 3 --------------------------------------------------------
def check(test):
    if test["actual"] >= test["minimum"]:
        return "PASS"
    else:
        return "FAIL"


print(check(parse_line_with_bug(lines[0])))      # PASS

# --- Paso 4, todavia con el bug -------------------------------------
passed = 0
failed = 0

for line in lines:
    test = parse_line_with_bug(line)
    result = check(test)
    print(test["name"], result)

    if result == "PASS":
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed:", passed, " Failed:", failed)
# Passed: 6  Failed: 2     <- NO coincide con la cuenta a mano (5 y 3)
# La prueba distinta:  fps_boss_fight PASS   (deberia ser FAIL: 9 < 30)

# --- Paso 5 --------------------------------------------------------
print(9 >= 30, "9" >= "30")          # False True
# El bug: minimum y actual son TEXTOS. Los textos se comparan como en un
# diccionario, letra por letra: "9" va despues de "3", asi que "9" es
# "mayor" que "30". Es el  "5" == 5  de la sesion 1.
# Arreglo: convertirlos en numeros al leerlos.


def parse_line(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": int(parts[1]), "actual": int(parts[2])}


print(parse_line(lines[0]))
# {'name': 'fps_main_menu', 'minimum': 30, 'actual': 60}

passed = 0
failed = 0

for line in lines:
    test = parse_line(line)
    result = check(test)
    print(test["name"], result)

    if result == "PASS":
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed:", passed, " Failed:", failed)
# Passed: 5  Failed: 3     <- coincide con la cuenta a mano

# --- Paso 6 --------------------------------------------------------
assert passed + failed == len(lines), "every line must be counted exactly once"

pass_rate = passed / len(lines) * 100
print("Pass rate:", pass_rate)       # Pass rate: 62.5

# --- Reto a --------------------------------------------------------
for line in lines:
    test = parse_line(line)
    if check(test) == "PASS":
        print(test["name"], "PASS")
    else:
        print(f"{test['name']} FAIL (minimum {test['minimum']}, got {test['actual']})")
# fps_harbor_level FAIL (minimum 30, got 28)
# fps_boss_fight FAIL (minimum 30, got 9)
# saved_replays FAIL (minimum 3, got 0)

# --- Reto b --------------------------------------------------------
# Con la linea  load_time_score,80,n/a  al final del archivo:
#
#   File "...", line NN, in <module>
#     test = parse_line(line)
#   File "...", line NN, in parse_line
#     return {"name": parts[0], "minimum": int(parts[1]), "actual": int(parts[2])}
#   ValueError: invalid literal for int() with base 10: 'n/a'
#
# Revienta dentro de parse_line. El origen esta en el ARCHIVO DE DATOS:
# "n/a" no es un numero. El codigo no tiene nada malo.

# --- Reto c --------------------------------------------------------
def validate(file_name):
    results_file = open(file_name)
    lines = results_file.readlines()
    results_file.close()

    passed = 0
    failed = 0

    for line in lines:
        if check(parse_line(line)) == "PASS":
            passed = passed + 1
        else:
            failed = failed + 1

    assert passed + failed == len(lines), "every line must be counted exactly once"
    return {"passed": passed, "failed": failed}


print(validate("test_results.txt"))  # {'passed': 5, 'failed': 3}
