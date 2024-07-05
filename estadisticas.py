import json
import math
import globales 


def calcular_estadisticas():
    productos = globales.leer_archivo_json('ventas.json')
    if not productos:
        print("no hay datos de ventas disponibles.")
        return
    
    productos = [producto['ventas'] for producto in productos]

    

    