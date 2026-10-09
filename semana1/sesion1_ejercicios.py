# Sesion 1: seguir el valor paso a paso
#
# Las lineas que empiezan con # son comentarios. Python no las ejecuta.
#
# Para ejecutar este archivo, escribe esto en la terminal:
#     python sesion1_ejercicios.py
#
# Antes de ejecutar cada ejercicio, intenta predecir el resultado.
# Anota tu respuesta donde veas ____ y luego quita el # de print para comprobar.

# Saludo inicial
# print() muestra algo en pantalla.
print("Hello, QV team")


# Ejercicio 1: variables y tipos
# Una variable es un nombre que guarda un valor. Cada valor tiene un tipo.
player_name = "German"      # str: texto, escrito entre comillas
player_speed = 5          # int: numero entero
player_health = 87.5      # float: numero con decimales
is_alive = True           # bool: verdadero o falso

print("\nEjercicio 1: variables y tipos")
print(player_name)
print(player_speed)
print(player_health)
print(is_alive)

# type() muestra el tipo de dato de cada valor.
print(type(player_name))
print(type(player_speed))
print(type(player_health))
print(type(is_alive))


# Ejercicio 2: sigue el valor
# El signo = guarda un valor en una variable; no significa "es igual a".

# 2a
score = 10
score = score + 5
score = score * 2
# Antes de comprobar, anota cuanto vale score: ____
print("\nEjercicio 2a: seguir el valor de score")
print(score)

# 2b
a = 3
b = a      
a = a + 4
b = b * 2
# Antes de comprobar, anota cuanto valen a y b: ____ y ____
print("\nEjercicio 2b: seguir el valor de a y b")
print(a, b)


# Ejercicio 3: operadores y comparaciones
# +, -, * y / hacen calculos.
# ==, !=, >, <, >= y <= comparan valores y dan True o False.
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100

print("\nEjercicio 3: operadores y comparaciones")
print(tests_failed)
print(pass_rate)

# Predice el resultado de cada linea antes de quitarle el #:
# print(pass_rate > 85)        # Tu respuesta: ____
# print(pass_rate >= 85)       # Tu respuesta: ____
# print(5 + 5)                 # Tu respuesta: ____
# print("5" + "5")             # Tu respuesta: ____
# print("5" == 5)              # Tu respuesta: ____


# Ejercicio 4: tomar decisiones
# La linea del if termina con dos puntos. Las instrucciones dentro del bloque
# llevan cuatro espacios al inicio.
crashes = 3

print("\nEjercicio 4: tomar decisiones")
if crashes == 0:
    print("No issues")
elif crashes <= 2:
    print("Minor")
else:
    print("Critical")

# Antes de cambiar crashes, predice que mensaje saldra:
#   Si crashes vale 0: ____
#   Si crashes vale 2: ____
# Luego cambia el valor y comprueba tus respuestas.


# Ejercicio 5: encuentra el error
# La regla del equipo dice: "La prueba pasa si el juego corre a 30 fps o mas."
# El codigo no muestra un error, pero el resultado no sigue esa regla.
# Revisa la condicion y corrige lo que haga falta.
fps = 30

print("\nEjercicio 5: encuentra el error")
if fps > 30:
    print("PASS")
else:
    print("FAIL")


# Ejercicio 6: escribe tu propio if / else
# Compara el valor esperado con el valor real.
expected = 5
actual = 7

# Si actual es igual a expected, muestra PASS.
# Si son distintos, muestra FAIL.

print("\nEjercicio 6: comparar valores")
# Escribe tu respuesta en el if / else de abajo. Antes de ejecutar, predice que mensaje saldra:


# Reto, si te queda tiempo
# a) Muestra ambos valores en el mensaje de error.
#    Pista: print(f"FAIL: expected {expected}, got {actual}")
#
# b) Escribe otro if / else. Si fps es 30 o mas y crashes es 0, muestra
#    "Build OK"; de lo contrario, muestra "Build needs review".
#    Pista: and permite comprobar que se cumplan las dos condiciones.
