#Polymorphism

class Animal:

    def __init__(self,type):
        self.type=type

    def speak(self):
        print("Animal speaks") 

#use super keyword to call parent class methods 

class Dog(Animal):

    def speak(self):
        
        super().speak()



        print(f"{self.type} Dog barks")

class Cat(Animal):
    def speak(self):
        
        super().speak()
        print(f"{self.type} Cat meows")

a1=Dog("Pet")
a2=Cat("Pet")    
a1.speak()
a2.speak()


