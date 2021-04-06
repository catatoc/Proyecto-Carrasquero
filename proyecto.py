import sys,os,random,prints,ahorcado,threading,preguntaspython,preguntas_matematicas,encuentralogica,adivinanzas,sopa_letras,culturaunimetana,palabramezclada,logicabooleana,json,requests,escogenumero,sopa_letras
from jugador import Jugador
from juegos import Juegos
from pyfiglet import Figlet
from time import *
from os import system
from datetime import date



def api():
    url = "https://api-escapamet.vercel.app/"
    response = requests.get(url).json()
    return response    

def temporizador():
    global cuenta_regresiva
    cuenta_regresiva = conteo*60
    for i in range(cuenta_regresiva):
        cuenta_regresiva -= 1
        sleep(1)
    prints.game_over()
    for i in range(3):
        sleep(1)
    os._exit(os.EX_OK)

def dificultad():
    """Función para conocer el tiempo, vida y cantidad de pistas iniciales

    Returns:
        Diccionario: Devuelve un diccionario con el tiempo, la vida y la cantidad de pistas de según la dificultad ingresada por el usuario.
    """
    tiempo_vida_pistas = []
    try:
        with open("/home/catato/proyecto-carrasquero/tiempo_vida_pistas.txt") as tvp:
            datos = tvp.readlines()
        if len(datos) == 0:
            print("\nRevisa el archivo txt.\n")
        else:
            for dato in datos:
                txt= dato[:-1].split("//")
                tiempo_vida_pistas.append(txt)

    except FileNotFoundError:
        print("\nTodavía no hay ningún jugador registrado.\n")
        return False
    global conteo
    diccionario = {}
    nivel_dificultad = input('************** DIFICULTAD **************\n\n1. Principiante -x minutos, 5 vidas y 5 pistas-\n2. Intermedio -x minutos, 3 vidas y 3 pistas-\n3. Avanzado -x minutos, 1 vida y 2 pistas-\n\n> ')
    while True:
        if nivel_dificultad == "1":
            diccionario["Tiempo"] = int(tiempo_vida_pistas[0][0])
            diccionario["Vida"] = int(tiempo_vida_pistas[0][1])
            diccionario["Pistas"] = int(tiempo_vida_pistas[0][2])
            diccionario["Nivel de dificultad"] = nivel_dificultad
            conteo = diccionario["Tiempo"]
            return diccionario
        elif nivel_dificultad == "2":
            diccionario["Tiempo"] = int(tiempo_vida_pistas[1][0])
            diccionario["Vida"] = int(tiempo_vida_pistas[1][1])
            diccionario["Pistas"] = int(tiempo_vida_pistas[1][2])
            diccionario["Nivel de dificultad"] = nivel_dificultad
            conteo = diccionario["Tiempo"]
            return diccionario
        elif nivel_dificultad == "3":
            diccionario["Tiempo"] = int(tiempo_vida_pistas[2][0])
            diccionario["Vida"] = int(tiempo_vida_pistas[2][1])
            diccionario["Pistas"] = int(tiempo_vida_pistas[2][2])
            diccionario["Nivel de dificultad"] = nivel_dificultad
            conteo = diccionario["Tiempo"]
            return diccionario
        else:
            print('Por favor ingrese una opción válida')
            nivel_dificultad = input('> ')

def jugador_existente(tiempo_vida_pistas):
    """Esta función revisa la base de datos y verifica si existen jugadores que coincidan con el usuario y clave ingresados por el jugador.

    Args:
        tiempo_vida_pistas (diccionario): Este diccionario consolida la información de dificultad de acuerdo a la preferencia indicada por el usuario. Se necesita porque una vez identificado el usuario hay que inicializarlo nuevamente.

    Returns:
        Bool: Retorna falso si el usuario no existe o si no hay usuarios registrados hasta el momento.
        Objeto: Si encuentra un jugador que coincide con la combinación nombre + contraseña retorna un objeto de tipo jugador inicializado en cero con nombre, contraseña... asociados a lo ingresado por el usuario.
    """
    jugadores = []
    try:
        with open("/home/catato/proyecto-carrasquero/Database_Players.txt") as dbp:
            datos = dbp.readlines()
        if len(datos) == 0:
            print("\nTodavía no hay ningún jugador registrado.\n")
            return False
        else:
            for dato in datos:
                player = dato[:-1].split("//")
                jugadores.append(Jugador(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9],player[10],player[11],player[12],player[13],player[14],player[15],player[16]))

            nombre_jugador = input('Ingrese el nombre del jugador: ')
            while not nombre_jugador.isalpha():
                print('Error')
                nombre_jugador = input('>  ')
            while True:
                for i in jugadores:
                    if nombre_jugador == i.nombre:
                        clave = input('Ingrese la contraseña: ')
                        while True:
                            if clave == i.clave:
                                print('Autenticación exitosa')
                                print(f'Bienvenido de vuelva {i.nombre} // {i.avatar}')
                                i.nivel_dificultad = tiempo_vida_pistas["Nivel de dificultad"]
                                i.tiempo = tiempo_vida_pistas["Tiempo"]
                                i.pistas = tiempo_vida_pistas["Pistas"]
                                i.vida = tiempo_vida_pistas["Vida"]
                                i.vida_inicial = tiempo_vida_pistas["Vida"]
                                i.saman = False
                                i.biblioteca = False
                                i.laboratorio = False
                                i.puerta_laboratorio = False
                                i.tiempo_realizado = " "
                                i.ubicacion = 0
                                i.inventario = {"Carnet": "No disponible", "Llave": "No disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "No disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No Disponible"}
                                return i
                            else:
                                print('Clave inválida. Intente nuevamente.\nSi olvidó su clave ingrese "x".')
                                clave = input('>  ')
                                if clave == "x":
                                    return False
                print('El nombre de usuario no existe')
                nombre_jugador = input('Intente nuevamente: ')
    except FileNotFoundError:
        print("\nTodavía no hay ningún jugador registrado.\n")
        return False

def crear_jugador(tiempo_vida_pistas):
    system('clear')
    nombre = input('************** NOMBRE ************** \n\nIngrese su nombre \n\n> ')
    while (not "".join(nombre.split(" ")).isalpha()):
        print('Error')
        nombre = input('> ')
    system('clear')
    clave = input('************** CONTRASEÑA ************** \n\nIngrese su contraseña \n\n>  ')
    while (not clave.isnumeric()) or (not len(clave) == 4):
        print('Error. Recuerde que su clave debe ser un pin de 4 números')
        clave = input('> ')
    system('clear')
    edad = input('************** EDAD **************\n\nIngrese su edad \n\n> ')
    while (not edad.isnumeric()) or (not int(edad) in range(7,120)):
        print('Error')
        edad = input('Ingrese su edad: ')
    system('clear')
    avatar = input('************** AVATARS **************\n\n1. Benjamín Sharifker \n2. Eugenio Mendoza\n3. Ronaldinho\n4. Ghandi\n5. Calvo de las empanadas\n\n> ')
    while True:
        if avatar == "1":
            avatar = "Benjamín Sharifker"
            break
        elif avatar == "2":
            avatar = "Eugenio Mendoza"
            break
        elif avatar == "3":
            avatar = "Ronaldinho"
            break
        elif avatar == "4":
            avatar = "Ghandi"
            break
        elif avatar == "5":
            avatar = "Calvo de las empanadas"
            break
        else:
            print('Error. Recuerde introducir el número referente al avatar que desea seleccionar.')
            avatar = input('> ')
    
    #Se inicializa el inventario 
    inventario = {"Carnet": "No disponible", "Llave": "No disponible", "Cable HDMI": "No disponible", "Libro de matemáticas": "No disponible", "Título universitario": "No disponible", "Martillo": "No disponible", "Contraseña": "No disponible", "Mensaje": "No disponible", "Disco duro": "No disponible", "Libro de física": "No disponible"}
    
    jugador = Jugador(nombre,edad,clave,avatar," "," ",inventario,tiempo_vida_pistas["Vida"], tiempo_vida_pistas["Pistas"], tiempo_vida_pistas["Tiempo"],tiempo_vida_pistas["Vida"],tiempo_vida_pistas["Nivel de dificultad"],False,False,False,False,0)
    
    
    print("\nJugador registrado con éxito.")
    sleep(2)
    return jugador

def ver_jugadores_existentes():
    """
    Esta función muestra la información de todos los jugadores previamente almacenada en la base de datos de jugadores.

    Argumentos => n/a

    Retorna => 
    \tSi hay jugadores registrados: imprime los jugadores numerados por orden de registro.
    \tSi el archivo .txt no existe (o sea, no hay nadie registrado): notifica que no existen jugadores registrados.

    """
    jugadores = []
    try:
        with open("/home/catato/proyecto-carrasquero/Database_Players.txt") as dbp:
            datos = dbp.readlines()
        if len(datos) == 0:
            print("\nTodavía no hay ningún jugador registrado.\n")
        else:
            for dato in datos:
                player = dato[:-1].split("//")
                jugadores.append(Jugador(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9],player[10],player[11],player[12],player[13],player[14],player[15],player[16]))

            print("\n\t\JUGADORES REGISTRADOS (por orden de registro)\n")
            for i,jug in enumerate(jugadores):
                print("-"*2,str(i+1),"-"*18)
                print(jug.mostrar_jugador())
            return True

    except FileNotFoundError:
        print("\nTodavía no hay ningún jugador registrado.\n")
        return False
    
def jugar():

    response = api()
    """Función madre. En ella se encuentra toda la lógica referente al juego como tal.
    """
    system('clear')
    tiempo_vida_pistas = dificultad() #Se inicializa un diccionario 
    system('clear')
    opcion = input('************** TIPO DE JUGADOR ************** \n\n1. Jugador existente\n2. Crear jugador\n\n> ')
    while True:
        if opcion == "1":
            if not ver_jugadores_existentes():
                opcion = input('************** TIPO DE JUGADOR ************** \n\n1. Jugador existente\n2. Crear jugador\n\n> ')
            else:
                jugador = jugador_existente(tiempo_vida_pistas) #Retorna jugador existente inicializado en cero
                break
                if not jugador:
                    return 
        elif opcion == "2":
            jugador = crear_jugador(tiempo_vida_pistas) #Retorna objeto de tipo jugador
            break
        else:
            print('Error')
            opcion = input('Ingrese el tipo de jugador\n1. Jugador existente\n2. Crear jugador\n> ')

    #Se agrega al txt. Esto debe estar al final del juego.        
    with open("/home/catato/proyecto-carrasquero/Database_Players.txt","a+") as dbp:
        dbp.write(f"{jugador.nombre}//{jugador.edad}//{jugador.clave}//{jugador.avatar}//{jugador.tiempo_realizado}//{jugador.cancion}//{jugador.inventario}//{jugador.vida}//{jugador.pistas}//{jugador.tiempo}//{jugador.vida_inicial}//{jugador.nivel_dificultad}//{jugador.saman}//{jugador.biblioteca}//{jugador.laboratorio}//{jugador.puerta_laboratorio}//{jugador.ubicacion}\n")
    prints.f_primera_narrativa(jugador) #Primera narrativa
    prints.f_segunda_narrativa(jugador) #Segunda narrativa

    #Inicio del juego en la biblioteca
    temporizador_thread = threading.Thread(target = temporizador) 
    temporizador_thread.start()
    jugador.biblioteca = True #Poner += 1
    jugador.ubicacion = 1
    while True:
        if jugador.ubicacion == 1:
            prints.biblioteca(jugador)
            accion = input('> ')
            if accion.isalpha() and (accion.lower() == "o" or accion.lower() == "t" or accion.lower() == "i" or accion.lower() == "s"):
                if accion.lower() == "o":
                    prints.opciones(jugador)
                elif accion.lower() == "t":
                    prints.mapa(jugador) #Aquí se utiliza la variable ubicación
                elif accion.lower() == "i":
                    prints.inventario(jugador)
                elif accion.lower() == "s":
                    jugador = prints.salir(jugador) 
            elif accion.isnumeric() and (accion == "1" or accion == "2" or accion == "3" or accion == "4" or accion == "5"):
                if accion == "1":
                    #Derivadas.  
                    prints.desarrollando() 
                elif accion == "2":
                    jugador = ahorcado.juego(jugador,response)
                    accion = input('> ')
                elif accion == "3":
                    jugador = criptograma.juego(jugador,response)
                    accion = input('> ')
                elif accion == "4":
                    jugador.ubicacion = 2
                elif accion == "5":
                    jugador.ubicacion = 3
            else:
                print('Error')
                accion = input('> ')
        elif jugador.ubicacion == 2:
            prints.saman(jugador)
            accion = input("> ")
            if accion.isalpha() and (accion.lower() == "o" or accion.lower() == "t" or accion.lower() == "i" or accion.lower() == "s"):
                if accion.lower() == "o":
                    prints.opciones(jugador)
                elif accion.lower() == "t":
                    prints.mapa(jugador) #Aquí se utiliza la variable ubicación
                elif accion.lower() == "i":
                    prints.inventario(jugador)
                elif accion.lower() == "s":
                    jugador = prints.salir(jugador) 
            elif accion.isnumeric() and (accion == "1" or accion == "2" or accion == "3" or accion == "4"):
                if accion == "1":
                    jugador = culturaunimetana.juego(jugador,response)
                elif accion == "2":
                    jugador = encuentralogica.juego(jugador,response)
                elif accion == "3":
                    #Memoria
                    prints.desarrollando()
                    print('Te regalamos el martillo mientras tanto')
                    jugador.inventario["Martillo"] = "Disponible" 
                    continuar = input('Pulse cualquier tecla para regresar > ')
                elif accion == "4":
                    jugador.ubicacion = 1
            else:
                print('Error')
                continuar = input('Pulse cualquier tecla para regresar > ')
        elif jugador.ubicacion == 3:
            prints.pasillo_laboratorio(jugador)
            accion = input('> ')
            if accion.isalpha() and (accion.lower() == "o" or accion.lower() == "t" or accion.lower() == "i" or accion.lower() == "s"):
                if accion.lower() == "o":
                    prints.opciones(jugador)
                elif accion.lower() == "t":
                    prints.mapa(jugador) #Aquí se utiliza la variable ubicación
                elif accion.lower() == "i":
                    prints.inventario(jugador)
                elif accion.lower() == "s":
                    jugador = prints.salir(jugador) 
            elif accion.isnumeric() and (accion == "1" or accion == "2" or accion == "3"):
                if accion == "1":
                    jugador = encuentralogica.juego(jugador,response)
                elif accion == "2":
                    jugador.ubicacion = 1
                elif accion == "3":
                    if jugador.inventario["Martillo"] == "Disponible":
                        jugador.ubicacion = 5
                    else:
                        print('Necesitas romper el candado de la puerta para poder pasar. Busca un martillo.')
                        continuar = input('Pulse cualquier tecla para regresar > ')
            else:
                print('Error')
                continuar = input('Pulse cualquier tecla para regresar > ')
        elif jugador.ubicacion == 4:
            prints.servidores(jugador)
            accion = input('> ')
            if accion.isalpha() and (accion.lower() == "o" or accion.lower() == "t" or accion.lower() == "i" or accion.lower() == "s"):
                if accion.lower() == "o":
                    prints.opciones(jugador)
                elif accion.lower() == "t":
                    prints.mapa(jugador) #Aquí se utiliza la variable ubicación
                elif accion.lower() == "i":
                    prints.inventario(jugador)
                elif accion.lower() == "s":
                    jugador = prints.salir(jugador) 
            elif accion.isnumeric() and (accion == "1" or accion == "2" or accion == "3" or accion == "4"):
                if accion == "1":
                    jugador = escogenumero.juego(jugador,response)
                elif accion == "2":
                    jugador = palabramezclada.juego(jugador,response)
                elif accion == "3":
                    #Juego libre
                    if jugador.inventario["Carnet"] == "Disponible" and jugador.inventario["Disco duro"] == "Disponible":
                        prints.gracias(jugador) 
                    print('Necesitas carnet de trabajador y disco duro para poder ingresar por esta puerta')
                    continuar = input('Pulse cualquier tecla para regresar > ')
                elif accion == "4":
                    jugador.ubicacion = 5

            else:
                print('Error')
                continuar = input('Pulse cualquier tecla para regresar > ')
        else:
            prints.laboratorio(jugador)
            accion = input('> ')
            if accion.isalpha() and (accion.lower() == "o" or accion.lower() == "t" or accion.lower() == "i" or accion.lower() == "s"):
                if accion.lower() == "o":
                    prints.opciones(jugador)
                elif accion.lower() == "t":
                    prints.mapa(jugador) #Aquí se utiliza la variable ubicación
                elif accion.lower() == "i":
                    prints.inventario(jugador)
                elif accion.lower() == "s":
                    jugador = prints.salir(jugador) 
            elif accion.isnumeric() and (accion == "1" or accion == "2" or accion == "3" or accion == "4" or accion == "5"):
                if accion == "1":
                    jugador = sopa_letras.juego(jugador,response)
                elif accion == "2":
                    jugador = preguntaspython.juego(jugador,response)
                elif accion == "3":
                    jugador = adivinanzas.juego(jugador,response)
                elif accion == "4":
                    jugador.ubicacion = 3
                elif accion == "5":
                    if jugador.inventario["Carnet"] == "Disponible":
                        jugador.ubicacion = 4
                    else:
                        print('Necesitas tener un carnet de trabajador para poder pasar')
                        continuar = input('Pulse cualquier tecla para regresar > ')

            else:
                print('Error')
                continuar = input('Pulse cualquier tecla para regresar > ')

def main():
    print('¡Hola! Es un placer darte la bienvenida a "ESCAPAMET"\n')
    accion = input('************** OPCIÓN A REALIZAR ************** \n\n1. Jugar\n2. Consultar resultados\n3. Salir\n\n> ')
    while True:
        if accion == "1": 
            jugar()
        elif accion == "2":
            prints.desarrollando()
            system('clear')
            accion = input('************** OPCIÓN A REALIZAR ************** \n\n1. Jugar\n2. Consultar resultados\n3. Salir\n\n> ')
        elif accion == "3":
            prints.game_over()
            break
        else:
            print('Error. Ingrese una opción válida')
            accion = input("> ")
main()