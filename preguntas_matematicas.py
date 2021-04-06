import json,requests,random,prints,math
from juegos import Juegos
from jugador import Jugador
from sympy import *

class derivadas(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas,mensaje_requerimiento): 
        self.preguntas = preguntas
        self.mensaje_requerimiento = mensaje_requerimiento
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas,mensaje_requerimiento)
    
def derivada():
    print('Hola')
    t = Symbol('t')
    f = ((cos(t))/2 - (tan(t))/5)
    f1 = lambdify(t,f)
    print(str(f1))
    print('Hola')
    print(f1(math.pi))
    return round(float(f1(0)),2)



    # # create a "symbol" called x
    # x = Symbol('x')
    
    # #Define function
    # f = x**2
    
    # f1 = lambdify(x, f)
    # #passing x=2 to the function
    # f1(2)

def juego(jugador):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    for i in response:
        if i["name"] == "Biblioteca":
            derivadas.nombre = i["objects"][1]["game"]["name"]
            derivadas.recompensa = i["objects"][1]["game"]["award"]
            derivadas.requerimiento = i["objects"][1]["game"]["requirement"]
            derivadas.mensaje_requerimiento = i["objects"][1]["game"]["message_requirement"]
            derivadas.reglas = i["objects"][1]["game"]["rules"]
            derivadas.preguntas = i["objects"][1]["game"]["questions"]

    #Se busca en el inventario del jugador el objeto llave. Si no lo tiene, no puede entrar.
    if jugador.inventario["Libro de matemáticas"] == "No disponible":
        print(derivadas.mensaje_requerimiento[x]["question"])
        return jugador
    derivada()
    x = random.randint(0,2)
    funciones = [((sin(x))/2),((cos(x))/2 - (tan(x))/5),((sin(x))/5 -(tan(x)))]
    f_x = funciones[x]
    print(f_x)
    print(derivada())
    y = x
    x = random.randint(0,2)
    while y == x:
        x = random.randint(0,2)
    f_y = ((cos(x))/2 - (tan(x))/5)
    z = x
    x = random.randint(0,2)
    while x == y or x == z:
        z = random.randint(0,2)
    f_z = ((sin(x))/5 -(tan(z)))
    #Pregunta 1
    print_derivadas(jugador, derivadas.preguntas[x]["question"])
    while True:
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_derivadas(jugador, derivadas.preguntas[x]["question"])
        elif accion == "1":
            respuesta = input('Ingrese su respuesta\n> ')
            if (respuesta.isnumeric() or "".join(respuesta.split(".")).isnumeric()) and float(respuesta) == (derivada()):
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/4
                print_derivadas(jugador, derivadas.preguntas[x]["question"])
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            print_pistas(jugador,"No hay pistas jajaja")
            jugador.pistas -= 1
            continuar = input('Pulse cualquier tecla para continuar > ')
            print_derivadas(jugador, derivadas.preguntas[x]["question"])
        elif accion == "3":
            return jugador
        else:
            print_derivadas(jugador, derivadas.preguntas[x]["question"])
            print('Error. Intente de nuevo.')

    #Pregunta 2
    print_derivadas(jugador, derivadas.preguntas[y]["question"])
    while True:
        print("Y")
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_derivadas(jugador, derivadas.preguntas[y]["question"])
        elif accion == "1":
            print(derivada(f_y))
            respuesta = input('Ingrese su respuesta\n> ')
            print(respuesta)
            if (respuesta.isnumeric() or "".join(respuesta.split(".")).isnumeric()) and float(respuesta) == (derivada()):
                print_correcto(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/4
                print_derivadas(jugador, derivadas.preguntas[y]["question"])
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            print_pistas(jugador,"No hay pistas jajaja")
            jugador.pistas -= 1
            continuar = input('Pulse cualquier tecla para continuar > ')
            print_derivadas(jugador, derivadas.preguntas[y]["question"])
        elif accion == "3":
            return jugador
        else:
            print_derivadas(jugador, derivadas.preguntas[y]["question"])
            print('Error. Intente de nuevo.')

    #Pregunta 3
    print_derivadas(jugador, derivadas.preguntas[z]["question"])
    while True:
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "v":
            print_derivadas(jugador, derivadas.preguntas[z]["question"])
        elif accion == "1":
            respuesta = input('Ingrese su respuesta\n> ')
            if "".join(respuesta.split(".")).isnumeric() and float(respuesta) == (derivada()):
                print_ganaste(jugador)
                continuar = input('Pulse cualquier tecla para continuar > ')
                break
            else:
                jugador.vida -= 1/4
                print_derivadas(jugador, derivadas.preguntas[z]["question"])
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            print_pistas(jugador,"No hay pistas jajaja")
            jugador.pistas -= 1
            continuar = input('Pulse cualquier tecla para continuar > ')
            print_derivadas(jugador, derivadas.preguntas[z]["question"])
        elif accion == "3":
            return jugador
        else:
            print_derivadas(jugador, derivadas.preguntas[z]["question"])
            print('Error. Intente de nuevo.')









def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def print_derivadas(jugador,pregunta):
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











                                                           CALCULA LA DERIVADA
                                                           -------------------
                                        {pregunta}















    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder')
    print('2. Pista')
    print('3. Rendirse')
    print('')
    print('Nota: en la respuesta solo debes colocar el resultado de la derivada (con dos decimales)')
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


# def main():
#     inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible"}
#     jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
#     juego(jugador)
# main()