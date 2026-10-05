# Demo de la sesion 1 (la ejecuta el instructor, no los alumnos).
# Genera 200 nombres de assets inventados, algunos con errores,
# y los valida todos en menos de un segundo.
#
# Convencion inventada para el curso:  <tipo>_<nombre>_<variante>
#   tipo:      tex, mesh o snd
#   nombre:    en minusculas, sin espacios
#   variante:  dos digitos (01, 02, ...)
# Ejemplo valido: tex_roca_01

import random
import time

TIPOS = ["tex", "mesh", "snd"]
NOMBRES = ["roca", "arbol", "puerta", "muro", "rio", "nube", "motor", "paso"]


def generar_nombre():
    tipo = random.choice(TIPOS)
    nombre = random.choice(NOMBRES)
    variante = random.randint(1, 20)
    correcto = f"{tipo}_{nombre}_{variante:02d}"

    # 1 de cada 5 nombres sale con un error tipico
    error = random.randint(1, 20)
    if error == 1:
        return correcto.upper()
    if error == 2:
        return correcto.replace("_", " ", 1)
    if error == 3:
        return f"{nombre}_{tipo}_{variante:02d}"
    if error == 4:
        return f"{tipo}_{nombre}_{variante}x"
    return correcto


def revisar(nombre):
    problemas = []
    if " " in nombre:
        problemas.append("tiene espacios")
    if nombre != nombre.lower():
        problemas.append("tiene mayusculas")
    partes = nombre.split("_")
    if partes[0].lower() not in TIPOS:
        problemas.append("el tipo no es tex, mesh ni snd")
    if not (partes[-1].isdigit() and len(partes[-1]) == 2):
        problemas.append("la variante no son dos digitos")
    return problemas


random.seed(2026)
nombres = [generar_nombre() for _ in range(200)]

inicio = time.perf_counter()
con_problemas = 0
for nombre in nombres:
    problemas = revisar(nombre)
    if problemas:
        con_problemas += 1
        print(f"ERROR  {nombre:<22} {', '.join(problemas)}")
duracion = time.perf_counter() - inicio

print()
print(f"Revisados:      {len(nombres)}")
print(f"Con problemas:  {con_problemas}")
print(f"Tiempo:         {duracion:.4f} segundos")
