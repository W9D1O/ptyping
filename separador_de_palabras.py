import os
import requests


def es_derecha(p: str) -> bool:
    car_der = "67890'¿yuiop´+hjklñ{\\}nm,.-_^&*()\"¡YUIOP¨*HJKLÑ[]NM;:_.óúíü"
    cd:int = 0
    ci:int = 0

    for i in range(len(p)):
        for j in range(len(car_der)):
            if p[i] == car_der[j]:
                cd += 1
    ci = len(p) - cd
    return cd > ci


def separar(path):

    der:list[str] = []
    izq:list[str] = []
    file = open(path,"r",encoding="utf-8")

    for i in file:
        if es_derecha(i):
            der.append(i)

        else:
            izq.append(i)

    if der:
        with open("der.txt","w",encoding="utf-8") as t1:
            for i in der:
                t1.write(i)
            t1.close()
    if izq:
        with open("izq.txt","w",encoding="utf-8") as t2:
            for i in izq:
                t2.write(i)
            t2.close()
    file.close()
    

def generar_txt():
    file_path = "0_palabras_todas.txt" # por si llego a cambiar la ubicacion del archivo
    file_name = "0_palabras_todas.txt"
    url = "https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/refs/heads/master/0_palabras_todas.txt"
    if os.path.exists(file_path):
        if not (os.path.exists("der.txt") and os.path.exists("izq.txt")):
            separar(file_path)
    else:
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            # Open the local file in binary write mode ('wb')
            with open(file_name, 'wb') as f:
                # Iterate over the response content in chunks to handle large files efficiently
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive new chunks
                        f.write(chunk)
            separar(file_path)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            exit()
