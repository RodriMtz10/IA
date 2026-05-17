# ANÁLISIS EXPLORATORIO: DECISIÓN DE SALTO EN UN SISTEMA SIMPLIFICADO

## Introducción
En este ejercicio se analiza un problema sencillo de toma de decisiones basado en datos. El objetivo es comprender cómo ciertas variables influyen en el comportamiento de un sistema, en este caso, la decisión de un personaje (muñeco) de saltar o no ante el lanzamiento de una pelota.

Este tipo de análisis permite identificar patrones y relaciones entre variables, lo cual es fundamental antes de implementar cualquier modelo de aprendizaje automático.

---

## Descripción del problema
Se plantea un escenario donde un objeto (pelota) es lanzado hacia un muñeco, quien debe decidir si realizar un salto o permanecer en su posición.

Cada evento está definido por las siguientes características:
* Altura de la pelota
* Velocidad del lanzamiento
* Acción del muñeco (saltar o no saltar)

---

## Identificación de variables
Dentro del conjunto de datos se distinguen dos tipos de variables bien definidas:

###  Variables de entrada (Features)
* **Altura**
* **Velocidad**

###  Variable de salida (Target)
* **Acción** (decisión final del muñeco)

El propósito central del análisis es determinar cuál de las variables de entrada tiene mayor influencia en la decisión final.

---

## Exploración de los datos
Al examinar estadísticamente el comportamiento del sistema, se identifica un patrón claro relacionado directamente con la **altura** de la pelota:

*  **Cuando la altura es baja:** el muñeco tiende a saltar.
*  **Cuando la altura es alta:** el muñeco no salta.

Por otro lado, la **velocidad** no muestra una relación estadísticamente significativa con la decisión tomada, lo que indica que su impacto en el resultado final es mínimo o irrelevante para este modelo.

---

## Interpretación del análisis
A partir de la exploración realizada, se concluye que la **altura es la variable determinante** en la toma de decisiones. Esto sugiere que el problema real puede simplificarse eliminando variables redundantes, centrándose en una relación directa entre la altura y la acción del muñeco.

Además, las observaciones permiten identificar una separación clara (linealmente clasificable) entre dos grupos:
1. Casos en los que el muñeco debe saltar.
2. Casos en los que el muñeco no debe saltar.

> **Nota de Modelado:** Esta separación tan marcada indica que el problema es fácilmente clasificable, lo cual resulta ideal para algoritmos de clasificación simples (como árboles de decisión o regresión logística).

---

## Conclusión
El análisis exploratorio permite reducir la complejidad del problema al identificar que una sola variable (altura) es suficiente para determinar la acción de manera óptima. Este tipo de hallazgos es clave en el desarrollo de modelos eficientes, ya que evita el uso innecesario de variables que no aportan valor (*feature selection*).

Comprender a fondo la relación entre las variables antes de comenzar a modelar no solo mejora el rendimiento y la interpretabilidad del sistema, sino que también simplifica drásticamente su posterior implementación.