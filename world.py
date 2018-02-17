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

class ForestPath(MapTile):
    def intro_text(self):
        return "You're on a small path surrounded by tall trees. It doesn't seem to be well-traveled."

class Clearing(MapTile):
    def intro_text(self):
        return "It's a small clearing."
    
class World:
    map = [
        [Start(),   None],
        [Blank(),  Village(),  Village(),  Village(),  Forest(),   ForestPath(),   Forest(),   Clearing(), Clearing(), Forest()],
        [Forest(),  Village(),  Village(),  Village(),  Forest(), ForestPath(),   ForestPath(), Clearing(), Clearing(), Forest()],
        [Forest(),  Village(),  Village(),  Village(),  Forest(), ForestPath(), Forest(),   Forest(),   Forest(),   Forest()],
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

