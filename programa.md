# Frostbite Technical Foundations

Programa introductorio de fundamentos técnicos para el equipo de QA/QV.

**Fechas:** martes y jueves, del 6 al 29 de octubre de 2026
**Formato:** 8 sesiones de 45 minutos (6 horas en total)

---

## 1. Objetivo

El programa **no** convierte a los participantes en Frostbite Technical Testers.

Lo que sí hace:

1. Determina objetivamente el nivel actual de cada persona.
2. Introduce fundamentos de programación con Python.
3. Desarrolla pensamiento lógico y técnico.
4. Muestra cómo esos fundamentos aparecen dentro de un engine.
5. Muestra Frostbite desde una perspectiva conceptual y controlada.
6. Deja una ruta de aprendizaje para continuar después.

## 2. Principio pedagógico

```text
Programming Fundamentals
        ↓
      Python
        ↓
  Logical Thinking
        ↓
     Debugging
        ↓
Technical Problem Solving
        ↓
 Understanding Systems
        ↓
   Engine Concepts
        ↓
Frostbite Tools / Workflow
        ↓
 Technical Validation
```

Dominar un nivel no significa dominar el siguiente:

- Saber qué es una variable ≠ saber programar una herramienta.
- Saber Python ≠ saber trabajar con Frostbite.
- Saber ejecutar una herramienta ≠ saber interpretar un assertion.
- Saber reproducir un problema ≠ saber identificar su causa.
- Completar una checklist ≠ comprender técnicamente el workflow.

Este programa cubre los cuatro primeros escalones y muestra los demás.

## 3. Modelo de enseñanza

```text
PARTICIPANTE → VS CODE + PYTHON
INSTRUCTOR   → FROSTBITE / FROSTED (demostración)
CONCEPTO     → LA MISMA IDEA EN LOS DOS ENTORNOS
```

Cada sesión sigue el mismo recorrido:

```text
CONCEPTO
   ↓
EJEMPLO SIMPLE EN PYTHON
   ↓
EJERCICIO DEL PARTICIPANTE EN VS CODE
   ↓
DEMOSTRACIÓN CONCEPTUAL EN FROSTBITE
   ↓
CONEXIÓN CON QA / DEBUGGING
```

Los participantes no manipulan Frostbite durante el programa. Todo el contenido de
los ejercicios es inventado: no se usa código, datos ni logs reales del proyecto.

## 4. Prerrequisitos

**Obligatorios**

- Computador funcional.
- Visual Studio Code instalado.
- Python 3 instalado.
- Poder ejecutar un archivo `.py` (se enseña en la sesión 1).
- Acceso a la carpeta de ejercicios.
- Conocimientos básicos de uso de computador.
- Disposición para participar en los ejercicios.

**No se requiere**

- Experiencia previa en Frostbite ni en game engines.
- Experiencia previa en Python ni en programación.

**Muy recomendados**

- Curiosidad técnica.
- Capacidad para leer instrucciones con atención.
- Disposición para equivocarse y corregir.
- Interés en seguir aprendiendo después del programa.

## 5. Calendario

| # | Fecha | Sesión | Python | Demostración en Frostbite |
|---|---|---|---|---|
| 0 | Mar 6 oct | Assessment | Diagnóstico en vivo y revisión | Ninguna |
| 1 | Jue 8 oct | Thinking Like a Programmer | Variables, tipos, operadores | Una propiedad con nombre, tipo y valor |
| 2 | Mar 13 oct | Decisions and Errors | Condiciones, primer error | Mensajes del engine y un assertion |
| 3 | Jue 15 oct | Repetition | Loops | Muchos objetos, la misma revisión |
| 4 | Mar 20 oct | Reusable Logic | Funciones | Una herramienta como función: entrada y salida |
| 5 | Jue 22 oct | Structured Data | Listas y diccionarios | Un objeto y sus propiedades |
| 6 | Mar 27 oct | Debugging and Logs | Tracebacks, `assert`, causa raíz y síntoma | Un error y un log del engine, guiados |
| 7 | Jue 29 oct | The Full Picture | Repaso y diagnóstico final | Recorrido por el workflow completo |

El material de las sesiones 0, 1 y 2 está en la carpeta `semana1`.

## 6. Diagnóstico

16 preguntas, 20 minutos, en vivo durante la sesión del 6 de octubre, en Pear Deck.
El 29 de octubre se aplica una versión paralela (misma estructura, otros valores),
porque las respuestas de esta se revisan en clase.
Detalle completo en `semana1/diagnostico.md`.

**Plataforma**

| Opción | Acceso corporativo | Código | Exporta | Veredicto |
|---|---|---|---|---|
| Microsoft Forms | Cuenta de la empresa | Como imagen | Excel | **Principal** |
| Plataforma interna de encuestas o formación | Depende | Depende | Depende | **Alternativa**, si existe |
| Google Forms | Cuenta externa | Como imagen | Sheets | Solo si la empresa lo permite |
| Kahoot, Quizizz, Mentimeter | Cuenta externa | Limitado | Limitado | Descartadas: premian velocidad |
| Typeform | Cuenta externa, de pago | Limitado | Sí | Descartada |
| Jupyter / Colab | Cuenta externa | Excelente | Manual | Descartada para el diagnóstico |

**Niveles de resultado**

| Puntaje | Nivel | Significado |
|---|---|---|
| 0 a 4 | Level 0 — No Foundation | Empieza desde conceptos computacionales básicos |
| 5 a 8 | Level 1 — Beginner | Comprende algunos conceptos; necesita práctica significativa |
| 9 a 12 | Level 2 — Foundational | Comprende programación básica y resuelve ejercicios sencillos |
| 13 a 16 | Level 3 — Strong Foundation | Lee código básico, razona sobre problemas y puede empezar conceptos más complejos |

Ningún resultado indica que la persona está preparada para realizar validaciones
independientes de Frostbite. El diagnóstico solo determina el punto de partida.

## 7. Reglas del programa

1. Los participantes trabajan en VS Code; Frostbite solo lo opera el instructor.
2. Un error en pantalla es información, no un fracaso.
3. Se trabaja en parejas y se rota el teclado.
4. Cada sesión termina con algo que funciona.
