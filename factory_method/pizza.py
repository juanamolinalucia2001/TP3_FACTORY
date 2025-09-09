from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; self.toppings=["Reggiano cheese"]

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name="NY Style Veggie"; self.toppings=["Reggiano cheese","Mushroom","Onion","Red Pepper"]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name="NY Style Pepperoni"; self.toppings=["Reggiano cheese","Sliced Pepperoni","Onion"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Veggie"; self.toppings=["Shredded Mozzarella","Mushroom","Onion","Red Pepper"]

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Pepperoni"; self.toppings=["Shredded Mozzarella","Sliced Pepperoni","Onion"]