# SESSION 1 - Thinking Like a Programmer: Follow the Value
#
# Las lineas que empiezan con # son comentarios. Python las ignora.
#
# Para ejecutar este archivo, en la terminal:
#     python sesion1_ejercicios.py
#
# REGLA DE HOY: antes de ejecutar, predice. Escribe tu prediccion donde
# veas ____ y solo despues quita el # del print para comprobar.

print("Hello, QA team")


# --- Ejercicio 1: variables y tipos --------------------------------
# Una variable es un nombre que guarda un valor. Cada valor tiene un tipo.
player_name = "Alex"      # str:   texto, siempre entre comillas
player_speed = 5          # int:   numero entero
player_health = 87.5      # float: numero con decimales
is_alive = True           # bool:  True o False

print(type(player_name))
print(type(player_speed))
print(type(player_health))
print(type(is_alive))


# --- Ejercicio 2: sigue el valor -----------------------------------
# El signo = no significa "es igual a". Significa "guarda esto aqui".

# 2a
score = 10
score = score + 5
score = score * 2
# Prediccion: score vale ____
# print(score)

# 2b
a = 3
b = a
a = a + 4
b = b * 2
# Prediccion: a vale ____   b vale ____
# print(a, b)


# --- Ejercicio 3: operadores y comparaciones -----------------------
#   +  -  *  /            calculan
#   ==  !=  >  <  >=  <=  comparan, y siempre responden True o False
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100

print(tests_failed)
print(pass_rate)

# Predice el resultado de cada linea ANTES de quitarle el #:
# print(pass_rate > 85)        # Prediccion: ____
# print(pass_rate >= 85)       # Prediccion: ____
# print(5 + 5)                 # Prediccion: ____
# print("5" + "5")             # Prediccion: ____
# print("5" == 5)              # Prediccion: ____


# --- Ejercicio 4: decisiones ---------------------------------------
# OJO: la linea del if termina con dos puntos, y las lineas de abajo
# empiezan con 4 espacios.
crashes = 3

if crashes == 0:
    print("No issues")
elif crashes <= 2:
    print("Minor")
else:
    print("Critical")

# Antes de cambiar nada, predice:
#   con crashes = 0 sale ____
#   con crashes = 2 sale ____
# Ahora cambia el valor de crashes y comprueba las dos.


# --- Ejercicio 5: encuentra el bug ---------------------------------
# La regla del equipo dice: "La prueba pasa si el juego corre a 30 fps o mas."
# Este codigo no da ningun error... pero el resultado esta mal.
# Encuentra el bug y arreglalo.
fps = 30

if fps > 30:
    print("PASS")
else:
    print("FAIL")


# --- Ejercicio 6: escribelo tu, desde cero -------------------------
# Tienes un valor esperado y un valor real.
expected = 5
actual = 7

# Escribe un if / else:
#   si actual es igual a expected, muestra  PASS
#   si no, muestra  FAIL

if actual == expected:
    print("PASS")
else:
    print("FAIL")
# --- Reto (si te sobra tiempo) -------------------------------------
# a) Haz que el FAIL diga los dos valores:  FAIL: expected 5, got 7
#    Pista: print(f"FAIL: expected {expected}, got {actual}")
#
# b) Escribe otro if / else: si fps es 30 o mas  Y  crashes es 0,
#    muestra  Build OK ; si no, muestra  Build needs review
#    Pista: la palabra  and  exige que se cumplan las dos condiciones.
