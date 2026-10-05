# SESION 2 - Soluciones (solo para el instructor)

# --- Ejercicio 2 ---------------------------------------------------
tipo = "mesh"
nombre = "arbol"
variante = "03"
completo = f"{tipo}_{nombre}_{variante}"
print(completo)                       # mesh_arbol_03

# --- Ejercicio 3 ---------------------------------------------------
# print("tex_roca_" + 1) produce:
#   TypeError: can only concatenate str (not "int") to str
# Explicacion: no se puede sumar un texto con un numero.
# Se arregla convirtiendo el numero a texto, o con una f-string:
print("tex_roca_" + str(1))           # tex_roca_1
print(f"tex_roca_{1:02d}")            # tex_roca_01  (02d = dos digitos)

# --- Ejercicio 4 ---------------------------------------------------
sucio = "Tex Roca 01"
limpio = sucio.lower().replace(" ", "_")
print(limpio)                         # tex_roca_01

# --- Ejercicio 5 ---------------------------------------------------
asset = "snd_motor_07"
partes = asset.split("_")
print(partes[1])                      # motor

# --- Ejercicio 6 ---------------------------------------------------
print(" " in "Tex Roca 01")           # True

# --- Reto ----------------------------------------------------------
# tipo = input("Tipo (tex, mesh, snd): ")
# nombre = input("Nombre: ")
# variante = input("Variante (dos digitos): ")
# print(f"{tipo}_{nombre}_{variante}")
