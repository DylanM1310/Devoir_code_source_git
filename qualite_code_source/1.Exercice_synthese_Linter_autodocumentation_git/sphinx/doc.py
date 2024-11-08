class Calculatrice:
    """
    Une classe utilisée pour effectuer des opérations mathématiques de base.
    """

    def __init__(self, a, b):
        """
        Initialise la calculatrice avec deux nombres.

        Parameters:
        a (int, float): Le premier nombre.
        b (int, float): Le second nombre.
        """
        self.a = a
        self.b = b

    def addition(self):
        """
        Calcule la somme de deux nombres.

        Returns:
        int, float: La somme de self.a et self.b.
        """
        return self.a + self.b

    def soustraction(self):
        """
        Calcule la différence entre deux nombres.

        Returns:
        int, float: La différence entre self.a et self.b.
        """
        return self.a - self.b

    def multiplication(self):
        """
        Calcule le produit de deux nombres.

        Returns:
        int, float: Le produit de self.a et self.b.
        """
        return self.a * self.b

    def division(self):
        """
        Calcule le quotient de deux nombres.

        Returns:
        float: Le quotient de self.a et self.b.
        
        Raises:
        ValueError: Si self.b est égal à 0.
        """
        if self.b == 0:
            raise ValueError("Le dénominateur ne peut pas être 0.")
        return self.a / self.b


# Exemple d'utilisation :
calculatrice = Calculatrice(10, 5)
print(f"Addition: {calculatrice.addition()}")
print(f"Soustraction: {calculatrice.soustraction()}")
print(f"Multiplication: {calculatrice.multiplication()}")
print(f"Division: {calculatrice.division()}")
