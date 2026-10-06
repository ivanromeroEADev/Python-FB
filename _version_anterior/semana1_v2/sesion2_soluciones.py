# SESSION 2 - Soluciones (solo para el instructor)

fps = 28
crashes = 3

# --- Ejercicio 2 ---------------------------------------------------
# crashes = 0 -> No issues
# crashes = 2 -> Minor   (2 es menor o igual que 2: el valor limite cuenta)
# crashes = 3 -> Critical

# --- Ejercicio 3 ---------------------------------------------------
# print("Crashes: " + crashes) produce:
#   TypeError: can only concatenate str (not "int") to str
# No se puede unir un texto con un numero. Dos arreglos:
print("Crashes: " + str(crashes))
print(f"Crashes: {crashes}")

# --- Ejercicio 4 ---------------------------------------------------
test_name = "Player speed"
expected = 5
actual = 7

if actual == expected:
    print("PASS")
else:
    print("FAIL")

# --- Ejercicio 5 ---------------------------------------------------
if fps >= 30 and crashes == 0:
    print("Build OK")
else:
    print("Build needs review")

# Sale Build OK solo con, por ejemplo, fps = 60 y crashes = 0.

# --- Reto ----------------------------------------------------------
if actual == expected:
    print(f"PASS: {test_name}")
else:
    print(f"FAIL: {test_name} - expected {expected}, got {actual}")

# --- Demo del instructor: assert -----------------------------------
# (se ejecuta desde sesion2_demo_assert.py)
