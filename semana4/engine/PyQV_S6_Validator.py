# PyQV Foundations - Session 6: Mini-project
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Es el validador que los participantes construyen en VS Code, y al final
# la misma estructura (leer, convertir, revisar, contar, resumir) sobre
# assets reales.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings, cada print recibe un solo texto y el porcentaje se
# calcula con 100.0.

TEST_ASSETS = [
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DetectionTest",
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_Combo01",
]

# Las mismas lineas del archivo test_results.txt de los participantes.
RESULT_LINES = [
    "fps_main_menu,30,60",
    "fps_city_level,30,30",
    "fps_harbor_level,30,28",
    "fps_boss_fight,30,9",
    "tricks_detected,5,5",
    "session_minutes,10,12",
    "saved_replays,3,0",
    "combo_points,80,95",
]


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


# ------------------------------------------------------------------
title("1. Texto contra numero")

print("9 >= 30        ->  " + str(9 >= 30))
print("'9' >= '30'    ->  " + str("9" >= "30") + "   (los textos se comparan letra por letra)")
print("int('30')      ->  " + str(int("30")) + "   " + str(type(int("30"))))


# ------------------------------------------------------------------
title("2. El validador, con el bug")


def parse_line_with_bug(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": parts[1], "actual": parts[2]}


def parse_line(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": int(parts[1]), "actual": int(parts[2])}


def check(test):
    if test["actual"] >= test["minimum"]:
        return "PASS"
    else:
        return "FAIL"


passed = 0
failed = 0

for line in RESULT_LINES:
    test = parse_line_with_bug(line)
    result = check(test)
    print(test["name"] + " " + result)

    if result == "PASS":
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed: " + str(passed) + "  Failed: " + str(failed) + "   (a mano: 5 y 3)")


# ------------------------------------------------------------------
title("3. El validador, arreglado")

passed = 0
failed = 0

for line in RESULT_LINES:
    test = parse_line(line)
    result = check(test)

    if result == "PASS":
        passed = passed + 1
        print(test["name"] + " PASS")
    else:
        failed = failed + 1
        print(test["name"] + " FAIL (minimum " + str(test["minimum"]) + ", got " + str(test["actual"]) + ")")

assert passed + failed == len(RESULT_LINES), "every line must be counted exactly once"

print("Passed: " + str(passed) + "  Failed: " + str(failed))
print("Pass rate: " + str(passed * 100.0 / len(RESULT_LINES)))


# ------------------------------------------------------------------
title("4. La misma estructura, sobre assets del engine")

minimum_steps = 5


def read_test_case(data_manager, asset_path):
    # LEER y CONVERTIR: de un asset a un diccionario.
    asset = data_manager.ReadPartition(asset_path).PrimaryInstance
    return {
        "name": str(asset.TestCaseName),
        "author": str(asset.TestAuthorName),
        "steps": len(str(asset.TestCaseData.Description).splitlines()),
        "failure_message": str(asset.TestCaseData.FailureMessage),
    }


def check_test_case(test_case):
    # REVISAR: devuelve una lista con los problemas encontrados.
    # Una lista vacia significa que el caso pasa.
    problems = []

    if test_case["name"] == "":
        problems.append("no tiene nombre")
    if not test_case["name"].startswith("QV_"):
        problems.append("el nombre no empieza por QV_")
    if test_case["author"] == "":
        problems.append("no tiene autor")
    if test_case["steps"] < minimum_steps:
        problems.append("describe " + str(test_case["steps"]) + " pasos (minimo " + str(minimum_steps) + ")")
    if test_case["failure_message"] == "":
        problems.append("no tiene mensaje de fallo")

    return problems


print("Reglas: tiene nombre, el nombre empieza por QV_, tiene autor,")
print("        describe " + str(minimum_steps) + " pasos o mas y tiene mensaje de fallo.")
print("")

try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

    passed = 0
    failed = 0

    # CONTAR: el mismo loop con contadores.
    for asset_path in TEST_ASSETS:
        test_case = read_test_case(data_manager, asset_path)
        problems = check_test_case(test_case)

        if len(problems) == 0:
            passed = passed + 1
            print("PASS: " + test_case["name"])
        else:
            failed = failed + 1
            print("FAIL: " + test_case["name"])
            for problem in problems:
                print("        - " + problem)

    assert passed + failed == len(TEST_ASSETS), "every asset must be counted exactly once"

    # RESUMIR.
    print("")
    print("Passed: " + str(passed) + "  Failed: " + str(failed))
    print("Pass rate: " + str(passed * 100.0 / len(TEST_ASSETS)))

except Exception as error:
    print("No se pudieron leer los assets desde este ambiente.")
    print("Detalle: " + str(error))
    print("Las secciones 1 a 3 no dependen de esto.")

print("")
print("Fin de la demo.")
