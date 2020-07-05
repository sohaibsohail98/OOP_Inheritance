from animal import Animal

class Mammal(Animal):
    def __init__(self, alive, hungry = True, sleeping = False, breathing = True, animaltype, prey, predator, origin):
        super().__init__(alive, hungry = True, sleeping = False, breathing = True)
        self.animaltype = animaltype #Self is related to the class within init..
        self.prey = prey
        self.predator = predator
        self.origin = origin

    def ground_sea_animal(self):
        print("This type of animal is a ground sea animal, a shark")

    def prey(self):
        self.prey = "The prey of this animal, is a small fish"
        print(self.prey)

    def predator(self):
        print("The predator of this animal is a larger shark")

    def origin(self):
        print("This is originated from North Sea")


