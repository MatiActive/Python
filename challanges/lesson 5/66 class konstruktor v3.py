class Pizza: 
    def __init__(self):
        self.ingredients = []
    def addIngredients(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)
        else: print("to nie jest skladnik pizzy")
            
    def showIngredients(self):
        print("Skladniki : ",self.ingredients)

Pizza = Pizza()
Pizza.addIngredients("ser")
Pizza.addIngredients("pomidor")
Pizza.addIngredients("pieczarki")
Pizza.showIngredients()