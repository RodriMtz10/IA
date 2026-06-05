import pygame

from config import *
from nodo import Nodo
from astar import algoritmo


VENTANA = pygame.display.set_mode(
    (ANCHO_VENTANA, ANCHO_VENTANA)
)

pygame.display.set_caption(TITULO)


def crear_grid(filas, ancho):

    grid = []

    espacio = ancho // filas

    for i in range(filas):

        grid.append([])

        for j in range(filas):

            nodo = Nodo(
                i,
                j,
                espacio,
                filas
            )

            grid[i].append(nodo)

    return grid


def dibujar_lineas(ventana, filas, ancho):

    espacio = ancho // filas

    for i in range(filas):

        pygame.draw.line(
            ventana,
            GRIS,
            (0, i * espacio),
            (ancho, i * espacio)
        )

        for j in range(filas):

            pygame.draw.line(
                ventana,
                GRIS,
                (j * espacio, 0),
                (j * espacio, ancho)
            )


def dibujar(ventana, grid, filas, ancho):

    ventana.fill(BLANCO)

    for fila in grid:

        for nodo in fila:

            nodo.dibujar(ventana)

    dibujar_lineas(
        ventana,
        filas,
        ancho
    )

    pygame.display.update()


def obtener_click(pos, filas, ancho):

    espacio = ancho // filas

    y, x = pos

    fila = y // espacio
    columna = x // espacio

    return fila, columna


def main():

    pygame.init()

    grid = crear_grid(
        FILAS,
        ANCHO_VENTANA
    )

    inicio = None
    fin = None

    corriendo = True

    while corriendo:

        dibujar(
            VENTANA,
            grid,
            FILAS,
            ANCHO_VENTANA
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                corriendo = False

            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()

                fila, columna = obtener_click(
                    pos,
                    FILAS,
                    ANCHO_VENTANA
                )

                nodo = grid[fila][columna]

                if not inicio and nodo != fin:
                    inicio = nodo
                    inicio.hacer_inicio()

                elif not fin and nodo != inicio:
                    fin = nodo
                    fin.hacer_fin()

                elif nodo != inicio and nodo != fin:
                    nodo.hacer_pared()

            elif pygame.mouse.get_pressed()[2]:

                pos = pygame.mouse.get_pos()

                fila, columna = obtener_click(
                    pos,
                    FILAS,
                    ANCHO_VENTANA
                )

                nodo = grid[fila][columna]

                nodo.reset()

                if nodo == inicio:
                    inicio = None

                if nodo == fin:
                    fin = None

            if evento.type == pygame.KEYDOWN:

                if (
                    evento.key == pygame.K_SPACE
                    and inicio
                    and fin
                ):

                    for fila in grid:
                        for nodo in fila:
                            nodo.actualizar_vecinos(grid)

                    algoritmo(
                        lambda: dibujar(
                            VENTANA,
                            grid,
                            FILAS,
                            ANCHO_VENTANA
                        ),
                        grid,
                        inicio,
                        fin
                    )

                if evento.key == pygame.K_c:

                    inicio = None
                    fin = None

                    grid = crear_grid(
                        FILAS,
                        ANCHO_VENTANA
                    )

    pygame.quit()


if __name__ == "__main__":
    main()