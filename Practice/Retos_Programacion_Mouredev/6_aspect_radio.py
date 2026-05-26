'''
 /*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
 '''

import math
import requests
from PIL import Image
from io import BytesIO


def obtener_tamano_imagen_url(url):
    try:
        # 1. Realizar la solicitud GET a la URL
        response = requests.get(url)
        response.raise_for_status() # Verifica que la solicitud fue exitosa

        # 2. Leer la imagen desde los bytes de la respuesta
        img = Image.open(BytesIO(response.content))
        img.show()

        # 3. Obtener el tamaño (ancho, alto)
        ancho, alto = img.size
       

        
        print(f"URL: {url}")
        print(f"Dimensiones: {ancho}x{alto} píxeles")
        

        factor = math.gcd(ancho,alto)
        print(f"Aspect Ratio: {int(ancho/factor)}:{int(alto/factor)} ")
        
        return ancho, alto
        # Calculo de Relacion Aspecto

    except Exception as e:
        print(f"Error al obtener la imagen: {e}")
        return None

# Ejemplo de uso

url = "https://preview.redd.it/purple-sunrise-1920x1080-v0-vo9vm1fcqrp71.jpg?auto=webp&s=929f29167c61cdc698e4691bd0de2bbff2e16288"
obtener_tamano_imagen_url(url)