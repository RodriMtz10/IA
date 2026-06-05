import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

from lector_rss import obtener_noticias, guardar_noticias_csv
from analizador import analizar_noticias


noticias_global = []


def cargar_noticias():
    global noticias_global

    tabla.delete(*tabla.get_children())
    estado.config(text="Obteniendo noticias...")

    try:
        noticias = obtener_noticias()
        noticias_global = analizar_noticias(noticias)
        guardar_noticias_csv(noticias_global)

        for i, noticia in enumerate(noticias_global, start=1):
            tabla.insert(
                "",
                "end",
                values=(
                    i,
                    noticia["fuente"],
                    noticia["categoria"],
                    noticia["sentimiento"],
                    noticia["titulo"],
                    noticia["fecha"],
                )
            )

        estado.config(text=f"Noticias cargadas: {len(noticias_global)} | Guardadas en noticias.csv")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar las noticias:\n{e}")
        estado.config(text="Error al cargar noticias")


def abrir_enlace():
    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona una noticia primero.")
        return

    item = tabla.item(seleccion[0])
    numero = int(item["values"][0]) - 1

    enlace = noticias_global[numero]["enlace"]
    webbrowser.open(enlace)


def filtrar():
    texto = entrada_busqueda.get().lower()

    tabla.delete(*tabla.get_children())

    for i, noticia in enumerate(noticias_global, start=1):
        contenido = f"{noticia['titulo']} {noticia['resumen']} {noticia['categoria']}".lower()

        if texto in contenido:
            tabla.insert(
                "",
                "end",
                values=(
                    i,
                    noticia["fuente"],
                    noticia["categoria"],
                    noticia["sentimiento"],
                    noticia["titulo"],
                    noticia["fecha"],
                )
            )


ventana = tk.Tk()
ventana.title("Analizador de Noticias IA")
ventana.geometry("1150x650")
ventana.configure(bg="#101820")

titulo = tk.Label(
    ventana,
    text="Analizador de Noticias IA",
    font=("Arial", 22, "bold"),
    bg="#101820",
    fg="#00E5FF"
)
titulo.pack(pady=15)

frame_botones = tk.Frame(ventana, bg="#101820")
frame_botones.pack(pady=5)

btn_cargar = tk.Button(
    frame_botones,
    text="Cargar noticias",
    command=cargar_noticias,
    width=18,
    bg="#00C853",
    fg="white",
    font=("Arial", 10, "bold")
)
btn_cargar.grid(row=0, column=0, padx=5)

btn_abrir = tk.Button(
    frame_botones,
    text="Abrir enlace",
    command=abrir_enlace,
    width=18,
    bg="#2962FF",
    fg="white",
    font=("Arial", 10, "bold")
)
btn_abrir.grid(row=0, column=1, padx=5)

entrada_busqueda = tk.Entry(frame_botones, width=40)
entrada_busqueda.grid(row=0, column=2, padx=10)

btn_buscar = tk.Button(
    frame_botones,
    text="Buscar",
    command=filtrar,
    width=12,
    bg="#FFAB00",
    fg="black",
    font=("Arial", 10, "bold")
)
btn_buscar.grid(row=0, column=3, padx=5)

columnas = ("#", "Fuente", "Categoría", "Sentimiento", "Título", "Fecha")

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=20
)

tabla.heading("#", text="#")
tabla.heading("Fuente", text="Fuente")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Sentimiento", text="Sentimiento")
tabla.heading("Título", text="Título")
tabla.heading("Fecha", text="Fecha")

tabla.column("#", width=40)
tabla.column("Fuente", width=120)
tabla.column("Categoría", width=120)
tabla.column("Sentimiento", width=120)
tabla.column("Título", width=520)
tabla.column("Fecha", width=220)

tabla.pack(padx=20, pady=15, fill="both", expand=True)

estado = tk.Label(
    ventana,
    text="Presiona 'Cargar noticias' para comenzar.",
    bg="#101820",
    fg="white",
    font=("Arial", 11)
)
estado.pack(pady=5)

ventana.mainloop()