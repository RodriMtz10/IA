import feedparser
import pandas as pd

from config import FUENTES_RSS, ARCHIVO_CSV


def obtener_noticias():
    noticias = []

    for fuente, url in FUENTES_RSS.items():
        feed = feedparser.parse(url)

        for entrada in feed.entries[:10]:
            titulo = entrada.get("title", "Sin título")
            resumen = entrada.get("summary", "Sin resumen")
            enlace = entrada.get("link", "Sin enlace")
            fecha = entrada.get("published", "Sin fecha")

            noticias.append({
                "fuente": fuente,
                "titulo": titulo,
                "resumen": resumen,
                "fecha": fecha,
                "enlace": enlace
            })

    return noticias


def guardar_noticias_csv(noticias):
    df = pd.DataFrame(noticias)
    df.to_csv(ARCHIVO_CSV, index=False, encoding="utf-8-sig")
    return ARCHIVO_CSV