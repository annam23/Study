EMPTY_CEIL = '*'
PLAYERS_SYMB = ['X', 'O']

#Функция для создания доски
def new_board(ask_about_board):
    ceils = [EMPTY_CEIL for i in range(ask_about_board ** 2)]
    for i in range(ask_about_board):
        for ceil in range(ask_about_board):
            print(*ceils[i + ceil * i] * ask_about_board)
        return ceils


def print_board(board):
    for ceil in board:
        print(ceil, end=" ")
    print()

#Проверка выигрыша
def is_win(player_move_hist, current_player, ask_about_board):
    if ask_about_board ** 2 == 9:
        win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
        for x in win_comb:
            if all(y in player_move_hist[current_player] for y in x):
                return True

        return False
    else:
        win_comb = [[range(1,6)], [range(6, 11)], [range(11, 16)], [range(16, 21)], [range(21, 26)], [1, 7, 13, 19, 25], [5, 9, 13, 17, 21]]
        for x in win_comb:
            if all(y in player_move_hist[current_player] for y in x):
                return True
        return False

#Проверка ничьи
def is_draw(player_move_hist, ask_about_board):
    if len(player_move_hist['X']) + len(player_move_hist["O"]) == ask_about_board ** 2:
        return True
    return False

#Смена игрока
def change_players(current_player):
    return current_player == 'O' if current_player == 'X' else current_player == 'X'

# Один цикл игры за любого игрока
def one_game_iteration(current_player, ask_about_board, board):
    player_move_hist = {'X': [], 'O': []}
    while True:
        print_board(board)
        try:
            step = int(input(f"Игрок : {current_player} введите номер ячейки: от 1 до {ask_about_board**2} "))
        except ValueError:
            print("Не верные данные, повторите.")
            continue

        if step < 1 or step > ask_about_board ** 2:
            print("Ячейка вне диапазона поля, повторите.")
            continue
        if board[step - 1] != EMPTY_CEIL:
            print("Ячейка уже занята, выберите новую")
            continue

        #Определяем координату игрока и записываем в список
        board[step - 1] = current_player
        player_move_hist[current_player].append(step)


        #Проверка выигрыша
        if is_win(player_move_hist, current_player, ask_about_board):
            print_board(board)
            print(f"{current_player} выиграл! \n")
            break

        # Проверка ничьи
        if is_draw(player_move_hist, ask_about_board):
            print_board(board)
            print("Ничья")
            break

        #смена игроков, inline почему-то не меняет
        #change_players(current_player)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

def main():
    player1 = input("Игрок 1, введите имя:\n")
    player2 = input("Игрок 2, введите имя:\n")
    current_player = player1
    ask_about_board = int(input("""Выберите размер поля:
                                     если хотите 3х3, нажмите 3
                                  если хотите 5х5, нажмите 5
                                   """))
    board = new_board(ask_about_board)
    player_= {'X': "", 'O': ""}

    while True:
        try:
            choice_symbol = int(input(f"{player1}, выбирайте символ: \n если хотите играть 'X', нажмите 1 \n если хотите играть 'O', нажмите 2:    "))
        except ValueError:
            print("Неверно, повторить ввод.\n")
            continue

        #Определяем, как стартует игрок
        if choice_symbol == 1:
            player_['X'] = current_player
            if current_player == player1:
                player_['O'] = player2
            else:
                player_['X'] = player1
        else:
            player_['X'] = current_player
            if current_player == player1:
                player_['O'] = player2
            else:
                player_["X"] = player1


        one_game_iteration(PLAYERS_SYMB[choice_symbol - 1],ask_about_board,board)
        break


if __name__ == "__main__":
    main()


