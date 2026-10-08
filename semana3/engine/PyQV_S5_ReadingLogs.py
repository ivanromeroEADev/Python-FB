# PyQV Foundations - Session 5: Reading Logs
# Demo del instructor para FrostEd. SOLO LECTURA: no modifica ningun asset
# ni ningun archivo.
#
# Son los mismos ejercicios que los participantes hacen en VS Code, y al
# final el mismo recorrido sobre un log real.
#
# ANTES DE LA CLASE: escribe en LOG_PATH la ruta completa de un log real que
# se pueda mostrar al grupo. Usa / en lugar de \. Si lo dejas vacio, la
# seccion 5 lo dice y el resto funciona igual.
#
# Nota: FrostEd usa una version de Python anterior a la de VS Code. Por eso
# aqui no hay f-strings y cada print recibe un solo texto.

LOG_PATH = ""

# Los logs reales no siempre escriben los niveles igual. Aqui se buscan sin
# distinguir mayusculas de minusculas.
ERROR_WORD = "error"
WARN_WORD = "warn"

# Cuantas lineas mostrar antes del primer error, para leer hacia arriba.
LINES_BEFORE = 5

SAMPLE_LOG = [
    "[09:14:02] INFO  Job 5120 started",
    "[09:14:03] INFO  Syncing workspace",
    "[09:14:41] WARN  Shader cache is 3 days old, rebuilding",
    "[09:16:10] INFO  Step 'compile_code' started",
    "[09:19:55] INFO  Step 'compile_code' finished",
    "[09:19:56] INFO  Step 'build_assets' started",
    "[09:21:30] ERROR Texture 'props/crate_02' has no source file",
    "[09:21:30] ERROR Asset 'props/crate_02' could not be built",
    "[09:21:31] WARN  Skipping 3 assets that depend on 'props/crate_02'",
    "[09:24:08] ERROR Step 'build_assets' failed with 1 error",
    "[09:24:08] INFO  Step 'package' skipped",
    "[09:24:09] ERROR Job 5120 finished with exit code 1",
]


def title(text):
    print("")
    print("=" * 60)
    print(text)
    print("=" * 60)


def short(line):
    # Recorta una linea muy larga para que quepa en la ventana de salida.
    text = line.strip()
    if len(text) > 160:
        text = text[0:160] + " ..."
    return text


# ------------------------------------------------------------------
title("1. Un log es una lista de textos")

lines = SAMPLE_LOG

print("len(lines)      = " + str(len(lines)))
print("lines[0]        = " + lines[0])
print("lines[11]       = " + lines[11])
print("type(lines[0])  = " + str(type(lines[0])))


# ------------------------------------------------------------------
title("2. Contar por nivel")

errors = 0
warnings = 0

for line in lines:
    if "ERROR" in line:
        errors = errors + 1
    if "WARN" in line:
        warnings = warnings + 1

print("Errors:   " + str(errors))
print("Warnings: " + str(warnings))


# ------------------------------------------------------------------
title("3. El bug: el ultimo error no es la causa")

last_error = ""
for line in lines:
    if "ERROR" in line:
        last_error = line

first_error = ""
for line in lines:
    if "ERROR" in line and first_error == "":
        first_error = line

print("Sin la segunda condicion  ->  " + last_error)
print("   (bug: es el ultimo error, el sintoma mas lejano)")
print("Con  first_error == ''    ->  " + first_error)
print("   (arreglado: es el primer error)")


# ------------------------------------------------------------------
title("4. Una funcion para cualquier lista de lineas")


def first_error_position(lines, error_word):
    # Devuelve la posicion de la primera linea con un error, o -1 si no hay.
    position = 0
    for line in lines:
        if error_word in line.lower():
            return position
        position = position + 1
    return -1


position = first_error_position(SAMPLE_LOG, ERROR_WORD)
print("Primer error del log de ejemplo: posicion " + str(position))
print(SAMPLE_LOG[position])


# ------------------------------------------------------------------
title("5. El mismo recorrido, sobre un log real")

if LOG_PATH == "":
    print("LOG_PATH esta vacio: no se eligio ningun log real.")
    print("Las secciones 1 a 4 no dependen de esto.")
else:
    try:
        log_file = open(LOG_PATH, "r")
        real_lines = log_file.readlines()
        log_file.close()

        errors = 0
        warnings = 0

        for line in real_lines:
            lowered = line.lower()
            if ERROR_WORD in lowered:
                errors = errors + 1
            if WARN_WORD in lowered:
                warnings = warnings + 1

        print("Archivo:  " + LOG_PATH)
        print("Lineas:   " + str(len(real_lines)))
        print("Errors:   " + str(errors))
        print("Warnings: " + str(warnings))
        print("")

        position = first_error_position(real_lines, ERROR_WORD)

        if position == -1:
            print("No hay ninguna linea con '" + ERROR_WORD + "'.")
        else:
            print("Primer error: linea " + str(position + 1) + " de " + str(len(real_lines)))
            print("")

            start = position - LINES_BEFORE
            if start < 0:
                start = 0

            print("Las lineas anteriores, para leer hacia arriba:")
            number = start
            for line in real_lines[start:position]:
                number = number + 1
                print("  " + str(number) + ": " + short(line))

            print("")
            print("El primer error:")
            print("  " + str(position + 1) + ": " + short(real_lines[position]))

    except Exception as error:
        print("No se pudo leer el log.")
        print("Detalle: " + str(error))
        print("Las secciones 1 a 4 no dependen de esto.")

print("")
print("Fin de la demo.")
