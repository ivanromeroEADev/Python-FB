# SESION 3 - Condicionales: que el script tome decisiones
#
# Convencion del curso:  <tipo>_<nombre>_<variante>   ejemplo: tex_roca_01
#   tipo:      tex, mesh o snd
#   nombre:    en minusculas, sin espacios
#   variante:  dos digitos
#
# Para ejecutar:  python sesion3_ejercicios.py

# --- Ejercicio 1: if / else ----------------------------------------
# OJO: las lineas debajo de if y else van con 4 espacios al inicio.
tam = 4096

if tam > 2048:
    print("Textura muy grande")
else:
    print("Tamano correcto")

# Cambia tam a 1024 y ejecuta de nuevo. Que cambio?


# --- Ejercicio 2: varias opciones con elif -------------------------
asset = "mesh_arbol_03"

if asset.startswith("tex_"):
    print("Es una textura")
elif asset.startswith("mesh_"):
    print("Es un modelo")
else:
    print("Tipo desconocido")

# Agrega un elif para que los nombres que empiezan por snd_ digan "Es un sonido".
# Pruebalo cambiando asset a "snd_motor_07".


# --- Ejercicio 3: el validador -------------------------------------
# Este script revisa UN nombre contra la convencion.
# La regla 1 ya esta hecha. Completa las reglas 2, 3 y 4.

nombre = "Tex_roca 1"
errores = 0

# Regla 1: no puede tener espacios
if " " in nombre:
    print("ERROR: tiene espacios")
    errores = errores + 1

# Regla 2: debe estar todo en minusculas
# Pista: un nombre esta en minusculas si es igual a nombre.lower()


# Regla 3: debe empezar por tex_, mesh_ o snd_
# Pista: usa  not  y  or  ->  if not (condicion_a or condicion_b or condicion_c):


# Regla 4: la ultima parte deben ser dos digitos
# Pista: ultima = nombre.split("_")[-1]
#        ultima.isdigit() dice si son solo numeros; len(ultima) dice cuantos son


# Resultado final
if errores == 0:
    print(f"OK: {nombre}")
else:
    print(f"{nombre} tiene {errores} error(es)")


# Prueba tu validador cambiando nombre por cada uno de estos:
#   tex_roca_01        -> debe salir OK
#   tex_Roca_01        -> 1 error (mayusculas)
#   roca_tex_01        -> 1 error (tipo)
#   mesh_arbol_3       -> 1 error (variante)
#   Tex_roca 1         -> 4 errores


# --- Reto (si te sobra tiempo) -------------------------------------
# Cambia la linea  nombre = "Tex_roca 1"  por:
#     nombre = input("Nombre del asset: ")
# y prueba con 5 nombres reales que hayas visto en el editor.
