from abc import ABC, abstractmethod

# Ingredient products
class Dough:    
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Sauce:    
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Cheese:   
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
class Clams:    
    def __init__(self, name): self.name=name;  
    def __str__(self): return self.name
# Nuevos ingredientes
class Onion:
    def __init__(self, name): self.name=name;
    def __str__(self): return self.name
class Garlic:
    def __init__(self, name): self.name=name;
    def __str__(self): return self.name
class Mushroom:
    def __init__(self, name): self.name=name;
    def __str__(self): return self.name
class Pepper:
    def __init__(self, name): self.name=name;
    def __str__(self): return self.name
class Pepperoni:
    def __init__(self, name): self.name=name;
    def __str__(self): return self.name

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
     # Nuevos métodos abstractos
    @abstractmethod
    def create_onion(self) -> Onion: ...
    @abstractmethod
    def create_mushroom(self) -> Mushroom: ...
    @abstractmethod
    def create_garlic(self) -> Garlic: ...
    @abstractmethod
    def create_pepper(self) -> Pepper: ...
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")
    # Agrega la implementación de los nuevos métodos
    def create_onion(self) -> Onion: return Onion("Sliced Onions")
    def create_mushroom(self) -> Mushroom: return Mushroom("Mushroom")
    def create_garlic(self) -> Garlic: return Garlic("Garlic")
    def create_pepper(self) -> Pepper: return Pepper("Red Pepper")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Sliced Pepperoni")

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")
     # Implementación para nuevos ingredientes
    def create_onion(self) -> Onion: return Onion("Diced Onions")
    def create_mushroom(self) -> Mushroom: return Mushroom("Mushroom")
    def create_garlic(self) -> Garlic: return Garlic("Garlic")
    def create_pepper(self) -> Pepper: return Pepper("Green Pepper")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Sliced Pepperoni")