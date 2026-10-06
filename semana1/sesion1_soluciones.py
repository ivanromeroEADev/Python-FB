# SESSION 1 - Soluciones (solo para el instructor)

# --- Ejercicio 2a --------------------------------------------------
score = 10
score = score + 5          # 15
score = score * 2          # 30
print(score)               # 30

# --- Ejercicio 2b --------------------------------------------------
a = 3
b = a                      # b guarda 3 (una copia del valor, no "sigue" a a)
a = a + 4                  # a pasa a 7; b sigue en 3
b = b * 2                  # b pasa a 6
print(a, b)                # 7 6

# --- Ejercicio 3 ---------------------------------------------------
tests_total = 40
tests_passed = 34
pass_rate = tests_passed / tests_total * 100    # 85.0

print(pass_rate > 85)      # False  (85.0 no es MAYOR que 85)
print(pass_rate >= 85)     # True   (el valor limite cuenta con >=)
print(5 + 5)               # 10
print("5" + "5")           # 55     (dos textos se pegan)
print("5" == 5)            # False  (un texto nunca es igual a un numero)

# --- Ejercicio 4 ---------------------------------------------------
# crashes = 0 -> No issues
# crashes = 2 -> Minor      (2 <= 2 es True: el valor limite cuenta)
# crashes = 3 -> Critical

# --- Ejercicio 5 ---------------------------------------------------
# El bug: la regla dice "30 o mas", pero el codigo usa >  (solo "mas de 30").
# Con fps = 30 deberia dar PASS y da FAIL. Arreglo: >=
fps = 30

if fps >= 30:
    print("PASS")
else:
    print("FAIL")

# --- Ejercicio 6 ---------------------------------------------------
expected = 5
actual = 7

if actual == expected:
    print("PASS")
else:
    print("FAIL")

# --- Reto a --------------------------------------------------------
if actual == expected:
    print("PASS")
else:
    print(f"FAIL: expected {expected}, got {actual}")

# --- Reto b --------------------------------------------------------
crashes = 3

if fps >= 30 and crashes == 0:
    print("Build OK")
else:
    print("Build needs review")
