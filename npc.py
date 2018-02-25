class NPC:
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0
    
    def handle_input(self, verb, noun1, noun2, inventory, player.playerType):
		return [False, None, inventory]
	

class VillagerBasic(NPC):
    def __init__(self):
        self.name = "Villager"
        self.description = " A Basic Villager. Likes Starbucks, Blondes, and Instagram"
        self.hp = 80

class VillagerQuest1(NPC)
    def __init__(self):
        
