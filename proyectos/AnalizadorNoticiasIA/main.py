from lector_rss import obtener_noticias, guardar_noticias_csv
from analizador import analizar_noticias


def mostrar_noticias(noticias):
    print("\n===== ANALIZADOR DE NOTICIAS IA =====\n")

    for i, noticia in enumerate(noticias, start=1):
        print(f"{i}. {noticia['titulo']}")
        print(f"   Fuente: {noticia['fuente']}")
        print(f"   Fecha: {noticia['fecha']}")
        print(f"   Categoría: {noticia['categoria']}")
        print(f"   Sentimiento: {noticia['sentimiento']}")
        print(f"   Enlace: {noticia['enlace']}")
        print("-" * 80)


def main():
    print("Obteniendo noticias RSS...")

    noticias = obtener_noticias()

    if not noticias:
        print("No se encontraron noticias.")
        return

    noticias_analizadas = analizar_noticias(noticias)

    archivo = guardar_noticias_csv(noticias_analizadas)

    mostrar_noticias(noticias_analizadas)

    print(f"\nNoticias guardadas en: {archivo}")


if __name__ == "__main__":
    main()