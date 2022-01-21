class Pet:

    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.tricks = data['tricks']
        self.health = 100
        self.energy = 50
        self.sound = data["sound"]

    def sleep(self):
        self.energy += 25
        print(f"After a good nap, {self.name} now has {self.energy} energy")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"After some good food, {self.name} now has {self.energy} energy and {self.health} health")
        return self

    def play(self):
        self.health += 5
        print(f"After having some fun during play time {self.name} now has {self.health} health")
        return self
    
    def noise(self):
        print(self.sound, self.sound, self.sound)


class Dog(Pet):
    def __init__(self, data):
        super().__init__(data)
        self.cuddles = True