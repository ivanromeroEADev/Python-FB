# SESSION 2 - Repetition: loops y listas
#
# Para ejecutar este archivo, en la terminal:
#     python sesion2_ejercicios.py
#
# REGLA: antes de ejecutar, predice. Escribe tu prediccion donde
# veas ____ y solo despues quita el # del print para comprobar.

print("Session 2 ready")


# --- Ejercicio 1: listas -------------------------------------------
# Una lista guarda varios valores, en orden, bajo un solo nombre.
# Cada valor tiene una posicion. La primera posicion es la 0.
results = ["pass", "fail", "pass", "pass"]

print(len(results))

# Prediccion: results[0] es ____   results[1] es ____
# print(results[0], results[1])

# Prediccion: results[3] es ____
# print(results[3])

# Prediccion: y esta, que hace? ____
# print(results[4])


# --- Ejercicio 2: for ----------------------------------------------
# for repite las lineas que estan debajo (con 4 espacios), una vez por
# cada valor de la lista.
for r in results:
    print("Checking:", r)
print("Done")

# Antes de cambiar nada, predice:
#   si le pongo 4 espacios al inicio a  print("Done") , Done sale ____ veces
# Ahora hazlo y comprueba. Despues dejalo como estaba.


# --- Ejercicio 3: sigue el contador --------------------------------
# Regla: "Contar cuantas muestras estan por debajo de 30 fps."
fps_samples = [45, 30, 28, 60, 29]
low = 0

for fps in fps_samples:
    if fps < 30:
        low = low + 1

# Completa la tabla ANTES de ejecutar. Una fila por vuelta del loop:
#
#   vuelta   fps   fps < 30 ?   low al terminar la vuelta
#     1      45      ____          ____
#     2      30      ____          ____
#     3      28      ____          ____
#     4      60      ____          ____
#     5      29      ____          ____
#
# Prediccion: low vale ____
# print(low)


# --- Ejercicio 4: encuentra el bug ---------------------------------
# La regla dice: "Contar cuantos builds tuvieron al menos un crash."
# Mira la lista: la respuesta correcta es 3.
# Este codigo no da ningun error... pero el resultado esta mal.
# Encuentra el bug y arreglalo.
crashes_per_build = [0, 3, 0, 1, 2]

for crashes in crashes_per_build:
    builds_with_crashes = 0
    if crashes > 0:
        builds_with_crashes = builds_with_crashes + 1

print("Builds with crashes:", builds_with_crashes)


# --- Ejercicio 5: escribelo tu, desde cero -------------------------
test_results = ["pass", "fail", "pass", "pass", "fail", "pass"]

# Escribe un loop que cuente cuantos "pass" hay en test_results.
# Al final debe mostrar:   Passed: 4
# Necesitas tres cosas: un contador que empieza en 0 (antes del loop),
# un for con un if adentro, y un print (despues del loop).



# --- Reto (si te sobra tiempo) -------------------------------------
# a) Cuenta tambien los "fail" y muestra:  Passed: 4  Failed: 2  Total: 6
#    Pista: el total es len(test_results).
#
# b) Muestra el porcentaje de exito:  Pass rate: 66.66666666666666
#    Pista: es la misma cuenta del ejercicio 3 de la sesion 1.
#
# c) Con crashes_per_build, suma TODOS los crashes y muestra:  Total crashes: 6
#    Pista: en lugar de sumar 1 en cada vuelta, suma el valor de esa vuelta.
