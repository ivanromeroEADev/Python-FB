# SESSION 3 - Reusable Logic: funciones y diccionarios
#
# Para ejecutar este archivo, en la terminal:
#     python sesion3_ejercicios.py
#
# REGLA: antes de ejecutar, predice. Escribe tu prediccion donde
# veas ____ y solo despues quita el # del print para comprobar.

print("Session 3 ready")


# --- Ejercicio 1: leer una funcion ---------------------------------
# Una funcion es una revision con nombre. Se escribe una vez (def) y se
# usa las veces que haga falta. Recibe un valor y devuelve (return) otro.
def check_fps(fps):
    if fps >= 30:
        return "PASS"
    else:
        return "FAIL"


print(check_fps(60))

# Prediccion: check_fps(29) devuelve ____   check_fps(30) devuelve ____
# print(check_fps(29), check_fps(30))


# --- Ejercicio 2: sigue el valor -----------------------------------
# 2a
def add_bonus(score):
    score = score + 5
    return score


score = 10
new_score = add_bonus(score)
# Prediccion: score vale ____   new_score vale ____
# print(score, new_score)

# 2b
def show_bonus(points):
    print(points + 5)


result = show_bonus(10)
# Prediccion: result vale ____
# print(result)


# --- Ejercicio 3: diccionarios -------------------------------------
# Un diccionario guarda juntos los datos de una misma cosa. Cada dato
# tiene un nombre (la clave) y un valor. Se pide por nombre, no por posicion.
build = {"name": "nightly_0412", "fps": 28, "crashes": 0}

print(build["name"])

# Prediccion: build["fps"] es ____   check_fps(build["fps"]) devuelve ____
# print(build["fps"], check_fps(build["fps"]))

build["fps"] = build["fps"] + 2
# Prediccion: ahora check_fps(build["fps"]) devuelve ____
# print(check_fps(build["fps"]))

# Prediccion: y esta, que hace? ____
# print(build["FPS"])


# --- Ejercicio 4: encuentra el bug ---------------------------------
# La regla dice: "Una velocidad es valida si esta entre 1 y 10, ambos incluidos."
# Este codigo no da ningun error, y con 5 responde bien.
# Tu trabajo de QA: elige valores de prueba hasta encontrar uno con el
# que responda mal. Despues encuentra el bug y arreglalo.
def is_valid(speed):
    return speed >= 1 or speed <= 10


print(is_valid(5))

# Valores que probe y lo que respondio:
#   is_valid(____) -> ____     deberia ser ____
#   is_valid(____) -> ____     deberia ser ____


# --- Ejercicio 5: escribelo tu, desde cero -------------------------
# Tres pruebas. Cada una es un diccionario; las tres estan en una lista.
tests = [
    {"name": "Player speed", "expected": 5, "actual": 5},
    {"name": "Jump height", "expected": 3, "actual": 4},
    {"name": "Max health", "expected": 100, "actual": 100},
]

# Escribe una funcion  check(test)  que reciba UN diccionario y devuelva
#   "PASS"  si su valor "actual" es igual a su valor "expected"
#   "FAIL"  si no
# Recuerda: def, dos puntos, 4 espacios, return.



# Cuando la tengas, quita el # de estas dos lineas. Debe salir:
#   Player speed PASS
#   Jump height FAIL
#   Max health PASS
# for test in tests:
#     print(test["name"], check(test))


# --- Reto (si te sobra tiempo) -------------------------------------
# a) Usa check dentro de un loop con contador y muestra:  Passed: 2 of 3
#
# b) check_fps tiene el 30 escrito adentro. Escribe  check_minimum(value, minimum)
#    que devuelva "PASS" si value es mayor o igual que minimum.
#    Comprueba: check_minimum(30, 30) -> PASS    check_minimum(59, 60) -> FAIL
#
# c) Agrega a tests una cuarta prueba que falle y confirma que tu loop la cuenta.
