from CartePizzeria import CartePizzeria, CartePizzeriaException
from pizza import Pizza

if __name__ == "__main__":
  
    carte = CartePizzeria()
    

    pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
    pizza2 = Pizza("Pepperoni", ["tomate", "mozzarella", "pepperoni"], 10.0)
    pizza3 = Pizza("Quatre Fromages", ["tomate", "mozzarella", "gorgonzola", "parmesan", "chèvre"], 12.0)
    
    carte.add_pizza(pizza1)
    carte.add_pizza(pizza2)
    carte.add_pizza(pizza3)
    
  
    print("Carte de la pizzeria:")
    print(carte)
    

    try:
        carte.remove_pizza("Pepperoni")
        print("\nAprès suppression de la pizza Pepperoni:")
        print(carte)
    except CartePizzeriaException as e:
        print(e)
    
   
    print("\nLa carte est vide ?", carte.is_empty())
