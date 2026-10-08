# SESSION 6 - Mini-project: validador de resultados de pruebas
#
# Este archivo necesita un archivo mas EN LA MISMA CARPETA:
#     test_results.txt
#
# Para ejecutar, en la terminal (abierta en esa carpeta):
#     python sesion6_ejercicios.py
#
# Hoy se construye UNA herramienta, paso a paso. Cada paso usa algo de una
# sesion anterior. No pases al siguiente hasta que el actual muestre lo
# que dice su  "Debe salir".
#
# LA REGLA:  una prueba PASA si su valor real es MAYOR O IGUAL que su minimo.

print("Session 6 ready")


# --- Paso 1: los datos, y la cuenta a mano (sin codigo) ------------
# Abre test_results.txt en VS Code. Cada linea es una prueba, con tres
# datos separados por comas:
#       nombre,minimo,valor_real
#
# Aplica LA REGLA a mano, linea por linea, y anota:
#   Cuantas lineas hay:   ____
#   Cuantas pruebas PASAN:   ____
#   Cuantas FALLAN:          ____
# Guarda estos numeros. Son tu forma de saber si la herramienta funciona.


# --- Paso 2: de una linea de texto a un diccionario (sesiones 3 y 5) ---
# Leer el archivo: ya lo hiciste en la sesion 5.
results_file = open("test_results.txt")
lines = results_file.readlines()
results_file.close()

print("Lines:", len(lines))


# Esta funcion ya esta escrita. Recibe una linea y devuelve un diccionario.
#   strip  le quita a un texto el salto de linea del final
#   split  corta un texto por las comas y entrega una lista con los pedazos
def parse_line(line):
    parts = line.strip().split(",")
    return {"name": parts[0], "minimum": parts[1], "actual": parts[2]}


# La primera linea del archivo es:   fps_main_menu,30,60
# Prediccion: parse_line(lines[0]) devuelve ____
# print(parse_line(lines[0]))

# Prediccion: type(parse_line(lines[0])["minimum"]) es ____
# print(type(parse_line(lines[0])["minimum"]))


# --- Paso 3: la revision (sesiones 1 y 3) --------------------------
# Escribe una funcion  check(test)  que reciba UN diccionario como los que
# devuelve parse_line, aplique LA REGLA y devuelva "PASS" o "FAIL".



# Cuando la tengas, quita el # de esta linea.  Debe salir:  PASS
# print(check(parse_line(lines[0])))


# --- Paso 4: todas las pruebas, y el resumen (sesion 2) ------------
# Escribe un loop que, por cada linea de  lines :
#   - la convierta en un diccionario con parse_line
#   - la revise con check
#   - muestre el nombre de la prueba y su resultado
#   - cuente cuantas pasan y cuantas fallan
# Despues del loop, muestra el resumen.
#
# Debe salir una linea por prueba, asi:   fps_main_menu PASS
# y al final:                             Passed: __  Failed: __



# --- Paso 5: comprueba tu herramienta ------------------------------
# Compara el resumen de tu herramienta con tu cuenta a mano del paso 1.
#   A mano:           PASS ____   FAIL ____
#   La herramienta:   PASS ____   FAIL ____
#
# Si no coinciden, hay un bug. No da ningun error.
#   Que prueba tiene un resultado distinto al tuyo?   ____
#
# Antes de buscarlo, predice estas dos:
#   Prediccion:  9 >= 30  es ____        "9" >= "30"  es ____
# print(9 >= 30, "9" >= "30")
#
# Pista para el arreglo:  int("30")  convierte el texto "30" en el numero 30.


# --- Paso 6: que la herramienta se revise a si misma (sesion 4) ----
# a) Escribe un assert que afirme que las que pasan mas las que fallan
#    son todas las lineas del archivo.
#
# b) Muestra el porcentaje de exito:   Pass rate: 62.5



# --- Reto (si te sobra tiempo) -------------------------------------
# a) Haz que cada FAIL diga por que:
#       fps_harbor_level FAIL (minimum 30, got 28)
#
# b) Agrega al final de test_results.txt esta linea, guarda y ejecuta:
#       load_time_score,80,n/a
#    Lee el error con el metodo de la sesion 4. En que funcion revienta?
#    Donde esta el origen? Despues borra esa linea del archivo.
#
# c) Convierte todo en una funcion  validate(file_name)  que devuelva un
#    diccionario:   {"passed": 5, "failed": 3}
