import pytest
from .store import NYPizzaStore, ChicagoPizzaStore
from .pizza import CheesePizza, ClamPizza, VeggiePizza
from .ingredients import Dough, Sauce, Cheese, Clams, NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory

# Test NYPizzaStore crea pizza de tipo CheesePizza
def test_ny_pizza_store_creates_cheese_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza, CheesePizza)

# Test ChicagoPizzaStore crea pizza de tipo ClamPizza
def test_chicago_pizza_store_creates_clam_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert isinstance(pizza, ClamPizza)

# Test Pizza de queso de NY tiene los ingredientes correctos
def test_ny_cheese_pizza_has_correct_ingredients():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    factory = NYPizzaIngredientFactory()
    assert isinstance(pizza.dough, type(factory.create_dough()))
    assert isinstance(pizza.sauce, type(factory.create_sauce()))
    assert isinstance(pizza.cheese, type(factory.create_cheese()))

# Test Pizza de almejas de Chicago tiene los ingredientes correctos
def test_chicago_clam_pizza_has_correct_ingredients():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    factory = ChicagoPizzaIngredientFactory()
    assert isinstance(pizza.dough, type(factory.create_dough()))
    assert isinstance(pizza.sauce, type(factory.create_sauce()))
    assert isinstance(pizza.cheese, type(factory.create_cheese()))
    assert isinstance(pizza.clam, type(factory.create_clam()))

# Test VeggiePizza de NY
def test_ny_veggie_pizza_ingredients():
    store = NYPizzaStore()
    pizza = store.order_pizza("veggie")
    factory = NYPizzaIngredientFactory()
    
    assert isinstance(pizza.dough, type(factory.create_dough()))
    assert isinstance(pizza.sauce, type(factory.create_sauce()))
    assert isinstance(pizza.onion, type(factory.create_onion()))
    assert isinstance(pizza.garlic, type(factory.create_garlic()))
    assert isinstance(pizza.mushroom, type(factory.create_mushroom()))
    assert isinstance(pizza.pepper, type(factory.create_pepper()))

# Test de error al ordenar pizzas fuera del menu
def test_pizza_kind_error():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    with pytest.raises(ValueError, match="No NY pizza for kind: Caprese"):
        ny_store.order_pizza("Caprese")
    with pytest.raises(ValueError, match="No Chicago pizza for kind: Caprese"):
        chicago_store.order_pizza("Caprese")

# Test de comparacion de pizzas e ingredientes de diferentes tiendas
def test_compare_ny_pizza_with_chicago_pizza():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    ny_pizza = ny_store.order_pizza("cheese")
    chicago_pizza = chicago_store.order_pizza("cheese")
    # Comparamos que tienen nombres distintos
    assert ny_pizza.name != chicago_pizza.name
    assert ny_pizza.dough.name != chicago_pizza.dough.name
    assert ny_pizza.sauce.name != chicago_pizza.sauce.name
    assert ny_pizza.cheese.name != chicago_pizza.cheese.name