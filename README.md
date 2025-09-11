# TP3 – Factory Method & Abstract Factory

## Decisiones de Diseño: Extensión del Patrón *Factory Method*

### Problema del *Simple Factory*
En el enfoque de *Simple Factory*:
- Toda la creación está centralizada en `SimplePizzaFactory` que usa un `if/else` o `switch` en `create_pizza(kind)`.
- `PizzaStore` depende directamente de la *factory* y de su método.
- La *factory* depende de cada producto concreto (`CheesePizza`, `VeggiePizza`, etc.).

#### Problemas
- **Alto acoplamiento**: cada vez que se agrega una pizza nueva hay que modificar el `switch` de la factory.
- **Violación de OCP** (*Open/Closed Principle*): la factory cambia con cada extensión.

### Solución
Con *Factory Method*:
- La creación se delega a cada tienda concreta, que redefine `create_pizza(kind)` e instancia sus propios productos.
- El cliente trabaja con la abstracción `PizzaStore`, sin conocer la factory concreta.
- Cada tienda concreta conoce sólo sus productos.  
  Ejemplo: el estilo Nueva York es creado en `NYPizzaStore`.

#### Beneficios
- **Menor acoplamiento**: para agregar una nueva variedad, sólo se modifica el `create_pizza` de la tienda correspondiente.
- **Cumple OCP**: se extiende agregando clases sin tocar código existente.
- **Cumple DIP** (*Dependency Inversion Principle*): el cliente depende de la abstracción (`PizzaStore`), no de la factory concreta.

---

## Decisiones de Diseño: Extensión del Patrón *Abstract Factory*

### Problema del *Factory Method*
El *Factory Method* permite crear nuevos estilos de pizza (`Veggie`, `Pepperoni`, etc.),  
pero **no asegura la consistencia de ingredientes por región**:
- Persiste un acoplamiento indirecto entre `Pizza` y los ingredientes concretos.

### Solución con *Abstract Factory*
- Se crearon las clases de ingredientes (`Dough`, `Sauce`, `Cheese`, `Pepperoni`, `Clams`, `Pepper`, `Mushroom`, `Onion`, `Garlic`).
- La interfaz `PizzaIngredientFactory` se extendió con métodos para crear estos ingredientes.
- Cada pizza concreta (`VeggiePizza`, `PepperoniPizza`, etc.) implementa `prepare()` usando la factory de ingredientes, en lugar de instanciar ingredientes directamente.

#### Beneficios
- Las pizzas dependen de la **interfaz** `PizzaIngredientFactory`, no de clases concretas.
- Se asegura la **consistencia regional**:  
  - `NYPizzaIngredientFactory` → ingredientes de NY.  
  - `ChicagoPizzaIngredientFactory` → ingredientes de Chicago.
- Diseño **robusto y extensible**: futuras variedades de ingredientes y pizzas se pueden añadir sin modificar código existente.

---

## Decisiones de Diseño de *Testing*

- **Probar el contrato, no la implementación interna**: verificamos que `order_pizza(kind)` devuelva un `Pizza` del subtipo correcto y que, tras `prepare()`, los atributos de ingredientes queden seteados conforme a la factory de su región.

### Factory Method
- Se testea que cada `PizzaStore` cree sus propios productos:  
  - `NYPizzaStore` → pizzas NY.  
  - `ChicagoPizzaStore` → pizzas Chicago.
- Se valida que un `kind` desconocido levante `ValueError`.

### Abstract Factory
- Se valida la **consistencia regional**: los ingredientes provienen de la factory de esa región, comparando con lo que devuelve `NYPizzaIngredientFactory` o `ChicagoPizzaIngredientFactory`.
- Para las verduras (onion, garlic, mushroom, pepper), se testean cada atributo por separado (no como un objeto `Veggies` agrupado).

### Inyección de Dependencias (DIP)
- Las pizzas reciben la fábrica de ingredientes desde afuera.  
  Esto garantiza que usan los objetos proporcionados por la factory inyectada y no crean dependencias internas, permitiendo testear su comportamiento de forma aislada.

---

