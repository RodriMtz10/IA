from textblob import TextBlob

from config import PALABRAS_CLAVE


def clasificar_categoria(texto):
    texto = texto.lower()

    for palabra in PALABRAS_CLAVE:
        if palabra.lower() in texto:
            return palabra.capitalize()

    return "General"


def analizar_sentimiento(texto):
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    if polaridad > 0.1:
        return "Positiva"

    if polaridad < -0.1:
        return "Negativa"

    return "Neutral"


def analizar_noticias(noticias):
    noticias_analizadas = []

    for noticia in noticias:
        texto_completo = f"{noticia['titulo']} {noticia['resumen']}"

        categoria = clasificar_categoria(texto_completo)
        sentimiento = analizar_sentimiento(texto_completo)

        noticia["categoria"] = categoria
        noticia["sentimiento"] = sentimiento

        noticias_analizadas.append(noticia)

    return noticias_analizadas