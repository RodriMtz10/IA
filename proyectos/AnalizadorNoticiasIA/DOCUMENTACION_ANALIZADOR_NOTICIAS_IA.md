# Documentación del Proyecto: Analizador de Noticias IA

## 1. Descripción general

El proyecto **Analizador de Noticias IA** es una aplicación desarrollada en Python que permite obtener noticias en tiempo real desde diferentes fuentes RSS, analizar su contenido y clasificarlas automáticamente.

La aplicación cuenta con una interfaz gráfica que facilita la visualización y búsqueda de noticias.

---

## 2. Objetivo

El objetivo del proyecto es implementar una aplicación capaz de:

* Obtener noticias desde Internet.
* Analizar información textual.
* Clasificar noticias por categoría.
* Determinar el sentimiento de cada noticia.
* Exportar los resultados a un archivo CSV.
* Mostrar la información mediante una interfaz gráfica.

---

## 3. Tecnologías utilizadas

* Python
* Tkinter
* Feedparser
* Pandas
* TextBlob

---

## 4. Estructura del proyecto

```text
AnalizadorNoticiasIA/
│
├── config.py
├── lector_rss.py
├── analizador.py
├── main.py
├── interfaz.py
├── requirements.txt
├── noticias.csv
├── README.md
└── DOCUMENTACION_ANALIZADOR_NOTICIAS_IA.md
```

---

## 5. Descripción de archivos

### config.py

Contiene la configuración principal del proyecto.

Define:

* Fuentes RSS.
* Nombre del archivo CSV.
* Palabras clave utilizadas para clasificar noticias.

---

### lector_rss.py

Se encarga de conectarse a diferentes fuentes RSS y obtener información de las noticias.

Para cada noticia recupera:

* Título.
* Resumen.
* Fecha.
* Fuente.
* Enlace.

Posteriormente almacena la información en un archivo CSV.

---

### analizador.py

Contiene las funciones encargadas del análisis de texto.

Sus principales tareas son:

* Clasificar noticias mediante palabras clave.
* Analizar el sentimiento del texto.
* Generar una categoría para cada noticia.

Los posibles sentimientos son:

* Positivo.
* Neutral.
* Negativo.

---

### main.py

Versión en consola del programa.

Permite:

1. Descargar noticias.
2. Analizarlas.
3. Mostrar los resultados por pantalla.
4. Guardar los resultados en un archivo CSV.

---

### interfaz.py

Implementa la interfaz gráfica del sistema.

Permite:

* Cargar noticias.
* Visualizar noticias en una tabla.
* Buscar noticias por palabras clave.
* Abrir enlaces directamente en el navegador.
* Consultar categoría y sentimiento de cada noticia.

---

## 6. Funcionamiento general

### Paso 1

El programa obtiene noticias desde distintas fuentes RSS.

Ejemplos:

* BBC Mundo.
* El País.
* CNN Español.

### Paso 2

Cada noticia es procesada para extraer:

* Título.
* Resumen.
* Fecha.
* Fuente.
* Enlace.

### Paso 3

El sistema analiza el contenido textual.

Se determina:

* Categoría.
* Sentimiento.

### Paso 4

La información es almacenada en un archivo:

```text
noticias.csv
```

### Paso 5

Los resultados se muestran mediante la interfaz gráfica.

---

## 7. Clasificación de noticias

La clasificación se realiza mediante palabras clave.

Algunas categorías utilizadas son:

* Inteligencia Artificial.
* Tecnología.
* Educación.
* Salud.
* Economía.
* Seguridad.
* Ciencia.

Si una noticia no coincide con ninguna categoría, se clasifica como:

```text
General
```

---

## 8. Análisis de sentimiento

Se utiliza la librería:

```python
TextBlob
```

para calcular la polaridad del texto.

Los resultados posibles son:

### Positivo

Cuando la polaridad es mayor que 0.1.

### Negativo

Cuando la polaridad es menor que -0.1.

### Neutral

Cuando la polaridad se encuentra entre ambos valores.

---

## 9. Interfaz gráfica

La interfaz permite:

### Cargar noticias

Obtiene noticias desde Internet y las muestra en una tabla.

### Buscar noticias

Filtra noticias utilizando palabras clave.

### Abrir enlaces

Permite acceder directamente a la noticia original en el navegador.

### Visualizar información

La tabla muestra:

* Fuente.
* Categoría.
* Sentimiento.
* Título.
* Fecha.

---

## 10. Exportación de datos

Los resultados obtenidos son almacenados automáticamente en:

```text
noticias.csv
```

Este archivo puede abrirse con:

* Excel.
* Google Sheets.
* LibreOffice Calc.

---

## 11. Instalación

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 12. Ejecución

### Modo consola

```bash
python main.py
```

### Modo interfaz gráfica

```bash
python interfaz.py
```

---

## 13. Aplicaciones

Este tipo de sistemas puede utilizarse para:

* Monitoreo de noticias.
* Clasificación automática de información.
* Análisis de texto.
* Sistemas de recomendación.
* Procesamiento de lenguaje natural.
* Inteligencia artificial aplicada a información.

---

## 14. Posibles mejoras futuras

* Integración con bases de datos.
* Uso de modelos de lenguaje más avanzados.
* Generación de gráficas estadísticas.
* Nube de palabras.
* Filtrado avanzado.
* Clasificación mediante Machine Learning.
* Traducción automática.
* Sistema de alertas.

---

## 15. Conclusión

El proyecto Analizador de Noticias IA demuestra cómo combinar técnicas de procesamiento de lenguaje natural, obtención de información desde Internet y análisis automático de texto para generar una herramienta capaz de clasificar y organizar noticias de manera sencilla e intuitiva.

La implementación integra tanto una versión de consola como una interfaz gráfica, permitiendo una interacción más cómoda con el usuario y mostrando una aplicación práctica de la Inteligencia Artificial en el tratamiento de información.
