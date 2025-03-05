import unittest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria, CartePizzeriaException
from pizza import Pizza

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()
        self.pizza_mock = MagicMock(spec=Pizza)
        self.pizza_mock.name = "MockPizza"
    
    def test_is_empty_initially(self):
        self.assertTrue(self.carte.is_empty())
    
    def test_add_pizza(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)
    
    def test_remove_pizza_success(self):
        self.carte.add_pizza(self.pizza_mock)
        self.carte.remove_pizza("MockPizza")
        self.assertTrue(self.carte.is_empty())
    
    def test_remove_pizza_not_found(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Inexistante")

if __name__ == "__main__":
    unittest.main()