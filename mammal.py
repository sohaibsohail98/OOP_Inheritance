from animal import Animal

class Mammal(Animal):
     def __init__(self, alive, hungry, sleeping, breathing, animaltype, prey, predator, origin):
        super().__init__(alive, hungry, sleeping, breathing) #This is importing the parent class into the child class
        self.animaltype = animaltype #Self is related to the class within init..
        self.prey = prey
        self.predator = predator
        self.origin = origin

     def animaltype(self):
         print("what the type of animal it is, in this case a Mammal.")

     def prey(self):
         print("a prey is something the animal would like to eat")

     def predator(self):
         print("a predator is a animal that will hunt this animal")

     def origin(self):
         print("Where the animal is from globally")


Tiger = Mammal(True, True, False, True, "Big cats", "Deer", "Crocodile", "Siberia")


