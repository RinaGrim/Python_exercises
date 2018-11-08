#!/usr/bin/python3
import random
"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
chips = [el for el in range(1, 91)]
random.shuffle(chips)
chip = 0


def lotto_card():

    """ This method generate lotto card and return it as list """

    card = []
    row1 = []
    row2 = []
    row3 = []
    for _ in range(15):
        card.append(f"{random.choice(chips)}|")
    index = 0
    for number in card:
        if index < 5:
            row1.append(number)
        elif index < 10:
            row2.append(number)
        else:
            row3.append(number)
        index += 1
    for _ in range(4):
        row1.append('  |')
        row2.append('  |')
        row3.append('  |')
    random.shuffle(row1)
    random.shuffle(row2)
    random.shuffle(row3)
    card.clear()
    for el in row1:
        card.append(el)
    for el in row2:
        card.append(el)
    for el in row3:
        card.append(el)
    return card


def display_card(card):

    """ This method displays the lotto card """

    index = 0
    print("----------------------------")
    while index < 27:
        print(f"|{''.join(card[index:index + 9])}\n")
        index += 9
    print("----------------------------")


def display_chip():

    """ This method shows the chip that came out in current step
        and the number of remaining chips"""

    chip = chips.pop(0)
    print(f"Новый бочонок: {chip} (осталось {len(chips)})")
    return chip


def comp_move(counter, chip):

    """ This method creates a computer step """

    if f"{chip}|" in comp_card:
        comp_card.insert(comp_card.index(f"{chip}|"), '--|')
        comp_card.remove(f"{chip}|")
        counter += 1
    else:
        counter = counter
    return counter


def steps(moving, player_counter, comp_counter):

    """ This method generate steps in the game
        and also check the result """

    while moving:
        move = True
        chip = display_chip()
        print("Карточка игрока")
        display_card(player_card)
        print("Карточка компьютера")
        display_card(comp_card)
        decide = input("Зачеркнуть число? (y/n)\n")
        if decide == 'y':
            if f"{chip}|" in player_card:
                player_card.insert(player_card.index(f"{chip}|"), '--|')
                player_card.remove(f"{chip}|")
                player_counter += 1
                comp_move(comp_counter, chip)
                moving = True
            else:
                moving = False
            move = moving
        elif decide == 'n':
            if f"{chip}|" in player_card:
                moving = False
            else:
                comp_move(comp_counter, chip)
            move = moving
        if player_counter == 15 and comp_counter < 15:
            print("-- Вы выиграли! --")
            moving = False
        elif (comp_counter == 15 and player_counter < 15) or not move:
            print("-- Вы проиграли! --")
            moving = False
        else:
            moving = True


def main():
    global player_card
    player_card = lotto_card()
    global comp_card
    comp_card = lotto_card()
    moving = True
    player_counter = 0
    comp_counter = 0
    steps(moving, player_counter, comp_counter)


if __name__ == '__main__':
    main()
