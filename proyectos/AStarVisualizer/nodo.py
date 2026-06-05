import pygame
from config import (
    BLANCO,
    NEGRO,
    GRIS,
    VERDE,
    ROJO,
    AZUL,
    NARANJA,
    MORADO,
    AMARILLO,
    CYAN,
)


class Nodo:
    def __init__(self, fila, columna, ancho, total_filas):
        self.fila = fila
        self.columna = columna
        self.x = columna * ancho
        self.y = fila * ancho
        self.color = BLANCO
        self.vecinos = []
        self.ancho = ancho
        self.total_filas = total_filas

    def get_pos(self):
        return self.fila, self.columna

    def es_cerrado(self):
        return self.color == ROJO

    def es_abierto(self):
        return self.color == VERDE

    def es_pared(self):
        return self.color == NEGRO

    def es_inicio(self):
        return self.color == NARANJA

    def es_fin(self):
        return self.color == MORADO

    def reset(self):
        self.color = BLANCO

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_cerrado(self):
        self.color = ROJO

    def hacer_abierto(self):
        self.color = VERDE

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = MORADO

    def hacer_camino(self):
        self.color = AMARILLO

    def hacer_actual(self):
        self.color = CYAN

    def dibujar(self, ventana):
        pygame.draw.rect(
            ventana,
            self.color,
            (self.x, self.y, self.ancho, self.ancho)
        )

    def actualizar_vecinos(self, grid):
        self.vecinos = []

        # Abajo
        if self.fila < self.total_filas - 1 and not grid[self.fila + 1][self.columna].es_pared():
            self.vecinos.append(grid[self.fila + 1][self.columna])

        # Arriba
        if self.fila > 0 and not grid[self.fila - 1][self.columna].es_pared():
            self.vecinos.append(grid[self.fila - 1][self.columna])

        # Derecha
        if self.columna < self.total_filas - 1 and not grid[self.fila][self.columna + 1].es_pared():
            self.vecinos.append(grid[self.fila][self.columna + 1])

        # Izquierda
        if self.columna > 0 and not grid[self.fila][self.columna - 1].es_pared():
            self.vecinos.append(grid[self.fila][self.columna - 1])

    def __lt__(self, other):
        return False