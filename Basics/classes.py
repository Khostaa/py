class Vehicle(): #declaring class
     #init is the function that calls when the object has been created
     #and its time to initialize the object's data
     def __init__(self,bodystyle):
          self.bodystyle = bodystyle

     def drive(self,speed):
          self.mode = "driving"
          self.speed = speed

#Sub classes Car and Motorcycle are derived(inherited) from Class Vehicle
class Car(Vehicle):
     def __init__(self,enginetype):
          #super function to initialize super class
          super().__init__("Car")
          self.Wheels = 4
          self.doors = 4
          self.enginetype = enginetype

     def drive(self,speed):
          super().drive(speed)
          print("Driving my",self.enginetype,"Car at", self.speed)

class Motorcycle(Vehicle):
     def __init__(self,enginetype,hassidecar):
          super().__init__("Motorcycle")
          if (hassidecar):
               self.wheels = 3
          else:
               self.wheels = 2
          self.doors = 0
          self.enginetype = enginetype

     def drive(self,speed):
          super().drive(speed)
          print("Driving my",self.enginetype,"Motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("Electric")
mc1 = Motorcycle("gas",True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)


car1.drive(30)
car2.drive(40)
mc1.drive(50)
