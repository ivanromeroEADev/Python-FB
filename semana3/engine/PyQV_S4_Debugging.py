# PyQV Foundations - Session 4: Debugging
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Son los mismos errores que los participantes provocan en VS Code, y al
# final assertions sobre assets reales.
#
# OJO: con RAISE_AT_END = True, el script TERMINA CON UN ERROR A PROPOSITO,
# para que se vea como muestra FrostEd un assertion que nadie atrapo.
# Ponlo en False si quieres que termine limpio.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings y cada print recibe un solo texto. Los mensajes de
# error pueden estar redactados de otra forma; el tipo de error es el mismo.

import traceback

RAISE_AT_END = True

TEST_ASSETS = [
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DetectionTest",
    "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_Combo01",
]


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


def show_error(error):
    # Muestra el tipo de error y su mensaje, como la ultima linea de un traceback.
    print(type(error).__name__ + ": " + str(error))


# ------------------------------------------------------------------
title("1. Las tres partes de un error")

tests_total = 40
tests_passed = 34

try:
    print(tests_pased)
except Exception as error:
    print(traceback.format_exc())
    print("Ultima linea -> que paso:")
    show_error(error)


# ------------------------------------------------------------------
title("2. Cuatro errores distintos")

crashes = 3
builds = ["b01", "b02", "b03"]
build = {"name": "b01", "fps": 28}

print("A) 'Crashes: ' + crashes")
try:
    print("Crashes: " + crashes)
except Exception as error:
    show_error(error)

print("B) builds[3]")
try:
    print(builds[3])
except Exception as error:
    show_error(error)

print("C) build['crashes']")
try:
    print(build["crashes"])
except Exception as error:
    show_error(error)

print("D) tests_passed / (tests_total - 40)")
try:
    print(tests_passed / (tests_total - 40))
except Exception as error:
    show_error(error)


# ------------------------------------------------------------------
title("3. Donde falla y donde se origina")


def pass_rate(passed, total):
    return passed * 100.0 / total


def report(name, passed, total):
    rate = pass_rate(passed, total)
    print(name + " " + str(rate))


report("Smoke", 34, 40)

try:
    report("Nightly", 0, 0)
except Exception as error:
    print(traceback.format_exc())
    print("Revienta dentro de pass_rate. El dato que lo causa viene de la llamada.")


# ------------------------------------------------------------------
title("4. El bug que no avisa")

load_a = 12
load_b = 15
load_c = 18

average_with_bug = load_a + load_b + load_c / 3.0
average_fixed = (load_a + load_b + load_c) / 3.0

print("load_a + load_b + load_c / 3      ->  " + str(average_with_bug) + "   (bug, sin ningun mensaje)")
print("(load_a + load_b + load_c) / 3    ->  " + str(average_fixed) + "   (arreglado)")


# ------------------------------------------------------------------
title("5. assert")

player_health = 20
damage = 35
player_health = player_health - damage
print("player_health = " + str(player_health))

try:
    assert player_health >= 0, "player_health must not be negative"
    print("Still running")
except AssertionError as error:
    show_error(error)
    print("(el programa se habria detenido aqui)")


# ------------------------------------------------------------------
title("6. Assertions sobre assets del engine")

minimum_steps = 5
print("Tres cosas que SIEMPRE deben ser verdad en un caso de prueba:")
print("  tiene nombre, tiene autor y describe " + str(minimum_steps) + " pasos o mas.")
print("")

failed_assertions = 0

try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

    for asset_path in TEST_ASSETS:
        asset = data_manager.ReadPartition(asset_path).PrimaryInstance

        name = str(asset.TestCaseName)
        author = str(asset.TestAuthorName)
        steps = len(str(asset.TestCaseData.Description).splitlines())

        print("Asset: " + name + "   (autor: " + author + ", pasos: " + str(steps) + ")")
        try:
            assert name != "", "TestCaseName must not be empty"
            assert author != "", "TestAuthorName must not be empty"
            assert steps >= minimum_steps, name + " must describe at least " + str(minimum_steps) + " steps, got " + str(steps)
            print("  OK: los tres assertions se cumplen")
        except AssertionError as error:
            failed_assertions = failed_assertions + 1
            print("  Assertion failed: " + str(error))

    print("")
    print("Assets con un assertion fallido: " + str(failed_assertions))

except Exception as error:
    print("No se pudieron leer los assets desde este ambiente.")
    print("Detalle: " + str(error))
    print("Las secciones 1 a 5 no dependen de esto.")


# ------------------------------------------------------------------
title("7. Un assertion que nadie atrapa")

print("Hasta aqui, el script atrapo cada error y siguio.")
print("Este ultimo no lo atrapa nadie. Mira como lo muestra FrostEd.")
print("")

if RAISE_AT_END:
    assert player_health >= 0, "player_health must not be negative"

print("Fin de la demo.")
