import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(), items.Dagger(),"Gold(5)","Crusty Bread"]

    def print_inventory(self):
        print("Inventory:")
        for item in self.invventory:
            print("*"+ str(item))
        
        
