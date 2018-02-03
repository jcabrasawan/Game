class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __repr__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name= "Rock"
        self.description= "A fist sized rock, suitable for bludgeoning"
        self.damage= 5
    def __str__(self):
        return self.description
    
#    def __repr__(self):
#        return self.name

class Dagger(Weapon):
    def __init__(self):
        self.name= "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 10
    def __str__(self):
        return self.description

#    def __repr__(self):
#       return self.name

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 20

    def __str__(self):
        return self.description

#    def __repr__(self):
#        return self.name

inventory = [Rock(), RustySword(), "Gold(5)", 'Crusty Bread']

def play():
    print('Escape from Cave Terror!')
    print(inventory)

def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass

    return best_weapon

play()
print('Your best weapon is: '+ repr(most_powerful_weapon(inventory)))
