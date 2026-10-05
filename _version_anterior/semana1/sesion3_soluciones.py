# SESION 3 - Soluciones (solo para el instructor)

# --- Ejercicio 2 ---------------------------------------------------
asset = "snd_motor_07"

if asset.startswith("tex_"):
    print("Es una textura")
elif asset.startswith("mesh_"):
    print("Es un modelo")
elif asset.startswith("snd_"):
    print("Es un sonido")
else:
    print("Tipo desconocido")


# --- Ejercicio 3: el validador completo ----------------------------
nombre = "Tex_roca 1"
errores = 0

# Regla 1: no puede tener espacios
if " " in nombre:
    print("ERROR: tiene espacios")
    errores = errores + 1

# Regla 2: debe estar todo en minusculas
if nombre != nombre.lower():
    print("ERROR: tiene mayusculas")
    errores = errores + 1

# Regla 3: debe empezar por tex_, mesh_ o snd_
if not (nombre.startswith("tex_") or nombre.startswith("mesh_") or nombre.startswith("snd_")):
    print("ERROR: el tipo no es tex, mesh ni snd")
    errores = errores + 1

# Regla 4: la ultima parte deben ser dos digitos
ultima = nombre.split("_")[-1]
if not (ultima.isdigit() and len(ultima) == 2):
    print("ERROR: la variante no son dos digitos")
    errores = errores + 1

# Resultado final
if errores == 0:
    print(f"OK: {nombre}")
else:
    print(f"{nombre} tiene {errores} error(es)")

# Resultados esperados:
#   tex_roca_01   -> OK
#   tex_Roca_01   -> 1 error  (mayusculas)
#   Tex_roca_01   -> 2 errores (mayusculas y tipo, porque "Tex_" no es "tex_")
#   roca_tex_01   -> 1 error  (tipo)
#   mesh_arbol_3  -> 1 error  (variante)
#   Tex_roca 1    -> 4 errores (espacios, mayusculas, tipo, variante)
