import json,requests,random,string,prints
from juegos import Juegos
from jugador import Jugador

class criptograma(Juegos): #Ahora esta clase tiene todos los atributos de la clase Juegos
    def __init__(self,preguntas): 
        self.preguntas = preguntas
        super().__init__(nombre,recompensa,reglas,requerimiento,preguntas)
    

def alfabeto_encriptado(alfabeto,x):
    alfabeto_encriptado = alfabeto[x+1:len(alfabeto)]
    for i in alfabeto:
        if i in alfabeto_encriptado:
            break
        else:
            alfabeto_encriptado.append(i)
    return alfabeto_encriptado

def juego(jugador,response):

    #Se crea un objeto tipo criptograma donde se agregatodo lo relacionado con este juego.

    for i in response:
        if i["name"] == "Biblioteca":
            criptograma.nombre = i["objects"][2]["game"]["name"]
            criptograma.recompensa = i["objects"][2]["game"]["award"]
            criptograma.requerimiento = i["objects"][2]["game"]["requirement"]
            criptograma.reglas = i["objects"][2]["game"]["rules"]
            criptograma.preguntas = i["objects"][2]["game"]["questions"]

    #Se busca en el inventario del jugador el objeto llave. Si no lo tiene, no puede entrar.
    if jugador.inventario["Llave"] == "No disponible":
        print('No me puedes abrir. Busca algo para abrirme')
        return jugador
    
    #Se inicializa la variable alfabeto con el abecedario en orden
    alfabeto = list(string.ascii_lowercase)

    #Se inicializan variables requeridas para el procedimiento
    utility = []
    y = random.randint(0,2)
    desplazamientos = []
    mensaje_encriptado = []
    dic_alfabeto = {}
    i = 0

    #Se ubican los desplazamientos en la API
    for i in criptograma.preguntas:
        desplazamientos.append(i["desplazamiento"])
    
    #Se escoge un desplazamiento de la API de manera aleatoria
    x = desplazamientos[y]
    
    #Se quita el acento en el mensaje
    mensaje = criptograma.preguntas[y]["question"].replace("á","a").lower()
    
    #Por comodidad se decidió hacer un diccionario con el abecedario con la letra y su posición en número. Ejemplo {"a": 1}
    contador = 1
    for i in alfabeto:
        dic_alfabeto[i] = contador
        contador += 1
    
    #Se busca el mensaje encriptado con la función del alfabeto_encriptado
    for i in mensaje:
        if i.lower() != " ":
            mensaje_encriptado.append(alfabeto_encriptado(alfabeto,x)[dic_alfabeto[i.lower()]-1])
        else:
            mensaje_encriptado.append(" ")

    #Se imprimen los mensajes en string
    print_criptograma(jugador,"".join(alfabeto),"".join(mensaje_encriptado),"".join(alfabeto_encriptado(alfabeto,x)))
    while True:
        accion = input('> ')
        if accion.isalpha() and accion.lower() == "o" or accion.lower() == "t"  or accion.lower() == "i" or accion.lower() == "v": #En caso de que el usuario quiera revisar el menú, inventario...
            opciones_menu(accion,jugador)
            print_criptograma(jugador,"".join(alfabeto),"".join(mensaje_encriptado),"".join(alfabeto_encriptado(alfabeto,x))) #En caso de que el usuario haya revisado el menú, inventario... y quiera regresar al juego.
        elif accion == "1":
            respuesta = input('Ingrese su respuesta\n> ')
            if "".join(respuesta.split(" ")).isalpha() and respuesta.lower() == mensaje:
                print_ganaste(jugador)
                jugador.inventario["Mensaje"] = "Si te gradúas pisas el Samán"
                continuar = input('Pulse cualquier tecla para regresar a la biblioteca > ')
                return jugador
            else:
                jugador.vida -= 1/4
                print_criptograma(jugador,"".join(alfabeto),"".join(mensaje_encriptado),"".join(alfabeto_encriptado(alfabeto,x)))
                utility = False
                if jugador.vida <= 0:
                    prints.game_over()
                    os._exit(os.EX_OK)
        elif accion == "2":
            print_pistas(jugador,"No hay pistas jajaja")
            jugador.pistas -= 1
            continuar = input('Pulse cualquier tecla para continuar > ')
            print_criptograma(jugador,"".join(alfabeto),"".join(mensaje_encriptado),"".join(alfabeto_encriptado(alfabeto,x)))
        elif accion == "3":
            return jugador
        else:
            print_criptograma(jugador,"".join(alfabeto),"".join(mensaje_encriptado),"".join(alfabeto_encriptado(alfabeto,x)))
            print('Error. Intente de nuevo.')

    y = random.randint(0,2)
    while y == x:
        y = random.randint(0,2)
    z = random.randint(0,2)
    while z == y or z == x:
        z = random.randint(0,2)
    ayuda = []
    letras_correctas = []
    contador_pistas = 0
    print(criptograma.preguntas[x]["desplazamiento"])








def opciones_menu(accion,jugador):
    if accion == "o":
        prints.opciones(jugador)
    elif accion == "t":
        prints.mapa(jugador)
    elif accion == "i":
        prints.inventario(jugador)
    elif accion == "v":
        return

def print_criptograma(jugador,alfabeto,mensaje_encriptado,alfabeto_encriptado):
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










                                                           MENSAJE ENCRIPTADO
                                                           ------------------
                                                      {mensaje_encriptado}




                            ALFABETO                                                          ALFABETO ENCRIPTADO
                            --------                                                          -------------------
                   {alfabeto}                                             {alfabeto_encriptado}














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


                                                                            TU RECOMPENSA ES EL MENSAJE

                                                                           "Si te graduas pisas el Samán"
                                                                                
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
    inventario = {"Carnet": "No disponible", "Llave": "Disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "No disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible", "Mensaje": "No Disponible", "Disco duro": "Disponible", "Mensaje": "No disponible", "Disco duro": "No disponible"}
    jugador = Jugador("Carlos","25","1234","Pepa"," "," ",inventario,3, 3, 3,3,"2",False,False,False,False,0)
    juego(jugador,response)
#main()