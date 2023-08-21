# Defino la lista de lenguajes afectivos
lenguajesafectivos = ["Contacto fisico", "Tiempo de calidad", "Regalos", "Palabras de afirmacion", "Actos de servicio"]

# Almacenar el valor de la variable contacto fisico
contacto_fisico = lenguajesafectivos[0]
tiempo_calidad = lenguajesafectivos[1]
regalos = lenguajesafectivos[2]
palabras_de_afrimacion = lenguajesafectivos[3]
actos_de_servicio = lenguajesafectivos[4]

# Crear un menú con la lista de lenguajes afectivos
menu = []
for lenguaje in lenguajesafectivos:
    menu.append(lenguaje)

# Imprimo el menú con una bienvenida
print("Bienvenido al menú de lenguajes afectivos apreta cualquier tecla para continuar:")
nombre = input("Ingresa tu nombre: ")
nombrepareja = input("Ingresa el nombre de tu pareja: ")
print("Hola", nombre, "y", nombrepareja, "por favor, ingresa los siguientes datos para poder ayudarte")
opcion1 = input("En que calificacion dirias que posicionarias a "+lenguajesafectivos[0] + " En una escala del 1 al 5?")
opcion2 = input("En que calificacion dirias que posicionarias a "+lenguajesafectivos[1] + " En una escala del 1 al 5?")
opcion3 = input("En que calificacion dirias que posicionarias a "+lenguajesafectivos[2] + " En una escala del 1 al 5?")
opcion4 = input("En que calificacion dirias que posicionarias a "+lenguajesafectivos[3] + " En una escala del 1 al 5?")
opcion5 = input("En que calificacion dirias que posicionarias a "+lenguajesafectivos[4] + " En una escala del 1 al 5?")
print("Gracias por tu respuesta")

# Crear un diccionario con los datos ingresados por el usuario
datos = {
    "Nombre": nombre,
    "Nombre de tu pareja": nombrepareja,
    "Contacto fisico": opcion1,
    "Tiempo de calidad": opcion2,
    "Regalos": opcion3,
    "Palabras de afirmacion": opcion4,
    "Actos de servicio": opcion5
}

# Imprimir el diccionario
print(datos)

# Obtener el nombre del lenguaje de amor más fuerte
lenguaje_de_amor_mas_fuerte = max(datos, key=datos.get)
nombre_lenguaje = lenguajesafectivos.index(lenguaje_de_amor_mas_fuerte)

# Imprimir el nombre del lenguaje más fuerte
print("El lenguaje de amor más fuerte es:", lenguajesafectivos[nombre_lenguaje])
print("En hora buena tu leguaje de amor mas fuerte es el de:" + lenguajesafectivos[nombre_lenguaje])
print("Felicidades" + "" + nombre + "Por descubrir tu lenguaje de amor, ahora puedes compartirlo con"+ "" + nombrepareja +"para que sepan como demostrarse su amor")
print("Gracias por usar el programa")
