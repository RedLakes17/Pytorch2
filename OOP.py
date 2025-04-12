#En OOP pdoemos crear clases con metodos y atirbutos 

class BankAccount(): #Clase
    def __init__(self, balance):
        self.balance=balance #atributo
    def deposit(self, amount): #Metodo
        self.balance= self.balance + amount


cuenta1=BankAccount(100) #Creamos un objeto de la clase
cuenta1.deposit(300) #Usamos un metodo
print(cuenta1.balance) #Consultamos el atributo