from player import player

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        action_input= get_playrt_command()
        if action_input in ["n","N","North","north"]
            print("Northward Ho!")
        elif action_input in ["s","S","South","south"]
            print("South, Baby!")
        elif action_input in ["w","W","West","west"]
            print("West of the Word, Lets Go!")
        elif action_input in ["e","E","East","east"]
            print("East.")
