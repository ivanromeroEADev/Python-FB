# SESSION 2 - Soluciones (solo para el instructor)

# --- Ejercicio 1 ---------------------------------------------------
results = ["pass", "fail", "pass", "pass"]

print(len(results))              # 4
print(results[0], results[1])    # pass fail  (la primera posicion es la 0)
print(results[3])                # pass       (la ultima: 4 valores, posiciones 0 a 3)
# print(results[4])              # IndexError: list index out of range
#                                  No existe la posicion 4. Es un valor limite.

# --- Ejercicio 2 ---------------------------------------------------
# Tal como esta: "Checking:" sale 4 veces y "Done" sale 1 vez.
# Con 4 espacios delante de print("Done"): Done sale 4 veces, una por vuelta.
# Los espacios deciden que pertenece al loop.

# --- Ejercicio 3 ---------------------------------------------------
fps_samples = [45, 30, 28, 60, 29]
low = 0

for fps in fps_samples:
    if fps < 30:
        low = low + 1

#   vuelta   fps   fps < 30 ?   low
#     1      45      False        0
#     2      30      False        0    (30 no es MENOR que 30)
#     3      28      True         1
#     4      60      False        1
#     5      29      True         2
print(low)                       # 2

# --- Ejercicio 4 ---------------------------------------------------
# El bug: builds_with_crashes = 0 esta DENTRO del loop. En cada vuelta el
# contador vuelve a cero, asi que al final solo cuenta la ultima vuelta: 1.
# Arreglo: sacar esa linea del loop y ponerla antes.
crashes_per_build = [0, 3, 0, 1, 2]
builds_with_crashes = 0

for crashes in crashes_per_build:
    if crashes > 0:
        builds_with_crashes = builds_with_crashes + 1

print("Builds with crashes:", builds_with_crashes)    # 3

# --- Ejercicio 5 ---------------------------------------------------
test_results = ["pass", "fail", "pass", "pass", "fail", "pass"]
passed = 0

for result in test_results:
    if result == "pass":
        passed = passed + 1

print("Passed:", passed)         # Passed: 4

# --- Reto a --------------------------------------------------------
passed = 0
failed = 0

for result in test_results:
    if result == "pass":
        passed = passed + 1
    else:
        failed = failed + 1

total = len(test_results)
print("Passed:", passed, " Failed:", failed, " Total:", total)

# --- Reto b --------------------------------------------------------
pass_rate = passed / total * 100
print("Pass rate:", pass_rate)   # 66.66666666666666

# --- Reto c --------------------------------------------------------
total_crashes = 0

for crashes in crashes_per_build:
    total_crashes = total_crashes + crashes

print("Total crashes:", total_crashes)    # 6
