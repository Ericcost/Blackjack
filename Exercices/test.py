from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(list(State))

name ="Beau"
name += " is my name"
print(name)

age = float(2)
print(f"""
I got 
{age}
years old
""")

print(name.islower())

#Classes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("wouf")

roger = Dog("Roger", 12)
print(roger.name, roger.age)
roger.bark()