# SESSION 1 - Programming Foundations: Thinking Like a Programmer
#
# Las lineas que empiezan con # son comentarios. Python las ignora.
#
# Para ejecutar este archivo, en la terminal:
#     python sesion1_ejercicios.py

# --- Ejercicio 1: print --------------------------------------------
# print() muestra algo en pantalla.
print("Hello, QA team")

# Cambia el texto por tu nombre, guarda (Ctrl+S) y ejecuta de nuevo.


# --- Ejercicio 2: variables ----------------------------------------
# Una variable es un nombre que guarda un valor.
player_name = "Alex"
player_speed = 5
player_health = 87.5
is_alive = True

print(player_name)
print(player_speed)
print(player_health)
print(is_alive)

# Cambia player_speed a 9 y ejecuta de nuevo.


# --- Ejercicio 3: tipos de datos -----------------------------------
# type() dice de que tipo es el valor guardado.
print(type(player_name))
print(type(player_speed))
print(type(player_health))
print(type(is_alive))


# --- Ejercicio 4: operadores para calcular -------------------------
#   +  sumar     -  restar     *  multiplicar     /  dividir
tests_total = 40
tests_passed = 34

tests_failed = tests_total - tests_passed
pass_rate = tests_passed / tests_total * 100

print(tests_failed)
print(pass_rate)

# Cambia tests_passed a 38. Antes de ejecutar: cuanto va a dar tests_failed?


# --- Ejercicio 5: operadores para comparar -------------------------
#   ==  igual     !=  distinto     >  mayor     <  menor
#   >=  mayor o igual     <=  menor o igual
# Una comparacion siempre responde True o False.
expected_speed = 5

print(player_speed == expected_speed)
print(pass_rate >= 90)
print(player_health > 100)


# --- Ejercicio 6: predice el resultado -----------------------------
# Sin ejecutar: que valor tiene score al final? Diselo a tu pareja.
# Despues quita el # de la ultima linea y comprueba.
score = 10
score = score + 5
score = score * 2
# print(score)


# --- Ejercicio 7: ahora tu -----------------------------------------
# Crea dos variables: bugs_found con el valor 12 y bugs_fixed con el valor 7.
# Crea una tercera, bugs_open, que sea la resta de las dos.
# Muestra bugs_open con print().

