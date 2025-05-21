from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("Humans walks on 2 legs.")
class Dog(Animal):
    def move(self):
        print("Dogs runs on 4 legs.")
choice = input("Enter an animal (human/dog): ").lower()
if choice == "human":
    a = Human()
    a.move()
elif choice == "dog":
    a = Dog()
    a.move()
else: print("Unknown animal.")
