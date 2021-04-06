import json,requests,random,prints,os,sys
from pyfiglet import Figlet
from juegos import Juegos
from jugador import Jugador

class ahorcado(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas): #Agregamos canción y autor
        #Sólo tenemos que hacer self con los atributos que no son de la clase padre
        self.preguntas = preguntas
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas)
    
def figlet_big(texto):
    f = Figlet(font='big')
    return(f'{f.renderText(texto)}')

def figlet_cybermedium(texto):
    f = Figlet(font='cybermedium')
    return(f'{f.renderText(texto)}')

def f_ayuda(ahorcado,letras_correctas,x):
    ayuda = []
    for i in ahorcado.preguntas[x]["answer"].lower():
        if i in set(letras_correctas):
            ayuda.append(i)
        else:
            ayuda.append("_")
    return ayuda


def juego(jugador,response):

    """En esta función está todo el juego del ahorcado. Pude hacerlo en varias funciones pero me dificultaba los prints de pantalla.

    Returns:
        objeto: Retorna el objeto de tipo jugador con sus atributos actualizados. En este juego pueden cambiar la vida, cantidad de pistas e inventario.
    """
    for i in response:
        if i["name"] == "Biblioteca":
            ahorcado.nombre = i["objects"][0]["game"]["name"]
            ahorcado.recompensa = i["objects"][0]["game"]["award"]
            ahorcado.requerimiento = i["objects"][0]["game"]["requirement"]
            ahorcado.reglas = i["objects"][0]["game"]["rules"]
            ahorcado.preguntas = i["objects"][0]["game"]["questions"]

    #Se variables con números random entre 0 y 2 para utilizarlos como índice al momento de buscar las preguntas de manera aleatoria.
    x = random.randint(0,2)
    y = random.randint(0,2)
    while y == x:
        y = random.randint(0,2)
    z = random.randint(0,2)
    while z == y or z == x:
        z = random.randint(0,2)
    ayuda = []
    letras_correctas = []
    contador_pistas = 0
    utility = False

    #Pregunta X 
    while True:
        if not utility:
            if len(letras_correctas) == 0:
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],"_ "*len(ahorcado.preguntas[x]["answer"]),letras_correctas)
            else:
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
        
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        
        elif accion == "1": #Ingresar letra
            letra = input('Ingrese la letra: ')
            if letra in ahorcado.preguntas[x]["answer"].lower():
                if letra not in letras_correctas:
                    ayuda = []  
                    letras_correctas.append(letra)
                    utility = True
                ayuda = f_ayuda(ahorcado,letras_correctas,x)
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                utility = False                
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "2": #Ingresar palabra
            palabra = input('Ingrese la respuesta: ')
            if palabra.lower() == ahorcado.preguntas[x]["answer"].lower():
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para ir a la siguiente pregunta')
                break
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                ayuda = f_ayuda(ahorcado,letras_correctas,x)
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                print('INCORRECTO')
                continuar = input('Pulse cualquier tecla para continuar')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "3":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar')
                ayuda = f_ayuda(ahorcado,letras_correctas,x)
                print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,ahorcado.preguntas[x]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,x)
                    print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[x]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,x)
                    print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[x]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,x)
                    print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
                else:
                    print('Se agotaron las pistas hay más pistas.')
        elif accion == "4":
            return jugador
        else:
            print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)
            print('Error')
        
        print_ahorcado(jugador,ahorcado.preguntas[x]["question"],(" ".join(ayuda)),letras_correctas)

    #Pregunta Y
    ayuda = []
    letras_correctas = []
    contador_pistas = 0
    utility = False
    while True:
        if not utility:
            if len(letras_correctas) == 0:
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],"_ "*len(ahorcado.preguntas[y]["answer"]),letras_correctas)
            else:
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
        
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        
        elif accion == "1": #Ingresar letra
            letra = input('Ingrese la letra: ')
            if letra in ahorcado.preguntas[y]["answer"].lower():
                if letra not in letras_correctas:
                    ayuda = []  
                    letras_correctas.append(letra)
                    utility = True
                ayuda = f_ayuda(ahorcado,letras_correctas,y)
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                utility = False                
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "2": #Ingresar palabra
            palabra = input('Ingrese la respuesta: ')
            if palabra.lower() == ahorcado.preguntas[y]["answer"].lower():
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para ir a la siguiente pregunta')
                break
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                ayuda = f_ayuda(ahorcado,letras_correctas,y)
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                print('INCORRECTO')
                continuar = input('Pulse cualquier tecla para continuar')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "3":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar')
                ayuda = f_ayuda(ahorcado,letras_correctas,y)
                print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,ahorcado.preguntas[y]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,y)
                    print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[y]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,y)
                    print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[y]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,y)
                    print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
                else:
                    print('Se agotaron las pistas hay más pistas.')
        elif accion == "4":
            return jugador
        else:
            print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)
            print('Error')
        
        print_ahorcado(jugador,ahorcado.preguntas[y]["question"],(" ".join(ayuda)),letras_correctas)

    #Pregunta Z
    ayuda = []
    letras_correctas = []
    contador_pistas = 0
    utility = False
    while True:
        if not utility:
            if len(letras_correctas) == 0:
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],"_ "*len(ahorcado.preguntas[z]["answer"]),letras_correctas)
            else:
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
        
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        
        elif accion == "1": #Ingresar letra
            letra = input('Ingrese la letra: ')
            if letra in ahorcado.preguntas[z]["answer"].lower():
                if letra not in letras_correctas:
                    ayuda = []  
                    letras_correctas.append(letra)
                    utility = True
                ayuda = f_ayuda(ahorcado,letras_correctas,z)
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                utility = False                
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "2": #Ingresar palabra
            palabra = input('Ingrese la respuesta: ')
            if palabra.lower() == ahorcado.preguntas[z]["answer"].lower():
                print_ganaste(jugador)
                jugador.inventario["Cable HDMI"] = "Disponible"
                continuar = input('Pulse cualquier tecla para regresar a la biblioteca')
                return jugador
            else:
                jugador.vida -= 1/4
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                ayuda = f_ayuda(ahorcado,letras_correctas,z)
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                print('INCORRECTO')
                continuar = input('Pulse cualquier tecla para continuar')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)

        elif accion == "3":
            if jugador.pistas == 0:
                pistas = 'En este momento no tiene pistas disponibles.'
                print_pistas(jugador,pistas)
                continuar = input('Pulse cualquier tecla para continuar')
                ayuda = f_ayuda(ahorcado,letras_correctas,z)
                print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
            else:
                if contador_pistas == 0:
                    jugador.pistas -= 1
                    contador_pistas += 1
                    print_pistas(jugador,ahorcado.preguntas[z]["clue_1"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,z)
                    print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 1:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[z]["clue_2"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,z)
                    print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                elif contador_pistas == 2:
                    contador_pistas += 1
                    jugador.pistas -= 1
                    print_pistas(jugador,ahorcado.preguntas[z]["clue_3"]) 
                    continuar = input('Pulse cualquier tecla para continuar')
                    ayuda = f_ayuda(ahorcado,letras_correctas,z)
                    print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
                else:
                    print('Se agotaron las pistas hay más pistas.')
        elif accion == "4":
            return jugador
        else:
            print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
            print('Error')
        
        print_ahorcado(jugador,ahorcado.preguntas[z]["question"],(" ".join(ayuda)),letras_correctas)
        

def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def print_ahorcado(jugador,pregunta,respuesta,letras_correctas):
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
    print(f'''










                                                                    {pregunta}



                                                                                     {respuesta}



                                                                                  Letras correctas:{letras_correctas}








    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Intentar letra')
    print('2. Responder palabra')
    print('3. Pista')
    print('4. Rendirse')
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














                                                                                  {pistas}












    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Intentar letra')
    print('2. Responder palabra')
    print('3. Pista')
    print('4. Rendirse')
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


                                                                            TU RECOMPENSA ES EL CABLE HDMI
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



def main():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    inventario = {"Carnet": "No disponible", "Llave": "No disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "No disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()