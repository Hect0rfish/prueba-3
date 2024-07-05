import json
import random
import globales 


productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]


def generar_ventas_aleatorias():
    empleados = []
    for producto in productos:
        empleado={
            "nombre": producto,
            "ventas": random.randint(1500000, 5000000)

        }
        empleados.append(empleado)

    globales.guardar_archivo_json('ventas.json',empleados)

if __name__ == "__main__":
    generar_ventas_aleatorias()
    print("ventas aleatorias generadas y guardadas en ventas.json")