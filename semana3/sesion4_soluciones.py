# SESSION 4 - Soluciones (solo para el instructor)
#
# Los numeros de linea se refieren a sesion4_ejercicios.py sin modificar.
# Si alguien agrego o quito lineas, sus numeros seran otros.

# --- Ejercicio 1 ---------------------------------------------------
# Traceback (most recent call last):
#   File "...sesion4_ejercicios.py", line 20, in <module>
#     print(tests_pased)
# NameError: name 'tests_pased' is not defined. Did you mean: 'tests_passed'?
#
#   Donde:            linea 20
#   Que linea fallo:  print(tests_pased)
#   Que paso:         NameError: ese nombre no existe. Le falta una s.
#
# (Las versiones recientes de Python agregan "Did you mean...". Las
# anteriores, y la de FrostEd, no.)
tests_total = 40
tests_passed = 34
print(tests_passed)                  # 34

# --- Ejercicio 2 ---------------------------------------------------
crashes = 3
builds = ["b01", "b02", "b03"]
build = {"name": "b01", "fps": 28}

# A) TypeError: can only concatenate str (not "int") to str      (linea 38)
#    Un texto no se puede unir con un numero.
# B) IndexError: list index out of range                          (linea 41)
#    Tres valores: posiciones 0, 1 y 2. La 3 no existe.
# C) KeyError: 'crashes'                                          (linea 44)
#    El diccionario tiene "name" y "fps". No tiene "crashes".
# D) ZeroDivisionError: division by zero                          (linea 47)
#    tests_total - 40 es 0, y no se puede dividir entre 0.

# --- Ejercicio 3 ---------------------------------------------------
def pass_rate(passed, total):
    return passed / total * 100


def report(name, passed, total):
    rate = pass_rate(passed, total)
    print(name, rate)


report("Smoke", 34, 40)              # Smoke 85.0

# Traceback (most recent call last):
#   File "...", line 63, in <module>
#     report("Nightly", 0, 0)
#   File "...", line 56, in report
#     rate = pass_rate(passed, total)
#   File "...", line 52, in pass_rate
#     return passed / total * 100
# ZeroDivisionError: division by zero
#
#   Que paso:                      ZeroDivisionError: se dividio entre cero
#   Donde revento:                 linea 52, dentro de pass_rate
#   Quien llamo a esa funcion:     report, en la linea 56
#   Donde esta el dato que lo causo: linea 63, la llamada con total = 0
#
# La linea 52 no tiene nada malo: es el sintoma. La causa esta en la 63.

# --- Ejercicio 4 ---------------------------------------------------
# El bug: la division se hace antes que la suma, asi que solo divide load_c.
#   12 + 15 + (18 / 3) = 12 + 15 + 6.0 = 33.0
# Arreglo: parentesis.
load_a = 12
load_b = 15
load_c = 18

print(load_a + load_b + load_c)      # 45
print(load_c / 3)                    # 6.0

average = (load_a + load_b + load_c) / 3
print("Average load time:", average)  # Average load time: 15.0

# --- Ejercicio 5 ---------------------------------------------------
player_health = 20
damage = 35
player_health = player_health - damage

# 5a
print(player_health)                 # -15

# 5b) No. El assert detiene el programa en esa linea:
#   AssertionError: player_health must not be negative
# "Still running" no llega a mostrarse.

# 5c) Con el bug del ejercicio 4 (average = 33.0), este assert detiene el
# programa. Con el arreglo, pasa sin decir nada.
assert average == 15, "average should be 15"
print("Still running")

# --- Reto a --------------------------------------------------------
print("Crashes: " + str(crashes))    # Crashes: 3
print("Crashes:", crashes)           # Crashes: 3

# --- Reto b --------------------------------------------------------
def report_safe(name, passed, total):
    if total == 0:
        print(name + ": no tests were run")
    else:
        rate = pass_rate(passed, total)
        print(name, rate)


report_safe("Nightly", 0, 0)         # Nightly: no tests were run

# --- Reto c --------------------------------------------------------
def pass_rate_checked(passed, total):
    assert total > 0, "pass_rate needs at least one test (total was 0)"
    return passed / total * 100


print(pass_rate_checked(34, 40))     # 85.0
# pass_rate_checked(0, 0)
# AssertionError: pass_rate needs at least one test (total was 0)
# Ese mensaje dice que se esperaba y que llego. "division by zero" solo
# dice que paso al final.
