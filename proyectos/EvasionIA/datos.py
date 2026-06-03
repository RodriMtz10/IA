import csv
from dataclasses import dataclass
from typing import List
from collections import Counter

from config import ARCHIVO_CSV


@dataclass
class RegistroJuego:
    velocidad_proyectil: float
    distancia: float
    altura_proyectil: float
    tipo_proyectil: int
    estado_jugador: int
    accion: int


class MemoriaJuego:
    def __init__(self):
        self.registros: List[RegistroJuego] = []

    def agregar_registro(
        self,
        velocidad_proyectil: float,
        distancia: float,
        altura_proyectil: float,
        tipo_proyectil: int,
        estado_jugador: int,
        accion: int
    ):
        registro = RegistroJuego(
            velocidad_proyectil=velocidad_proyectil,
            distancia=distancia,
            altura_proyectil=altura_proyectil,
            tipo_proyectil=tipo_proyectil,
            estado_jugador=estado_jugador,
            accion=accion
        )

        self.registros.append(registro)

    def cantidad(self):
        return len(self.registros)

    def limpiar(self):
        self.registros.clear()

    def obtener_x_y(self):
        x = []
        y = []

        for r in self.registros:
            x.append([
                r.velocidad_proyectil,
                r.distancia,
                r.altura_proyectil,
                r.tipo_proyectil,
                r.estado_jugador
            ])

            y.append(r.accion)

        return x, y

    def resumen_acciones(self):
        acciones = [r.accion for r in self.registros]
        return Counter(acciones)

    def exportar_csv(self, ruta=ARCHIVO_CSV):
        if not self.registros:
            return False, "No hay datos para exportar."

        try:
            with open(ruta, "w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)

                writer.writerow([
                    "velocidad_proyectil",
                    "distancia",
                    "altura_proyectil",
                    "tipo_proyectil",
                    "estado_jugador",
                    "accion"
                ])

                for r in self.registros:
                    writer.writerow([
                        r.velocidad_proyectil,
                        r.distancia,
                        r.altura_proyectil,
                        r.tipo_proyectil,
                        r.estado_jugador,
                        r.accion
                    ])

            return True, f"Datos exportados correctamente en {ruta}"

        except Exception as e:
            return False, f"Error al exportar datos: {e}"