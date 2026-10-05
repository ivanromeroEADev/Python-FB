# SESION 2 - Tipos y texto
#
# Convencion del curso:  <tipo>_<nombre>_<variante>   ejemplo: tex_roca_01
#
# Para ejecutar:  python sesion2_ejercicios.py

# --- Ejercicio 1: tipos --------------------------------------------
# type() dice de que tipo es un valor. Ejecuta y lee el resultado.
print(type("tex_roca_01"))
print(type(512))
print(type(0.5))
print(type(True))


# --- Ejercicio 2: unir texto ---------------------------------------
tipo = "tex"
nombre = "roca"
variante = "01"

# Una f-string permite meter variables dentro de un texto usando llaves.
completo = f"{tipo}_{nombre}_{variante}"
print(completo)

# Cambia las tres variables para que salga:  mesh_arbol_03


# --- Ejercicio 3: un error a proposito -----------------------------
# Quita el # de la linea de abajo, ejecuta y LEE el mensaje de error.
# Despues vuelve a poner el #.
# print("tex_roca_" + 1)


# --- Ejercicio 4: limpiar un nombre --------------------------------
sucio = "Tex Roca 01"

# .lower() pasa a minusculas.  .replace(a, b) cambia a por b.
print(sucio.lower())
print(sucio.replace(" ", "_"))

# Escribe una linea que deje el nombre limpio del todo:  tex_roca_01
# Pista: se pueden encadenar ->  sucio.lower().replace(...)
limpio = sucio
print(limpio)


# --- Ejercicio 5: partir un nombre ---------------------------------
asset = "snd_motor_07"
partes = asset.split("_")
print(partes)
print(partes[0])     # la primera parte (se cuenta desde 0)
print(partes[-1])    # la ultima parte

# Muestra con print() solo la parte del medio ("motor").


# --- Ejercicio 6: preguntas con respuesta Si/No --------------------
# Estas instrucciones responden True (verdadero) o False (falso).
print(asset.startswith("snd_"))
print(asset.startswith("tex_"))
print(" " in asset)
print(len(asset))

# Escribe una linea que responda: el nombre "Tex Roca 01" tiene espacios?


# --- Reto (si te sobra tiempo) -------------------------------------
# input() le pide un dato a la persona que ejecuta el script.
# Quita los # y completa para construir un nombre con lo que escriban.
# tipo = input("Tipo (tex, mesh, snd): ")
# nombre = input("Nombre: ")
# variante = input("Variante (dos digitos): ")
# print(...)
