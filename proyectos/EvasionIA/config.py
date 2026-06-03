# ==============================
# CONFIGURACIÓN GENERAL DEL JUEGO
# ==============================

ANCHO_VENTANA = 1080
ALTO_VENTANA = 720
FPS = 45

TITULO_JUEGO = "Evasion IA - Robot vs Proyectiles"


# ==============================
# COLORES
# ==============================

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (180, 180, 180)
GRIS_OSCURO = (35, 35, 35)

AZUL = (80, 160, 255)
VERDE = (80, 220, 120)
ROJO = (255, 90, 90)
AMARILLO = (255, 220, 100)
MORADO = (170, 100, 255)


# ==============================
# JUGADOR
# ==============================

JUGADOR_X = 90
JUGADOR_ANCHO = 42
JUGADOR_ALTO = 64
JUGADOR_ALTO_AGACHADO = 32

GRAVEDAD = 1.1
FUERZA_SALTO = 18

DURACION_ESCUDO = 18
ENFRIAMIENTO_ESCUDO = 45


# ==============================
# PROYECTILES
# ==============================

PROYECTIL_ANCHO = 22
PROYECTIL_ALTURA = 22

VELOCIDAD_PROYECTIL_MIN = 7
VELOCIDAD_PROYECTIL_MAX = 14

# Tipos de proyectil
TIPO_PROYECTIL_BAJO = 0
TIPO_PROYECTIL_ALTO = 1
TIPO_PROYECTIL_DIAGONAL = 2


# ==============================
# ACCIONES DEL MODELO
# ==============================

ACCION_NADA = 0
ACCION_SALTAR = 1
ACCION_AGACHARSE = 2
ACCION_ESCUDO = 3

NOMBRES_ACCIONES = {
    ACCION_NADA: "Nada",
    ACCION_SALTAR: "Saltar",
    ACCION_AGACHARSE: "Agacharse",
    ACCION_ESCUDO: "Escudo"
}


# ==============================
# IA / ENTRENAMIENTO
# ==============================

MIN_DATOS_ENTRENAMIENTO = 120

ARCHIVO_CSV = "datos_evasion.csv"