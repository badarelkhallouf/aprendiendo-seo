import requests

urls = [
    "https://monverdjardins.com/robots.txt"
]

for url in urls:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if "Disallow" in r.text:
                print(f"{url} encontrado y contiene reglas de Disallow:\n{r.text}")
            else:
                print(f"{url} encontrado, sin restricciones de indexación:\n{r.text}")
        else:
            print(f"{url} devolvió código {r.status_code}")
    except Exception as e:
        print(f"Error con {url}: {e}")
