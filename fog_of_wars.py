from pyfiglet import Figlet








def main():
    game_name = 'FOG OF WARS'
    display_game_title(game_name)
    print(f"\n{input("Press Enter to start the game...")}")


def display_game_title(msg):
    f = Figlet(font='rectangles')
    print(f.renderText(msg))




if __name__ == "__main__":
    main()