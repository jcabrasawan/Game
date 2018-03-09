import items
import enemies
import barriers
import npc

from random import randint 	# Used to generate random integers.

class MapTile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	npcs = []
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = [], npcs = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
		for npc in npcs:
			self.add_npc(npc)
	
	def intro_text(self):
		text = self.description
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()

		return text
		
	def handle_input(self, verb, noun1, noun2, player):
		if(not noun2):
			if(verb == 'check'):
				for barrier in self.barriers:
					if(barrier.name):
						if(barrier.name.lower() == noun1):
							return [True, barrier.description(), player]
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), player]
				for enemy in self.enemies:
					if(enemy.name.lower() == noun1):
						return [True, enemy.check_text(), player]
				for npc in self.npcs:
					if(npc.name.lower() == noun1):
						return [True, npc.check_text(), player]
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1 or noun1 in self.items[index].synonyms):
						if(isinstance(self.items[index], items.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							player.inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, player]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, player]
			elif(verb == 'drop'):
				for index in range(len(player.inventory)):
					if(player.inventory[index].name.lower() == noun1):
						player.inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % player.inventory[index].name
						self.add_item(player.inventory[index])
						player.inventory.pop(index)
						return [True, drop_text, player]

		for list in [self.barriers, self.items, self.enemies, self.npcs]:
			for item in list:
				[status, description, player] = item.handle_input(verb, noun1, noun2, player)
				if(status):
					return [status, description, player]
					
		for list in [self.barriers, self.items, self.enemies, self.npcs]:			# Added to give the player feedback if they have part of the name of an object correct.
			for item in list:
				if(item.name):
					if(noun1 in item.name):
						return [True, "Be more specific.", player]
			
		return [False, "", player]
		
	def add_barrier(self, barrier):
		if(len(self.barriers) == 0):
			self.barriers = [barrier]		# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)	# Add to the list if it is not empty.
			
	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if(len(self.enemies) == 0):
			self.enemies = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)	# Add to the list if it is not empty.
			
	def add_npc(self, npc):
		if(len(self.npcs) == 0):
			self.npcs = [npc]		# Initialize the list if it is empty.
		else:
			self.npcs.append(npc)	# Add to the list if it is not empty.
			
	def random_spawn(self):
		pass						# Update this for your specific subclass if you want randomly spawning enemies.
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if (not self.enemies[index].is_alive()):
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if(self.x == player.x and self.y == player.y):
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)
		return player


class StartTile(MapTile):
	items = [items.Rock()]
	description = """You find yourself in a cave with a flickering torch on the wall.
		You can make out a path to the east and to the west, each equally as dark and foreboding.
		"""

class Corridor(MapTile):
	description = """You find yourself in a poorly lit corridor."""
	flavor_text = ["This portion of the cave seems particularly musty.", \
				"You head nearly brushes the low ceiling.", \
				"The sound of bats in the distance gives you a chill."]
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = [], npcs = []):	# Since this tile appears so much, I gave it its own __init__() function to add random flavor text to some of the tiles.
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
		for npc in npcs:
			self.add_npc(npc)
			
		num = randint(0,len(self.flavor_text)*3-1)	# Generate a random number. Based on our range, 1 in 3 corridors will have added flavor text.
		if(num < len(self.flavor_text)):
			self.description += " " + self.flavor_text[num]
	
	def intro_text(self):	# Since this tile appears so much, I gave it its own intro_text function to make its text more descriptive.
		text = self.description
			
		directions_clear = ['north', 'south', 'east', 'west']
		for barrier in self.barriers:
			try:
				directions_clear.pop(directions_clear.index(barrier.direction))		# Attempt to remove the barrier's direction from the list of clear directions.
			except:
				pass		# If the barrier direction is not in the list of clear directions already, then we ignore it.
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		
		if(len(directions_clear) == 1):
			text += " There is a clear pathway leading to the %s." % directions_clear[0]
		elif(len(directions_clear) == 2):
			text += " There are clear pathways leading to the %s and %s." % (directions_clear[0], directions_clear[1])
		elif(len(directions_clear) == 3):
			text += " There are clear pathways leading to the %s, %s, and %s." % (directions_clear[0], directions_clear[1], directions_clear[2])
		elif(len(directions_clear) == 4):
			text += " It appears that your path is clear in all directions." 
		
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()
		return text
		
class StoreRoom(MapTile):
	items = [items.Rusty_Sword("A rusty sword is propped against a shelf in the corner of the room."), \
			items.Red_Potion("A glowing bottle of mysterious red potion sits on one of the shelves."), \
			items.Old_Chest([items.Mountain_of_Gold()]), \
			items.Gold_Coins("A shiny handful of gold coins is on the ground near the chest.")]
	
	description = """You seem to have entered an underground storeroom!"""
		
class ExpanseSW(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the northeast."""
	
	def random_spawn(self):
		if(randint(0,3) == 0):		# 1 in 4 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
				
class ExpanseSE(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the northwest. There is a small corridor leading to the east from here."""
	
	def random_spawn(self):
		if(randint(0,2) == 0):		# 1 in 3 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
			
class ExpanseNW(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the southeast. There is a small corridor leading to the north from here."""

	def random_spawn(self):
		if(randint(0,3) == 0):		# 1 in 4 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
				
class ExpanseNE(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the southwest. A small nook lies to your east."""

	def random_spawn(self):
		if(randint(0,1) == 0):		# 1 in 2 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
			
class Nook(MapTile):
	enemies = [enemies.RockMonster()]
	description = """You have entered a shadowy nook of the cave. The only way out is back the way you came."""
	
class Cave(MapTile):
	npcs = [npc.OldMan()]
	description = """You have entered a very dark portion of the cave. Two small fires, one on each side of the room, are glowing softly."""
				
class NearVictory(MapTile):
	description = """You can see a light to the east at the end of this corridor. Could that be your way out?"""

class VictoryTile(MapTile):
	description = """You see a beast light in the distance...
		It grows as you get closer! It's sunlight!	
		Victory is yours!
		"""

class Start(MapTile):
	items = [items.Ancient_Coin('An antique coin sits on the ground. '), items.Fluffy_Blanket('A baby blanket is next to the coin. It looks soft.'), items.Toy_Skull('A beaten-up toy skull is next to the blanket.')]
	description = "You're in a small, drab room with no apparent way out."
	item_taken = False
	
	def intro_text(self):
		text = self.description
		if(not self.item_taken):
			text += " You feel a temptation to pick up one of the items."
		
		directions_blocked = []
		
		#for enemy in self.enemies:
		#	if (enemy.direction):
		#		if(enemy.direction not in directions_blocked):
		#			directions_blocked.append(enemy.direction)
		#	text += " " + enemy.check_text()
		#for barrier in self.barriers:
		#	if (barrier.direction):
		#		if(barrier.direction not in directions_blocked):
		#			if(barrier.verbose):
		#				text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()
		return text
		
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if (not self.enemies[index].is_alive()):
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if(self.x == player.x and self.y == player.y):
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very agitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)
		
		class_item_counter = 0
		for item in self.items:
			if(isinstance(item, items.Class)):
				class_item_counter += 1
		if(class_item_counter < 3):	#If a class item has been taken
			self.item_taken = True
			self.items = []
			player.x = 0
			player.y = 1
		return player
		
		#something wrong: since the count is always < 3 it will always tp back to 0,1 w/every update room
			
					

class VillageNW(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the southeast."

class VillageN(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the south."

class VillageNE(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the southwest."

class VillageCenter(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village extends in all directions."

class VillageE(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the west."

class VillageSW(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the northeast."

class VillageS(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the north."

class VillageSE(MapTile):
   
	description = "It's a small village with plenty of friendly villagers. The village expands before you to the northwest."

class Forest(MapTile):
	
	description = "You're surrounded by tall trees."
	
class ForestL(MapTile):
	description = "You're surrounded by tall trees. You can hear muffled chatter through the trees to the east."
class ForestR(MapTile):
	description = "You're surrounded by tall trees. You can hear muffled chatter through the trees to the west."

class ForestPath(MapTile):
	description = "You're on a small path surrounded by tall trees with %s."

	def intro_text(self):	# Since this tile appears so much, I gave it its own intro_text function to make its text more descriptive.
		text = self.description
			
		directions_clear = ['north', 'south', 'east', 'west']
		for barrier in self.barriers:
			try:
				directions_clear.pop(directions_clear.index(barrier.direction))		# Attempt to remove the barrier's direction from the list of clear directions.
			except:
				pass		# If the barrier direction is not in the list of clear directions already, then we ignore it.
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		
		if(len(directions_clear) == 1):
			text += " There is a clear pathway leading to the %s." % directions_clear[0]
		elif(len(directions_clear) == 2):
			text += " There are clear pathways leading to the %s and %s." % (directions_clear[0], directions_clear[1])
		elif(len(directions_clear) == 3):
			text += " There are clear pathways leading to the %s, %s, and %s." % (directions_clear[0], directions_clear[1], directions_clear[2])
		elif(len(directions_clear) == 4):
			text += " It appears that your path is clear in all directions." 
	


class Clearing(MapTile):
	description = "It's a small clearing."
	
class House(MapTile):
	description = "TODO House"

class Door(MapTile):
	description = "TODO Door"
		
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Start(barriers = [barriers.Wall('e'), barriers.Wall('s'), barriers.Wall('w')])],
		[VillageNW(barriers = [barriers.Wall('s'), barriers.Wall('n')]),	VillageN(),  											VillageNE(),	ForestR(),		ForestPath(),  														Forest(),															Clearing(),									Clearing()],
		[House(barriers = [barriers.Wall('n'), barriers.Wall('s')]),		VillageCenter(barriers = [barriers.WoodenDoor('w')]),	VillageE(),		ForestPath(),	ForestPath(barriers = [barriers.Wall('s')]),   						ForestPath(barriers = [barriers.Wall('n')]),						Clearing(), 								Clearing()],
		[VillageSW(),														VillageS(),												VillageSE(),	ForestR(),		ForestPath(barriers = [barriers.Wall('w'), barriers.Wall('e')]),	Forest(barriers = [barriers.Wall('w')]),							Forest(),									Forest()],
		]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j,i)	# If there are implied barriers (e.g. edge of map, adjacent None room, etc.) add a Wall.
						
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'north'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'south'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'west'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'east'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]
			
	def add_implied_barriers(self, x, y):

		[status, text] = self.check_north(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'north':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('n'))	
				
		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'south':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('s'))	
			
		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'east':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('e'))	
			
		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'west':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('w'))	
		
	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if(room):
					room.update(player)
		return player