class Vehicle: 
    def __init__(self):
        self.name = "unknow"
        self.productionYear = "productionYear"
        self.MaxSpeed = "MaxSpeed"

    def VehiclePrintData(self):
        print(self.name, self.productionYear, self.MaxSpeed)

vehicle1 = Vehicle()
vehicle1.VehiclePrintData()

class Car(Vehicle):
    def PrintDataCar(self):
        self.name = "volkswagen"
        self.productionYear = 2007
        self.MaxSpeed = 200
        print("Car name: ", self.name)
        print("Production Year: ", self.productionYear)
        self.VehiclePrintData()
car1 = Car()
car1.PrintDataCar()


class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("printVehicleInfo: ", self.brand, self.name
                , self.topSpeed, self.numWheels)

    def printNumWheels(self):
        print("Vehicle.numWheels:", self.numWheels)


vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo()

class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 230
        print("printCarInfo: ", self.brand, self.name, 
                self.topSpeed, self.numWheels)

    def printVehicleInfo(self):
        print("Car.printVehicleInfo: ", self.brand, self.name
                , self.topSpeed, self.numWheels)

car1 = Car("Ford", "Mustang")
car1.printCarInfo()
car1.printVehicleInfo()
car1.printNumWheels()


class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed = 301
        print("Super car reached 300!")

superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300()
superCar1.printVehicleInfo()
superCar1.printNumWheels()

