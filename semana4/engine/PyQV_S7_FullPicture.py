# PyQV Foundations - Session 7: The Full Picture
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Una validacion completa, de principio a fin, contada en siete etapas.
# Cada etapa usa lo que se vio en una sesion. Mientras trabaja, el script
# escribe su propio log; al final, lo lee con el metodo de la sesion 5.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings, cada print recibe un solo texto y el porcentaje se
# calcula con 100.0.

TEST_ASSETS = [
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DetectionTest",
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_Combo01",
]

# Con INCLUDE_MISSING_ASSET = True se agrega a la lista un asset que NO
# EXISTE, a proposito: asi el log de la demo tiene un error que leer.
# PRUEBALO ANTES DE LA CLASE. Si FrostEd reacciona mal al pedirle un asset
# que no existe (un dialogo, un bloqueo), ponlo en False.
INCLUDE_MISSING_ASSET = True

if INCLUDE_MISSING_ASSET:
    TEST_ASSETS.append("ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DoesNotExist")


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


# El log de este script: una lista de textos, como en la sesion 5.
log_lines = []


def log(level, message):
    line = level + "  " + message
    log_lines.append(line)
    print(line)


# ------------------------------------------------------------------
title("Etapa 1 - Las reglas son variables            (sesion 1)")

minimum_steps = 5
required_prefix = "QV_"

log("INFO ", "Validation started")
log("INFO ", "Rule: at least " + str(minimum_steps) + " steps")
log("INFO ", "Rule: name starts with " + required_prefix)


# ------------------------------------------------------------------
title("Etapa 2 - Lo que se revisa es una lista       (sesion 2)")

log("INFO ", "Assets to check: " + str(len(TEST_ASSETS)))


# ------------------------------------------------------------------
title("Etapa 3 - Cada asset es un diccionario        (sesion 3)")


def read_test_case(data_manager, asset_path):
    asset = data_manager.ReadPartition(asset_path).PrimaryInstance
    return {
        "name": str(asset.TestCaseName),
        "author": str(asset.TestAuthorName),
        "steps": len(str(asset.TestCaseData.Description).splitlines()),
    }


def check_test_case(test_case):
    # Devuelve una lista con los problemas. Lista vacia = el caso pasa.
    problems = []

    if not test_case["name"].startswith(required_prefix):
        problems.append("name does not start with " + required_prefix)
    if test_case["author"] == "":
        problems.append("author is empty")
    if test_case["steps"] < minimum_steps:
        problems.append("has " + str(test_case["steps"]) + " steps, minimum is " + str(minimum_steps))

    return problems


print("read_test_case:   recibe una ruta, devuelve un diccionario")
print("check_test_case:  recibe un diccionario, devuelve los problemas")


# ------------------------------------------------------------------
title("Etapa 4 - La misma revision, para todos       (sesiones 2 y 3)")

passed = 0
failed = 0
unreadable = 0
engine_available = True

try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

except Exception as error:
    engine_available = False
    log("ERROR", "Engine data is not available here: " + str(error))

if engine_available:
    for asset_path in TEST_ASSETS:
        short_name = asset_path.split("/")[-1]

        try:
            test_case = read_test_case(data_manager, asset_path)
        except Exception as error:
            unreadable = unreadable + 1
            log("ERROR", "Could not read asset '" + short_name + "'")
            continue

        problems = check_test_case(test_case)

        if len(problems) == 0:
            passed = passed + 1
            log("INFO ", "PASS " + test_case["name"])
        else:
            failed = failed + 1
            for problem in problems:
                log("WARN ", "FAIL " + test_case["name"] + ": " + problem)


# ------------------------------------------------------------------
title("Etapa 5 - Lo que siempre debe ser verdad      (sesion 4)")

if engine_available:
    assert passed + failed + unreadable == len(TEST_ASSETS), "every asset must be counted exactly once"
    print("assert: passed + failed + unreadable == total   ->  se cumple")
else:
    print("Sin datos del engine no hay nada que contar.")


# ------------------------------------------------------------------
title("Etapa 6 - El resumen")

if engine_available:
    checked = passed + failed

    log("INFO ", "Passed: " + str(passed) + "  Failed: " + str(failed) + "  Unreadable: " + str(unreadable))
    if checked > 0:
        log("INFO ", "Pass rate: " + str(passed * 100.0 / checked))

    if unreadable > 0:
        log("ERROR", "Validation finished with errors")
    else:
        log("INFO ", "Validation finished")


# ------------------------------------------------------------------
title("Etapa 7 - Leer el log que acabamos de escribir (sesion 5)")

errors = 0
warnings = 0
first_error = ""

for line in log_lines:
    if "ERROR" in line:
        errors = errors + 1
        if first_error == "":
            first_error = line
    if "WARN" in line:
        warnings = warnings + 1

print("Lineas del log: " + str(len(log_lines)))
print("Errors:   " + str(errors))
print("Warnings: " + str(warnings))
print("")

if first_error == "":
    print("No hubo errores.")
else:
    print("Ultima linea del log:")
    print("  " + log_lines[-1])
    print("Primer error (por donde empezar a leer):")
    print("  " + first_error)

print("")
print("Fin de la demo.")
