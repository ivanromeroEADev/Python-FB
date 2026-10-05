# SESSION 2 - Decisions and Errors
#
# Para ejecutar este archivo, en la terminal:
#     python sesion2_ejercicios.py

# --- Ejercicio 1: if / else ----------------------------------------
# OJO: las lineas debajo de if y de else empiezan con 4 espacios.
fps = 28

if fps >= 30:
    print("PASS")
else:
    print("FAIL")

# Cambia fps a 60 y ejecuta de nuevo. Que cambio?


# --- Ejercicio 2: varias opciones con elif -------------------------
crashes = 3

if crashes == 0:
    print("No issues")
elif crashes <= 2:
    print("Minor")
else:
    print("Critical")

# Prueba con crashes = 0 y con crashes = 2. Sale lo que esperabas?


# --- Ejercicio 3: un error a proposito -----------------------------
# Quita el # de la linea de abajo, ejecuta y LEE el mensaje.
# Despues vuelve a poner el #.
# print("Crashes: " + crashes)


# --- Ejercicio 4: test checker -------------------------------------
# Compara el valor esperado con el valor real.
test_name = "Player speed"
expected = 5
actual = 7

# Escribe un if / else:
#   si actual es igual a expected, muestra  PASS
#   si no, muestra  FAIL



# Comprueba: con actual = 7 debe salir FAIL; con actual = 5 debe salir PASS.


# --- Ejercicio 5: dos condiciones a la vez -------------------------
#   and  -> se deben cumplir las dos
#   or   -> basta con que se cumpla una
# Escribe un if / else:
#   si fps es mayor o igual a 30  Y  crashes es igual a 0, muestra  Build OK
#   si no, muestra  Build needs review



# Prueba cambiando fps y crashes arriba hasta que salga Build OK.


# --- Reto (si te sobra tiempo) -------------------------------------
# Mejora el ejercicio 4 para que el mensaje diga los dos valores, por ejemplo:
#   FAIL: Player speed - expected 5, got 7
# Pista: print(f"FAIL: {test_name} - expected {expected}, got {actual}")
