import items

class Player:
	def __init__(self):
		self.inventory = [items.Rock(),
						items.Dagger(),
						items.Crusty_Bread()]
        self.gold = 0
        self.hp = 100
        self.mp = 0
        self.carry = 0
        self.x = 2
        self.y = 3  
        
        mage = False
        warrior = False
        thief = False
        

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item).title())
			best_weapon = self.most_powerful_weapon()
		print("* %i Gold" % self.gold)
		print("Your best weapon is your {}".format(best_weapon))
	
	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass
		return best_weapon
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)
		
	def consolidate_inventory(self):
		self.move(dx=-1, dy=0)
		
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		return [False, ""]
		
	def update_inventory(self):
		gold_indices = []
		gold_total = 0
		for index in range(len(self.inventory)):
			if(isinstance(self.inventory[index], items.Gold)):
				gold_total += self.inventory[index].value
				gold_indices.append(index)
		if(gold_total > 0):
			for index in gold_indices:	
				self.inventory.pop(index)
			self.gold += gold_total
			print("Your wealth increased by %d Gold." % gold_total)
    
              
    def update_class(self):
        for item in self.inventory:
            if(isinstance(item, items.Toy_Skull):
               self.mage = True   
               print("You have now become a Mage.")
               print(class_description.mage)
            
            elif(isinstance(item, items.Fluffy_Blanket):
               self.warrior = True
               print("You have now become a Warror.")
               print(class_description.warrior)
           
            elif(isinstance(item, items.Ancient_Coin):
               self.thief = True
               print("You have now become a Thief.")
               print(class_description.thief)
                
            else: 
                print('You cannot change classes right now.')
    
                 
            print('You have '+self.hp+' remaining HP.')
            print('You have '+self.mp+' remaining MP.')
            print('You can carry '+self.carry+' more items.')
       
    def mage(self):
        self.hp = 75
        self.mp = 75
        self.carry = 25

        description = "You can do all sorts of mage-like things now " \
                            "like eat souls and fight with mushrooms. Because obviously that's how this all works."

    def warrior(self):
        self.hp = 125
        self.mp = 0
        self.carry = 20

        description = "You're an all-around cool dude warrior, well-loved by everyone. " \
                            "You were the bomb back in high school, voted most likely to be successful for 3 years, but " \
                            "you followed your dreams and now you bake for a living. " \
                            "However, all of your pastries are so bad they're basically weapons. At least you're happy."

    def thief(self):
        self.hp = 100
        self.mp = 0
        self.carry = 50

        description = "You're a thief, but not a very good one. No one has any clue who you are or where you came from. "\
                            "You seem like a nice person at first, but everyone has an inherent distrust of you. "\
                            "You've had to resort to stealing anything you can get your hands on, even if that person is "\
                            "completely aware of you."
  
         