import player
class Barrier:
	name = None
	passable = False
	state = None	# Used to store the state of doors or hidden passages.
	locked = None	# Used to store the state of locked doors, if applicable.
	
	verbose = False	# Used to determine whether or not include the barrier's description in the room description.

	def __init__(self, direction):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			raise NotImplementedError("Barrier direction is not recognized.")
	
	def description(self):
		raise NotImplementedError("Create a subclass instead!")
		
	def handle_input(self, verb, noun1, noun2, player):
		return [False, None, player]
		
class Wall(Barrier):
	def description(self):
		return "There doesn't seem to be a path to the %s." % self.direction
		
class WoodenDoor(Barrier):
	name = 'Wooden Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			return "An old wooden door blocks your path to the %s." % self.direction
		else:
			return "An old wooden door lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'door' or noun1 == 'wooden door'):
			if(verb == 'check'):
				return [True, self.description(), player]
			if(verb == 'open'):
				if(self.state == 'closed'):
					self.state = 'open'
					self.passable = True
					return [True, "You tug on the handle, and the wooden door creaks open.", player]
				else:
					return [True, "The door is already open.", player]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You slam the old wooden door shut.", player]
				else:
					return [True, "The door is already closed.", player]
			
		return [False, "", player]
		
		
class LockedDoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "An imposing door with a large iron padlock blocks a passageway to the %s." % self.direction
			else:
				return "An imposing door blocks a passageway to the %s. A large iron padlock which once held it shut lies on the ground beside it." % self.direction
		else:
			return "An imposing door lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, player):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), player]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to open the door, but the padlock holds it firmly shut. You need to unlock it first.", player]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You heave the once-locked door open.", player]
				else:
					return [True, "The door is already open.", player]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You push the massive door closed.", player]
				else:
					return [True, "The door is already closed.", player]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'iron key'):
						for index in range(len(player.inventory)):
							if(player.inventory[index].name.lower() == 'iron key'):
								player.inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You insert the iron key into the padlock and twist. The padlock falls free with a clang.", player]
						return [True, "You don't seem to have the right key for that door.", player]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This door only takes a specific key.", player]
					else:
						return [True, "What item do you plan to unlock that door with?", player]
				else:
					return [True, "The door is already unlocked.", player]
			
		return [False, "", player]
class VillageWall(Barrier):
    name = 'Village Wall'

    def description(self):
        return "There's a tall, smooth stone wall to the %s. It reminds you of a medieval castle's battlements." % self.direction

class BrokenDownWall(Barrier):
	name = 'Broken Wall'
	
	def description(self):
		return "There's a worn down section of the stone wall. It looks climbable for a healthy person."
    
	def handle_input(self, verb, noun1, noun2, player):
		if(verb == 'climb'):
			return [False, "", player]
			#if(player.hp >= 50):
			#	self.passable = True
			#	return [True, 'You scale the wall, with some difficulty', player.hp]
			#else:
			#	self.passable = False
			#	return [False, "You're too injured to climb the wall.", player.hp]

#class BigWoodenDoor(Barrier):
 
    
    