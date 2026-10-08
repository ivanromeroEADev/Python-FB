# PyQV Foundations - Session 2: Repetition
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Son los mismos ejercicios que los participantes hacen en VS Code, y al
# final el mismo loop con contador, pero recorriendo assets reales.
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
title("1. Listas")

results = ["pass", "fail", "pass", "pass"]

print("results      = " + str(results))
print("len(results) = " + str(len(results)))
print("results[0]   = " + results[0])
print("results[3]   = " + results[3])
print("results[4]   -> no existe: la ultima posicion es la 3")


# ------------------------------------------------------------------
title("2. for")

for r in results:
    print("Checking: " + r)
print("Done")


# ------------------------------------------------------------------
title("3. Sigue el contador")

fps_samples = [45, 30, 28, 60, 29]
low = 0
lap = 0

print("Regla: contar las muestras por debajo de 30 fps.")
for fps in fps_samples:
    lap = lap + 1
    if fps < 30:
        low = low + 1
    print("vuelta " + str(lap) + "   fps = " + str(fps) + "   fps < 30 -> " + str(fps < 30) + "   low = " + str(low))

print("low vale " + str(low))


# ------------------------------------------------------------------
title("4. El bug del contador que se reinicia")

crashes_per_build = [0, 3, 0, 1, 2]
print("Regla: contar los builds con al menos un crash. Lo correcto es 3.")

for crashes in crashes_per_build:
    count_with_bug = 0
    if crashes > 0:
        count_with_bug = count_with_bug + 1

count_fixed = 0
for crashes in crashes_per_build:
    if crashes > 0:
        count_fixed = count_fixed + 1

print("contador = 0 dentro del loop   ->  " + str(count_with_bug) + "   (bug)")
print("contador = 0 antes del loop    ->  " + str(count_fixed) + "   (arreglado)")


# ------------------------------------------------------------------
title("5. Contar los pass")

test_results = ["pass", "fail", "pass", "pass", "fail", "pass"]
passed = 0

for result in test_results:
    if result == "pass":
        passed = passed + 1

print("Passed: " + str(passed))


# ------------------------------------------------------------------
title("6. El mismo loop, sobre assets del engine")

minimum_steps = 5
print("Regla: un caso de prueba pasa si describe " + str(minimum_steps) + " pasos o mas.")
print("Assets en la lista: " + str(len(TEST_ASSETS)))
print("")

try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

    passed = 0

    for asset_path in TEST_ASSETS:
        asset = data_manager.ReadPartition(asset_path).PrimaryInstance

        name = str(asset.TestCaseName)
        steps = len(str(asset.TestCaseData.Description).splitlines())

        if steps >= minimum_steps:
            passed = passed + 1
            print("PASS: " + name + " tiene " + str(steps) + " pasos")
        else:
            print("FAIL: " + name + " tiene " + str(steps) + " pasos")

    print("")
    print("Passed: " + str(passed) + " de " + str(len(TEST_ASSETS)))

except Exception as error:
    print("No se pudieron leer los assets desde este ambiente.")
    print("Detalle: " + str(error))
    print("Las secciones 1 a 5 no dependen de esto.")

print("")
print("Fin de la demo.")
