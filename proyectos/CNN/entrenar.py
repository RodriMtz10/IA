import os
import re
import cv2
import numpy as np

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    LeakyReLU
)
from tensorflow.keras.utils import to_categorical


# =====================================
# CONFIGURACIÓN
# =====================================

IMG_SIZE = 64

CLASES = [
    "ranas",
    "pajaros",
    "ballenas",
    "changos",
    "aranas"
]

# =====================================
# CARGA DEL DATASET
# =====================================

dataset_path = os.path.join(os.getcwd(), "dataset")

imagenes = []
etiquetas = []

print("\nCargando imágenes...")
print("-" * 50)

for indice, clase in enumerate(CLASES):

    carpeta = os.path.join(dataset_path, clase)

    if not os.path.exists(carpeta):
        print(f"No existe la carpeta: {carpeta}")
        continue

    contador = 0

    for archivo in os.listdir(carpeta):

        if re.search(r"\.(jpg|jpeg|png|bmp)$", archivo, re.IGNORECASE):

            ruta = os.path.join(carpeta, archivo)

            imagen = cv2.imread(ruta)

            if imagen is None:
                continue

            imagen = cv2.resize(
                imagen,
                (IMG_SIZE, IMG_SIZE)
            )

            imagenes.append(imagen)
            etiquetas.append(indice)

            contador += 1

    print(f"{clase}: {contador} imágenes")

print("-" * 50)
print(f"Total cargadas: {len(imagenes)}")

print("\nDistribución de etiquetas:")
print(np.unique(etiquetas, return_counts=True))

# =====================================
# PREPARACIÓN DE DATOS
# =====================================

X = np.array(imagenes, dtype=np.float32)
X = X / 255.0

y = np.array(etiquetas)

num_clases = len(CLASES)

y = to_categorical(y, num_clases)

train_X, valid_X, train_y, valid_y = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=np.argmax(y, axis=1)
)

print("\nEntrenamiento:", train_X.shape)
print("Validación:", valid_X.shape)

# =====================================
# MODELO CNN
# =====================================

animal_model = Sequential(name="ClasificadorFaunaCNN")

animal_model.add(
    Conv2D(
        32,
        (3, 3),
        padding="same",
        input_shape=(64, 64, 3)
    )
)

animal_model.add(
    LeakyReLU(negative_slope=0.1)
)

animal_model.add(
    MaxPooling2D(pool_size=(2, 2))
)

animal_model.add(
    Dropout(0.25)
)

# -------------------------------------

animal_model.add(
    Conv2D(
        64,
        (3, 3),
        padding="same"
    )
)

animal_model.add(
    LeakyReLU(negative_slope=0.1)
)

animal_model.add(
    MaxPooling2D(pool_size=(2, 2))
)

animal_model.add(
    Dropout(0.25)
)

# -------------------------------------

animal_model.add(
    Conv2D(
        128,
        (3, 3),
        padding="same"
    )
)

animal_model.add(
    LeakyReLU(negative_slope=0.1)
)

animal_model.add(
    MaxPooling2D(pool_size=(2, 2))
)

animal_model.add(
    Dropout(0.25)
)

# -------------------------------------

animal_model.add(Flatten())

animal_model.add(Dense(256))

animal_model.add(
    LeakyReLU(negative_slope=0.1)
)

animal_model.add(
    Dropout(0.5)
)

animal_model.add(
    Dense(
        num_clases,
        activation="softmax"
    )
)

# =====================================
# COMPILACIÓN
# =====================================

animal_model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

animal_model.summary()

# =====================================
# ENTRENAMIENTO
# =====================================

historial = animal_model.fit(
    train_X,
    train_y,
    epochs=10,
    batch_size=32,
    validation_data=(valid_X, valid_y),
    verbose=1
)

# =====================================
# GUARDAR MODELO
# =====================================

animal_model.save("modelo_fauna.keras")

print("\nModelo guardado correctamente")
print("Archivo: modelo_fauna.keras")