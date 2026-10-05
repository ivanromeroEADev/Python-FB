# Curso: Python desde cero aplicado a Frostbite

**Fechas:** lunes 5 al viernes 30 de octubre de 2026
**Formato:** 3 sesiones por semana (lunes, miércoles, viernes), 45 minutos cada una
**Total:** 12 sesiones, 9 horas de clase

## Objetivo realista para 9 horas

Al terminar, cada persona habrá escrito y ejecutado scripts propios, sabrá leer un
script simple y un mensaje de error, y habrá visto dónde encaja eso en el trabajo
real del motor. No salen listos para hacer pipeline, build ni arreglo de jobs por
su cuenta; salen sabiendo qué es ese trabajo y cuál es el camino para llegar.

## Calendario

| # | Fecha | Tema de Python | Práctica | Contacto con Frostbite |
|---|---|---|---|---|
| 1 | Lun 5 oct | Qué es un script, `print`, variables | Primeros 5 comandos | Observar: nombres de assets en el editor |
| 2 | Mié 7 oct | Tipos y texto (strings) | Construir y limpiar nombres de assets | Comparar con la convención real |
| 3 | Vie 9 oct | Condicionales (`if`) | Validador de un nombre | Probar 5 nombres reales |
| 4 | Lun 12 oct* | Listas y bucles (`for`) | Validar una lista completa | Observar: cuántos assets tiene una carpeta |
| 5 | Mié 14 oct | Diccionarios | Un asset con sus propiedades | Observar: propiedades de un asset en el editor |
| 6 | Vie 16 oct | Funciones | Mini-proyecto: validador reutilizable | Demo de las parejas |
| 7 | Lun 19 oct | Archivos, rutas y JSON | Escanear una carpeta y escribir un reporte | Leer datos exportados de prueba |
| 8 | Mié 21 oct | Errores y tracebacks | Romper scripts a propósito | Leer un error real, guiado |
| 9 | Vie 23 oct | Leer logs | Causa raíz vs. síntoma | Log de un job fallido, guiado |
| 10 | Lun 26 oct | Primer script en el editor | Solo lectura: listar assets | Ejecutar en sandbox |
| 11 | Mié 28 oct | Modificar en lote | Cambiar una propiedad en assets de prueba | Modificar en sandbox |
| 12 | Vie 30 oct | Cierre | Demos, repetir diagnóstico | Mapa de lo que sigue |

\* El lunes 12 de octubre es festivo en varios países. Si aplica, la sesión 4 pasa
al martes 13.

Si una semana solo hay 2 sesiones, se fusionan así: 4+5, 8+9 o 10+11 (en ese orden
de preferencia). Las sesiones 1, 2, 3, 6 y 12 no se recortan.

## Reglas del curso (decirlas el día 1)

1. Nadie toca producción. Todo lo que se modifica es de prueba.
2. Un error en pantalla no es un fracaso, es información.
3. Se trabaja en parejas y se rota quién escribe.
4. Cada sesión termina con algo que funciona.

## Antes del lunes 5

- [ ] Enviar el diagnóstico (`semana1/diagnostico.md`) para que lo respondan antes de la sesión 1
- [ ] Confirmar que cada máquina tiene Python 3 (`python --version` en una terminal)
- [ ] Confirmar un editor: VS Code, o IDLE que ya viene con Python
- [ ] Compartir la carpeta `semana1` con los archivos de ejercicios (sin las soluciones)
- [ ] Probar tú la demo: `python sesion1_demo_validador.py`
- [ ] Sustituir, si quieres, la convención de nombres inventada por la real del proyecto
