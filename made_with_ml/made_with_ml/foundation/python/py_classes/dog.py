"""
This module demonstrates the creation of a class plus magic functions
"""

# Creating the class
class Pet():
    """Class object for pet"""
    def __init__(self, species, name):
        """initialize a Pet"""
        self.species = species
        self.name = name

    def __str__(self):
        """Output when printing an instance of a Pet"""
        return f"{self.species} named {self.name}"
           
    def change_name(self, new_name):
        """Change the name of your Pet"""
        self.name = new_name

# Inheritance
class Dog(Pet):
    """Inherinting from the parent class Pet"""
    def __init__(self, name, breed):
        """Initializing a dog"""
        super().__init__(species="dog", name=name)
        self.breed = breed

    def __str__(self):
        """Output when printing an instance of a dog"""
        return f"A {self.breed} dogo named {self.name}"
    
    @classmethod
    def from_dict(cls, d):
        """Create a class by passing an uninstanciated class"""
        return cls(name=d["name"], breed=d["breed"])
    
    @staticmethod
    def is_cute(breed):
        """Can be called from an uninstantiated class"""
        return True

my_dog = Pet(species="dog", name="scooby")
print(my_dog)
print(my_dog.name)

my_dog.change_name(new_name="Scraby")
print(my_dog)
print(my_dog.name)

# Inherited class
scooby = Dog(breed="Great Dane", name="Scooby")
print(scooby)
scooby.change_name(new_name="scraby")
print("New name:",scooby.name)

# Create instance
d = {"name":"Cassie","breed":"Border Collie"}
cassie = Dog.from_dict(d=d)
print(cassie)

# Static method
Dog.is_cute(breed="Border Collie")
