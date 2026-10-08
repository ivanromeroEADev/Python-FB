# PyQV Foundations - Session 3: Reusable Logic
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Son los mismos ejercicios que los participantes hacen en VS Code, y al
# final las mismas dos ideas (una funcion y un diccionario) sobre assets
# reales.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings y cada print recibe un solo texto.

TEST_ASSETS = [
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DetectionTest",
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_Combo01",
]


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


# ------------------------------------------------------------------
title("1. Leer una funcion")


def check_fps(fps):
    if fps >= 30:
        return "PASS"
    else:
        return "FAIL"


print("check_fps(60)  ->  " + check_fps(60))
print("check_fps(29)  ->  " + check_fps(29))
print("check_fps(30)  ->  " + check_fps(30))


# ------------------------------------------------------------------
title("2. Sigue el valor")


def add_bonus(score):
    score = score + 5
    return score


score = 10
new_score = add_bonus(score)
print("score = 10, new_score = add_bonus(score)")
print("score vale " + str(score) + ", new_score vale " + str(new_score))


def show_bonus(points):
    print("(show_bonus muestra " + str(points + 5) + ", pero no devuelve nada)")


result = show_bonus(10)
print("result = show_bonus(10)  ->  result vale " + str(result))


# ------------------------------------------------------------------
title("3. Diccionarios")

build = {"name": "nightly_0412", "fps": 28, "crashes": 0}

print("build['name']  = " + build["name"])
print("build['fps']   = " + str(build["fps"]) + "   ->  " + check_fps(build["fps"]))
build["fps"] = build["fps"] + 2
print("build['fps']   = " + str(build["fps"]) + "   ->  " + check_fps(build["fps"]))
print("build['FPS']   -> no existe: la clave es 'fps', en minusculas")


# ------------------------------------------------------------------
title("4. El bug de or en lugar de and")


def is_valid_with_bug(speed):
    return speed >= 1 or speed <= 10


def is_valid(speed):
    return speed >= 1 and speed <= 10


print("Regla: una velocidad es valida si esta entre 1 y 10, ambos incluidos.")
for speed in [0, 1, 5, 10, 11]:
    print("speed = " + str(speed) + "   con or -> " + str(is_valid_with_bug(speed)) + "   con and -> " + str(is_valid(speed)))


# ------------------------------------------------------------------
title("5. Una funcion que recibe un diccionario")

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
    print(test["name"] + " " + check(test))


# ------------------------------------------------------------------
title("6. Un asset del engine, como diccionario")

minimum_steps = 5


def read_test_case(data_manager, asset_path):
    # Lee un asset y devuelve sus propiedades en un diccionario.
    asset = data_manager.ReadPartition(asset_path).PrimaryInstance
    return {
        "name": str(asset.TestCaseName),
        "author": str(asset.TestAuthorName),
        "steps": len(str(asset.TestCaseData.Description).splitlines()),
        "failure_message": str(asset.TestCaseData.FailureMessage),
    }


def check_steps(test_case):
    if test_case["steps"] >= minimum_steps:
        return "PASS"
    else:
        return "FAIL"


try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

    for asset_path in TEST_ASSETS:
        test_case = read_test_case(data_manager, asset_path)

        print("name            = " + test_case["name"])
        print("author          = " + test_case["author"])
        print("steps           = " + str(test_case["steps"]))
        print("failure_message = " + test_case["failure_message"])
        print("check_steps     -> " + check_steps(test_case))
        print("")

except Exception as error:
    print("No se pudieron leer los assets desde este ambiente.")
    print("Detalle: " + str(error))
    print("Las secciones 1 a 5 no dependen de esto.")

print("")
print("Fin de la demo.")
