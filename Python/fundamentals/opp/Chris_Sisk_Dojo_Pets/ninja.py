import pet

class Ninja:
    def __init__(self, first_name, last_name, pet_type, pet_info, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet_type(pet_info)
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

ninja_one = Ninja("Chris", "Sisk", pet.Dog, {"name": "Rajah", "type": "Golder Retriever", "tricks": ["Lay Down", "Sit", "Stay"]}, "Hydrolized Treats", "Hydrolized Food")

print(f"Hi, my name is {ninja_one.first_name} {ninja_one.last_name}. I have {ninja_one.treats} and {ninja_one.pet_food} for my pet.")
print(f"My pet's name is {ninja_one.pet.name}, she is a {ninja_one.pet.type} and she can do tricks like {ninja_one.pet.tricks[0]}, {ninja_one.pet.tricks[1]}, and {ninja_one.pet.tricks[2]}.")
if (ninja_one.pet.cuddles == True):
    print("I am also a good cuddler")


ninja_one.walk()
ninja_one.feed()
ninja_one.bathe()