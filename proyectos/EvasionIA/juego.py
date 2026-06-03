import random
import pygame

from config import (
ANCHO_VENTANA,
ALTO_VENTANA,
FPS,
TITULO_JUEGO,
BLANCO,
GRIS,
GRIS_OSCURO,
AZUL,
VERDE,
ROJO,
AMARILLO,
MORADO,
JUGADOR_X,
JUGADOR_ANCHO,
JUGADOR_ALTO,
JUGADOR_ALTO_AGACHADO,
GRAVEDAD,
FUERZA_SALTO,
DURACION_ESCUDO,
ENFRIAMIENTO_ESCUDO,
PROYECTIL_ANCHO,
PROYECTIL_ALTURA,
VELOCIDAD_PROYECTIL_MIN,
VELOCIDAD_PROYECTIL_MAX,
TIPO_PROYECTIL_BAJO,
TIPO_PROYECTIL_ALTO,
TIPO_PROYECTIL_DIAGONAL,
ACCION_NADA,
ACCION_SALTAR,
ACCION_AGACHARSE,
ACCION_ESCUDO
)

from datos import MemoriaJuego
from modelo_ia import ModeloIA

class JuegoEvasionIA:
    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption(TITULO_JUEGO)

        self.reloj = pygame.time.Clock()

        self.fuente = pygame.font.SysFont("Arial", 24)
        self.fuente_chica = pygame.font.SysFont("Arial", 18)

        self.suelo_y = ALTO_VENTANA - 110

        self.memoria = MemoriaJuego()
        self.modelo_ia = ModeloIA()

        self.modo_auto = False
        self.mensaje = "Modo manual: genera datos esquivando proyectiles."

        self.puntaje = 0
        self.vidas = 3
        self.frames = 0

        self.jugador = pygame.Rect(
            JUGADOR_X,
            self.suelo_y - JUGADOR_ALTO,
            JUGADOR_ANCHO,
            JUGADOR_ALTO
        )

        self.velocidad_y = 0
        self.en_suelo = True
        self.agachado = False

        self.escudo_activo = False
        self.escudo_timer = 0
        self.escudo_cooldown = 0

        self.proyectil = pygame.Rect(
            ANCHO_VENTANA + 100,
            self.suelo_y - PROYECTIL_ALTURA,
            PROYECTIL_ANCHO,
            PROYECTIL_ALTURA
        )

        self.proyectil_activo = False
        self.velocidad_proyectil = 0
        self.tipo_proyectil = TIPO_PROYECTIL_BAJO
        self.altura_proyectil = 0.0
        self.velocidad_vertical_proyectil = 0

        self.contador_registro = 0
        self.corriendo = True

# ==========================
# ESTADOS DEL JUGADOR
# ==========================

    def estado_jugador(self):
        if self.escudo_activo:
            return 3
        if self.agachado:
            return 2
        if not self.en_suelo:
            return 1
        return 0

    def accion_manual_actual(self):
        if self.escudo_activo:
            return ACCION_ESCUDO
        if self.agachado:
            return ACCION_AGACHARSE
        if not self.en_suelo:
            return ACCION_SALTAR
        return ACCION_NADA

    # ==========================
    # ACCIONES
    # ==========================

    def saltar(self):
        if self.en_suelo and not self.agachado:
            self.velocidad_y = -FUERZA_SALTO
            self.en_suelo = False

    def agacharse(self):
        if self.en_suelo and not self.escudo_activo:
            self.agachado = True
            self.jugador.height = JUGADOR_ALTO_AGACHADO
            self.jugador.y = self.suelo_y - JUGADOR_ALTO_AGACHADO

    def dejar_agacharse(self):
        if self.agachado:
            self.agachado = False
            self.jugador.height = JUGADOR_ALTO
            self.jugador.y = self.suelo_y - JUGADOR_ALTO

    def activar_escudo(self):
        if self.escudo_cooldown <= 0 and not self.agachado:
            self.escudo_activo = True
            self.escudo_timer = DURACION_ESCUDO
            self.escudo_cooldown = ENFRIAMIENTO_ESCUDO

    # ==========================
    # PROYECTILES
    # ==========================

    def crear_proyectil(self):
        self.tipo_proyectil = random.choice([
            TIPO_PROYECTIL_BAJO,
            TIPO_PROYECTIL_ALTO,
            TIPO_PROYECTIL_DIAGONAL
        ])

        self.velocidad_proyectil = random.randint(
            VELOCIDAD_PROYECTIL_MIN,
            VELOCIDAD_PROYECTIL_MAX
        )

        self.proyectil.x = ANCHO_VENTANA + random.randint(40, 180)
        self.proyectil.width = PROYECTIL_ANCHO
        self.proyectil.height = PROYECTIL_ALTURA

        if self.tipo_proyectil == TIPO_PROYECTIL_BAJO:
            self.proyectil.y = self.suelo_y - PROYECTIL_ALTURA
            self.altura_proyectil = 0.0
            self.velocidad_vertical_proyectil = 0

        elif self.tipo_proyectil == TIPO_PROYECTIL_ALTO:
            self.proyectil.y = self.suelo_y - JUGADOR_ALTO - 5
            self.altura_proyectil = 1.0
            self.velocidad_vertical_proyectil = 0

        else:
            self.proyectil.y = self.suelo_y - JUGADOR_ALTO - 80
            self.altura_proyectil = 0.5
            self.velocidad_vertical_proyectil = 2

        self.proyectil_activo = True

    def actualizar_proyectil(self):
        if not self.proyectil_activo:
            self.crear_proyectil()
            return

        self.proyectil.x -= self.velocidad_proyectil

        if self.tipo_proyectil == TIPO_PROYECTIL_DIAGONAL:
            self.proyectil.y += self.velocidad_vertical_proyectil

            limite_diagonal = self.suelo_y - JUGADOR_ALTO

            if self.proyectil.y > limite_diagonal:
                self.proyectil.y = limite_diagonal

        if self.proyectil.right < 0:
            self.proyectil_activo = False
            self.puntaje += 1

    # ==========================
    # FÍSICA
    # ==========================

    def actualizar_jugador(self):
        if not self.en_suelo:
            self.jugador.y += self.velocidad_y
            self.velocidad_y += GRAVEDAD

            if self.jugador.bottom >= self.suelo_y:
                self.jugador.bottom = self.suelo_y
                self.velocidad_y = 0
                self.en_suelo = True

        if self.escudo_activo:
            self.escudo_timer -= 1
            if self.escudo_timer <= 0:
                self.escudo_activo = False

        if self.escudo_cooldown > 0:
            self.escudo_cooldown -= 1

    # ==========================
    # IA Y DATOS
    # ==========================

    def distancia_proyectil(self):
        return float(self.proyectil.x - self.jugador.x)

    def registrar_datos_manual(self):
        if not self.proyectil_activo:
            return

        distancia = self.distancia_proyectil()

        # Solo guardar datos cuando el proyectil está cerca del jugador
        if distancia > 260 or distancia < -40:
            return

        self.contador_registro += 1

        if self.contador_registro % 2 != 0:
            return

        accion = self.accion_manual_actual()

        self.memoria.agregar_registro(
            velocidad_proyectil=float(self.velocidad_proyectil),
            distancia=distancia,
            altura_proyectil=float(self.altura_proyectil),
            tipo_proyectil=int(self.tipo_proyectil),
            estado_jugador=int(self.estado_jugador()),
            accion=int(accion),
        )

    def aplicar_ia(self):
        if not self.modo_auto:
            return
        
        distancia = self.distancia_proyectil()

        if 30 < distancia < 170:
            if self.tipo_proyectil == TIPO_PROYECTIL_BAJO:
                self.saltar()
                return

            if self.tipo_proyectil == TIPO_PROYECTIL_ALTO:
                self.agacharse()
                return

            if self.tipo_proyectil == TIPO_PROYECTIL_DIAGONAL:
                self.activar_escudo()
                return

        accion = self.modelo_ia.predecir(
            velocidad_proyectil=float(self.velocidad_proyectil),
            distancia=self.distancia_proyectil(),
            altura_proyectil=float(self.altura_proyectil),
            tipo_proyectil=int(self.tipo_proyectil),
            estado_jugador=int(self.estado_jugador())
        )

        if accion == ACCION_SALTAR:
            self.saltar()

        elif accion == ACCION_AGACHARSE:
            self.agacharse()

        elif accion == ACCION_ESCUDO:
            self.activar_escudo()

        elif accion == ACCION_NADA:
            if self.agachado:
                self.dejar_agacharse()

    # ==========================
    # COLISIONES
    # ==========================

    def revisar_colision(self):
        if not self.proyectil_activo:
            return

        if self.jugador.colliderect(self.proyectil):
            if self.escudo_activo:
                self.proyectil_activo = False
                self.puntaje += 1
            else:
                self.vidas -= 1
                self.proyectil_activo = False
                self.dejar_agacharse()

                if self.vidas <= 0:
                    self.reiniciar_partida()

    def reiniciar_partida(self):
        self.puntaje = 0
        self.vidas = 3
        self.proyectil_activo = False

        self.jugador.x = JUGADOR_X
        self.jugador.y = self.suelo_y - JUGADOR_ALTO
        self.jugador.height = JUGADOR_ALTO

        self.velocidad_y = 0
        self.en_suelo = True
        self.agachado = False

        self.escudo_activo = False
        self.escudo_timer = 0
        self.escudo_cooldown = 0

        self.mensaje = "Partida reiniciada."

    # ==========================
    # EVENTOS
    # ==========================

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False

                elif evento.key == pygame.K_SPACE and not self.modo_auto:
                    self.saltar()

                elif evento.key == pygame.K_DOWN and not self.modo_auto:
                    self.agacharse()

                elif evento.key == pygame.K_e and not self.modo_auto:
                    self.activar_escudo()

                elif evento.key == pygame.K_m:
                    self.modo_auto = False
                    self.mensaje = "Modo manual activado."

                elif evento.key == pygame.K_i:
                    if self.modelo_ia.entrenado:
                        self.modo_auto = True
                        self.mensaje = "Modo IA activado."
                    else:
                        self.mensaje = "Primero entrena la IA con la tecla T."

                elif evento.key == pygame.K_t:
                    ok, msg = self.modelo_ia.entrenar(self.memoria)
                    self.mensaje = msg
                    self.modo_auto = False

                elif evento.key == pygame.K_c:
                    ok, msg = self.memoria.exportar_csv()
                    self.mensaje = msg

                elif evento.key == pygame.K_r:
                    self.memoria.limpiar()
                    self.modelo_ia.reiniciar()
                    self.modo_auto = False
                    self.mensaje = "Datos e IA reiniciados."

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_DOWN and not self.modo_auto:
                    self.dejar_agacharse()

    # ==========================
    # DIBUJO
    # ==========================

    def dibujar_texto(self, texto, x, y, color=BLANCO, chica=False):
        fuente = self.fuente_chica if chica else self.fuente
        render = fuente.render(texto, True, color)
        self.pantalla.blit(render, (x, y))

    def dibujar(self):
        self.pantalla.fill((12, 14, 25))

        # Fondo con estrellas/cuadrícula
        for i in range(0, ANCHO_VENTANA, 80):
            pygame.draw.line(self.pantalla, (25, 30, 50), (i, 0), (i, ALTO_VENTANA), 1)

        for j in range(0, ALTO_VENTANA, 80):
            pygame.draw.line(self.pantalla, (25, 30, 50), (0, j), (ANCHO_VENTANA, j), 1)

        # Suelo futurista
        pygame.draw.rect(
            self.pantalla,
            (30, 34, 48),
            (0, self.suelo_y, ANCHO_VENTANA, ALTO_VENTANA - self.suelo_y)
        )

        pygame.draw.line(
            self.pantalla,
            (0, 255, 180),
            (0, self.suelo_y),
            (ANCHO_VENTANA, self.suelo_y),
            4
        )

        # Robot
        x, y = self.jugador.x, self.jugador.y
        w, h = self.jugador.width, self.jugador.height

        color_robot = (70, 160, 255)

        if self.agachado:
            color_robot = (80, 230, 130)

        if self.escudo_activo:
            color_robot = (255, 220, 80)

        # Cuerpo
        pygame.draw.rect(
            self.pantalla,
            color_robot,
            self.jugador,
            border_radius=8
        )

        # Cabeza
        cabeza = pygame.Rect(x + 4, y - 24, w - 8, 24)
        pygame.draw.rect(
            self.pantalla,
            (180, 210, 255),
            cabeza,
            border_radius=6
        )

        # Visor
        visor = pygame.Rect(x + 9, y - 15, w - 18, 7)
        pygame.draw.rect(
            self.pantalla,
            (10, 20, 40),
            visor,
            border_radius=4
        )

        # Piernas
        if not self.agachado:
            pygame.draw.rect(self.pantalla, (45, 100, 180), (x + 5, y + h, 10, 18), border_radius=4)
            pygame.draw.rect(self.pantalla, (45, 100, 180), (x + w - 15, y + h, 10, 18), border_radius=4)

        # Escudo
        if self.escudo_activo:
            pygame.draw.circle(
                self.pantalla,
                (255, 230, 90),
                self.jugador.center,
                60,
                4
            )
            pygame.draw.circle(
                self.pantalla,
                (255, 230, 90),
                self.jugador.center,
                72,
                1
            )

        # Proyectil con brillo
        if self.tipo_proyectil == TIPO_PROYECTIL_BAJO:
            color_proyectil = (255, 70, 70)
            tipo_txt = "Bajo"
        elif self.tipo_proyectil == TIPO_PROYECTIL_ALTO:
            color_proyectil = (180, 90, 255)
            tipo_txt = "Alto"
        else:
            color_proyectil = (255, 210, 70)
            tipo_txt = "Diagonal"

        pygame.draw.circle(
            self.pantalla,
            color_proyectil,
            self.proyectil.center,
            20
        )

        pygame.draw.circle(
            self.pantalla,
            (255, 255, 255),
            self.proyectil.center,
            7
        )

        pygame.draw.circle(
            self.pantalla,
            color_proyectil,
            self.proyectil.center,
            30,
            2
        )

        # Panel HUD izquierdo
        pygame.draw.rect(
            self.pantalla,
            (18, 22, 35),
            (15, 15, 360, 230),
            border_radius=12
        )

        pygame.draw.rect(
            self.pantalla,
            (0, 255, 180),
            (15, 15, 360, 230),
            2,
            border_radius=12
        )

        modo = "IA" if self.modo_auto else "Manual"

        self.dibujar_texto(f"Modo: {modo}", 35, 35)
        self.dibujar_texto(f"Puntaje: {self.puntaje}", 35, 65)
        self.dibujar_texto(f"Vidas: {self.vidas}", 35, 95)
        self.dibujar_texto(f"Datos: {self.memoria.cantidad()}", 35, 125)
        self.dibujar_texto(
            f"IA entrenada: {'Sí' if self.modelo_ia.entrenado else 'No'}",
            35,
            155
        )
        self.dibujar_texto(f"Proyectil: {tipo_txt}", 35, 190, (255, 220, 90))

        # Mensaje inferior
        pygame.draw.rect(
            self.pantalla,
            (18, 22, 35),
            (15, 260, 700, 42),
            border_radius=10
        )

        self.dibujar_texto(
            f"Mensaje: {self.mensaje}",
            30,
            270,
            BLANCO,
            chica=True
        )

        # Panel controles
        pygame.draw.rect(
            self.pantalla,
            (18, 22, 35),
            (ANCHO_VENTANA - 330, 15, 310, 310),
            border_radius=12
        )

        pygame.draw.rect(
            self.pantalla,
            (180, 90, 255),
            (ANCHO_VENTANA - 330, 15, 310, 310),
            2,
            border_radius=12
        )

        controles = [
            "Controles:",
            "ESPACIO = Saltar",
            "FLECHA ABAJO = Agacharse",
            "E = Escudo",
            "T = Entrenar IA",
            "I = Modo IA",
            "M = Modo Manual",
            "C = Exportar CSV",
            "R = Reiniciar datos/modelo",
            "ESC = Salir"
        ]

        y_controles = 35

        for linea in controles:
            self.dibujar_texto(
                linea,
                ANCHO_VENTANA - 305,
                y_controles,
                BLANCO,
                chica=True
            )
            y_controles += 26

        if self.modelo_ia.ultima_precision is not None:
            self.dibujar_texto(
                f"Precisión IA: {self.modelo_ia.ultima_precision:.3f}",
                ANCHO_VENTANA - 305,
                y_controles + 10,
                (80, 255, 140),
                chica=True
            )

        pygame.display.flip()
    # ==========================
    # LOOP PRINCIPAL
    # ==========================

    def ejecutar(self):
        while self.corriendo:
            self.manejar_eventos()

            if self.modo_auto:
                self.aplicar_ia()
            else:
                self.registrar_datos_manual()

            self.actualizar_jugador()
            self.actualizar_proyectil()
            self.revisar_colision()
            self.dibujar()

            self.frames += 1
            self.reloj.tick(FPS)

        pygame.quit()


def main():
    juego = JuegoEvasionIA()
    juego.ejecutar()


if __name__ == "__main__":
    main()