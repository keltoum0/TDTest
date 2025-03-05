class CartePizzeria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self) -> bool:
        return len(self.pizzas) == 0
    
    def nb_pizzas(self) -> int:
        return len(self.pizzas)
    
    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)
    
    def remove_pizza(self, name: str):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")
    
    def __str__(self):
        return "\n".join(str(pizza) for pizza in self.pizzas) if self.pizzas else "La carte est vide."