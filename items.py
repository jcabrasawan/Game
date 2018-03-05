from random import randint 	# Used to generate random integers.


class Item:
	name = "Do not create raw Item objects!"
	synonyms = []
	
	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."
	
	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.
	
	value = 0		# Used to establish value if item is for sale.
	
		
	def __init__(self, description = "", value = 0):
		if(description):
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description
		
		if(self.value == 0):
			self.value = value
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(not self.is_dropped):					# We may want to have a different description for a weapon the first time it is encountered vs. after it has been dropped.
			return self.intro_description
		else:
			return self.dropped_description

	def check_text(self):
		return self.description
		
	def drop(self):
		self.is_dropped = True
		
	def pick_up(self):
		self.is_dropped = False
		
	def handle_input(self, verb, noun1, noun2, player):
		return [False, None, player]
		
		
class Iron_Key(Item):
	name = "iron key"
	
	description = "An old iron key. It looks like it would open a massive door."
	dropped_description = "An old iron key is lying on the ground."		
		
		
class Consumable(Item):
	consume_description = "You should define flavor text for consuming this item in its subclass."

	healing_value = 0		# Define this appropriately in your subclass.
		
	def consume(self):
		return [self.consume_description, self.healing_value]
			
class Shroom(Item):
	name = 'Shroom'
	description = "Carried by every villager. Doesn't do anything, at least you think. They get them from the Shroom House on the west side of town."

class Crusty_Bread(Consumable):
	name = "crusty bread"
	healing_value = 10
	
	description = "Just a stale old piece of bread."
	dropped_description = "A piece of crusty bread is lying on the ground."
	consume_description = "You eat the crusty piece of bread. Your jaw aches."
			
class Red_Potion(Consumable):
	name = "red potion"
	healing_value = 50
	
	description = "A bottle of mysterious, glowing red potion. For some reason it looks healthy."
	dropped_description = "A bottle of red potion is glowing on the ground."
	consume_description = "You drink the glowing red potion. The world spins for a moment."
	
class Muffin(Consumable):
	name = "Soft Muffin"
	synonyms = ['tasty muffin']
	healing_value = 30
	
	description = 'A soft muffin. It looks tasty.'
	dropped_description = "A muffin is sitting sadly on the ground."
	consume_description = "You ate the muffin. It's quite good."

class Baguette(Consumable):
	name = 'Crunchy Baguette'
	synonyms = ['long baguette']
	healing_value = 45

	description = "A long baguette. You wonder if it's magical, but then you remember that you don't understand French, so you won't get that joke. (it isn't. but you can eat it.)"
	dropped_description = "A crunchy baguette is lying on the ground. It looks tempting."
	consume_description = "You ate the baguette. It took awhile, because, you know, it's a big piece of bread."

class Cupcake(Consumable):
	name = 'Small Cupcake'
	healing_value = 10

	description = "A small cupcake. It doesn't look all that nutritious, but who would turn down a cupcake?"
	dropped_description = "A cupcake is lying on the ground, its frosting smushed."
	consume_description = "You ate the cupcake. You feel a little sick from the sweetness."

class Weapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.
		
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]		# Return damage and a random attack description from your list.

class Rock(Weapon):
	name = "rock"
	
	description = "A fist-sized rock, suitable for bludgeoning."
	dropped_description = "A fist-sized rock lies on the ground. It looks like it would be suitable for bludgeoning someone... or something."
	equip_description = "You arm yourself with the rock."
	attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
	
	damage = 5

class Dagger(Weapon):
	name = "dagger"
	
	description = "A small dagger with some rust. It looks pretty sharp."
	dropped_description = "A dagger lies on the ground. It looks somewhat more dangerous than a rock."
	equip_description = "You take the dagger in your hand."
	attack_descriptions = ["You lunge forward with the dagger.", "You stab wildly with the dagger.", "You swing the dagger at your foe."]
	
	damage = 10

class Rusty_Sword(Weapon):
	name = "rusty sword"
	
	description = "A rusty sword. Despite its age, it still looks deadly."
	dropped_description = "There is a rusty sword lying on the ground."
	equip_description = "You arm yourself with the rusty sword."
	attack_descriptions = ["You slash with your rusty sword.", "Your rusty sword connects mightily with your enemy.", "You swing the rusty sword with all your might."]
	
	damage = 15
	

class Green_Potion(Weapon):
	name = 'Green Potion'

	description = "A bright green potion. It looks volatile, so you feel you should handle it gently. (hint: equip)"
	dropped_description = "A bright green potion lies on the ground, pulsing with light."
	equip_description = "You unstopper the Green Potion and hold it carefully."
	attack_descriptions = ["You throw some potion on the enemy.", 'You swing the ever-full bottle at your enemy.', 'You splash the potion everywhere.']

	damage = 20

class Pink_Potion(Weapon):
	name = "Pink Potion"

	description = "A bright pink potion. You take a sniff and are immediately enveloped in sparkles. You think any more exposure will cause you to die."
	dropped_description ="A bright pink potion lies on the ground, pulsing with light."
	equip_description = "You unstopper the Pink Potion and hold it carefully."
	attack_descriptions = attack_descriptions = ["You throw some potion on the enemy.", 'You swing the ever-full bottle at your enemy.', 'You splash the potion everywhere.']

	damage = 20

class Multi_Potion(Weapon):
	name = 'Tie-Die Potion'
	synonyms = ['tie-dye potion', 'tye-dye potion']

	description = "A tie-die potion. That's a pun, not a typo. Seems dangerous."
	dropped_description = "A bright tie-die potion lies on the ground, pulsing with light."
	equip_description = "You unstopper the Tie-Die Potion and hold it carefully."
	attack_descriptions = attack_descriptions = ["You throw some potion on the enemy.", 'You swing the ever-full bottle at your enemy.', 'You splash the potion everywhere.']

	damage = 30
	

class Old_Muffin(Weapon):
	name = "Old Muffin"
	synonyms = ['stale muffin']

	description = "An old, stale muffin. It feels like it'd do the damage of a heavy rock. (hint: equip)"
	dropped_description = "An old muffin lies on the ground."
	equip_description = "You carefully hold the rock-like muffin in your hand."
	attack_descriptions = ['You hit the enemy with the muffin', 'You swing viciously at it with a muffin.']

	damage = 20

class Old_Baguette(Weapon):
	name = 'Old Baguette'
	synonyms = ['stale baguette', 'long baguette']

	description = "A long, stale baguette. It's hard enough to use as a bo staff. (hint: equip)"
	dropped_description = "A stale baguette lies on the ground."
	equip_description = "You arm yourself with the baguette as if it were a baseball bat, feeling mildly ridiculous."
	attack_descriptions = ['You use your limited knowledge of wushu to attack the enemy.', 'You swing viciously at it, HOME RUN!']

	damage = 20

class Old_Cupcake(Weapon):
	name = 'Old Cupcake'
	synonyms = ['stale cupcake', 'rancid cupcake']

	description = "A stale cupcake. The icing looks rancid, and when you smell it you're immediately hit with debilitating nausea. (hint: equip)"
	dropped_description = "A rancid cupcake lies on the ground, looking altogether disgusting."
	equip_description = "You carefully handle the cupcake. You really need to wash your hand before eating anything."
	attack_descriptions = ["You wave the cupcake in front of the enemy's face.","The smell of the cupcake offends the enemy, who isn't quite as used to it as you. You relate."]

	damage = 30

class Gold(Item):
	value = 0		# Define this appropriately in your subclass.
		
	def obtain_text(self):
		return "%i gold was added to your inventory." % value

		
class Gold_Coins(Gold):
	name = "gold coins"
	value = 5		
	
	description = "A small handful of gold coins."
	dropped_description = "A shiny handful of gold coins is lying on the ground."
	

class Mountain_of_Gold(Gold):
	name = "mountain of gold"
	value = 100		
	
	description = "A lustrous mountain of gold coins."
	dropped_description = "A lustrous mountain of gold coins is lying on the ground."
	
	
class Container:
	name = "Do not create raw Container objects!"
	
	closed_description = "You should define a closed description for containers in their subclass."
	open_description = "You should define an open description for containers in their subclass."
	
	closed = True
	
	contents = []
	
	def __init__(self, items = []):
		for item in items:
			if(len(self.contents) == 0):
				self.contents = [item]
			else:
				self.contents.append(item)
	
	def add_item(self, item):
		if(len(self.contents) == 0):
			self.contents = [item]		# Initialize the list if it is empty.
		else:
			self.contents.append(item)	# Add to the list if it is not empty.
			
	def remove_item(self, item):
		removal_index = -1
		for index in range(len(self.contents)):
			if(self.contents[index].name == item.name):
				removal_index = index
		if(removal_index >= 0):
			self.contents.pop(removal_index)
	
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(self.closed):					# We may want to have a different description for a container if it is open or closed.
			return self.closed_description
		else:
			return self.open_description

	def check_text(self):
		if(self.closed):
			return self.closed_description
		else:
			if(len(self.contents) > 0):
				print("The %s contains:" % self.name)
				for item in self.contents:
					print('* ' + str(item).title())
			else:
				return "The %s is empty." % self.name
		
	def handle_input(self, verb, noun1, noun2, player):			
		return [False, "", player]

		
class Old_Chest(Container):
	name = "old chest"
	closed_description = "A battered old chest sits against the far wall, its lid shut tightly."
	open_description = "A battered old chest sits against the far wall, its lid open wide."
	
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == self.name):
			if(verb == 'check'):
				return [True, self.check_text(), player]
			if(verb == 'open'):
				if(self.closed == True):
					self.closed = False
					return [True, "You pry the lid of the battered old chest open.", player]
				else:
					return [True, "The old chest is already wide open.", player]
			if(verb == 'close'):
				if(self.closed == False):
					self.closed = True
					return [True, "You push down the lid of the old chest and it closes with a bang.", player]
				else:
					return [True, "The old chest is already closed.", player]
		elif(noun1):
			if(verb == 'take'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								pickup_text = "You took the %s from the old chest and added it to your inventory." % self.contents[index].name
								inventory.append(self.contents[index])
								self.contents.pop(index)
								return [True, pickup_text, player]
							else:
								return [True, "The %s is too heavy to pick up." % self.contents[index].name, player]
			if(verb == 'check'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								return [True, self.contents[index].check_text(), player]
		return [False, None, player]
		
class Class(Item):
	define_description = "Flavor text in subclass"
	healing_value = 0
	
	
	def teleport(self):
		pass
		
class Toy_Skull(Class):
	name = "Toy Skull"
	synonyms = ['skull']
	
	description = "A small toy skull that looks scarily realistic."
			
class Fluffy_Blanket(Class):
	name = "Baby Blanket"
	synonyms = ['fluffy blanket', 'blanket']
	
	description = "A tiny blanket that looks like it would only cover your feet."
		
class Ancient_Coin(Class):
	name = "Antique Coin"
	synonyms = ['coin', 'ancient coin']
	
	description = "An antique brittle coin. It doesn't look valuable."