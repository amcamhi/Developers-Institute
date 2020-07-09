table = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def print_table(table):
    print(table['7'] + '|' + table['8'] + '|' + table['9'])
    print('-+-+-')
    print(table['4'] + '|' + table['5'] + '|' + table['6'])
    print('-+-+-')
    print(table['1'] + '|' + table['2'] + '|' + table['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print_table(table)
        print("It's your turn," + turn + ".Move to which position?")

        move = input()

        if table[move] == ' ':
            table[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
# Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if table['7'] == table['8'] == table['9'] != ' ':  # across the top
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['4'] == table['5'] == table['6'] != ' ':  # across the middle
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['1'] == table['2'] == table['3'] != ' ':  # across the bottom
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['1'] == table['4'] == table['7'] != ' ':  # down the left side
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['2'] == table['5'] == table['8'] != ' ':  # down the middle
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['3'] == table['6'] == table['9'] != ' ':  # down the right side
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['7'] == table['5'] == table['3'] != ' ':  # diagonal
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif table['1'] == table['5'] == table['9'] != ' ':  # diagonal
                print_table(table)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


#         table[key] = " "

game()

restart = input("Do want to play Again?(y/n)")

if restart == "y" or restart == "Y":

    game()
else:
    print("Ok, bye!")
