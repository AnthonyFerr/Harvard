class Vending_Machine():
    def __init__(self, drinks):
        self.drinks = drinks
    
    def listDrinks(self):
        allDrinks = ", ".join(self.drinks.keys())
        print(f"We have {allDrinks}")

    def getPrice(self, drink):
        print(f"{drink} is {self.drinks.get(drink)}")

    def getDrink(self, drink):
        if drink in self.drinks:
            print(f"You received {drink}")
        else:
            print("We don't have that in stock.")
