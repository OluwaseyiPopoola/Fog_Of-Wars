from pyfiglet import Figlet
from random import randint
MAX = 100

class Board:
    def __init__(self):
        self.rows = randint(10, 20)
        self.cols = randint(10, 20)

        self.walls = set((randint(0, self.rows-1), randint(0, self.cols-1)) for _ in range(randint(int(0.05*self.rows*self.cols), int(0.20*self.rows*self.cols))))

        self.board_positions_objects = {(row, col): None for row in range(self.rows) for col in range(self.cols)}

        for wall_positions in self.walls: 
            self.board_positions_objects[wall_positions] = '#'


        self.warriors = [Warrior(self.get_random_empty_position()) for _ in range(self.cols // 3)]
        self.paladins = [Paladin(self.get_random_empty_position()) for _ in range(self.cols // 3)]
        self.spies = [Spy(self.get_random_empty_position()) for _ in range(self.cols - (2 * (self.cols // 3)))]
    
        self.enemies = self.warriors + self.paladins + self.spies

        for enemy in self.enemies:
            self.add_object(enemy, tuple(enemy.position)) 

        self.regularchests = [RegularChest(self.get_random_empty_position()) for _ in range(self.cols // 5)]
        self.orbchests1 = [OrbChest1(self.get_random_empty_position()) for _ in range(self.cols // 5)]
        self.orbchests2 = [OrbChest2(self.get_random_empty_position()) for _ in range(self.cols // 5)]
        self.orbchests3 = [Orbchest3(self.get_random_empty_position()) for _ in range(self.cols // 5)]
        self.teleportchests = [TeleportChest(self.get_random_empty_position()) for _ in range(self.cols - (4 * (self.cols // 5)))]

        self.chests = self.regularchests + self.orbchests1 + self.orbchests2 + self.orbchests3 + self.teleportchests
    
        for chest in self.chests:
            self.add_object(chest, tuple(chest.position))
     
    def get_random_empty_position(self):
        empty_positions = [pos for pos in self.board_positions_objects if self.board_positions_objects[pos] is None]
        return empty_positions[randint(0, len(empty_positions)-1)] if empty_positions else None   


    def add_object(self, obj, position):
        if position in self.board_positions_objects:
            self.board_positions_objects[position] = obj

    def update_character_position(self, character, new_position):
        if character.position: 
            self.board_positions_objects[character.position] = None
        
        character.position = new_position
        self.board_positions_objects[new_position] = character


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

    def die(self):
        print(f"{self.name} has been defeated!")
        self.strength = 0
        self.attack = 0
        self.position = None

        

class Hero(Character):
    def __init__(self, name, position,):
        super().__init__(name, position, randint(MAX//10, MAX), randint(MAX//10, MAX), 'H')

    def move_wasdx(self, direction, board):
        row, col = self.position

        if direction.upper() == 'W':
            new_pos = (row - 1, col)
        elif direction.upper() == 'S':
            new_pos = (row + 1, col)
        elif direction.upper() == 'A':
            new_pos = (row, col - 1)
        elif direction.upper() == 'D':
            new_pos = (row, col + 1)
        elif direction.upper() == 'X':
            new_pos = (row, col)  # stay in place
        
        board.update_character_position(self, new_pos)
              

class Enemy(Character):
    def __init__(self, name, position, strength, attack):
        super().__init__(name, position, strength, attack, 'E')

    def random_move(self, board):
        directions = ['W', 'A', 'S', 'D', 'X']  # X means stay in place
        direction = directions[randint(0, len(directions)-1)]
        row, col = self.position

        if direction == 'W' and row > 0 and board.board_positions_objects.get((row - 1, col)) != '#':
            new_pos = (row - 1, col)
        elif direction == 'S' and row < board.rows - 1 and board.board_positions_objects.get((row + 1, col)) != '#':
            new_pos = (row + 1, col)
        elif direction == 'A' and col > 0 and board.board_positions_objects.get((row, col - 1)) != '#':
            new_pos = (row, col - 1)
        elif direction == 'D' and col < board.cols - 1 and board.board_positions_objects.get((row, col + 1)) != '#':
            new_pos = (row, col + 1)
        else:
            new_pos = (row, col)  # stay in place if move is invalid
        
        board.update_character_position(self, new_pos)
    


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

    def open_chest(self, character):
        character.add_strength(self.value)
        character.add_attack(self.value)
        print(f"{character.name} opened a Regular Chest and gained {self.value} strength and attack!")

class OrbChest(Chest):
    def __init__(self, position):
        super().__init__(1, position)
    pass

class OrbChest1(OrbChest):
    def open_chest(self, character):
        character.strength //= 2
        character.attack *= 2
        print(f"Orb Chest 1 opened! {character.name}'s strength halved and attack doubled.")

       
class OrbChest2(OrbChest):

    def open_chest(self, character):
        character.strength *= 2
        character.attack //= 2
        print(f"Orb Chest 2 opened! {character.name}'s strength doubled and attack halved.")

class Orbchest3(OrbChest):
    def open_chest(self, character, combatants):
        nearest_combatant = get_nearest_combatant(character, combatants)
        if nearest_combatant:
            nearest_combatant.die()
            print(f"Orb Chest 3 opened! Nearest combatant {nearest_combatant.name} has been removed from the game.")
        else:
            print("No enemies to remove.")

class TeleportChest(Chest):
    def __init__(self, position):
        super().__init__(1, position)  # fixed init

    def open_chest(self, character, board):
        possible_positions = []
        for r in range(max(0, character.position[0] - 10), min(board.rows, character.position[0] + 11)):
            for c in range(max(0, character.position[1] - 10), min(board.cols, character.position[1] + 11)):
                if board.board_positions_objects[(r, c)] != '#':  # ✅ No wall
                    possible_positions.append((r, c))
        
        if possible_positions:
            new_position = possible_positions[randint(0, len(possible_positions) - 1)]
            
            board.update_character_position(character, new_position)

            print(f"{character.name} teleported to {new_position}.")
        else:
            print("No valid positions to teleport.")


def get_nearest_combatant(character, combatants):
    if not combatants:
        return None
    nearest_enemy = min(combatants, key=lambda enemy: get_distance(character, enemy))
    return nearest_enemy

def get_distance(character1, character2):
    return ((character1.position[0] - character2.position[0]) ** 2 + (character1.position[1] - character2.position[1]) ** 2) ** 0.5  
    



def main():
    game_name = 'FOG OF WARS'
    display_game_title(game_name)
    input("Press Enter to start the game...")
    
    introduce_game_story()
    board = Board()
    hero = Hero(input("Enter your hero's name: "), choose_empty_position(board))
    

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

def choose_empty_position(board):  
    empty_positions = [pos for pos, obj in board.board_positions_objects.items() if obj is None]

    print("\nAvailable positions for your hero:")
    for idx, pos in enumerate(empty_positions):
        print(f"{idx + 1}: {pos}")

    while True:
        try:
            choice = int(input(f"Choose a position (1-{len(empty_positions)}): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:   
            if 0 <= choice < len(empty_positions):
                return empty_positions[choice]
            else:
                print("Invalid choice. Please select a valid position number.")



if __name__ == "__main__":
    main()