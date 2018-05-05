import items

class NPC:
	name = "Do not create raw NPCs!"
	description = "There is no description here because you should not create raw NPC objects!"
	
	goods = []	# Stuff an NPC is carrying.
	quantities = []	# Quantities of that stuff.
	
	first_encounter = True			# Used to do something different on first encounter.
	
	def __str__(self):
		return self.name
		
	def check_text(self):
		if(self.first_encounter):
			text = self.first_time()
			return text
		else:
			return self.description

	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		return "The %s doesn't seem to have anything to say." % self.name		

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		return self.description
		
	def handle_input(self, verb, noun1, noun2, player):
		return [False, None, player]


class OldMan(NPC):
	name = "Merchant"
	goods = [items.Green_Potion(value=15), items.Red_Potion(value = 15), items.Crusty_Bread(value = 5)]
	quantities = [-1, -1, 2]		# Set quantity to -1 if you want it to be infinite.
	
	description = "This man looks like he has the stuff. You want it."
	
	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		print("The money man says: I can sell the stuffs, if you are interested:")
		for item in self.goods:
			if item.value > 0:
				if(self.quantities[self.goods.index(item)] > 0):
					quantity = "quantity = %d" % self.quantities[self.goods.index(item)]
				else:
					quantity = "quantity = unlimited"
				print("* " + item.name.title() + " (" + str(item.value) + " gold, " + quantity + ")")
		return ""
		
	def give(self, item, inventory):
		for good in self.goods:
			if(good == item):
				inventory.append(good)
				if(self.quantities[self.goods.index(good)] > 0):
					self.quantities[self.goods.index(good)] -= 1
		for index in reversed(range(len(self.quantities))):	# Get rid of items with zero quantity.
			if(self.quantities[index] == 0):
				self.quantities.pop(index)
				self.goods.pop(index)
		return inventory

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		text = self.description
		text += " You look like a turtle."
		return text
		
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'merchant' or noun1 == 'money man' or noun1=="man"):
			if(verb == 'check'):
				return [True, self.check_text(), player]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, player]
		elif(verb == 'take'):
			for good in self.goods:
				if(good.name.lower() == noun1):
					if(good.value == 0):
						player.inventory = self.give(good, player.inventory)
						return [True, "The merchant threw the %s at you." % good.name, player]
					else:
						return [True, "'Hey, what are you trying to pull? If you want that, the cost is %d gold.'" % good.value, player]
		return [False, "", player]

class Villager_Basic(NPC):
	name: "Villager"
	goods= [items.Shroom(value=1000), items.Old_Baguette(value = 5)]
	quantities=[1]

	description: "Just your generic, nondescript Villager."
	def talk(self):
		print("Oh. Hey. Found you passed out on the north side of town, dragged you to my place.")
	
	def give(self, item, inventory):
		for good in self.goods:
			if(good == item):
				inventory.append(good)
				if(self.quantities[self.goods.index(good)] > 0):
					self.quantities[self.goods.index(good)] -= 1
		for index in reversed(range(len(self.quantities))):	# Get rid of items with zero quantity.
			if(self.quantities[index] == 0):
				self.quantities.pop(index)
				self.goods.pop(index)
		return inventory

	
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'villager' or noun1 == 'meme' or noun1=="memelord"):
			if(verb == 'check'):
				return [True, self.check_text(), player]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, player]
		elif(verb == 'take'):
			for good in self.goods:
				if(good.name.lower() == noun1):
					if(good.value == 0):
						player.inventory = self.give(good, player.inventory)
						return [True, "The villager tossed you the %s" % good.name, player]
		elif(verb == 'steal'):
			for good in self.goods:
				if player.is_thief = True:
					player.inventory = self.give(good, player.inventory)
					return [True, 'Yo man, what gives?! (you obtained the %s' % good.name]
		else:
			return [True, "'dude, that's not very cool. if you want it, you gotta give me %s gold." % good.value, player]
		return [False, "", player]	

