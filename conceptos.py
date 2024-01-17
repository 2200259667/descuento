# Clases para demostrar herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Clases para demostrar encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # El guion bajo indica que es un atributo protegido
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def obtener_edad(self):
        return self._edad

# Clases para demostrar polimorfismo
class Figura:
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio

# Crear instancias y utilizar métodos
mi_perro = Perro("Buddy")
una_persona = Persona("Juan", 25)

print(f"{mi_perro.nombre} hace {mi_perro.hacer_sonido()}")
print(f"{una_persona.obtener_nombre()} tiene {una_persona.obtener_edad()} años")

# Ejemplo de polimorfismo
cuadrado = Cuadrado(5)
circulo = Circulo(3)

print(f"Área del cuadrado: {cuadrado.calcular_area()}")
print(f"Área del círculo: {circulo.calcular_area()}")
