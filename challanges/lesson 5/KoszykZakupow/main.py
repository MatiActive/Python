from cart import *

cart = Card()
prod1 = Phone("iphone", 1000, "red" )
prod2 = Phone("iphone2", 1200, "red2" )
tv1 = Tv("iphone3", 1300, "red1" )
cart.addProduct(prod1)
cart.addProduct(prod2)
cart.addProduct(tv1)
print(cart)