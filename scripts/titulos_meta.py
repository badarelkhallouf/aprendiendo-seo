import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

# URL del sitemap
sitemap_url = "https://monverdjardins.com/sitemap.xml"

# Obtener el sitemap
response = requests.get(sitemap_url)
urls = []

if response.status_code == 200:
    # Parsear el sitemap XML
    root = ET.fromstring(response.content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    for url in root.findall('ns:url/ns:loc', namespace):
        urls.append(url.text)
else:
    print(f"No se pudo acceder al sitemap: {sitemap_url}")

# Crear archivo de resultados con fecha y hora
fecha = datetime.now().strftime("%Y_%m_%d_%H_%M")
archivo_salida = f"resultados_titulos_meta_{fecha}.txt"

with open(archivo_salida, "w", encoding="utf-8") as f:
    for url in urls:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.title.string if soup.title else "Sin título"
            meta = soup.find("meta", attrs={"name": "description"})
            meta_desc = meta["content"] if meta and meta.get("content") else "Sin meta descripción"
            f.write(f"{url}\nTítulo: {title}\nMeta descripción: {meta_desc}\n\n")
        except Exception as e:
            f.write(f"Error con {url}: {e}\n")

print(f"Resultados guardados en: {archivo_salida}")
