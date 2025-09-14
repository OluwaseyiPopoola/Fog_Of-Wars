from pyfiglet import Figlet
from random import randint

class Board:
    def __init__(self):
        self.rows = randint(10, 20)
        self.cols = randint(10, 20)

        self.walls = set((randint(0, self.rows-1), randint(0, self.cols-1)) for _ in range(randint(int(0.05*self.rows*self.cols), int(0.20*self.rows*self.cols))))

        self.board_positions_objects = {(row, col): None for row in range(self.rows) for col in range(self.cols)}

        for wall in self.walls: 
            self.board_positions_objects[wall] = 'WALL'


    def add_object(self, obj, position):
        if position in self.board_positions_objects:
            self.board_positions_objects[position] = obj




    


    








def main():
    game_name = 'FOG OF WARS'
    display_game_title(game_name)
    print(f"\n{input("Press Enter to start the game...")}")
    
    introduce_game_story()
    board = Board()
    print(board.board_positions_objects)


def display_game_title(msg):
    f = Figlet(font='rectangles')
    print(f.renderText(msg))

def introduce_game_story():

    print("\nIn a land shrouded by the Fog of War, \na lone hero embarks on a quest to vanquish enemies and uncover hidden treasures.")
    wait_for_user()
    print("\nArmed with courage and determination, \nthe hero must navigate through treacherous terrains, face formidable foes, ")
    wait_for_user()
    print("\nAnd unlock the secrets of mystical chests that hold the key to ultimate power. \nWill the hero emerge victorious or succumb to the perils that lie ahead?")
    wait_for_user()

def wait_for_user():
    input("\nPress Enter to continue...")



if __name__ == "__main__":
    main()