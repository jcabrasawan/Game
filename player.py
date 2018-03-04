import items
#testing git
class Player:
	def __init__(self):
		self.inventory = [items.Crusty_Bread()]
						
		self.weapon = None
		
		self.gold = 5
		
		self.hp = 30
		self.max_hp = 50
		
		self.mp = 0
		self.carry = 0
		
		self.x = 0
		self.y = 0
		
		mage = False
		warrior = False
		thief = False

	def print_inventory(self):
		print("Inventory:")
		best_weapon = None
		equipped_weapon = False
		for item in self.inventory:
			inventory_text = '* ' + str(item).title()
			if(item == self.weapon and not equipped_weapon):
				inventory_text += ' (equipped)'
				equipped_weapon = True
			print(inventory_text)
			best_weapon = self.most_powerful_weapon()
		print("* %i Gold" % self.gold)
		if(best_weapon):
			print("Your best weapon is your {}.".format(best_weapon))
		else:
			print("You are not carrying any weapons.")
	
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
		
	def update_inventory(self):
		gold_indices = []
		gold_total = 0
		for index in range(len(self.inventory)):
			if(isinstance(self.inventory[index], items.Gold)):
				gold_total += self.inventory[index].value
				gold_indices.append(index)
		if(gold_total > 0):
			for index in reversed(gold_indices):		# Reversed to avoid popping the wrong element.	
				self.inventory.pop(index)
			self.gold += gold_total
			print("Your wealth increased by %d Gold." % gold_total)
		has_weapon = False
		for item in self.inventory:
			if(item == self.weapon):
				has_weapon = True
		if not has_weapon:
			self.weapon = None	# Drop the equipped item if it is no longer in inventory.
		self.update_class()	
			
			
	def heal(self, amount):
		self.hp += amount
		if(self.hp > self.max_hp):
			self.hp = self.max_hp
			return "Your health is fully restored."
		else:
			return "Your health was restored by %d HP." % amount
			
	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			return "Your health is critical... everything is getting dark."
		else:
			return "You took %d damage." % amount
			
	def is_alive(self):
		if(self.hp <= 0):
			return False
		else:
			return True
			
	
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			if(noun1 == 'self' or noun1 == 'health' or noun1 == 'hp'):
				return [True, "Your health is currently %d / %d." % (self.hp, self.max_hp)]
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		elif(verb == 'consume'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Consumable)):
						heal_text = item.consume_description
						heal_text += " " + self.heal(item.healing_value)
						self.inventory.pop(self.inventory.index(item))
						return [True, heal_text]
		elif(verb == 'equip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Weapon)):
						if(self.weapon != item):
							self.weapon = item
							return [True, item.equip_description]
						else:
							return [True, "You already have your %s equipped." % item.name]
		elif(verb == 'unequip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Weapon)):
						if(self.weapon == item):
							self.weapon = None
							return [True, "You have unequipped your %s." % item.name]
			return [True, "That does not appear to be equipped right now."]
		return [False, ""]
		

	def update_class(self):
		for item in self.inventory:
			if(isinstance(item, items.Toy_Skull)):
				print("You have now become a Mage.")
				self.mage()
			elif(isinstance(item, items.Fluffy_Blanket)):
				print("You have now become a Warror.")
				self.warrior()
			elif(isinstance(item, items.Ancient_Coin)):
				print("You have now become a Thief.")
				self.thief()								
			else: 
				pass
	   
	def mage(self):
		self.hp = 75
		self.max_hp = 100
		self.mp = 75
		self.carry = 25
		self.mage = True   

		description = "You can do all sorts of mage-like things now " \
					"like eat souls and fight with mushrooms. Because obviously that's how this all works."
		print(description)

	def warrior(self):
		self.hp = 125
		self.max_hp = 150
		self.mp = 0
		self.carry = 20
		self.warrior = True

		description = "You're an all-around cool dude warrior, well-loved by everyone. " \
					"You were the bomb back in high school, voted most likely to be successful for 3 years, but " \
					"you followed your dreams and now you bake for a living. " \
					"However, all of your pastries are so bad they're basically weapons. At least you're happy."
		print(description)

	def thief(self):
		self.hp = 100
		self.max_hp = 150
		self.mp = 0
		self.carry = 50
		self.thief = True

		description = "You're a thief, but not a very good one. No one has any clue who you are or where you came from. "\
					"You seem like a nice person at first, but everyone has an inherent distrust of you. "\
					"You've had to resort to stealing anything you can get your hands on, even if that person is "\
					"completely aware of you."
		print(description)
  
         