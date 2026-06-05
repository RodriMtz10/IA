# Documentación del Proyecto: Visualizador A*

## 1. Descripción general

Este proyecto consiste en un visualizador interactivo del algoritmo de búsqueda A*, desarrollado en Python con Pygame.

El programa permite crear un mapa en forma de cuadrícula, seleccionar un punto inicial, un punto final y colocar obstáculos. Después, el algoritmo A* calcula y muestra visualmente el camino más corto entre el inicio y el destino.

## 2. Objetivo

El objetivo del proyecto es demostrar el funcionamiento del algoritmo A* de manera visual e interactiva.

Este algoritmo es utilizado en áreas como:

- Videojuegos
- Robótica
- GPS
- Navegación
- Inteligencia Artificial
- Grafos

## 3. Tecnologías utilizadas

- Python
- Pygame
- Algoritmo A*
- Grafos
- Heurística Manhattan

## 4. Estructura del proyecto

```text
AStarVisualizer/
│
├── config.py
├── nodo.py
├── astar.py
├── main.py
├── requirements.txt
├── README.md
└── DOCUMENTACION_ASTAR.md
```

## 5. Descripción de archivos
config.py

Contiene la configuración general del programa:

Tamaño de ventana
Cantidad de filas
FPS
Colores
Título de la ventana
nodo.py

Contiene la clase Nodo.

Cada nodo representa una celda de la cuadrícula y puede tener diferentes estados:

Libre
Inicio
Fin
Obstáculo
Abierto
Cerrado
Camino final
astar.py

Contiene la implementación del algoritmo A*.

Este archivo calcula el camino más corto usando:

f(n) = g(n) + h(n)

Donde:

g(n) es el costo desde el inicio hasta el nodo actual.
h(n) es la heurística desde el nodo actual hasta el destino.
f(n) es el costo total estimado.
main.py

Es el archivo principal.

Se encarga de:

Crear la ventana.
Crear la cuadrícula.
Detectar clicks del mouse.
Ejecutar el algoritmo.
Dibujar la animación.

## 6. Controles
Click izquierdo
Primer click: selecciona el nodo inicial.
Segundo click: selecciona el nodo final.
Clicks posteriores: colocan obstáculos.
Click derecho

Borra un nodo seleccionado.

Tecla ESPACIO

Ejecuta el algoritmo A*.

Tecla C

Limpia toda la cuadrícula.

## 7. Colores utilizados
Naranja: nodo inicial.
Morado: nodo final.
Negro: obstáculos.
Verde: nodos abiertos.
Rojo: nodos cerrados.
Amarillo: camino final.
Blanco: espacios libres.

## 8. Funcionamiento del algoritmo

El algoritmo A* busca el camino más corto desde un nodo inicial hasta un nodo final.

Para hacerlo, evalúa cada nodo usando una función de costo:

f(n) = g(n) + h(n)

La heurística utilizada es la distancia Manhattan:

h(n) = |x1 - x2| + |y1 - y2|

Esta heurística es adecuada porque el movimiento se realiza en cuatro direcciones:

Arriba
Abajo
Izquierda
Derecha

## 9. Proceso de búsqueda

El algoritmo funciona de la siguiente manera:

Agrega el nodo inicial a una cola de prioridad.
Selecciona el nodo con menor costo estimado.
Revisa sus vecinos.
Actualiza los costos si encuentra un camino mejor.
Marca los nodos explorados.
Repite el proceso hasta llegar al nodo final.
Reconstruye el camino encontrado.

## 10. Aplicaciones reales

El algoritmo A* se utiliza en:

Enemigos de videojuegos que persiguen al jugador.
Sistemas GPS.
Robots que evitan obstáculos.
Simuladores.
Planeación de rutas.
Inteligencia artificial en juegos.

## 11. Cómo ejecutar el proyecto

Instalar dependencias:

pip install -r requirements.txt

Ejecutar:

python main.py

## 12. Posibles mejoras futuras
Agregar laberintos aleatorios.
Comparar A* con BFS y DFS.
Mostrar el costo total del camino.
Mostrar cantidad de nodos explorados.
Agregar diagonal.
Agregar un menú principal.
Mejorar el diseño visual.
Agregar animaciones más suaves.

## 13. Conclusión

Este proyecto permite visualizar de forma clara cómo funciona el algoritmo A*. A través de una cuadrícula interactiva, se puede observar cómo el algoritmo explora caminos, evita obstáculos y encuentra una ruta óptima hacia el objetivo.