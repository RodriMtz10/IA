from collections import Counter
from typing import Optional, Tuple

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from config import (
    ACCION_NADA,
    ACCION_SALTAR,
    ACCION_AGACHARSE,
    ACCION_ESCUDO,
    MIN_DATOS_ENTRENAMIENTO,
    NOMBRES_ACCIONES
)


class ModeloIA:
    def __init__(self):
        self.modelo: Optional[MLPClassifier] = None
        self.scaler: Optional[StandardScaler] = None
        self.entrenado = False
        self.clase_unica: Optional[int] = None
        self.ultima_precision: Optional[float] = None

    def reiniciar(self):
        self.modelo = None
        self.scaler = None
        self.entrenado = False
        self.clase_unica = None
        self.ultima_precision = None

    def entrenar(self, memoria) -> Tuple[bool, str]:
        cantidad = memoria.cantidad()

        if cantidad < MIN_DATOS_ENTRENAMIENTO:
            return (
                False,
                f"Faltan datos. Necesitas mínimo {MIN_DATOS_ENTRENAMIENTO}, tienes {cantidad}."
            )

        x, y = memoria.obtener_x_y()

        conteo = Counter(y)

        if len(conteo) == 1:
            self.reiniciar()
            self.clase_unica = y[0]
            self.entrenado = True

            accion = NOMBRES_ACCIONES.get(y[0], "Desconocida")

            return (
                True,
                f"Modelo simple entrenado. Solo se detectó una acción: {accion}."
            )

        try:
            x_train, x_test, y_train, y_test = train_test_split(
                x,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y
            )
        except ValueError:
            x_train, x_test, y_train, y_test = train_test_split(
                x,
                y,
                test_size=0.2,
                random_state=42
            )

        scaler = StandardScaler()

        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

        modelo = MLPClassifier(
            hidden_layer_sizes=(128, 64, 32),
            activation="relu",
            solver="adam",
            max_iter=1500,
            random_state=42
        )

        modelo.fit(x_train, y_train)

        precision = modelo.score(x_test, y_test)

        self.modelo = modelo
        self.scaler = scaler
        self.entrenado = True
        self.clase_unica = None
        self.ultima_precision = precision

        resumen = dict(conteo)

        return (
            True,
            f"IA entrenada correctamente. Precisión: {precision:.3f} | Datos: {resumen}"
        )

    def predecir(
        self,
        velocidad_proyectil: float,
        distancia: float,
        altura_proyectil: float,
        tipo_proyectil: int,
        estado_jugador: int
    ) -> int:
        if not self.entrenado:
            return ACCION_NADA

        if self.clase_unica is not None:
            return self.clase_unica

        if self.modelo is None or self.scaler is None:
            return ACCION_NADA

        entrada = [[
            velocidad_proyectil,
            distancia,
            altura_proyectil,
            tipo_proyectil,
            estado_jugador
        ]]

        entrada_escalada = self.scaler.transform(entrada)

        accion = self.modelo.predict(entrada_escalada)[0]

        return int(accion)

    def predecir_probabilidades(
        self,
        velocidad_proyectil: float,
        distancia: float,
        altura_proyectil: float,
        tipo_proyectil: int,
        estado_jugador: int
    ):
        if not self.entrenado:
            return None

        if self.modelo is None or self.scaler is None:
            return None

        if not hasattr(self.modelo, "predict_proba"):
            return None

        entrada = [[
            velocidad_proyectil,
            distancia,
            altura_proyectil,
            tipo_proyectil,
            estado_jugador
        ]]

        entrada_escalada = self.scaler.transform(entrada)

        probabilidades = self.modelo.predict_proba(entrada_escalada)[0]
        clases = self.modelo.classes_

        resultado = {}

        for clase, probabilidad in zip(clases, probabilidades):
            resultado[int(clase)] = float(probabilidad)

        return resultado

    def nombre_accion(self, accion: int) -> str:
        return NOMBRES_ACCIONES.get(accion, "Desconocida")