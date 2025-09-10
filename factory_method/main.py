from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1)
    p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2)
    p3 = ny.order_pizza("veggie"); print("Fede ordered:", p3)
    p4 = chi.order_pizza("pepperonI"); print("Juana ordered:", p4)
    

if __name__ == "__main__":
    main()
