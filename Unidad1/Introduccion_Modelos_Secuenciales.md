# INTRODUCCIÓN A REDES RECURRENTES: MODELO VANILLA RNN

## Introducción
Las Redes Neuronales Recurrentes (RNN) son modelos diseñados para procesar información secuencial, permitiendo que los datos anteriores influyan en las decisiones actuales. A diferencia de otros modelos, las RNN incorporan memoria mediante un estado interno que se actualiza en cada paso temporal.

En esta actividad se analiza el comportamiento de una RNN básica (*Vanilla RNN*) utilizando una analogía sencilla basada en estados emocionales.

---

## Concepto general
Una RNN combina dos elementos principales en cada instante de tiempo:
* **Entrada actual ($x_t$):** Información nueva que llega en el momento presente.
* **Estado previo ($h_{t-1}$):** Representación de la información acumulada del pasado.

La actualización del estado se puede expresar de forma simplificada mediante la siguiente ecuación lineal:

$$h_t = x_t + \alpha h_{t-1}$$

Donde $\alpha$ representa el **factor de memoria** (qué tanto del pasado se conserva).

### Comportamiento del modelo
El estado actual no depende únicamente del evento reciente, sino también de la memoria previa. Esto permite que eventos pasados influyan en el resultado, aunque con el tiempo su impacto disminuye. 

Este fenómeno es conocido como **desvanecimiento de la memoria**, ya que la información antigua pierde relevancia progresivamente dentro del sistema.

---

##  Misión 1: Pérdida de información con el tiempo

### Objetivo
Observar cómo un evento significativo pierde impacto a lo largo de los días si no existen estímulos posteriores.

### Parámetros de entrada
* **Día 1:** $x_1 = +10$
* **Día 2 a Día 5:** $x_t = 0$
* **Factor de memoria:** $\alpha = 0.5$

### Desarrollo del cálculo
$$\begin{aligned}
h_1 &= 10 \\
h_2 &= 0 + 0.5(10) = 5 \\
h_3 &= 0 + 0.5(5) = 2.5 \\
h_4 &= 0 + 0.5(2.5) = 1.25 \\
h_5 &= 0 + 0.5(1.25) = 0.625
\end{aligned}$$

### Resultado
El estado final en el quinto día es:
$$h_5 = 0.625$$

>  **Conclusión de la misión:** Esto demuestra empíricamente que el efecto de un estímulo inicial disminuye de manera exponencial con el paso del tiempo.

---

##  Misión 2: Recuperación de un estado negativo

### Objetivo
Determinar la magnitud que debe tener un nuevo evento para revertir una tendencia negativa acumulada en el historial.

### Parámetros de entrada
* **Día 1:** $x_1 = -6$
* **Día 2:** $x_2 = -4$
* **Día 3:** $x_3 = 0$
* **Día 4:** $x_4 = x$ *(valor desconocido a calcular)*
* **Factor de memoria:** $\alpha = 0.5$

### Desarrollo del cálculo
$$\begin{aligned}
h_1 &= -6 \\
h_2 &= -4 + 0.5(-6) = -7 \\
h_3 &= 0 + 0.5(-7) = -3.5 \\
h_4 &= x + 0.5(-3.5) = x - 1.75
\end{aligned}$$

Establecemos la condición de éxito para volver a un estado positivo ($h_4 > 0$):
$$x - 1.75 > 0 \implies x > 1.75$$

### Resultado
Para revertir la tendencia negativa, el evento del Día 4 debe cumplir estrictamente con:
$$x > 1.75$$

---

##  Misión 3: Constancia vs. evento aislado

### Objetivo
Comparar el impacto en el estado final de un evento único de gran magnitud frente a estímulos moderados pero constantes.

### Escenario A (Estímulo aislado)
* **Día 1:** $+10$ | **Días 2 al 5:** $0$
* **Resultado final:**
$$h_5 = 0.625$$

### Escenario B (Estímulo constante)
* **Día 1 al Día 5:** $+3$ constante.
* **Desarrollo matemático:**
$$\begin{aligned}
h_1 &= 3 \\
h_2 &= 3 + 0.5(3) = 4.5 \\
h_3 &= 3 + 0.5(4.5) = 5.25 \\
h_4 &= 3 + 0.5(5.25) = 5.625 \\
h_5 &= 3 + 0.5(5.625) = 5.8125
\end{aligned}$$
* **Resultado final:**
$$h_5 = 5.8125$$

### Interpretación del análisis
El segundo escenario ($B$) produce un resultado significativamente mayor ($5.8125 > 0.625$). Esto demuestra que una estructura de tipo RNN tiende a **favorecer la información reciente y repetida** en lugar de aferrarse a eventos aislados que ocurrieron al inicio de la secuencia.

---

## Conclusión
Las *Vanilla RNN* permiten modelar información en el tiempo con éxito, pero presentan limitaciones arquitectónicas importantes, como la pérdida progresiva de información pasada en secuencias de largo alcance. Esta incapacidad para recordar eventos lejanos es lo que motiva en la práctica el uso de celdas más avanzadas basadas en compuertas, tales como **LSTM** (*Long Short-Term Memory*) o **GRU** (*Gated Recurrent Unit*).

El análisis realizado deja en claro que la constancia y frecuencia en los datos tiene un impacto superior al de los eventos únicos, un factor clave al diseñar y entrenar sistemas secuenciales eficientes.