class MapTile:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a sublass instead!")

class Start(MapTile):
    def intro_text(self):
        return "Welcome! Please choose one item to continue!"
#find out a way to teleport from this tile to the village, will probably go in this class.

class Village(MapTile):
    def intro_text(self):
        return "It's a small village with plenty of friendly villagers."

class Blank(MapTile):
    def intro_text(self):
        return "CONSTRUCTION TILE FOR GMs"

class Forest(MapTile):
    def intro_text(self):
        return "You're surrounded by tall trees."
class ForestL(MapTile):
    def intro_text(self):
        return "You're surrounded by tall trees. You can hear muffled chatter through the trees to your right."
class ForestR(MapTile):
    def intro_text(self):
        return "You're surrounded by tall trees. You can hear muffled chatter through the trees to your left."

class ForestPathN(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees that travels south. It doesn't seem to be well-traveled."
class ForestPathM(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees with branches lying to your left, right, and north. It doesn't seem to be well-traveled."
class ForestPathtoS(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees running east-west with a clear path south. It doesn't seem to be well-traveled."
class ForestPathNS(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees running north-south."
class ForestPath(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees running east-west. You can see a break in the trees to your left."

class Clearing(MapTile):
    def intro_text(self):
        return "It's a small clearing."
    
class World:
    map = [
        [None, None, None],
        [None,  Start(),   None,    None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
        [None, Blank(),   Blank(),  Village(),  Village(),  Village(),  ForestR(),   ForestPathN(),   Forest(),   Clearing(), Clearing(), Forest(),  None],
        [None, ForestL(),  Village(),  Village(),  Village(),  ForestPath(), ForestPathtoS(),   ForestPathM(), Clearing(), Clearing(), Forest(), Forest(),  None],
        [None, ForestL(),  Village(),  Village(),  Village(),  ForestR(), ForestPathNS(), Forest(),   Forest(),   Forest(),   Forest(), Forest(),   None],
        ]
        
    def __init__(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if(self.map[i][j]):
                    self.map[i][j].x = j
                    self.map[i][j].y = i
					
    def tile_at(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.map[y][x]
        except IndexError:
            return None
			
    def check_north(self, x, y):
        if y-1 < 0:
    	    room = None
        try:
            room = self.map[y-1][x]
        except IndexError:
    	    room = None
		
        if(room):
            return [True, "Northward Ho!"]
        else:
            return [False, "Nah fam."]
			
    def check_south(self, x, y):
        if y+1 < 0:
            room = None
        try:
            room = self.map[y+1][x]
        except IndexError:
            room = None
    
        if(room):
            return [True, "South, Baby!"]
        else:
            return [False, "Nah fam."]

    def check_west(self, x, y):
        if x-1 < 0:
            room = None
        try:
            room = self.map[y][x-1]
        except IndexError:
            room = None

        if(room):
            return [True, "West of the Word, Lets Go!"]
        else:
            return [False, "Nah fam."]

    def check_east(self, x, y):
        if x+1 < 0:
            room = None
        try:
            room = self.map[y][x+1]
        except IndexError:
            room = None

        if(room):
            return [True, "East."]
        else:
            return [False, "Nah fam."]

