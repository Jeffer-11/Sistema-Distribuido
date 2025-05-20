

class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model 
        
    def printMensaje(self):
        return "This is a vehicle."

class Car(Vehicle):
    def __init__(self, maker, doors, model):  
        super().__init__(maker, model)
        self.doors = doors

    def info(self):
        return f"Maker: {self.maker}, Model: {self.model}, Doors: {self.doors}"    

class Bike(Vehicle):
    def __init__(self, maker, model, weight):
        super().__init__(maker, model)
        self.weight = weight

    def info(self):
        return f"Maker: {self.maker}, Model: {self.model}, Weight: {self.weight}"

vehicleobj = Vehicle("Toyota", "Corolla")
carobj = Car("Toyota", 4, "Corolla")
bikeobj = Bike("Yamaha", "YZF-R3", 169)

print(vehicleobj.printMensaje())
print(carobj.info())
print(bikeobj.info())




