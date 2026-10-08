# SESSION 5 - Reading Logs: causa raiz y sintoma
#
# Este archivo necesita dos archivos mas EN LA MISMA CARPETA:
#     build_5120.log     nightly_5121.log
#
# Para ejecutar, en la terminal (abierta en esa carpeta):
#     python sesion5_ejercicios.py
#
# REGLA: antes de ejecutar, predice. Escribe tu prediccion donde
# veas ____ y solo despues quita el # del print para comprobar.

print("Session 5 ready")


# --- Ejercicio 1: leer un log a ojo (sin codigo) -------------------
# Abre build_5120.log en VS Code (panel izquierdo) y leelo completo.
# Cada linea tiene tres partes:   [hora]  NIVEL  mensaje
# Los niveles son:  INFO (informa)   WARN (advierte)   ERROR (algo fallo)
#
# Responde aqui, contando a mano:
#   Cuantas lineas tiene el log:     ____
#   Cuantas son ERROR:               ____
#   Cual es la CAUSA RAIZ (hora):    ____
#   Cuales son SINTOMAS (horas):     ____
#   Hay algun WARN que sea RUIDO (no tiene que ver con el fallo)?  ____


# --- Ejercicio 2: abrir el archivo con Python ----------------------
# open abre el archivo, readlines lo lee y entrega una LISTA: un
# elemento por cada linea. close lo cierra.
log_file = open("build_5120.log")
lines = log_file.readlines()
log_file.close()

# Prediccion: len(lines) vale ____
# print(len(lines))

# Prediccion: lines[0] es la linea que dice ____
# print(lines[0])

# Prediccion: la ULTIMA linea esta en la posicion ____
# print(lines[____])

# Prediccion: type(lines[0]) es ____     (str, int, float, bool o list?)
# print(type(lines[0]))


# --- Ejercicio 3: contar por nivel ---------------------------------
# La palabra  in  pregunta si un texto esta dentro de otro, y responde
# True o False:    "ERROR" in "[09:21:30] ERROR Texture..."   ->  True
errors = 0

for line in lines:
    if "ERROR" in line:
        errors = errors + 1

# Prediccion: errors vale ____   (es lo que contaste a mano en el ejercicio 1?)
# print("Errors:", errors)

# Ahora tu: cuenta tambien los WARN, en una variable  warnings , y muestra:
#   Warnings: 2



# --- Ejercicio 4: encuentra el bug ---------------------------------
# Este codigo deberia mostrar la CAUSA RAIZ del fallo: el primer ERROR.
# No da ningun error... pero lo que muestra no es la causa.
# Encuentra el bug y arreglalo.
first_error = ""

for line in lines:
    if "ERROR" in line:
        first_error = line

print("Root cause:", first_error)


# --- Ejercicio 5: una funcion para cualquier log -------------------
# Convierte lo anterior en una funcion que sirva para cualquier archivo.
# Escribe  first_error_in(file_name)  que:
#   - abra y lea el archivo cuyo nombre recibe
#   - busque el PRIMER error (con tu arreglo del ejercicio 4)
#   - lo devuelva con return
# Casi todo el codigo ya lo tienes en los ejercicios 2 y 4.



# Cuando la tengas, quita el # de estas dos lineas:
# print(first_error_in("build_5120.log"))
# print(first_error_in("nightly_5121.log"))

# Ultima pregunta, y esta es para ti, no para Python.
# Abre nightly_5121.log y leelo completo.
#   Lo que encontro tu funcion, es la causa raiz?  ____
#   Que linea explica POR QUE ocurrio ese error?   ____


# --- Reto (si te sobra tiempo) -------------------------------------
# a) Cambia el nombre del archivo del ejercicio 2 por uno que no exista,
#    por ejemplo "build_9999.log". Predice el tipo de error, ejecuta y
#    leelo con el metodo de la sesion 4. Despues dejalo como estaba.
#
# b) Muestra solo la hora de la causa raiz:  09:21:30
#    Pista: un texto tambien tiene posiciones.  first_error[1:9]  entrega
#    los caracteres desde la posicion 1 hasta la 8.
#
# c) Cuenta los tres niveles en un diccionario y muestralo:
#       {'INFO': 6, 'WARN': 2, 'ERROR': 4}
#    Pista: empieza con  counts = {"INFO": 0, "WARN": 0, "ERROR": 0}
#    y recorre las claves con  for level in counts:
