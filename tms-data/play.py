from dataclasses import dataclass, field

from typing import Tuple, List

@dataclass
class Person(order=True):
    sort_index = field(init=False, repr=False)
    name: str = "someone"
    age: int = "1"
    height: float = "1.60"
    house_coords: Tuple[float, float] = (38.0, 38.0,)
    email: str = 'joe@dataquest.io'
    
    def __post_init__(self):
        self.sort_index = self.age

@dataclass
class People():
    people: List[Person]

p1 = Person(name="panos", age=33, height=1.84, email="kapsali29@gmail.com", house_coords=(40.74, 39.80,))
p2 = Person(name="vas", age=30, height=1.70, email="kapsali29@gmail.com", house_coords=(40.74, 39.80,))
pe = People([p1,p2])
print(p1)
print(p1.name)
print(pe)

print(p1 == p1)
print(p1 == p2)
print(Person() == Person())