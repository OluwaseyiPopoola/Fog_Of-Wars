from pyfiglet import Figlet
from random import randint
MAX = 100

class Board:
    def __init__(self):
        self.rows = randint(10, 20)
        self.cols = randint(10, 20)

        self.walls = set((randint(0, self.rows-1), randint(0, self.cols-1)) for _ in range(randint(int(0.05*self.rows*self.cols), int(0.20*self.rows*self.cols))))

        self.board_positions_objects = {(row, col): None for row in range(self.rows) for col in range(self.cols)}

        for wall in self.walls: 
            self.board_positions_objects[wall] = '#'


    def add_object(self, obj, position):
        if position in self.board_positions_objects:
            self.board_positions_objects[position] = obj


class Character:
    def __init__(self, name, position, strength, attack, symbol):
        self.position = position
        self.strength = strength
        self.attack = attack  
        self.symbol = symbol
        self.name = name


    def add_strength(self, amount):
        self.strength += amount
    
    def reduce_strength(self, amount):
        self.strength -= amount

    def add_attack(self, amount):
        self.attack += amount

    def reduce_attack(self, amount):
        self.attack -= amount

class Hero(Character):
    def __init__(self, name, position,):
        super().__init__(name, position, randint(MAX//10, MAX), randint(MAX//10, MAX), 'H')
        

class Enemy(Character):
    def __init__(self, name, position, strength, attack):
        super().__init__(name, position, strength, attack, 'E')


class Warrior(Enemy):
    def __init__(self, position):
        super().__init__("Warrior", position, MAX // 3, MAX // 3)
     
class Paladin(Enemy):
    def __init__(self, position):
        super().__init__("Paladin", position, MAX // 5, MAX // 5)
       
class Spy(Enemy):
    def __init__(self, position):
        super().__init__("Spy", position, MAX // 7, MAX // 7)

class Chest:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.symbol = 'C'

class RegularChest(Chest): 
    def __init__(self, position):
        super().__init__(randint(1, MAX//10), position)

    def open(self, character):
        character.add_strength(self.value)
        character.add_attack(self.value)
        print(f"{character.name} opened a Regular Chest and gained {self.value} strength and attack!")

class Orbchest(Chest):
    pass





def main():
    game_name = 'FOG OF WARS'
    display_game_title(game_name)
    print(f"\n{input("Press Enter to start the game...")}")
    
    introduce_game_story()
    board = Board()
    

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