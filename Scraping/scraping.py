"""Obtiene html y titulo de la pagina consultada
"""


import requests
from bs4 import BeautifulSoup


url = "http://httpbin.org"

try:
    
    response = requests.get(url)
    
    
    print("Código de estado:", response.status_code)
    
    
    if response.status_code == 200:
       
        print("\nContenido HTML de la página:")
        print(response.text)
        
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        title = soup.title.string if soup.title else "No se encontró un título"
        print("\nTítulo de la página:", title)
    else:
        print("Error al acceder a la página. Código de estado:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Ocurrió un error al realizar la solicitud:", e)
