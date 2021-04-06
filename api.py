api = [
{
"name": "Laboratorio SL001",
"objects": [
{
"name": "pizarra",
"position": "center",
"game": {
"requirement": false,
"name": "sopa_letras",
"award": "vida extra",
"rules": "pierde media vida por palabra incorrecta",
"questions": [
{
"answer_1": "Pilar",
"answer_2": "Ardila",
"answer_3": "Scharifker",
"clue_1": "apellido directora de escuela de sistemas",
"clue_2": "apellido jefe del CeTIC",
"clue_3": "apellido rector Unimet"
},
{
"answer_1": "Bello",
"answer_2": "Marcano",
"answer_3": "DaGama",
"clue_1": "apellido de profesor Luis",
"clue_2": "apellido del profesor Alejandro",
"clue_3": "apellido del Presidente de la Unimet"
},
{
"answer_1": "Boada",
"answer_2": "Llorante",
"answer_3": "DaGama",
"clue_1": "apellido del coronel de Seguridad de la Unimet",
"clue_2": "apellido del presidente de la FCE-UNIMET ",
"clue_3": "apellido de Vicerrectora Académica de la Unimet"
}
]
}
},
{
"name": "computadora 1",
"position": "left",
"game": {
"message_requirement": "mi pantalla no funciona",
"requirement": "cable HDMI",
"name": "Preguntas sobre python",
"rules": "pierde media vida por cada prueba incorrecta",
"award": "carnet",
"questions": [
{
"question": "Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\". Escribe en una línea de código como extraer de este string los 50 en formato entero",
"answer": "Validar en python que de el siguiente resultado: 50.00 en formato entero",
"clue_1": "utiliza replace",
"clue_2": "utiliza split",
"clue_3": "utiliza int"
},
{
"question": "Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\"",
"answer": "string invertido",
"clue_1": "utiliza slices"
}
]
}
},
{
"name": "computadora 2",
"position": "right",
"game": {
"message_requirement": "necesita contraseña para ingresar",
"requirement": "introducir contraseña de la computadora",
"award": "llave",
"name": "Adivinanzas",
"rules": "pierde media vida por cada pregunta incorrecta",
"questions": [
{
"question": "Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo?",
"answers": [
"una vela",
"vela",
"Vela",
"la Vela",
"La Vela"
],
"clue_1": "lo usas cuando se va la luz",
"clue_2": "lo puedes prender con un encendedor",
"clue_3": "es de cera"
},
{
"question": "Es pequeño como una pera, pero alumbra la casa entera. ¿Qué soy yo?",
"answers": [
"un bombillo",
"bombillo",
"El Bombillo",
"el bombillo",
"Bombillo"
],
"clue_1": "lo usas cuando hay luz",
"clue_2": "gracias a estar encendido puedes leer",
"clue_3": "se coloca en las lámparas"
},
{
"question": "Oro parece y plata no es, y no lo adivinas de aquí a un mes ¿Qué soy yo?",
"answers": [
"un platano",
"platano",
"El Platano",
"Platano",
"plátano",
"Plátano"
],
"clue_1": "fruta",
"clue_2": "POTASIO",
"clue_3": "parecido al cambur"
}
]
}
}
]
},
{
"name": "Biblioteca",
"objects": [
{
"name": "mueble de libros",
"position": "center",
"game": {
"requirement": false,
"name": "ahorcado",
"award": "cable HDMI",
"rules": "pierde un cuarto de vida por letra incorrecta",
"questions": [
{
"question": "Me encuentro en la entrada de la Universidad",
"answer": "Metromix",
"clue_1": "sitio de comida",
"clue_2": "al lado de las copias",
"clue_3": "Comienza por Metro"
},
{
"question": "Me buscan y nunca me encuentran en la Universidad",
"answer": "Piscina",
"clue_1": "Es rectangular",
"clue_2": "Tiene agua",
"clue_3": "Se puede nadar"
},
{
"question": "Tienes que subir muchos pisos para llegar a mi",
"answer": "Rectorado",
"clue_1": "Esta en el Eugenio Mendoza",
"clue_2": "Ultimo piso del Eugenio",
"clue_3": "Oficina del Rector"
}
]
}
},
{
"name": "mueble de sentarse",
"position": "left",
"game": {
"message_requirement": "Necesito que sepas derivar",
"requirement": "libro de matemáticas",
"name": "Preguntas matemáticas",
"award": "vida extra",
"rules": "pierde un cuarto de vida por respuesta incorrecta",
"questions": [
{
"question": "Calcula la derivada de la función en pi  f(x)=((sen(x))/2)",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
},
{
"question": "Calcula la derivada de la función en pi  f(x)=((cos(x))/2 - (tan(x))/5)  ",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
},
{
"question": "Calcula la derivada de la función en pi/3 f(x)=((sen(x))/5 -(tan(x)))",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
}
]
}
},
{
"name": "mueble con gabetas",
"position": "right",
"game": {
"message_requirement": "No me puedes abrir, busca algo para abrirme",
"requirement": "llave",
"name": "Criptograma",
"award": "Mensaje: Si estas gradudado puedes pisar el Samán",
"rules": "pierde una vida por partida pérdida",
"questions": [
{
"question": "Si te graduas pisas el samán",
"desplazamiento": 2
},
{
"question": "Si te graduas pisas el samán",
"desplazamiento": 4
},
{
"question": "Si te graduas pisas el samán",
"desplazamiento": 5
}
]
}
}
]
},
{
"name": "Plaza Rectorado",
"objects": [
{
"name": "Saman",
"position": "center",
"game": {
"name": "Encuentra la lógica y resuelve",
"message_requirement": "pierdes una vida por pisar el samán 🥵",
"requirement": [
"Titulo Universitario",
"Mensaje"
],
"award": "Disco Duro",
"rules": "pierdes una vida por pisar el samán 🥵, pero si tienes en tu inventario lo requerido, puedes jugar el juego del Samán",
"questions": [
"🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?",
"🐧+🐧+🐧=27 \n 🐧+🐝+🐝=19 \n 🐝+🐦+🐦=13 \n 🐝x🐧-🐦=?"
]
}
},
{
"name": "Banco 1",
"position": "left",
"game": {
"requirement": false,
"name": "Quizizz Cultura Unimetana",
"award": "libro de matemáticas",
"rules": "pierde media vida por opción incorrecta",
"questions": [
{
"question": "¿En qué fecha es el Aniversario de la Universidad Metropolitana?",
"correct_answer": "22 de octubre",
"answer_2": "22 de septiembre",
"answer_3": "25 de octubre",
"answer_4": "25 de septiembre",
"clue_1": "es en octubre"
},
{
"question": "¿En qué año fue Fundada la Universidad Metropolitana?",
"correct_answer": "1970",
"answer_2": "1969",
"answer_3": "1980",
"answer_4": "1979",
"clue_1": "termina en 0 el año"
},
{
"question": "¿Quién fundó la Unimet?",
"correct_answer": "Eugenio Mendoza",
"answer_2": "Rafael Matiezo",
"answer_3": "Lorenzo Mendoza",
"answer_4": "Luis Miguel Da Gama",
"clue_1": "tiene una estatua"
}
]
}
},
{
"name": "Banco 2",
"position": "right",
"game": {
"requirement": false,
"name": "memoria con emojis",
"award": "martillo",
"rules": "un cuarto de vida por elección incorrecta",
"questions": [
{
"question": "[['😀', '🙄', '🤮', '🥰'],\n                                                    ['🤮', '😨', '🤓', '😷'],\n                                                    ['😨', '🤓', '🥰', '😷'],\n                                                    ['🤑', '🤑', '🙄', '😀']]",
"clue_1": "Decirte donde está escondida una que levantes"
}
]
}
}
]
},
{
"name": "Pasillo Laboratorios ",
"objects": [
{
"name": "puerta",
"position": "center",
"game": {
"message_requirement": "Está cerrado con candado!!!!!",
"requirement": "martillo",
"name": "Lógica Booleana",
"award": "vida extra",
"rules": "pierde media vida por opción incorrecta",
"questions": [
{
"question": "¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b) ",
"answer": "False"
},
{
"question": "¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and a) or (b) or (b or a) or (a and not a and not b)",
"answer": "True"
}
]
}
}
]
},
{
"name": "Cuarto de Servidores ",
"objects": [
{
"name": "puerta",
"position": "center",
"game": {
"message_requirement": "Necesitas tener un carnet de trabajador para poder pasar",
"requirement": [
"carnet",
"Disco Duro"
],
"name": "Juego Libre",
"award": "Parar el cronómetro y ganar el juego",
"rules": "pierde una vida completa por partida pérdida",
"description": "Pueden hacer este juego de pipes y tienen puntos extras https://www.youtube.com/watch?list=PLH_elo2OIwaBiCJdcKKocFs1oXCItI9wB&v=DfDn5AFRnFI&feature=emb_title",
"questions": [
{
"question": "",
"answer": "False"
}
]
}
},
{
"name": "Rack",
"position": "left",
"game": {
"requirement": false,
"name": "Palabra mezclada",
"award": "contraseña",
"rules": "media vida menos por cada palabra incorrecta",
"questions": [
{
"question": "Reordena los caracteres para formar una palabra correcta y con sentido",
"category": "Cocina",
"words": [
"sarten",
"paleta",
"olla",
"vaso",
"hornilla"
]
},
{
"question": "Reordena los caracteres para formar una palabra correcta y con sentido",
"category": "Baño",
"words": [
"poceta",
"cepillo",
"afeitadora",
"regadera",
"grifo"
]
},
{
"question": "Reordena los caracteres para formar una palabra correcta y con sentido",
"category": "Baile",
"words": [
"zumba",
"salsa",
"flamengo",
"tango",
"perreo"
]
}
]
}
},
{
"name": "papelera",
"position": "right",
"game": {
"requirement": false,
"name": "escoge un número entre",
"award": "título Universitario",
"rules": "un cuarto de vida menos por 3 intentos seguidos fallando",
"questions": [
{
"question": "Escoge una número entre 1-15",
"answer": "Random con python",
"clue_1": "Estas cerca un poco abajo, Estás cerca un poco arriba,  estás muy abajo, estás muy arriba"
}
]
}
}
]
}
]