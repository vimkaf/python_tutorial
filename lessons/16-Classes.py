"""
A class is a template that contains attributes(variables) and behaviour(methods/functions)
Class
    - Attributes / variables
    - Behaviour / methods
"""
#For convinience class name should start with an uppercase
class Car:

    #static or class variables
    tyres = 4
    color = None
    model = None
    manufacturer = None
    numOfGears = 4
    numOfDoors = 4

    #Constructor
    def __init__(self,man,model,col):
        #instance variables
        self.manufacturer = man
        self.model = model
        self.color = col
        print("Object created")


    def start(self):
        print(self.model , "is running")

    def increaseSpeed():
        pass

    def stop(self):
        print(self.model , "is not running")


    def reverse():
        pass

testCar = Car("Toyota","Camry","Blue")
testCar.start()
testCar.stop()
# print(testCar.manufacturer)


#print(Car.__dict__)

# model = input("Enter the model of your car: ")
# color = input("Enter the color of your car: ")
# manufacturer = input("Enter the manufacturer of your car: ")

# userCar = Car(manufacturer,model,color)

# print(userCar.__dict__)


# print(userCar.numOfGears)
# lexus450 = Car()

# lexus450.manufacturer = "Lexus"
# lexus450.color = "Black"
# lexus450.model = "L450"
# lexus450.numOfGears = 6
# print(lexus450.color)

# mercedes = Car()
# mercedes.color = "Red"
# mercedes.model = "E-Classic"
# mercedes.numOfDoors = 2

