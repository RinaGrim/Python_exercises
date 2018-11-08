import random
import time

game_field = ["_1_|", "_2_|", "_3_|", "_4_|", "_5_|", "_6_|", "_7_|", "_8_|", "_9_|"]
field_index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player_comb = []
comp_comb = []
cross = "_X_|"
zero = "_O_|"



def field():

    """ This method displays the playing field """

    index = 0
    while index < 9:
        print(f"|{''.join(game_field[index:index + 3])}\n")
        index += 3


def movePlayer(choice):

    """ This method creates a player step """

    cell = int(input("Введите номер ячейки:\n"))
    if cell in field_index:
        game_field[cell - 1] = f"{choice}"
        field_index.remove(cell)
        player_comb.append(cell)
    else:
        print("Ячейка уже занята")
        movePlayer(choice)


def moveComp(choice):

    """ This method creates a computer step """

    comp_best_move = []
    comp_protect_move = []
    if choice == zero:
        lens = 8
    else:
        lens = 7
    if len(field_index) >= lens:
        cell = random.choice(field_index)
        cell_check(choice, cell)
    else:
        index = 0
        while index < len(win_list) and comp_protect_move != 1:
            comp_best_move.clear()
            comp_protect_move.clear()
            comp_protect_move = [element for element in win_list[index] if element not in player_comb]
            comp_best_move = [element for element in win_list[index] if element not in comp_comb]
            index += 1
            if len(comp_protect_move) == 1:
                if len(comp_best_move) == 1:
                    cell = comp_best_move[0]
                    win_list.pop(index - 1)
                    cell_check(choice, cell)
                    break
                else:
                    cell = comp_protect_move[0]
                    win_list.pop(index - 1)
                    cell_check(choice, cell)
                    break
        if len(comp_protect_move) > 1:
            cell = random.choice(field_index)
            cell_check(choice, cell)


def cell_check(choice, cell):

    """ This method checks if the cell is free to fill """

    if cell in field_index:
        print("Ход компьютера")
        game_field[cell - 1] = f"{choice}"
        field_index.remove(cell)
        field()
        comp_comb.append(cell)
    else:
        moveComp(choice)


def check(number):

    """ This method sets the course of the game and checks
        if there are winning combinations on the game field """

    if number == 0:
        movePlayer(cross)
        moveComp(zero)
    else:
        moveComp(cross)
        movePlayer(zero)
    if len(field_index) > 3:
        check(number)
    else:
        player_comb.sort()
        comp_comb.sort()
        index = 0
        while index < len(win_list):
            player = [element for element in player_comb if element in win_list[index]]
            comp = [element for element in comp_comb if element in win_list[index]]
            index += 1
            if len(player) == 3 or len(comp) == 3:
                break
        if len(player) == 3:
            print("== Вы выиграли! ==")
        elif len(field_index) < 1:
            print("== Ничья ==")
        elif len(player) < 3 and len(comp) < 3 and len(field_index) > 2:
            check(number)
        else:
            print("== Вы проиграли! ==")


def main():
    field()
    choice = input("Выберите чем будете играть (Х или О):\n")
    if choice.lower() == "x" or choice.lower() == "х":
        print("Вы ходите первыми!")
        check(0)
    elif choice.lower() == "o" or choice.lower() == "о":
        print("Компьютер ходит первым!")
        time.sleep(1)
        check(1)
    else:
        print("Выберите Х или О")
        main()


if __name__ == '__main__':
    main()