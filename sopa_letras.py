import json,requests,random,prints,math,string
from juegos import Juegos
from jugador import Jugador
from sympy import *

class sopadeletras(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
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
            sopadeletras.nombre = i["objects"][0]["game"]["name"]
            sopadeletras.recompensa = i["objects"][0]["game"]["award"]
            sopadeletras.requerimiento = i["objects"][0]["game"]["requirement"]
            sopadeletras.reglas = i["objects"][0]["game"]["rules"]
            sopadeletras.preguntas = i["objects"][0]["game"]["questions"] #Lista de diccionarios. [0 a 2] answer_1,answer_2,answer_3 y [3 a 5] clue_1,clue_2,clue_3. Son 3 diciconarios.

    alfabeto = list((string.ascii_uppercase)) #Para traer el abecedario de forma desordenada
    fila = []
    matriz = []
    for i in range(15):
        for j in range(15):
            t = random.randint(0,25)
            fila.append(alfabeto[t])
        matriz.append(fila)
        fila = []
    
    #Se selecciona de manera random el diccionario que contiene las preguntas (hay 3 opciones de sopa de letras).
    palabras = []
    pistas = []
    x = random.randint(0,2)
    contador = 1
    for i in range(3):
        respuesta = "answer_"+str(contador) #Se busca las respuestas para esa sopa de letras en el api 
        palabras.append(sopadeletras.preguntas[x][respuesta].lower())
        contador += 1
    contador = 1
    for i in range(3):
        pista = "clue_"+str(contador) #Se busca las respuestas para esa sopa de letras en el api 
        pistas.append(sopadeletras.preguntas[x][pista])
        contador += 1
    
    print(palabras)
    print(pistas)

    y = random.randint(0,2)
    while y == x:
        y = random.randint(0,2)
    z = random.randint(0,2)
    while z == y or z == x:
        z = random.randint(0,2)

    matriz = vertical(palabras,y,matriz)
    matriz = horizontal(palabras,x,matriz)
    matriz = diagonal(palabras,z,matriz)

    #Pregunta X
    correctas = []
    contador_pistas = 0
    while True:
        print_sopadeletras(jugador,matriz)
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta.isalpha() and respuesta.lower() in palabras:
                if respuesta.lower() in correctas:
                    print('Ya adivinó a esta persona')
                    continuar = input('Pulse cualquier tecla para continuar > ')
                correctas.append(respuesta)
                if len(correctas) == 3:
                    print('No voy a dar la vida porque se va a descuadrar la barrita de la vida')
                    continuar = input('Pulse cualquier tecla para continuar > ')
                    print_ganaste(jugador)
                    continuar = input('Pulse cualquier tecla para continuar > ')
                    return jugador
                else:
                    print_correcto(jugador)
                    continuar = input('Pulse cualquier tecla para continuar > ')
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
                    print_pistas(jugador,pistas[0]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,pistas[1]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,pistas[2]) 
                    continuar = input('Pulse cualquier tecla para continuar > ')
                else:
                    print('Se agotaron las pistas hay más pistas.')
                    continuar = input('Pulse cualquier tecla para continuar > ')
        elif accion == "3":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')






















def mostrar_sopaletras(matriz):
    for i in matriz:
        print(f'                                                {"    ".join(i)}')
        print("")

def horizontal(palabras,numero_random,matriz): 
    w = random.randint(8,14) #Número random para saber la altura de la palabra horizontal en la sopa de letras
    contador = 1
    for i in palabras[numero_random][::-1]:
        matriz[w][contador] = i.upper()
        contador += 1
    return matriz

def vertical(palabras,numero_random,matriz):
    w = random.randint(11,14)
    contador = random.randint(0,5)
    for i in palabras[numero_random]:
        matriz[contador][w] = i.upper()
        contador += 1
    return matriz

def diagonal(palabras,numero_random,matriz):
    w = random.randint(0,3)
    contador = random.randint(0,3)
    for i in palabras[numero_random][::-1]:
        matriz[contador][w] = i.upper()
        contador += 1
        w+=1
    return matriz


    

    #Variables para escoger los diccionarios con las sopas de letra de manera random
    





def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def print_sopadeletras(jugador,matriz):
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
    print()
    mostrar_sopaletras(matriz)
    print()
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Pista')
    print('3. Rendirse')
    print('')
    print('Nota: tiene que adivinar los apellidos de tres (3) personas que hacen vida en la Universidad')
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


                                                                            TU RECOMPENSA ES EL MENSAJE

                                                                           "Si te graduas pisas el saman"
                                                                                
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
    print(jugador.vida)
    print(jugador.nivel_dificultad)
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
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()