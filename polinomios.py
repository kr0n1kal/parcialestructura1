bandera = 0
cant = 0
class NodoPolinomios:
    def __init__(self, idPolinomio, componente, coeficiente):
        self.idPolinomio = idPolinomio
        self.componente = componente
        self.coeficiente = coeficiente
        self.next = None


class ListaPolinomios:
    def __init__(self):
        self.Head = None

    def agregarpolinomio(self, idPolinomio, componente, coeficiente):
        nuevopolinomio = NodoPolinomios(idPolinomio, componente, coeficiente)
        if self.Head is None:
            self.Head = nuevopolinomio
        else:
            current = self.Head
            while current.next is not None:
                current = current.next
            current.next = nuevopolinomio

    def mostrarpolinomios(self):
        current = self.Head
        while current is not None:
            print(f'{current.componente}x^{current.coeficiente}', end=" ")
            if current.next is not None:
                print("+", end=" ")
            if current.coeficiente == 0:
                print("\n")
            current = current.next

    def evaluar(self, x):
        resultado = 0
        current = self.Head
        while current is not None:
            resultado += current.componente * (x**current.coeficiente)
            current = current.next
        return 'El resultado de evaluar el polinomio es: ',resultado
    
    def sumar(self, polinomio2):
        resultado = ListaPolinomios()
        current_self = self.Head
        current_otro = polinomio2.Head

        while current_self is not None or current_otro is not None:
            comp_self = current_self.componente if current_self else 0
            coef_self = current_self.coeficiente if current_self else 0
            comp_otro = current_otro.componente if current_otro else 0
            coef_otro = current_otro.componente if current_otro else 0

            if comp_self == comp_otro:
                resultado.agregarpolinomio(comp_self + comp_otro, coef_self)
                current_self = current_self.next if current_self else None
                current_otro = current_otro.next if current_otro else None
            elif comp_self > coef_otro:
                resultado.agregarpolinomio(comp_self, coef_self)
                current_self = current_self.next
            else:
                resultado.agregarpolinomio(comp_otro, coef_otro)
                current_otro = current_otro.next
        return resultado
    
    def restar(self, polinomio2):
        resultado = ListaPolinomios()
        current_self = self.Head
        current_otro = polinomio2.Head

        while current_self is not None or current_otro is not None:
            comp_self = current_self.componente if current_self else 0
            coef_self = current_self.coeficiente if current_self else 0
            comp_otro = current_otro.componente if current_otro else 0
            coef_otro = current_otro.componente if current_otro else 0

            if comp_self == comp_otro:
                resultado.agregarpolinomio(comp_self - comp_otro, coef_self)
                current_self = current_self.next if current_self else None
                current_otro = current_otro.next if current_otro else None
            elif comp_self > coef_otro:
                resultado.agregarpolinomio(comp_self, coef_self)
                current_self = current_self.next
            else:
                resultado.agregarpolinomio(-comp_otro, coef_otro)
                current_otro = current_otro.next
        return resultado

polinomios = ListaPolinomios()
while bandera == 0:
    print("BIENVENIDO AL MENU DE POLINOMIOS")
    print("1. Agregar un nuevo polinomio")
    print("2. Mostrar el Estado Actual de los polinomios")
    print("3. Suma de Polinomios")
    print("4. Resta de Polinomios")
    print("5. Evaluar Polinomios")
    print("6. Salir")
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case '1':
            idPolinomio = 0
            cantidad = int(input("Ingrese la cantidad de polinomios a ingresar: "))
            while cant != cantidad:
                idPolinomio += 1
                coeficiente = int(input("Ingrese el coeficiente del polinomio: "))
                for i in range(0, coeficiente+1):
                    componente = int(input("Ingrese el componente del polinomio: "))
                    polinomios.agregarpolinomio(idPolinomio, componente, coeficiente)
                    coeficiente-=1
                cant += 1
        case '2':
            polinomios.mostrarpolinomios()
        case '3':
            print(polinomios.sumar())
        case '4':
            print(polinomios.restar())
        case '5':
            x = int(input("Ingrese el valor de x para el polinomio: "))
            print(polinomios.evaluar(x))
        case '6':
            print("Saliendo del programa...")
            bandera = 1
        case _:
            print("No ingreso una opcion valida!")