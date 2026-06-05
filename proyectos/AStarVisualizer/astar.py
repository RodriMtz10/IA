from queue import PriorityQueue


def heuristica(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruir_camino(came_from, actual, dibujar):
    while actual in came_from:
        actual = came_from[actual]
        actual.hacer_camino()
        dibujar()


def algoritmo(dibujar, grid, inicio, fin):

    contador = 0
    abiertos = PriorityQueue()
    abiertos.put((0, contador, inicio))

    came_from = {}

    g_score = {nodo: float("inf") for fila in grid for nodo in fila}
    g_score[inicio] = 0

    f_score = {nodo: float("inf") for fila in grid for nodo in fila}
    f_score[inicio] = heuristica(inicio.get_pos(), fin.get_pos())

    conjunto_abiertos = {inicio}

    while not abiertos.empty():

        actual = abiertos.get()[2]
        conjunto_abiertos.remove(actual)

        if actual == fin:
            reconstruir_camino(came_from, fin, dibujar)
            fin.hacer_fin()
            inicio.hacer_inicio()
            return True

        for vecino in actual.vecinos:

            temp_g = g_score[actual] + 1

            if temp_g < g_score[vecino]:

                came_from[vecino] = actual
                g_score[vecino] = temp_g

                f_score[vecino] = (
                    temp_g
                    + heuristica(
                        vecino.get_pos(),
                        fin.get_pos()
                    )
                )

                if vecino not in conjunto_abiertos:
                    contador += 1

                    abiertos.put(
                        (
                            f_score[vecino],
                            contador,
                            vecino
                        )
                    )

                    conjunto_abiertos.add(vecino)
                    vecino.hacer_abierto()

        dibujar()

        if actual != inicio:
            actual.hacer_cerrado()

    return False