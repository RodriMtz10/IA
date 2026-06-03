# Documentación del Proyecto: Evasión IA

## 1. Descripción general

**Evasión IA** es un videojuego desarrollado en Python utilizando la librería Pygame. El objetivo principal del juego es controlar a un robot que debe esquivar diferentes tipos de proyectiles.

El proyecto integra inteligencia artificial mediante un modelo MLP, el cual aprende a tomar decisiones a partir de los datos generados por el jugador en modo manual.

## 2. Objetivo

El objetivo del proyecto es implementar un videojuego interactivo donde el jugador pueda generar datos jugando manualmente y posteriormente entrenar una IA capaz de imitar las decisiones del jugador.

La IA puede aprender acciones como:

* No hacer nada
* Saltar
* Agacharse
* Activar escudo

## 3. Tecnologías utilizadas

* Python
* Pygame
* Scikit-learn
* NumPy
* Matplotlib

## 4. Estructura del proyecto

```text
EvasionIA/
│
├── config.py
├── datos.py
├── modelo_ia.py
├── juego.py
├── requirements.txt
└── DOCUMENTACION_EVASIONIA.md
```

## 5. Descripción de archivos

### config.py

Contiene la configuración general del juego, como:

* Tamaño de ventana
* FPS
* Colores
* Medidas del jugador
* Parámetros de proyectiles
* Acciones disponibles
* Cantidad mínima de datos para entrenar la IA

### datos.py

Este archivo se encarga de almacenar los datos generados durante el modo manual.

Cada registro contiene:

* Velocidad del proyectil
* Distancia entre el proyectil y el jugador
* Altura del proyectil
* Tipo de proyectil
* Estado actual del jugador
* Acción realizada por el jugador

Estos datos se utilizan posteriormente para entrenar el modelo de inteligencia artificial.

### modelo_ia.py

Contiene la clase encargada de entrenar y utilizar el modelo de inteligencia artificial.

El modelo utilizado es un **MLPClassifier**, una red neuronal multicapa incluida en Scikit-learn.

El modelo aprende a predecir una acción dependiendo de las condiciones actuales del juego.

### juego.py

Es el archivo principal del proyecto.

Contiene:

* La ventana del juego
* El jugador
* Los proyectiles
* La lógica de movimiento
* Las colisiones
* El modo manual
* El modo IA
* El HUD visual
* La interacción con el modelo de IA

## 6. Funcionamiento del juego

El juego tiene dos modos principales:

### Modo manual

En este modo, el jugador controla al personaje usando el teclado.

Controles principales:

```text
ESPACIO = Saltar
FLECHA ABAJO = Agacharse
E = Activar escudo
T = Entrenar IA
I = Activar modo IA
M = Volver a modo manual
C = Exportar datos a CSV
R = Reiniciar datos y modelo
ESC = Salir
```

Mientras el jugador juega manualmente, el sistema guarda datos sobre cada situación del juego.

### Modo IA

Después de recolectar suficientes datos y entrenar el modelo, se puede activar el modo IA.

En este modo, el personaje toma decisiones automáticamente con base en lo aprendido.

La IA analiza:

* La velocidad del proyectil
* La distancia al jugador
* La altura del proyectil
* El tipo de proyectil
* El estado actual del jugador

Con esa información decide si debe saltar, agacharse, activar el escudo o no hacer nada.

## 7. Tipos de proyectiles

El juego cuenta con tres tipos de proyectiles:

### Proyectil bajo

Va cerca del suelo.

Acción recomendada:

```text
Saltar
```

### Proyectil alto

Va a una altura media/alta.

Acción recomendada:

```text
Agacharse
```

### Proyectil diagonal

Desciende desde la parte superior hacia el jugador.

Acción recomendada:

```text
Activar escudo
```

## 8. Acciones del jugador

El jugador puede realizar cuatro acciones:

```text
0 = Nada
1 = Saltar
2 = Agacharse
3 = Escudo
```

Estas acciones son las etiquetas que utiliza el modelo para aprender.

## 9. Recolección de datos

Durante el modo manual, el sistema guarda información del entorno y la acción realizada por el jugador.

Ejemplo de registro:

```text
velocidad_proyectil, distancia, altura_proyectil, tipo_proyectil, estado_jugador, accion
10, 180, 0.0, 0, 0, 1
12, 160, 1.0, 1, 0, 2
8, 140, 0.5, 2, 0, 3
```

Estos datos indican cómo reaccionó el jugador ante diferentes situaciones.

## 10. Entrenamiento de la IA

Para entrenar la IA, primero se deben recolectar datos jugando en modo manual.

Una vez recolectados suficientes datos, se presiona la tecla:

```text
T
```

El sistema entrena un modelo MLP utilizando los datos almacenados.

El modelo divide los datos en:

* Datos de entrenamiento
* Datos de prueba

Luego calcula una precisión aproximada del modelo.

## 11. Modelo utilizado

El modelo usado es:

```python
MLPClassifier
```

La arquitectura utilizada es:

```python
hidden_layer_sizes=(128, 64, 32)
```

Esto significa que la red neuronal tiene tres capas ocultas con 128, 64 y 32 neuronas respectivamente.

El modelo utiliza:

```python
activation="relu"
solver="adam"
```

Esto permite aprender patrones en los datos registrados durante el juego.

## 12. Exportación de datos

El juego permite exportar los datos recolectados a un archivo CSV presionando:

```text
C
```

El archivo generado puede utilizarse para revisar los datos o analizarlos externamente.

## 13. Interfaz visual

El juego cuenta con una interfaz visual estilo futurista.

Incluye:

* Fondo oscuro con cuadrícula
* Suelo iluminado
* Robot con colores dinámicos
* Proyectiles con brillo
* Panel de información
* Panel de controles
* Indicador de modo manual o IA
* Puntaje
* Vidas
* Cantidad de datos recolectados
* Estado del modelo IA

## 14. Cómo ejecutar el proyecto

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Ejecutar el juego

```bash
python juego.py
```

### Paso 3: Recolectar datos

Jugar en modo manual usando:

```text
ESPACIO
FLECHA ABAJO
E
```

### Paso 4: Entrenar la IA

Presionar:

```text
T
```

### Paso 5: Activar modo IA

Presionar:

```text
I
```

## 15. Recomendaciones para entrenar la IA

Para que la IA funcione correctamente, se recomienda recolectar datos variados.

Es importante usar todas las acciones:

* Saltar ante proyectiles bajos
* Agacharse ante proyectiles altos
* Usar escudo ante proyectiles diagonales

Si la mayoría de los datos corresponden a la acción "nada", la IA puede aprender a no reaccionar correctamente.

## 16. Posibles mejoras futuras

Algunas mejoras que se pueden agregar son:

* Sprites personalizados para el robot
* Sonidos
* Música de fondo
* Animaciones
* Menú principal
* Sistema de niveles
* Mayor variedad de proyectiles
* Guardar y cargar modelos entrenados
* Mejorar el balance del dataset
* Mostrar probabilidades de decisión de la IA

## 17. Conclusión

Evasión IA combina videojuegos e inteligencia artificial en un mismo proyecto. El jugador genera datos mediante sus acciones y posteriormente entrena un modelo capaz de tomar decisiones automáticamente.

Este proyecto demuestra cómo una red neuronal simple puede aprender comportamientos dentro de un entorno interactivo usando datos generados por el usuario.