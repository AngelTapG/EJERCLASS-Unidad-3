class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        # Agrega un elemento a la pila
        self.pila.append(elemento)

    def desapilar(self):
        
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return "La pila está vacía"

    def esta_vacia(self):
        
        return len(self.pila) == 0

    def ver_pila(self):
        
        return self.pila

def menu():
    pila = Pila()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un elemento a la pila")
        print("2. Quitar el último elemento de la pila")
        print("3. Mostrar la pila")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            elemento = input("Introduce el elemento que deseas agregar: ")
            pila.apilar(elemento)
            print(f"Se ha agregado '{elemento}' a la pila.")

        elif opcion == "2":
            elemento = pila.desapilar()
            if elemento != "La pila está vacía":
                print(f"Se ha quitado '{elemento}' de la pila.")
            else:
                print(elemento)

        elif opcion == "3":
            print("Los elementos en la pila son:", pila.ver_pila())

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()