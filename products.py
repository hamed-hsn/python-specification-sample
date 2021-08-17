
class Product:

    def __init__(self, name, price, color):
        self.__name = name
        self.__price = price
        self.__color = color
    
    @property
    def name(self):
        return self.__name
    
    @property
    def color(self):
        return self.__color
    
    @property
    def price(self):
        return self.__price
    
    def __repr__(self):
        return f'product {{name :{self.__name} - color : {self.__color} - price : {self.__price}}}'
        