import game


def get_user_menu_choice():
    print('**Menu**')
    action = input("(g) Play a new game \n(x)Show score and exit: ")
    return action


def print_results(results):
    for key in results:
        print(f'You {key} {results[key]} times.')


def main():
