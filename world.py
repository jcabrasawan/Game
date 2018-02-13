class MapTile:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a sublass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return "Welcome! Please choose one item to continue!"

class World:
    map = [
        [StartTile()]
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
            return [True, "You head to the north."]
        else:
            return [False, "There doesn't seem to be anything to the north."]
			
    def check_south(self, x, y):
        if y+1 < 0:
            room = None
        try:
            room = self.map[y+1][x]
        except IndexError:
            room = None
    
        if(room):
            return [True, "You head to the south."]
        else:
            return [False, "There doesn't seem to be anything to the south."]

    def check_west(self, x, y):
        if x-1 < 0:
            room = None
        try:
            room = self.map[y][x-1]
        except IndexError:
            room = None

        if(room):
            return [True, "You head to the west."]
        else:
            return [False, "There doesn't seem to be anything to the west."]

    def check_east(self, x, y):
        if x+1 < 0:
            room = None
        try:
            room = self.map[y][x+1]
        except IndexError:
            room = None

        if(room):
            return [True, "You head to the east."]
        else:
            return [False, "There doesn't seem to be anything to the east."]

