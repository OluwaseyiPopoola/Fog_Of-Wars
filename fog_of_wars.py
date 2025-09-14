from pyfiglet import Figlet








def main():
    game_name = 'FOG OF WARS'
    display_game_title(game_name)
    print(f"\n{input("Press Enter to start the game...")}")
    
    introduce_game_story()


def display_game_title(msg):
    f = Figlet(font='rectangles')
    print(f.renderText(msg))

def introduce_game_story():

    print("\nIn a land shrouded by the Fog of War, a lone hero embarks on a quest to vanquish enemies and uncover hidden treasures.")
    wait_for_user()
    print("\nArmed with courage and determination, the hero must navigate through treacherous terrains, face formidable foes, ")
    wait_for_user()
    print("\nand unlock the secrets of mystical chests that hold the key to ultimate power. Will the hero emerge victorious or succumb to the perils that lie ahead?")
    wait_for_user()

def wait_for_user():
    input("\nPress Enter to continue...")



if __name__ == "__main__":
    main()