from abc import ABC, abstractmethod
class BaseClass(ABC):
    def display_value(self, value):
        print(f"Value entered: {value}")
    @abstractmethod
    def abstract_method(self):
        pass
class SubClass(BaseClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method in the subclass.")
user_input = input("Enter a value: ")
obj = SubClass()
obj.display_value(user_input)
obj.abstract_method()
