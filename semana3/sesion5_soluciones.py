# SESSION 5 - Soluciones (solo para el instructor)
#
# Necesita build_5120.log y nightly_5121.log en la misma carpeta.

# --- Ejercicio 1 ---------------------------------------------------
#   Lineas del log:   12
#   Lineas ERROR:     4
#   Causa raiz:       09:21:30  Texture 'props/crate_02' has no source file
#                     (el PRIMER error; todo lo demas viene de ahi)
#   Sintomas:         09:21:30  Asset 'props/crate_02' could not be built
#                     09:24:08  Step 'build_assets' failed with 1 error
#                     09:24:09  Job 5120 finished with exit code 1
#                     El WARN de 09:21:31 (Skipping 3 assets) tambien es una
#                     consecuencia, aunque no diga ERROR.
#   Ruido:            09:14:41  Shader cache is 3 days old, rebuilding
#                     Ocurrio siete minutos antes y no detuvo nada.

# --- Ejercicio 2 ---------------------------------------------------
log_file = open("build_5120.log")
lines = log_file.readlines()
log_file.close()

print(len(lines))            # 12
print(lines[0])              # [09:14:02] INFO  Job 5120 started
#                              (sale una linea en blanco debajo: cada linea
#                              del archivo trae su salto de linea al final)
print(lines[11])             # [09:24:09] ERROR Job 5120 finished with exit code 1
#                              12 lineas: posiciones 0 a 11. lines[12] da IndexError.
print(type(lines[0]))        # <class 'str'>  Todo lo que se lee de un archivo
#                              es texto, incluida la hora.

# --- Ejercicio 3 ---------------------------------------------------
errors = 0
warnings = 0

for line in lines:
    if "ERROR" in line:
        errors = errors + 1
    if "WARN" in line:
        warnings = warnings + 1

print("Errors:", errors)         # Errors: 4
print("Warnings:", warnings)     # Warnings: 2

# --- Ejercicio 4 ---------------------------------------------------
# El bug: first_error se sobrescribe en CADA linea ERROR, asi que al final
# guarda el ultimo error, no el primero. Muestra el sintoma mas lejano:
#   Root cause: [09:24:09] ERROR Job 5120 finished with exit code 1
# Arreglo: guardar solo si todavia no se ha guardado ninguno.
first_error = ""

for line in lines:
    if "ERROR" in line and first_error == "":
        first_error = line

print("Root cause:", first_error)
# Root cause: [09:21:30] ERROR Texture 'props/crate_02' has no source file

# --- Ejercicio 5 ---------------------------------------------------
def first_error_in(file_name):
    log_file = open(file_name)
    lines = log_file.readlines()
    log_file.close()

    first_error = ""

    for line in lines:
        if "ERROR" in line and first_error == "":
            first_error = line

    return first_error


print(first_error_in("build_5120.log"))
# [09:21:30] ERROR Texture 'props/crate_02' has no source file
print(first_error_in("nightly_5121.log"))
# [02:41:50] ERROR Could not write 'levels/harbor_03.cache': not enough space on disk

# La pregunta final. En nightly_5121.log la funcion encuentra bien el primer
# ERROR, pero la explicacion esta 38 minutos antes, y es un WARN:
#   [02:03:15] WARN  Disk space low on D: (1.2 GB free)
# La herramienta senala donde empezar a leer. Decidir cual es la causa
# sigue siendo trabajo de una persona.

# --- Reto a --------------------------------------------------------
# open("build_9999.log")
# FileNotFoundError: [Errno 2] No such file or directory: 'build_9999.log'

# --- Reto b --------------------------------------------------------
first_error = first_error_in("build_5120.log")
print(first_error[1:9])          # 09:21:30

# --- Reto c --------------------------------------------------------
counts = {"INFO": 0, "WARN": 0, "ERROR": 0}

for line in lines:
    for level in counts:
        if level in line:
            counts[level] = counts[level] + 1

print(counts)                    # {'INFO': 6, 'WARN': 2, 'ERROR': 4}
