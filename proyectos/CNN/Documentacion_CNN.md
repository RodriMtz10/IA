# Documentación del Proyecto: Clasificador de Fauna CNN

## 1. Nombre del proyecto

**Clasificador de Fauna CNN**

## 2. Descripción general

Este proyecto consiste en un sistema de clasificación de imágenes utilizando una Red Neuronal Convolucional, también conocida como CNN. El objetivo principal es identificar automáticamente a qué clase pertenece una imagen de animal.

El sistema trabaja con cinco categorías:

* Ranas
* Pájaros
* Ballenas
* Changos
* Arañas

El proyecto fue desarrollado en Python y utiliza TensorFlow/Keras para la creación y entrenamiento del modelo, OpenCV para el procesamiento de imágenes y Tkinter para la interfaz gráfica.

## 3. Objetivo del proyecto

El objetivo del proyecto es entrenar una red neuronal convolucional capaz de clasificar imágenes de fauna en diferentes categorías. Además, se implementó una interfaz gráfica que permite al usuario seleccionar una imagen desde su computadora y obtener como resultado la clase detectada junto con el porcentaje de confianza del modelo.

## 4. Estructura del proyecto

La estructura del proyecto es la siguiente:

```text
ClasificadorFaunaCNN/
│
├── dataset/
│   ├── ranas/
│   ├── pajaros/
│   ├── ballenas/
│   ├── changos/
│   └── aranas/
│
├── entrenar.py
├── clasificar.py
├── modelo_fauna.keras
├── requirements.txt
└── DOCUMENTACION.md
```

## 5. Descripción de carpetas y archivos

### dataset/

Esta carpeta contiene las imágenes utilizadas para entrenar el modelo. Cada subcarpeta representa una clase diferente.

Ejemplo:

```text
dataset/ranas/
dataset/pajaros/
dataset/ballenas/
dataset/changos/
dataset/aranas/
```

Cada imagen dentro de estas carpetas se utiliza como ejemplo para que la red neuronal aprenda a reconocer patrones visuales de cada animal.

### entrenar.py

Este archivo contiene el proceso de entrenamiento del modelo CNN.

Sus funciones principales son:

* Cargar las imágenes desde la carpeta `dataset`.
* Redimensionar todas las imágenes a 64x64 píxeles.
* Normalizar los valores de los pixeles.
* Convertir las etiquetas en formato categórico.
* Dividir el dataset en entrenamiento y validación.
* Crear la arquitectura de la red neuronal convolucional.
* Entrenar el modelo.
* Guardar el modelo entrenado como `modelo_fauna.keras`.

### clasificar.py

Este archivo contiene la interfaz gráfica del proyecto.

Sus funciones principales son:

* Cargar el modelo entrenado `modelo_fauna.keras`.
* Abrir una ventana con Tkinter.
* Permitir al usuario seleccionar una imagen.
* Mostrar la imagen seleccionada.
* Procesar la imagen para que tenga el mismo tamaño utilizado en el entrenamiento.
* Realizar la predicción.
* Mostrar la clase detectada y el porcentaje de confianza.

### modelo_fauna.keras

Este archivo es el modelo entrenado. Se genera automáticamente después de ejecutar `entrenar.py`.

El archivo contiene los pesos y la arquitectura aprendida por la red neuronal.

### requirements.txt

Este archivo contiene las librerías necesarias para ejecutar el proyecto.

## 6. Librerías utilizadas

El proyecto utiliza las siguientes librerías:

```text
tensorflow
numpy
opencv-python
matplotlib
scikit-learn
pillow
```

### TensorFlow / Keras

Se utiliza para crear, entrenar y guardar la red neuronal convolucional.

### NumPy

Se utiliza para el manejo de arreglos numéricos y procesamiento de datos.

### OpenCV

Se utiliza para leer y redimensionar imágenes durante el entrenamiento.

### Scikit-learn

Se utiliza para dividir el dataset en datos de entrenamiento y validación.

### Pillow

Se utiliza para abrir y mostrar imágenes dentro de la interfaz gráfica.

### Tkinter

Se utiliza para crear la ventana de la aplicación.

## 7. Funcionamiento general del sistema

El funcionamiento del proyecto se divide en dos etapas principales:

1. Entrenamiento del modelo.
2. Clasificación de imágenes.

## 8. Entrenamiento del modelo

Para entrenar el modelo se ejecuta el archivo:

```bash
python entrenar.py
```

Durante este proceso, el programa busca las imágenes dentro de la carpeta `dataset`.

Cada carpeta representa una clase. Por ejemplo:

```text
ranas     → Clase 0
pajaros   → Clase 1
ballenas  → Clase 2
changos   → Clase 3
aranas    → Clase 4
```

El programa carga todas las imágenes, las redimensiona a 64x64 píxeles y las convierte en arreglos numéricos.

Después, los valores de los pixeles se normalizan dividiéndolos entre 255. Esto permite que los valores estén entre 0 y 1, lo cual ayuda a que la red neuronal entrene de forma más estable.

Posteriormente, el dataset se divide en dos partes:

* 80% para entrenamiento.
* 20% para validación.

El conjunto de entrenamiento sirve para que la red neuronal aprenda, mientras que el conjunto de validación sirve para medir qué tan bien funciona el modelo con imágenes que no se usaron directamente durante el entrenamiento.

## 9. Arquitectura del modelo CNN

El modelo utilizado es una Red Neuronal Convolucional.

La arquitectura general está compuesta por:

* Capas convolucionales `Conv2D`.
* Funciones de activación `LeakyReLU`.
* Capas de reducción `MaxPooling2D`.
* Capas de regularización `Dropout`.
* Una capa `Flatten`.
* Capas densas `Dense`.
* Una capa final con activación `softmax`.

La capa final utiliza `softmax` porque el modelo debe elegir entre varias clases posibles.

## 10. Capas principales del modelo

### Capas Conv2D

Las capas convolucionales se encargan de extraer características visuales de las imágenes, como bordes, formas, texturas y patrones.

### MaxPooling2D

Estas capas reducen el tamaño de la información procesada, conservando las características más importantes.

### Dropout

Esta técnica ayuda a reducir el sobreajuste, apagando aleatoriamente algunas neuronas durante el entrenamiento.

### Flatten

Convierte la información extraída por las capas convolucionales en un vector para poder conectarlo con las capas densas.

### Dense

Las capas densas procesan la información final y ayudan a decidir a qué clase pertenece la imagen.

### Softmax

La función `softmax` genera una probabilidad para cada clase. La clase con la probabilidad más alta es la predicción final.

## 11. Clasificación de imágenes

Después de entrenar el modelo, se puede ejecutar la interfaz gráfica con:

```bash
python clasificar.py
```

El programa abre una ventana donde el usuario puede seleccionar una imagen.

Una vez seleccionada la imagen:

1. Se carga la imagen.
2. Se muestra en la interfaz.
3. Se redimensiona a 64x64 píxeles.
4. Se normalizan sus pixeles.
5. Se envía al modelo entrenado.
6. El modelo genera una predicción.
7. Se muestra la clase detectada y el porcentaje de confianza.

## 12. Ejemplo de salida

Un ejemplo de resultado dentro de la interfaz sería:

```text
Animal detectado: changos
Confianza: 100.00%
```

Esto significa que el modelo clasificó la imagen seleccionada como un chango y tiene una confianza del 100% según su predicción.

## 13. Resultados obtenidos

Durante el entrenamiento, el modelo logró una precisión de validación alta. Esto indica que el modelo fue capaz de aprender los patrones visuales de las cinco clases del dataset.

Ejemplo de resultado obtenido:

```text
val_accuracy: 0.9984
val_loss: 0.0140
```

Esto significa que el modelo obtuvo aproximadamente un 99.84% de precisión en el conjunto de validación.

## 14. Consideraciones importantes

El modelo funciona correctamente con imágenes pertenecientes al dataset utilizado para el entrenamiento y validación.

Sin embargo, al probar imágenes externas descargadas de internet, el modelo puede presentar errores. Esto puede ocurrir porque las imágenes externas pueden tener diferentes fondos, tamaños, ángulos, iluminación o calidad.

Para mejorar este comportamiento, se podría aplicar aumentación de datos, conocida como `Data Augmentation`, utilizando técnicas como:

* Rotación de imágenes.
* Cambios de brillo.
* Zoom.
* Volteo horizontal.
* Desplazamientos.
* Recortes.

Esto permitiría que el modelo aprenda una mayor variedad de ejemplos y pueda generalizar mejor con imágenes nuevas.

## 15. Cómo ejecutar el proyecto

### Paso 1: Crear o activar el entorno virtual

```bash
python -m venv env
```

En Windows:

```bash
env\Scripts\activate
```

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Entrenar el modelo

```bash
python entrenar.py
```

Al finalizar, se generará el archivo:

```text
modelo_fauna.keras
```

### Paso 4: Ejecutar la interfaz gráfica

```bash
python clasificar.py
```

### Paso 5: Seleccionar una imagen

Dentro de la ventana, presionar el botón **Seleccionar Imagen** y elegir una imagen de alguna de las clases del dataset.

## 16. Explicación técnica breve

El sistema utiliza una CNN porque este tipo de red neuronal es adecuada para trabajar con imágenes. Las CNN pueden detectar patrones visuales mediante filtros convolucionales. En este proyecto, la red aprende características de cada animal y utiliza esas características para clasificar nuevas imágenes.

La predicción se realiza comparando la imagen seleccionada con los patrones aprendidos durante el entrenamiento. Finalmente, el modelo devuelve la clase con mayor probabilidad.

## 17. Posibles mejoras futuras

Algunas mejoras que se podrían agregar al proyecto son:

* Implementar aumentación de datos.
* Agregar una matriz de confusión.
* Mostrar la probabilidad de todas las clases.
* Permitir clasificar varias imágenes al mismo tiempo.
* Guardar un historial de predicciones.
* Mejorar el diseño visual de la interfaz.
* Probar el modelo con imágenes externas al dataset.
* Usar modelos preentrenados como MobileNet o ResNet.

## 18. Conclusión

El proyecto permite clasificar imágenes de animales utilizando una Red Neuronal Convolucional. Se logró entrenar un modelo capaz de reconocer cinco clases diferentes de fauna y se agregó una interfaz gráfica para facilitar su uso.

Este proyecto demuestra el uso práctico de redes neuronales convolucionales en tareas de clasificación de imágenes, integrando procesamiento de datos, entrenamiento de modelos y una interfaz visual para el usuario.
