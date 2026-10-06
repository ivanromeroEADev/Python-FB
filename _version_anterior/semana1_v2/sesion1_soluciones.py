# SESSION 1 - Soluciones (solo para el instructor)

# --- Ejercicio 4 ---------------------------------------------------
tests_total = 40
tests_passed = 38
tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100
print(tests_failed)        # 2
print(pass_rate)           # 95.0

# --- Ejercicio 5 (con los valores originales del archivo) ----------
# player_speed == expected_speed   -> True   (5 es igual a 5)
# pass_rate >= 90                  -> False  (85.0 no llega a 90)
# player_health > 100              -> False  (87.5 no es mayor que 100)
# Si ya cambiaron player_speed a 9 y tests_passed a 38, sale: False, True, False

# --- Ejercicio 6 ---------------------------------------------------
score = 10
score = score + 5          # 15
score = score * 2          # 30
print(score)               # 30

# --- Ejercicio 7 ---------------------------------------------------
bugs_found = 12
bugs_fixed = 7
bugs_open = bugs_found - bugs_fixed
print(bugs_open)           # 5
