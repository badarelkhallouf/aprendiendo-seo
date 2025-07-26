import requests
from bs4 import BeautifulSoup

urls = [
    "https://monverdjardins.com",
    "https://monverdjardins.com/servicios",
    "https://monverdjardins.com/contacto"
]

for url in urls:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else "Sin título"
        meta = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta["content"] if meta and meta.get("content") else "Sin meta descripción"
        print(f"{url}\nTítulo: {title}\nMeta descripción: {meta_desc}\n")
    except Exception as e:
        print(f"Error con {url}: {e}")
