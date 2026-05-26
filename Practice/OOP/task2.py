
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # Atributo PRIVADO 
        self.__saldo = saldo_inicial

    # GETTER
    def consultar_saldo(self):
        return self.__saldo

    # SETTER
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Error: No puedes depositar montos negativos.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.__saldo}")
        else:
            print("Error: Fondos insuficientes o monto inválido.")

mi_cuenta1 = CuentaBancaria("BAco",500)
print(mi_cuenta1.consultar_saldo())
mi_cuenta1.depositar(500)
print(mi_cuenta1.consultar_saldo())


