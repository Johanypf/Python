import math


class Calculadora:
    

    def suma(self,x,y):
        return x + y
    
    def resta(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def division(self,x,y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Divsion por 0 no permitido"
    
    
    def potencia(self,x,y):
        return(math.pow(x,y))
    
    def raiz(self,x):
        if x < 0:
            return ("Error: No se puede calcular Raiz cuadrada de Un Numero Negativo.")
        return(math.sqrt(x))
    
    def seno(self,x):
        return(math.sin(x))
    
    def menu(self):
        while True:
            print("\n------Calculadora Cientifica ------")
            print("1- Suma")
            print("2- Resta")
            print("3- Multiplicacion")
            print("4- Division")
            print("5- Potencia")
            print("6- Raiz Cuadrada")
            print("7- Seno")
            print("8- Salir")

            opcion = input("Digite Opcion Valida entre 1- 8: ")

            if opcion ==8:
                    print("Saliendo..... ")
                    break
            
            if opcion in ["1", "2","3",'4','5']:
                num1 = float(input("Digite Primer Numero: "))
                num2 = float(input("Digite Segundo Numero: "))
                if opcion == "1":
                    print(f" Resultado :  {self.suma(num1,num2)}")
                elif opcion == "2":
                    print(f" Resultado : {self.resta(num1,num2)}")
                elif opcion == "3":
                    print(f" Resultado : {self.multiply(num1,num2)}")
                elif opcion == "4":
                    print(f" Resultado : {self.division(num1,num2)}")
                elif opcion == "5":
                    print(f" Resultado : {self.potencia(num1,num2)}")

            elif opcion in ["6", "7"]:
                 num1 = float(input("Digite el Numero: "))
                 if opcion == "6":
                     print(f" Resultado : {self.raiz(num1)}")
                 elif opcion == "7":
                     print(f" Resultado : {self.seno(num1)}")
            
            else:
                print(f"Opcion No valida.., Por favor seleccione una Opcion entre 1-8")



if __name__ == "__main__":
    cal = Calculadora()
    cal.menu()










