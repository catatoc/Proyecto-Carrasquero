class Jugador():
    def __init__(self,nombre,clave,edad,avatar,tiempo_realizado,cancion,inventario,vida,pistas,tiempo,vida_inicial,nivel_dificultad,saman,biblioteca,laboratorio,puerta_laboratorio,ubicacion):
        self.nombre = nombre
        self.edad = edad 
        self.clave = clave 
        self.avatar = avatar 
        self.tiempo_realizado = tiempo_realizado
        self.cancion = cancion
        self.inventario = inventario
        self.vida = vida
        self.pistas = pistas
        self.tiempo = tiempo
        self.vida_inicial = vida_inicial
        self.nivel_dificultad = nivel_dificultad
        self.saman = saman
        self.biblioteca = biblioteca
        self.laboratorio = laboratorio
        self.puerta_laboratorio = puerta_laboratorio
        self.ubicacion = ubicacion

    def mostrar_jugador(self):
        return (f"Nombre: {self.nombre}\nEdad: {self.edad}\nAvatar: {self.avatar}\nTiempo realizado: {self.tiempo_realizado}\nNivel de dificultadl: {self.nivel_dificultad}\nVida: {self.vida}")