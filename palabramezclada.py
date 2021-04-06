import json,requests,random,prints,math,string,os
from juegos import Juegos
from jugador import Jugador
from sympy import *

class palabra_mezclada(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas,mensaje_requerimiento): 
        self.preguntas = preguntas
        self.mensaje_requerimiento = mensaje_requerimiento
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas)
    
    def mostrar(self): #Para verificar que se trajo bien la API
        return print(f'Nombre: {self.nombre}\preguntas: {self.preguntas}')



def juego(jugador,response):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.

    for i in response:
        if i["name"] == "Cuarto de Servidores ":
            palabra_mezclada.nombre = i["objects"][1]["game"]["name"]
            palabra_mezclada.recompensa = i["objects"][1]["game"]["award"]
            palabra_mezclada.requerimiento = i["objects"][1]["game"]["requirement"]
            palabra_mezclada.reglas = i["objects"][1]["game"]["rules"]
            palabra_mezclada.preguntas = i["objects"][1]["game"]["questions"] #Lista de 3 diccionarios. "question", "category", "words"

    #Se variables con números random entre 0 y 2 para utilizarlos como índice al momento de buscar las preguntas de manera aleatoria.



    q,w,e,r,t = "","","","",""
    x = random.randint(0,2)
    #Pregunta 1
    print(palabra_mezclada.nombre)
    palabras_desordenadas = []
    ordenada = []
    contador = 0
    for i,j in enumerate(palabra_mezclada.preguntas[x]["words"]):
        ordenada = []
        contador = 0
        while contador < len(j):
            ordenada.append(j[contador])
            contador += 1
        desordenada = random.shuffle(ordenada)  
        palabras_desordenadas.append("".join(ordenada))  
    

    while q == "" or w == "" or e == "" or r == "" or t == "":
        prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
        elif accion == "1": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta == palabra_mezclada.preguntas[x]["words"][0]:
                print_correcto(jugador)
                q = "CORRECTA"
            else:
                jugador.vida -= 1/2
                prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
                print('Incorrecto')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta == palabra_mezclada.preguntas[x]["words"][1]:
                print_correcto(jugador)
                w = "CORRECTA"
            else:
                jugador.vida -= 1/2
                prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
                print('Incorrecto')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "3": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta == palabra_mezclada.preguntas[x]["words"][2]:
                print_correcto(jugador)
                e = "CORRECTA"
            else:
                jugador.vida -= 1/2
                prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
                print('Incorrecto')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "4": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta == palabra_mezclada.preguntas[x]["words"][3]:
                print_correcto(jugador)
                r = "CORRECTA"
            else:
                jugador.vida -= 1/2
                prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
                print('Incorrecto')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "5": #Ingresar respuesta
            respuesta = input('Ingrese la respuesta > ')
            if respuesta == palabra_mezclada.preguntas[x]["words"][4]:
                print_correcto(jugador)
                t = "CORRECTA"
            else:
                jugador.vida -= 1/2
                prints_palabramezclada(jugador,palabra_mezclada.preguntas[x]["category"],palabras_desordenadas,q,w,e,r,t)
                print('Incorrecto')
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "6":
            return jugador
        else:
            print('Error')
            continuar = input('Pulse cualquier tecla para continuar > ')        

    jugador.inventario["Contraseña"] = "feliz"
    print_ganaste(jugador)
    continuar = input('Pulse cualquier tecla para continuar > ')
    return jugador



def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def prints_palabramezclada(jugador,categoria,palabra,q,w,e,r,t):
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










                                                            CATEGORÍA: {categoria.upper()}
                                                            -----------{"-"*len(categoria)}

                                                            A. {palabra[0]} {q}                                       
                        
                                                            B. {palabra[1]} {w}
                        
                                                            C. {palabra[2]} {e}
                        
                                                            D. {palabra[3]} {r}

                                                            E. {palabra[4]} {t}                                      











    ''')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('Ingresa una opción:                                    [O] Opciones                               [T] Tiempo, ubicación y pistas                         [I] Consultar inventario  ')
    print('+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    print('1. Responder "A"')
    print('2. Responder "B"')
    print('3. Responder "C"')
    print('4. Responder "D"')
    print('5. Responder "E"')
    print('6. Rendirse')
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


                                                                            TU RECOMPENSA ES LA CONTRASEÑA

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
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "Disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible", "Mensaje":"Disponible","Disco duro":"Disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()