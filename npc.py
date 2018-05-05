import items
from player import Player
player = Player()

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
	name = "Old Man"
	goods = [items.Shroom(value=1000), items.Crusty_Bread(value = 5), items.Cupcake(value = 20)]
	quantities = [1, 3, 1]		# Set quantity to -1 if you want it to be infinite.
	
	description = "You see an old man carrying large sacks of... something."
	
	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		print("If you're ever feeling weak, I've got just the stuff for you; at the right price, of course. [Actions: buy, take, steal]")
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
		text += 'The old man looks suprised to see you, exclaiming, "Who are you?"'
		return text
		
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'old man' or noun1 == 'merchant' or noun1=="Merchant" or noun1 == "old dude" or noun1 == 'old guy'):
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
		elif(verb == 'steal'):
			for good in self.goods:
				if(player.is_thief == True):
					player.inventory = self.give(good, player.inventory)
					return [True, "It's terribly rude to steal from an old man... (you obtained the %s , feeling incredibly guilty.)" % good.name, player]
				elif(player.is_mage == True): 
					return[True, "You can't do that, I'm afraid. [You must be a Thief to complete this action.]", player]
				elif(player.is_warrior == True): 
					return[True, "You can't do that, I'm afraid. [You must be a Thief to complete this action.]", player]
		return [False, "", player]

#steal is only returning shroom

class Villager_WD(NPC):
	name: 'Vill W.D. Ager'
	goods= [items.Shroom(value=1000), items.Old_Baguette(value = 10), items.Old_Cupcake(value = 25),]
	quantities=[1,1,1]

	description = "You see a small man a few paces away. He's wearing a nametag that says 'Vill W.D. Ager'. (You should probably call him that, he looks quite dangerous if angry)."
	
	def talk(self):
		print("What d'you want? [Actions: buy, take, steal]")
		for item in self.goods:
			if item.value > 0:
				if(self.quantities[self.goods.index(item)] > 0):
					quantity = "quantity = %d" % self.quantities[self.goods.index(item)]
				else:
					quantity = "quantity = unlimited"
				print("* " + item.name.title() + " (" + str(item.value) + " gold, " + quantity + ")")
		return ""

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		text = self.description
		text += "As you approach him, he says: Oh. Hey. Found you passed out on the north side of town, dragged you to my place. If you found anything there, then feel free to keep it."
		return text
	
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
		if(noun1 == 'villager' or noun1 == 'Vill W.D. Ager' or noun1=="vill" or noun1 == 'Vill' or noun1 == "weapons dealer" or noun1 == 'W.D.' or noun1 == 'wd'):
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
							return [True, "W.D. tossed you the %s" % good.name, player]
						else:
							return [True, "Dude, that's not very cool. if you want it, you gotta give me %s gold." % good.value, player]
		return [False, "", player]	

class Villager(NPC):
	name = 'Villager'
	goods = [items.Shroom(value=1000)]
	quantities = [1]
	
	description = "You see a villager. You can't seem to make out their face, because it's so ordinary."

	def talk(self):
		print("hello. i. am. a. villager. [Actions: take, steal]")
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

	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'villager'):
			if(verb == 'check'):
				return [True, self.check_text(), player]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, player]
			elif(verb == 'steal'):
				for good in self.goods:
					if(player.is_thief == True):
						player.inventory = self.give(good, player.inventory)
						return [True, 'oh. i. see. how. it. is. (you obtained the %s)' % good.name, player]
					elif(player.is_mage == True): 
						return[True, "You can't do that, I'm afraid. [You must be a Thief to complete this action.]", player]
					elif(player.is_warrior == True): 
						return[True, "You can't do that, I'm afraid. [You must be a Thief to complete this action.]", player]
			else:
				return [False, "", player]
		return [False, "", player]