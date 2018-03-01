class NPC:
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects.")
        
        self.name = "enter a name within individual subclass."
        self.hp = 'enter a value within individual subclass.'
        self.dmg = 'enter a value within individual subclass.'

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0
    
    def is_dead(self):
        return self.hp = 0
    
    def is_soulless(self):
        return self.hp = 50000
    
    def handle_input(self, verb, noun1, noun2, inventory, player.playerType):
		return [False, None, inventory]
	

class VillagerBasic(NPC):
    def __init__(self):
        self.name = "Villager"
        self.description = " A Basic Villager. Likes Starbucks, Blondes, and Instagram"
        self.hp = 80

class Villager(NPC)
    def __init__(self):
        
