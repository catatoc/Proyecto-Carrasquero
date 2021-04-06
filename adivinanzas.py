import json,requests,random,prints,math,string
from juegos import Juegos
from jugador import Jugador
from sympy import *
from time import *

class adivinanza(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas,mensaje_requerimiento): 
        self.preguntas = preguntas
        self.mensaje_requerimiento = mensaje_requerimiento
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas,mensaje_requerimiento)
    
    def mostrar(self): #Para verificar que se trajo bien la API
        return print(f'Nombre: {self.nombre}\preguntas: {self.preguntas}')



def juego(jugador,response):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.

    for i in response:
        if i["name"] == "Laboratorio SL001":
            adivinanza.nombre = i["objects"][2]["game"]["name"]
            adivinanza.recompensa = i["objects"][2]["game"]["award"]
            adivinanza.requerimiento = i["objects"][2]["game"]["requirement"]
            adivinanza.requerimiento = i["objects"][2]["game"]["message_requirement"]
            adivinanza.reglas = i["objects"][2]["game"]["rules"]
            adivinanza.preguntas = i["objects"][2]["game"]["questions"] #Lista de 3 diccionarios. "question", "answers", clue_1, clue_2, clue_3

    #Se variables con números random entre 0 y 2 para utilizarlos como índice al momento de buscar las preguntas de manera aleatoria.
    if jugador.inventario["Contraseña"] == "feliz":
        clave = input('Ingrese la contraseña\n> ')
        if clave == "feliz":
            apagada()
            sleep(3)
            prendida()
            sleep(3)
        else:
            return jugador
    else:
        return jugador







    x = random.randint(0,2)
    y = random.randint(0,2)
    while y == x:
        y = random.randint(0,2)
    z = random.randint(0,2)
    while z == y or z == x:
        z = random.randint(0,2)
    contador_pistas = 0

    #Pregunta X
    contador_pistas = 0
    while True:
        print_adivinanzas(jugador,adivinanza.preguntas[x]["question"]) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta in adivinanza.preguntas[x]["answers"]:
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/2
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar > ')
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,adivinanza.preguntas[x]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[x]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[x]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                else:
                    print('Se agotaron las pistas hay más pistas.')
                    continuar = input('Pulse cualquier tecla para continuar > ')
        elif accion == "3":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')
    
    #Pregunta Y
    contador_pistas = 0
    while True:
        print_adivinanzas(jugador,adivinanza.preguntas[y]["question"]) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta in adivinanza.preguntas[y]["answers"]:
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/2
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar > ')
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,adivinanza.preguntas[y]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[y]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[y]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                else:
                    print('Se agotaron las pistas hay más pistas.')
                    continuar = input('Pulse cualquier tecla para continuar > ')
        elif accion == "3":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')

    #Pregunta Z
    contador_pistas = 0
    while True:
        print_adivinanzas(jugador,adivinanza.preguntas[z]["question"]) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta in adivinanza.preguntas[z]["answers"]:
                jugador.inventario["Llave"] = "Disponible"
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
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar > ')
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,adivinanza.preguntas[z]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[z]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,adivinanza.preguntas[z]["clue_3"]) 
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
        pass

def print_adivinanzas(jugador,pregunta):
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













                                                              ADIVINANZAS
                                                              ------------
                                    {pregunta}















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


                                                                             TU RECOMPENSA ES LA LLAVE

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

def prendida():

    print('\n\n\n\n')
    print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
    print(f'                                                                                                                                            ')
    print('                                                                                                                                     ------------------------------')
    print(f'                                                                                                                                     ')
    print('                                                                                                                                     ------------------------------')
    print(f'''








                                                                   _______________                        |*\_/*|________
                                                                  |  ___________  |     .-.     .-.      ||_/-\_|______  |
                                                                  | |           | |    .****. .****.     | |           | |
                                                                  | |   0   0   | |    .*****.*****.     | |   0   0   | |
                                                                  | |     -     | |     .*********.      | |     -     | |
                                                                  | |   \___/   | |      .*******.       | |   \___/   | |
                                                                  | |___     ___| |       .*****.        | |___________| |
                                                                  |_____|\_/|_____|        .***.         |_______________|
                                                                    _|__|/ \|_|_.............*.............._|________|_
                                                                 ./  **********  \.                      ./  **********  \.
                                                                ./  ************  \.                    ./  ************  \.
                                                                --------------------                    --------------------













    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('')
    print('')
    print('')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

def apagada():

    print('\n\n\n\n')
    print('+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n')
    print(f'                                                                                                                                            ')
    print('                                                                                                                                     ------------------------------')
    print(f'                                                                                                                                     ')
    print('                                                                                                                                     ------------------------------')
    print(f'''








                                                                   _______________                        |*\_/*|________
                                                                  |  ___________  |                      ||_/-\_|______  |
                                                                  | |           | |                      | |           | |
                                                                  | |           | |                      | |           | |
                                                                  | |           | |                      | |           | |
                                                                  | |           | |                      | |           | |
                                                                  | |___     ___| |                      | |___________| |
                                                                  |_____|\_/|_____|                      |_______________|
                                                                    _|__|/ \|_|_                            _|________|_
                                                                 ./  **********  \.                      ./  **********  \.
                                                                ./  ************  \.                    ./  ************  \.
                                                                --------------------                    --------------------













    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('')
    print('')
    print('')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')


def main():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible", "Mensaje": "No disponible", "Disco duro": "No disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 4, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()