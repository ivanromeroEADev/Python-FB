# SESSION 4 - Debugging: tracebacks, assert y bugs silenciosos
#
# Para ejecutar este archivo, en la terminal:
#     python sesion4_ejercicios.py
#
# HOY EL ARCHIVO SE ROMPE A PROPOSITO. Cada ejercicio tiene lineas con #
# que producen un error. Se trabaja asi, una linea a la vez:
#     1. predice    2. quita el #    3. ejecuta    4. LEE el mensaje
#     5. vuelve a poner el #  (si no, el programa se detiene ahi y no
#        llega a los ejercicios siguientes)

print("Session 4 ready")


# --- Ejercicio 1: las tres partes de un error ----------------------
tests_total = 40
tests_passed = 34

# Quita el # de la linea de abajo, ejecuta y NO lo arregles todavia.
# print(tests_pased)

# Lee el mensaje y responde:
#   Donde (numero de linea):        ____
#   Que linea fallo (Python la copia): ____
#   Que paso (la ultima linea):     ____
# Ahora si: arreglalo.


# --- Ejercicio 2: que error va a salir? ----------------------------
# Cuatro lineas, cuatro errores distintos. Antes de ejecutar cada una,
# elige cual de estos va a salir:
#     NameError    TypeError    IndexError    KeyError    ZeroDivisionError
crashes = 3
builds = ["b01", "b02", "b03"]
build = {"name": "b01", "fps": 28}

# A) Prediccion: ____
# print("Crashes: " + crashes)

# B) Prediccion: ____
# print(builds[3])

# C) Prediccion: ____
# print(build["crashes"])

# D) Prediccion: ____
# print(tests_passed / (tests_total - 40))


# --- Ejercicio 3: donde falla y donde se origina -------------------
def pass_rate(passed, total):
    return passed / total * 100


def report(name, passed, total):
    rate = pass_rate(passed, total)
    print(name, rate)


report("Smoke", 34, 40)

# Quita el # de la linea de abajo y ejecuta. El mensaje es mas largo.
# report("Nightly", 0, 0)

# Lee el mensaje de ABAJO hacia ARRIBA y responde:
#   Que paso (la ultima linea):               ____
#   En que linea revento, y de que funcion:   ____
#   Quien llamo a esa funcion:                ____
#   En que linea esta el dato que lo causo:   ____


# --- Ejercicio 4: el bug que no avisa ------------------------------
# Tres tiempos de carga, en segundos: 12, 15 y 18. El promedio es 15.
# Este codigo no da ningun error... pero el resultado esta mal.
load_a = 12
load_b = 15
load_c = 18

average = load_a + load_b + load_c / 3
print("Average load time:", average)

# No hay mensaje que leer. Para encontrarlo, muestra los pasos intermedios:
#   Prediccion: load_a + load_b + load_c vale ____
#   Prediccion: load_c / 3 vale ____
# Escribe dos print para comprobar tus predicciones. Despues arreglalo.


# --- Ejercicio 5: assert -------------------------------------------
# Un assert es una comprobacion: "esto SIEMPRE debe ser verdad".
# Si no lo es, el programa se detiene y avisa.
player_health = 20
damage = 35
player_health = player_health - damage

# 5a) Prediccion: player_health vale ____
# print(player_health)

# 5b) Prediccion: con el assert activo, sale "Still running"? ____
# assert player_health >= 0, "player_health must not be negative"
print("Still running")

# 5c) Escribe un assert que hubiera detectado el bug del ejercicio 4.
#     Pista: tu sabes cuanto deberia valer average.



# --- Reto (si te sobra tiempo) -------------------------------------
# a) Arregla la linea A del ejercicio 2 de dos formas distintas.
#    Pistas: str(crashes)  convierte un numero en texto;
#            print("Crashes:", crashes)  recibe dos valores separados por coma.
#
# b) Haz que report no reviente cuando total es 0: si total es 0, que
#    muestre  Nightly: no tests were run  y no llame a pass_rate.
#
# c) Agrega un assert al inicio de pass_rate que exija que total sea mayor
#    que 0, con un mensaje claro. Ejecuta  report("Nightly", 0, 0)  y compara
#    ese mensaje con el ZeroDivisionError. Cual te ayuda mas a entender que paso?
