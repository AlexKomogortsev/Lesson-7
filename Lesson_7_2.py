# Task 2

class Clothes:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Наденьте ваш {self.name}'


class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    def __str__(self):
        return f"Our {self.name} requires {self.tissue} amount of tissue"

    @property
    def tissue(self):
        return self.V / 6.5 + 5

class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    def __str__(self):
        return f"Our {self.name} requires {self.tissue} amount of tissue"

    @property
    def tissue(self):
        return self.H * 2 + 0.3


coat_Zara = Coat(name='coat', V=52)
print(coat_Zara)
suit_Massimo = Suit(name='suit', H=180)
print(suit_Massimo)
whole_tissue = coat_Zara.tissue + suit_Massimo.tissue
print(f'I have to buy {whole_tissue} amount of tissue in order to construct required clothes')
