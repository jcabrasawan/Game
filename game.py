from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input= get_player_command()
        if action_input in ["n","N","North","north"]:
            player.move_north()
            print("Northward Ho!")
        elif action_input in ["s","S","South","south"]:
            player.move_south()
            print("South, Baby!")
        elif action_input in ["w","W","West","west"]:
            player.move_west()
            print("West of the Word, Lets Go!")
        elif action_input in ["e","E","East","east"]:
            player.move_east()
            print("East.")
        elif action_input in ['i', 'I', 'inventory']:
            player.print_inventory()
        else:
            print("Can't do that yet, bub.")

def get_player_command():
    return input('Action: ')


play()
        
