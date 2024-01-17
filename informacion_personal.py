# DICCIONARIO

diccionario = {"Nombre":"Doris","Edad":"20","Ciudad":"Quito","Profesion":"Abogada"}

diccionario["Ciudad"] = "Ambato"

diccionario["Ocupacion"] = "Estilista"

diccionario["Telefono"] = "0945872300"

del(diccionario["Edad"])

print(diccionario)


# Se ingresa las claves: nombre, edad, ciudad, profesion. con letra mayuscula al inicio de cada palabra.
# el valor de la clave "ciudad" se cambia con una ciudad diferente; de "Quito a Ambato"
# Se agraga nueva clave y valor en el diccionario que representa una ocupacion personal: de "Abogada a Estilista"
# luego de verificar la no existencia del valor "telefono" se procede agregar en el diccionario.
# elimine la clave "Edad" del resultado
# al finalizar se realiza impresion de resultados donde muestra las siguientes claves:
# nombre, ciudad, profesion, se agrega la clave "ocupacion" y telefono.
# y no se muestra la clave "edad" porque se elimino del diccionario.