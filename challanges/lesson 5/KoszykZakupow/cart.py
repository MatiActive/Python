from product import *

class Card:
    def __init__(self):
        self.__productsCard = []
        self.__productsValue = 0
    def addProduct(self, product):
        if isinstance(product, Product):
            if product not in self.__productsCard:
                self.__productsCard.append(product)
                self.calculateCard()
    def calculateCard(self):
        self.__productsValue = 0
        for i in self.__productsCard:
            self.__productsValue += i.price
    
    def __str__(self):
        strData= "\n Product List :"
        for i in self.__productsCard:
            strData += "\n - "+ str(i.name) + " " + str(i.price)
        strData += "\n Card Value " + str(self.__productsValue)
        return strData