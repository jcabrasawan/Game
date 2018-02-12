class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0


class Shroom(Enemy):
	def __init__(self):
		self.name = "Shroom"
		self.hp = 10
		self.damage = 2


class Cactus(Enemy):
	def __init__(self):
		self.name = "Cactus"
		self.hp = 30
		self.damage = 10


class ButterflyColony(Enemy):
	def __init__(self):
		self.name = "Colony of Butterflies"
		self.hp = 100
		self.damage = 4


class Rock(Enemy):
	def __init__(self):
		self.name = "Rock"
		self.hp = 80
		self.damage = 15
		
class VillagerRage(Ememy):
        def __init__(self):
                self.name = "Enraged Villager"
                self.hp = 120
                self.damage = 15

class VillagerSouless(Ememy):
        def __init__(self):
                self.name = "Souless Villager"
                self.hp = 100
                self.damage = 20
