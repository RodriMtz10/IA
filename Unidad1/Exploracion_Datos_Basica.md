# ANÁLISIS EXPLORATORIO DE DATOS PARA RECONOCIMIENTO DE DÍGITOS (1, 2, 3)

## Introducción
El análisis exploratorio de datos (EDA) es una etapa fundamental en el desarrollo de modelos de reconocimiento de imágenes. En este caso, se enfoca en comprender las características de un conjunto de datos diseñado para identificar los dígitos 1, 2 y 3 bajo distintas condiciones visuales.

Este análisis permite evaluar la calidad, diversidad y distribución de los datos antes de entrenar un modelo de aprendizaje automático.

---

## Objetivo del análisis
El objetivo principal es examinar un conjunto de imágenes que serán utilizadas para entrenar un modelo capaz de reconocer los números 1, 2 y 3 en diferentes contextos.

El sistema debe ser capaz de identificar correctamente los dígitos en situaciones de variabilidad real como:
* Escritura manual
* Texto impreso
* Fotografías
* Pantallas digitales
* Variaciones en el fondo
* Diferentes tamaños
* Cambios de iluminación
* Distintas orientaciones

---

## Estructura del dataset
El conjunto de datos se organiza en carpetas en el sistema de archivos, donde cada directorio representa una clase específica:

```text
Dataset/
 ├── Clase_1/   # Contiene imágenes del dígito 1
 ├── Clase_2/   # Contiene imágenes del dígito 2
 └── Clase_3/   # Contiene imágenes del dígito 3
 ```

Dentro de cada carpeta se almacenan los archivos de imagen correspondientes al número asignado.

## Características del dataset
Para que el modelo tenga un buen desempeño, es necesario que el dataset incluya una amplia variedad de ejemplos. Algunas características analizadas e indispensables son:

Diferentes estilos de escritura.

Números escritos a mano alzada.

Variaciones de escala y tamaño.

Diversidad de canales de colores (RGB, escala de grises).

Imágenes rotadas o con inclinación.

Fondos variados (texturas, ruido visual).

## Representaciones visuales distintas del mismo número.

💡 Principio clave: Esta diversidad permite que el modelo generalice mejor y sea más robusto ante datos completamente nuevos en entornos de producción.

Cantidad y distribución de datos
Se recomienda contar con un número suficiente de imágenes para cada clase con el fin de evitar problemas de subajuste (underfitting) durante el entrenamiento.

![Imagen](https://3.bp.blogspot.com/-DMA8dcxkC0w/Xiq-VcBoroI/AAAAAAAA3yI/oo5W8Ow3rhoK19s5m-tKN0KzhuQMcNoagCLcBGAsYHQ/s1600/1.png)


Una distribución de referencia adecuada para este proyecto es:

Clase 1: 1,000 imágenes

Clase 2: 1,000 imágenes

Clase 3: 1,000 imágenes

Total: 3,000 imágenes distribuidas de manera equilibrada.

## Importancia del balanceo
Mantener el mismo número de imágenes por clase es fundamental para evitar sesgos en el modelo. Si una clase tuviera significativamente más ejemplos que otra, el sistema podría inclinarse a predecir esa clase con mayor frecuencia por pura probabilidad previa, reduciendo su precisión y fiabilidad general en escenarios reales.

## Conclusión
El análisis exploratorio de datos permite identificar aspectos clave del dataset antes de proceder a la fase de entrenamiento del modelo. En este caso, la diversidad y el balance estricto entre clases son los factores determinantes para lograr un sistema de reconocimiento de dígitos eficiente.

Un dataset bien estructurado, limpio y variado mejora significativamente la capacidad del algoritmo para adaptarse de manera óptima a diferentes escenarios del mundo real.