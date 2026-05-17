# RESOLUCIÓN DE PROBLEMAS CLÁSICOS EN INTELIGENCIA ARTIFICIAL

## Introducción
En esta sección se analizan problemas clásicos utilizados en Inteligencia Artificial para estudiar el comportamiento de agentes, la toma de decisiones y la representación de estados. Cada problema se aborda desde la perspectiva de un agente racional, considerando su objetivo, conocimiento del entorno, acciones posibles y percepciones.

---

## Problema 1: Monjes y Caníbales

### Descripción
Tres monjes y tres caníbales deben cruzar un río utilizando una embarcación con capacidad máxima de dos personas. La restricción principal es que en ningún lado del río los caníbales pueden superar en número a los monjes, ya que esto pondría en riesgo a los monjes.

### Criterio de éxito
El objetivo se cumple cuando todos los individuos se encuentran en el lado opuesto del río sin haber violado la restricción durante el proceso.

### Conocimiento del agente
El agente dispone de la siguiente información:
* Cantidad de monjes y caníbales.
* Capacidad máxima del bote.
* Posición actual del bote.
* Reglas del problema.
* Distribución de individuos en cada lado.

### Acciones posibles
El agente puede ejecutar las siguientes acciones:
1. Transportar un monje.
2. Transportar dos monjes.
3. Transportar un caníbal.
4. Transportar dos caníbales.
5. Transportar un monje y un caníbal.

### Percepciones del agente
En cada estado, el agente puede observar:
* Número de monjes en cada lado.
* Número de caníbales en cada lado.
* Ubicación del bote.

---

## Problema 2: Maridos y Esposas

### Descripción
Tres parejas deben cruzar un río en un bote con capacidad para dos personas. La condición es que ninguna esposa puede permanecer en compañía de otro hombre si su esposo no se encuentra presente.

### Criterio de éxito
El objetivo se alcanza cuando todas las personas llegan al lado opuesto del río respetando la restricción en todo momento.

### Conocimiento del agente
El agente conoce:
* Número total de personas.
* Relación entre parejas.
* Capacidad del bote.
* Posición del bote.
* Restricción de convivencia.
* Estado actual de cada lado.

### Acciones posibles
El agente puede realizar las siguientes acciones (siempre cumpliendo con las restricciones del problema):
* Transportar una persona.
* Transportar dos personas.

### Percepciones del agente
El agente puede identificar:
* Distribución de personas en cada lado.
* Quiénes están en el bote.
* Posición del bote.

---

## Problema 3: Intercambio de Ranas

### Descripción
Se tienen tres ranas en el lado izquierdo mirando hacia la derecha y tres ranas en el lado derecho mirando hacia la izquierda. El objetivo es intercambiar sus posiciones respetando ciertas reglas de movimiento.

### Criterio de éxito
El problema se resuelve cuando las ranas intercambian completamente sus posiciones iniciales.

### Conocimiento del agente
El agente dispone de la siguiente información:
* Número de ranas y la posición de cada una.
* Ubicación del espacio vacío.
* Reglas de movimiento.
* Estado actual del sistema.

### Acciones posibles
El agente puede realizar:
* Avanzar hacia un espacio vacío.
* Saltar sobre otra rana (solo una).

> **Restricciones críticas:**
> * No se permite retroceder.
> * No se pueden saltar más de una rana a la vez.
> * No se puede ocupar un espacio que ya esté lleno.

### Percepciones del agente
El agente observa:
* Posición de cada rana.
* Ubicación del espacio vacío.
* Dirección de movimiento permitida.

---

## Conclusión
Estos problemas representan ejemplos clásicos de **sistemas basados en estados y reglas**, donde un agente debe tomar decisiones bajo restricciones específicas. Su análisis permite comprender conceptos clave como la representación del entorno, el espacio de estados, las acciones válidas y la importancia de definir correctamente los objetivos y restricciones.

Este tipo de ejercicios fortalece la lógica necesaria para diseñar e implementar algoritmos de búsqueda (como *BFS, DFS, o A**) y resolución de problemas avanzados en Inteligencia Artificial.