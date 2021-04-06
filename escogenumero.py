import json,requests,random,prints,math,string
from juegos import Juegos
from jugador import Jugador
from sympy import *

class escoge_numero(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas): 
        self.preguntas = preguntas
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas)
    
    def mostrar(self): #Para verificar que se trajo bien la API
        return print(f'Nombre: {self.nombre}\preguntas: {self.preguntas}')



def juego(jugador,response):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.

    for i in response:
        if i["name"] == "Cuarto de Servidores ":
            escoge_numero.nombre = i["objects"][2]["game"]["name"]
            escoge_numero.recompensa = i["objects"][2]["game"]["award"]
            escoge_numero.requerimiento = i["objects"][2]["game"]["requirement"]
            escoge_numero.reglas = i["objects"][2]["game"]["rules"]
            escoge_numero.preguntas = i["objects"][2]["game"]["questions"] #Lista de 3 diccionarios. "question", "answers", clue_1, clue_2, clue_3

    
    
    #Variable para ganar
    x = random.randint(1,15)
    contador = 0
    #Pregunta X
    while True:
        print_escogenumero(jugador) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta.isnumeric() and int(respuesta) in range(1,16):
                contador +=1
                if int(respuesta) == x:
                    jugador.inventario["Título universitario"] = "Disponible"
                    print_ganaste(jugador)
                    continuar = input('Pulse cualquier tecla para continuar > ')
                    return jugador
                else:
                    if contador == 3:
                        jugador.vida -= 1/4
                        contador = 0
                        if jugador.vida <= 0:
                            prints.game_over()
                            os._exit(os.EX_OK)
                    pistas = (f'Su número ingresado es el {respuesta}')
                    print_pistas(jugador,pistas)
                    ver_pista = input('¿Desea utilizar una pista para revisar si está cerca o lejos? (s) o (n)\n> ')
                    while not ver_pista.isalpha() and not ver_pista.lower() == "s" and not ver_pista.lower() == "n":
                        print('Error')
                        print('> ')
                    if ver_pista == "s":
                        jugador.pistas -= 1
                        if jugador.pistas == 0:
                            print('Se te acabaron las pistas ')
                            continuar = input('Pulse cualquier tecla para regresar > ')
                        else:
                            if x > int(respuesta):
                                if x - int(respuesta) <= 5:
                                    pistas = "Estás un poco por debajo"
                                else:
                                    pistas = "Estás muy por debajo" 
                            else:
                                if int(respuesta) - x <= 5:
                                    pistas = "Estás un poco por arriba"
                                else:
                                    pistas = "Estás muy por arriba"
                            print_pistas2(jugador,pistas)
                            continuar = input('Pulse cualquier tecla para regresar > ')
        elif accion == "2":
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

def print_escogenumero(jugador):
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













                                                                     ADIVINA NÚMERO ENTRE 1 y 15
                                                                     ---------------------------
                                                                       
                                                                                ¿?















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Rendirse')
    print('')
    print('')
    print('Nota: perderás 1/4 de vida por cada 3 intentos')
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


                                                                       TU RECOMPENSA ES EL LIBRO DE FÍSICA

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













                                                                INCORRECTO
                                                                ----------
                                                                {pistas}















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Rendirse')
    print('')
    print('')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

def print_pistas2(jugador,pistas):
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















                                                                {pistas}















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Rendirse')
    print('')
    print('')
    print('')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')


def main():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "Disponible", "Contraseña": "No Disponible", "Mensaje": "No disponible", "Disco duro": "No disponible", "Libro de física": "No disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 4, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()