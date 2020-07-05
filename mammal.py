from animal import Animal

class Mammal(Animal):
     def __init__(self, alive, hungry, sleeping, breathing, animaltype, prey, predator, origin):
        super().__init__(alive, hungry, sleeping, breathing) #This is importing the parent class into the child class
        self.animaltype = animaltype #Self is related to the class within init..
        self.prey = prey
        self.predator = predator
        self.origin = origin

     def animaltype(self):
        self.animaltype = "what the type of animal it is, in this case a Mammal."
        print(self.animaltype)

     def prey(self):
         self.prey = "a prey is something the animal would like to eat"
         print(self.prey)

     def predator(self):
         self.predator = "a predator is a animal that will hunt this animal"
         print(self.predator)

     def origin(self):
         self.origin = "Where the animal is from globally"
         print(self.origin)


Tiger = Mammal(True, True, False, True, "Big cats", "Deer", "Crocodile", "Siberia")
Tiger.animaltype()

