## 📚 **Book Scraper con Scrapy & MongoDB**

Este proyecto es un pequeño **web scraper** construido con 🕷️ **Scrapy** y 💾 **MongoDB**, creado con fines **educativos y de práctica**.  
Forma parte de mi proceso de aprendizaje de Scrapy y fue desarrollado siguiendo el excelente tutorial de Real Python 👉  
🔗 [Web Scraping With Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#debug-and-test-your-scrapy-web-scraper)

---

### 🚀 **Descripción**

El objetivo de este proyecto fue **extraer información de libros** desde el sitio [Books to Scrape](https://books.toscrape.com/), una página diseñada especialmente para practicar web scraping.

Cada libro contiene información como:
- 🏷️ Título  
- 💰 Precio  
- 🔗 URL del producto  

Los datos extraídos se almacenan en una base de datos **MongoDB**, aplicando un pequeño **pipeline** para evitar duplicados y manejar la conexión de forma eficiente.

---

### ⚙️ **Tecnologías utilizadas**

- 🐍 **Python 3.x**
- 🕷️ **Scrapy**
- 🍃 **MongoDB**
- 🧩 **PyMongo**
- 🧪 **unittest** (para las pruebas del spider)

---

### 📦 **Estructura del proyecto**

```text
books/
│
├── books/
│ ├── init.py
│ ├── items.py
│ ├── pipelines.py
│ ├── settings.py
│ └── spiders/
│ └── book_spider.py
│
└── tests/
└── test_spider.py
```

---

### 🧠 **Cómo funciona**

1. **El spider (`book_spider.py`)** inicia en la URL principal del sitio.  
2. **Extrae** los datos de cada libro (título, precio, URL).  
3. Si hay una página siguiente ➡️, Scrapy crea una nueva solicitud (`Request`) y se llama recursivamente al método `parse()`.  
4. **El pipeline (`MongoPipeline`)** procesa cada item:
   - Calcula un ID único usando `hashlib` (basado en la URL).  
   - Inserta los datos en MongoDB si aún no existen.  
5. Al finalizar, se cierra la conexión con la base de datos.

---

### 🧩 **Ejecución**

1. Asegúrate de tener MongoDB en ejecución:
   ```bash 
   mongod
   ```
2. Ejecuta el spider:
   ```bash 
   scrapy crawl book
   ```
3. Verifica los datos en MongoDB:
   ```bash 
   mongo
   use books_db
   db.books.find().pretty()
   ```

---

### 🧪 **Pruebas**

El proyecto incluye **pruebas unitarias** con un HTML de ejemplo para validar que el método `parse()`:
- Extrae correctamente los libros 🧾  
- Detecta el enlace a la siguiente página 🔄  

Ejecuta las pruebas con:
```bash
pytest
```

--

### 💡 **Conclusión**

Este proyecto fue una excelente oportunidad para entender cómo funciona **Scrapy** en conjunto con **MongoDB**, aplicando conceptos como:
- Pipelines para procesar y almacenar datos.
- Manejo de errores con `errback`.
- Uso eficiente de `yield` para scraping asíncrono.
- Testing de spiders con HTML simulado.

📚 Si estás comenzando con Scrapy, te recomiendo seguir el tutorial original de **Real Python**, que explica cada paso con claridad y ejemplos prácticos:  
👉 [Web Scraping with Scrapy and MongoDB - Real Python](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#debug-and-test-your-scrapy-web-scraper)

🚀 Próximo paso: crear un **scraper propio**, aplicando todo lo aprendido y explorando nuevas formas de almacenar, validar y analizar los datos obtenidos.
