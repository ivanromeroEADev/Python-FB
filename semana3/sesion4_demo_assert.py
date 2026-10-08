# SESSION 4 - Demo del instructor: que es un assertion
#
# Un assert es una comprobacion: "esto SIEMPRE debe ser verdad".
# Si no lo es, el programa se detiene y avisa.

player_speed = -1

assert player_speed >= 0, "player_speed must not be negative"

print("Esta linea solo aparece si el assert se cumple")
