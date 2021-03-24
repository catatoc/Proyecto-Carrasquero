import proyecto_carrasquero
import requests




def api():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    for i in response:
        print(f'{i["name"]}')

# print(proyecto_carrasquero.biblioteca())

def agregar_json(jugadores):
    with open('/home/catato/proyecto-carrasquero/base_datos.json', 'w') as bd:
        bd.write(f'{jugadores}')

def revisar_json():
    with open('/home/catato/proyecto-carrasquero/base_datos.json') as bd:
        for i in (bd):
            print(i)
            for j in i:
                print(j)
                
def main():
    jugadores = [
{"nombre":"Catato", "puntuación":100},
{"nombre": "Juan", "puntuación": 200}
]
    for i in jugadores:
        for j in i.keys():
            print(j)
    # agregar_json(jugadores)
    revisar_json()
main()
    
def prueba_json():
    with open('/home/catato/proyecto-carrasquero/base_datos.json') as bd:
        catato = {"nombre":"Pedro", "puntuación":200}
        print(bd)

    with open('/home/catato/proyecto-carrasquero/base_datos.json', 'a') as bd:
        bd.write








