class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement move() method")

class Dog(Animal):
    def move(self):
        return "🐕 Running on land"

class Bird(Animal):
    def move(self):
        return "🐦 Flying in the sky"

class Fish(Animal):
    def move(self):
        return "🐟 Swimming in water"


# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
# Demonstrating polymorphism with different animal classes