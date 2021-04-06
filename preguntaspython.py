import json,requests,random,prints,math,string
from juegos import Juegos
from jugador import Jugador
from sympy import *

class preguntas_python(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas,mensaje_requerimiento): 
        self.preguntas = preguntas
        self.mensaje_requerimiento = mensaje_requerimiento
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas)
    
    def mostrar(self): #Para verificar que se trajo bien la API
        return print(f'Nombre: {self.nombre}\preguntas: {self.preguntas}')



def juego(jugador,response):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.

    for i in response:
        if i["name"] == "Laboratorio SL001":
            preguntas_python.nombre = i["objects"][1]["game"]["name"]
            preguntas_python.recompensa = i["objects"][1]["game"]["award"]
            preguntas_python.requerimiento = i["objects"][1]["game"]["requirement"]
            preguntas_python.reglas = i["objects"][1]["game"]["rules"]
            preguntas_python.preguntas = i["objects"][1]["game"]["questions"] #Lista de dos diccionarios. "question", "answer", clue_1, clue_2, clue_3

    #Se variables con números random entre 0 y 2 para utilizarlos como índice al momento de buscar las preguntas de manera aleatoria.
    respuestas = ["""int(float((frase.replace(",",".").split(" ")[4])))""","""" ".join(frase[::-1].split(" ")[::-1])"""]
    contador_pistas = 0

    if not jugador.inventario["Cable HDMI"] == "Disponible":
        print('Necesitas repararme con el cable HDMI')
        continuar = input('Pulse cualquier tecla para continuar >')
        return jugador

    #Pregunta X 
    while True:
        print_preguntaspython(jugador,preguntas_python.preguntas[1]["question"]) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        print(respuestas)
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la línea de cógigo\n> ')
            if respuesta == respuestas[1]:
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/2
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
                print('Incorrecto')
        elif accion == "2":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador)
                continuar = input('Pulse cualquier tecla para continuar >')
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,preguntas_python.preguntas[1]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar >')
                else:
                    print('Se agotaron las pistas hay más pistas.')
                    continuar = input('Pulse cualquier tecla para continuar >')
        elif accion == "3":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')

    #Pregunta Y 
    contador_pistas = 0
    while True:
        print_preguntaspython(jugador,preguntas_python.preguntas[0]["question"]) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        print(respuestas)
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la línea de cógigo\n> ')
            if respuesta == respuestas[0]:
                jugador.inventario["Carnet"] = "Disponible"
                print_ganaste(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                return jugador
            else:
                jugador.vida -= 1/2
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,preguntas_python.preguntas[0]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,preguntas_python.preguntas[0]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,preguntas_python.preguntas[0]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                else:
                    print('Se agotaron las pistas hay más pistas.')
                    continuar = input('Pulse cualquier tecla para continuar > ')
        elif accion == "3":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')
        




def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def print_preguntaspython(jugador,pregunta):
    if jugador.nivel_dificultad == "1":
        barra_vida = "|"*int((jugador.vida*10)*6/10) #Principiante
    elif jugador.nivel_dificultad == "2":
        barra_vida = "|"*int((jugador.vida*10)*10/10) #Intermedio
        print(len(barra_vida))
    else:
        barra_vida = "|"*int((jugador.vida*10)*30/10) #Avanzado


    print('\n\n\n\n')
    print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
    print(f'                                                                                                                                           {jugador.vida}/{jugador.vida_inicial}   --   {int(jugador.vida/jugador.vida_inicial*100)}% ')
    print('                                                                                                                                     ------------------------------')
    print(f'                                                                                                                                     {barra_vida}')
    print('                                                                                                                                     ------------------------------')
    print(f'''













                                                            ESCRIBE EL CÓDIGO
                                                            -----------------
                    {pregunta}















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Pista')
    print('3. Rendirse')
    print('')
    print('Nota: en la respuesta solo debes colocar la línea de código utilizando "frase" como variable')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

def print_correcto(jugador):
  if jugador.nivel_dificultad == "1":
    barra_vida = "|"*int((jugador.vida*10)*6/10) #Principiante
  elif jugador.nivel_dificultad == "2":
    barra_vida = "|"*int((jugador.vida*10)*10/10) #Intermedio
  else:
    barra_vida = "|"*int((jugador.vida*10)*30/10) #Avanzado


  print('\n\n\n\n')
  print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
  print(f'                                                                                                                                           {jugador.vida}/{jugador.vida_inicial}   --   {int(jugador.vida/jugador.vida_inicial*100)}% ')
  print('                                                                                                                                     ------------------------------')
  print(f'                                                                                                                                     {barra_vida}')
  print('                                                                                                                                     ------------------------------')
  print('''











                                                              _____ ____  _____  _____  ______ _____ _______ ____  _ 
                                                             / ____/ __ \|  __ \|  __ \|  ____/ ____|__   __/ __ \| |
                                                            | |   | |  | | |__) | |__) | |__ | |       | | | |  | | |
                                                            | |   | |  | |  _  /|  _  /|  __|| |       | | | |  | | |
                                                            | |___| |__| | | \ \| | \ \| |___| |____   | | | |__| |_|
                                                             \_____\____/|_|  \_\_|  \_\______\_____|  |_|  \____/(_)















  ''')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
  print('Escoge modo de juego:                                 [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

def print_ganaste(jugador):
  if jugador.nivel_dificultad == "1":
    barra_vida = "|"*int((jugador.vida*10)*6/10) #Principiante
  elif jugador.nivel_dificultad == "2":
    barra_vida = "|"*int((jugador.vida*10)*10/10) #Intermedio
  else:
    barra_vida = "|"*int((jugador.vida*10)*30/10) #Avanzado


  print('\n\n\n\n')
  print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
  print(f'                                                                                                                                           {jugador.vida}/{jugador.vida_inicial}   --   {int(jugador.vida/jugador.vida_inicial*100)}% ')
  print('                                                                                                                                     ------------------------------')
  print(f'                                                                                                                                     {barra_vida}')
  print('                                                                                                                                     ------------------------------')
  print('''










                                                              _____          _   _           _____ _______ ______ _ _ _ 
                                                             / ____|   /\   | \ | |   /\    / ____|__   __|  ____| | | |
                                                            | |  __   /  \  |  \| |  /  \  | (___    | |  | |__  | | | |
                                                            | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __| | | | |
                                                            | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____|_|_|_|
                                                             \_____/_/    \_\_| \_/_/    \_\_____/   |_|  |______(_|_|_)


                                                                            TU RECOMPENSA ES EL CARNET

                                                                               (revisa tu inventario)











  ''')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
  print('Escoge modo de juego:                                 [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

def print_pistas(jugador,pistas):
    if jugador.nivel_dificultad == "1":
        barra_vida = "|"*int((jugador.vida*10)*6/10) #Principiante
    elif jugador.nivel_dificultad == "2":
        barra_vida = "|"*int((jugador.vida*10)*10/10) #Intermedio
        print(len(barra_vida))
    else:
        barra_vida = "|"*int((jugador.vida*10)*30/10) #Avanzado


    print('\n\n\n\n')
    print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
    print(f'                                                                                                                                           {jugador.vida}/{jugador.vida_inicial}   --   {int(jugador.vida/jugador.vida_inicial*100)}% ')
    print('                                                                                                                                     ------------------------------')
    print(f'                                                                                                                                     {barra_vida}')
    print('                                                                                                                                     ------------------------------')
    print(f'''















                                                                {pistas.upper()}















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Pista')
    print('3. Rendirse')
    print('')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')


def main():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible", "Mensaje": "No disponible", "Disco duro": "No disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()