# class_static_methods_demo.py

class Calculator:
    """Class demonstrating static and class methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers without needing class state."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product and accesses the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b