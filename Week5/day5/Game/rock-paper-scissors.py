import game


def get_user_menu_choice():
    print('**Menu**')
    action = input("(g) Play a new game \n(x)Show score and exit: ")
    action = action.lower()
    if action == "g":
        return "g"
    elif action == "x":
        return "x"
    else:
        print("invalid input, please enter 'g' for playing or 'x' to exit the game.")


def print_results(results):
    for x, y in game.Game().results:
        print(f'You {x} {y} times.')
    print("thanks for playing!")


def main():
    while True:
        if get_user_menu_choice() == "x":
            print_results(game.Game().results)
            break
        elif get_user_menu_choice() == "g":
            game.Game().play()
