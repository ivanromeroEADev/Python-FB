# PyQV Foundations - Session 1: Follow the Value
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset.
#
# Son los mismos ejercicios que los participantes hacen en VS Code, y al
# final la misma comprobacion (valor real contra valor esperado) sobre un
# asset real.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings, y los porcentajes se calculan con 100.0 (con
# decimales): en esta version, 34 / 40 da 0.

TEST_ASSET = "ztest/users/ivromero/QV_Ivan_TrickTest/QV_Ivan_DetectionTest"


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


# ------------------------------------------------------------------
title("1. Variables y tipos")

player_name = "Alex"
player_speed = 5
player_health = 87.5
is_alive = True

print("player_name   = " + str(player_name) + "    " + str(type(player_name)))
print("player_speed  = " + str(player_speed) + "       " + str(type(player_speed)))
print("player_health = " + str(player_health) + "    " + str(type(player_health)))
print("is_alive      = " + str(is_alive) + "    " + str(type(is_alive)))


# ------------------------------------------------------------------
title("2. Sigue el valor")

score = 10
print("score = 10           ->  score vale " + str(score))
score = score + 5
print("score = score + 5    ->  score vale " + str(score))
score = score * 2
print("score = score * 2    ->  score vale " + str(score))

print("")
a = 3
b = a
print("a = 3, b = a         ->  a vale " + str(a) + ", b vale " + str(b))
a = a + 4
print("a = a + 4            ->  a vale " + str(a) + ", b vale " + str(b))
b = b * 2
print("b = b * 2            ->  a vale " + str(a) + ", b vale " + str(b))


# ------------------------------------------------------------------
title("3. Operadores y comparaciones")

tests_total = 40
tests_passed = 34
tests_failed = tests_total - tests_passed
pass_rate = tests_passed * 100.0 / tests_total

print("tests_failed = " + str(tests_failed))
print("pass_rate    = " + str(pass_rate))
print("")
print("pass_rate > 85     ->  " + str(pass_rate > 85))
print("pass_rate >= 85    ->  " + str(pass_rate >= 85))
print("5 + 5              ->  " + str(5 + 5))
print("'5' + '5'          ->  " + "5" + "5")
print("'5' == 5           ->  " + str("5" == 5))


# ------------------------------------------------------------------
title("4. Decisiones")

crashes = 2

if crashes == 0:
    severity = "No issues"
elif crashes <= 2:
    severity = "Minor"
else:
    severity = "Critical"

print("crashes = " + str(crashes) + "  ->  " + severity)


# ------------------------------------------------------------------
title("5. El bug del valor limite")

fps = 30
print("Regla: la prueba pasa si el juego corre a 30 fps o mas.")
print("fps = " + str(fps))

if fps > 30:
    result_with_bug = "PASS"
else:
    result_with_bug = "FAIL"

if fps >= 30:
    result_fixed = "PASS"
else:
    result_fixed = "FAIL"

print("if fps > 30    ->  " + result_with_bug + "   (bug: falta el igual)")
print("if fps >= 30   ->  " + result_fixed + "   (arreglado)")


# ------------------------------------------------------------------
title("6. Valor real contra valor esperado, en un asset del engine")

print("Asset: " + TEST_ASSET)
print("")

try:
    import Frostbite.Framework.DataManager as DataManager

    try:
        data_manager = DataManager.Instance
    except Exception:
        import Frostbite.Framework.AddInManager as AddInManager
        data_manager = AddInManager.Instance.GetInstance[DataManager]()

    partition = data_manager.ReadPartition(TEST_ASSET)
    asset = partition.PrimaryInstance

    # Tres variables, leidas del asset en lugar de escritas a mano.
    actual_name = str(asset.TestCaseName)
    actual_author = str(asset.TestAuthorName)
    actual_steps = len(str(asset.TestCaseData.Description).splitlines())

    print("actual_name   = " + actual_name + "    " + str(type(actual_name)))
    print("actual_author = " + actual_author + "    " + str(type(actual_author)))
    print("actual_steps  = " + str(actual_steps) + "    " + str(type(actual_steps)))
    print("")

    expected_name = "QV_Ivan_DetectionTest"
    expected_author = "Ivan Romero"
    minimum_steps = 5

    if actual_name == expected_name:
        print("PASS: el nombre del caso es el esperado")
    else:
        print("FAIL: nombre - expected " + expected_name + ", got " + actual_name)

    if actual_author == expected_author:
        print("PASS: el autor es el esperado")
    else:
        print("FAIL: autor - expected " + expected_author + ", got " + actual_author)

    if actual_steps >= minimum_steps:
        print("PASS: tiene " + str(actual_steps) + " pasos (minimo " + str(minimum_steps) + ")")
    else:
        print("FAIL: tiene " + str(actual_steps) + " pasos (minimo " + str(minimum_steps) + ")")

except Exception as error:
    print("No se pudo leer el asset desde este ambiente.")
    print("Detalle: " + str(error))
    print("Las secciones 1 a 5 no dependen de esto.")

print("")
print("Fin de la demo.")
