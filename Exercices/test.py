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