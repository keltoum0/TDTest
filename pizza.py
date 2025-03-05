class CartePizzeriaException(Exception):
    """Exception levée pour les erreurs liées à la CartePizzeria."""
    pass

class Pizza:
    def __init__(self, name: str, ingredients: list, price: float):
        self.name = name
        self.ingredients = ingredients
        self.price = price
    
    def __str__(self):
        return f"{self.name} ({', '.join(self.ingredients)}) - {self.price:.2f}€"