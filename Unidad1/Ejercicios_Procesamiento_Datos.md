# ANÁLISIS DE SECUENCIAS: FUNDAMENTOS DE UNA RNN BÁSICA

## Introducción
En esta actividad se estudia el funcionamiento interno de una Red Neuronal Recurrente (RNN) desde una perspectiva conceptual y matemática. A través de analogías y ejercicios, se busca comprender cómo fluye la información en el tiempo, cómo se combinan los datos actuales con los pasados y cuáles son los retos asociados al entrenamiento de este tipo de modelos.

---

## 1. Interpretación conceptual del modelo
Se presenta una analogía en forma de texto que describe los elementos principales de una celda recurrente. Cada fragmento representa un componente matemático dentro de la ecuación de una RNN.

### Actividad 2.1: Identificación de componentes
Dada la ecuación de una RNN básica:

$$h_t = \tanh(W_{hx} x_t + W_{hh} h_{t-1} + b)$$

Se identifican los elementos principales:
* **Entrada actual ($x_t$):** Representa la información nueva en el tiempo actual.
* **Estado anterior ($h_{t-1}$):** Contiene el contexto acumulado de pasos anteriores.
* **Matrices de pesos ($W_{hx}, W_{hh}$):** Transforman la información de entrada y del estado previo.
* **Sesgo ($b$):** Ajusta el resultado de la combinación lineal.
* **Función de activación ($\tanh$):** Limita los valores dentro de un rango controlado.
* **Estado actual ($h_t$):** Resultado final que se utilizará en el siguiente paso temporal.

---

### Actividad 2.2: Análisis de dimensiones
Se define lo siguiente:
* **Vector de entrada:** dimensión 20 $\rightarrow x_t \in \mathbb{R}^{20 \times 1}$
* **Estado oculto:** dimensión 64 $\rightarrow h_t \in \mathbb{R}^{64 \times 1}$

#### Dimensiones de las matrices
* **$W_{hx}$:** transforma de 20 a 64 $\rightarrow W_{hx} \in \mathbb{R}^{64 \times 20}$
* **$W_{hh}$:** transforma de 64 a 64 $\rightarrow W_{hh} \in \mathbb{R}^{64 \times 64}$

#### Justificación matemática
$$\begin{aligned}
(W_{hx} \cdot x_t) & \rightarrow (64 \times 20) \times (20 \times 1) = (64 \times 1) \\
(W_{hh} \cdot h_{t-1}) & \rightarrow (64 \times 64) \times (64 \times 1) = (64 \times 1)
\end{aligned}$$

#### Resultado final
$$h_t \in \mathbb{R}^{64 \times 1}$$

---

### Actividad 2.3: Interpretación del sesgo
El sesgo permite desplazar la salida de la función de activación, evitando que el modelo esté limitado a pasar por el origen.

> **Descripción:** > El sesgo actúa como un ajuste fino dentro del modelo, permitiendo modificar la salida incluso cuando las entradas son cercanas a cero. Esto mejora la flexibilidad del sistema y facilita el aprendizaje de patrones más complejos.

---

### Actividad 2.4: Saturación de la función de activación
Se analiza la función y su derivada:
* $f(z) = \tanh(z)$
* $f'(z) = 1 - \tanh^2(z)$

Si el valor de entrada es muy grande, por ejemplo, $z = 500$:
* $\tanh(500) \approx 1$
* $f'(500) \approx 0$

#### Consecuencia
Cuando la derivada se aproxima a cero:
1. El gradiente desaparece.
2. Los pesos dejan de actualizarse.
3. El modelo pierde capacidad de aprendizaje en secuencias largas.

> ⚠️ **Nota:** Este fenómeno se conoce como *desvanecimiento del gradiente* (Vanishing Gradient).

---

### Actividad 2.5: Propagación del error
Durante el entrenamiento, el error se propaga hacia atrás en el tiempo para ajustar los parámetros del modelo (BPTT - Backpropagation Through Time).

#### Flujo del error
El error atraviesa:
* La función de activación (mediante su derivada)
* Las matrices de pesos
* Los estados ocultos anteriores

#### Representación matemática
$$\frac{\partial L}{\partial h_{t-1}} = \frac{\partial L}{\partial h_t} \cdot \frac{\partial h_t}{\partial h_{t-1}}$$

*Este proceso se basa en la **regla de la cadena**, fundamental en cálculo diferencial.*

---

### Actividad 2.6: Corrección de implementación
Se presenta un fragmento de código con un error conceptual en el uso de operadores:

#### Código Erróneo
```python
def paso_rnn_erroneo(x_t, h_prev, W_hx, W_hh, b):
    # ERROR: Uso de '*' para multiplicación matricial
    combinacion = (W_hx * x_t) + (W_hh * h_prev) + b
    return np.tanh(combinacion)
```

Error identificado
El operador * en NumPy realiza una multiplicación elemento a elemento (Hadamard product), lo cual no corresponde a la multiplicación matricial requerida en este contexto algebraico.

Corrección
El operador @ permite realizar correctamente el producto matricial (dot product).

```Python
def paso_rnn_correcto(x_t, h_prev, W_hx, W_hh, b):
    # CORRECCIÓN: Uso de '@' para el producto de matrices
    combinacion = (W_hx @ x_t) + (W_hh @ h_prev) + b
    return np.tanh(combinacion)
```

## Conclusión
Las Redes Neuronales Recurrentes permiten modelar información secuencial al combinar datos actuales con información pasada. Sin embargo, presentan desafíos importantes como la saturación de funciones de activación y la dificultad en la propagación del gradiente a lo largo del tiempo.

Comprender tanto su estructura matemática como su implementación a nivel de código es fundamental para evitar errores y mejorar su desempeño en aplicaciones reales.