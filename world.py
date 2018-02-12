class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a sublass instead!")

class StartFile(MapTitle):
    def intro_text(self):
        return ""
        
