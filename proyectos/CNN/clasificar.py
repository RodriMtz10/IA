import os
import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
from PIL import Image, ImageTk

from tensorflow.keras.models import load_model


# ==========================
# CONFIGURACIÓN
# ==========================

IMG_SIZE = 64

CLASES = [
    "ranas",
    "pajaros",
    "ballenas",
    "changos",
    "aranas"
]

RUTA_MODELO = "modelo_fauna.keras"


# ==========================
# CARGAR MODELO
# ==========================

if not os.path.exists(RUTA_MODELO):
    raise FileNotFoundError(
        "No se encontró modelo_fauna.keras. "
        "Primero ejecuta: python entrenar.py"
    )

print("Cargando modelo desde:", os.path.abspath(RUTA_MODELO))

modelo = load_model(RUTA_MODELO)


# ==========================
# CLASIFICAR IMAGEN
# ==========================

def clasificar_imagen():
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp")
        ]
    )

    if not ruta:
        return

    try:
        # Abrir imagen con Pillow
        imagen_original = Image.open(ruta).convert("RGB")

        # Mostrar imagen en la ventana
        imagen_mostrar = imagen_original.copy()
        imagen_mostrar.thumbnail((350, 350))

        foto = ImageTk.PhotoImage(imagen_mostrar)

        lbl_imagen.config(image=foto)
        lbl_imagen.image = foto

        # Preparar imagen para el modelo
        imagen_red = imagen_original.resize((IMG_SIZE, IMG_SIZE))
        imagen_red = np.array(imagen_red)

        # IMPORTANTE:
        # El entrenamiento usó OpenCV, y OpenCV usa BGR.
        # Pillow usa RGB, por eso convertimos RGB a BGR.
        imagen_red = imagen_red[:, :, ::-1]

        imagen_red = imagen_red.astype("float32") / 255.0
        imagen_red = np.expand_dims(imagen_red, axis=0)

        predicciones = modelo.predict(imagen_red, verbose=0)

        indice = np.argmax(predicciones)
        animal = CLASES[indice]
        confianza = np.max(predicciones) * 100

        print("\nImagen:", ruta)
        print("Predicciones:", predicciones)
        print("Clase detectada:", animal)
        print("Confianza:", confianza)

        resultado.config(
            text=(
                f"Animal detectado: {animal}\n"
                f"Confianza: {confianza:.2f}%"
            )
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Ocurrió un problema:\n\n{e}"
        )


# ==========================
# INTERFAZ
# ==========================

ventana = tk.Tk()
ventana.title("Clasificador de Fauna CNN")
ventana.geometry("750x750")

titulo = tk.Label(
    ventana,
    text="Clasificador de Fauna CNN",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=20)

boton = tk.Button(
    ventana,
    text="Seleccionar Imagen",
    command=clasificar_imagen,
    width=25,
    height=2
)
boton.pack(pady=10)

lbl_imagen = tk.Label(ventana)
lbl_imagen.pack(pady=20)

resultado = tk.Label(
    ventana,
    text="Seleccione una imagen",
    font=("Arial", 16)
)
resultado.pack(pady=20)

ventana.mainloop()