EMPTY_CEIL = '*'
PLAYER_SYMB1 = ' X '
PLAYER_SYMB2 = ' O '

#Функция для создания доски
def get_board() -> list:
    size = int(input("""Выберите размер поля: 
                    если хотите 3х3, нажмите 3
                    если хотите 5х5, нажмите 5
                    """))
    small_3x3 = 3
    big_5x5 = 5
    board = []
    if size == small_3x3:
        board = [EMPTY_CEIL for i in range(9)]
        for i in range(3):
            print(board[i*3], board[1+i*3], board[2+i*3])
    elif size == big_5x5:
        board = [EMPTY_CEIL for i in range(25)]
        for i in range(5):
            print(board[i*3], board[1+i*3], board[2+i*3], board[3+i*3], board[4+i*3])

    return board

#Функция, чтобы печатать доску
def print_board(board):
    for ceil in board:
        print(ceil)
    print()

#Проверка выигрыша
def is_win(player_move_hist: dict, current_player):
    if len(get_board()) == 9:
        win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
        for x in win_comb:
            if all(y in player_move_hist[current_player] for y in x):
                return True

        return False
    else:
        win_comb = [[range(5)], [range(5, 10)], [range(10, 15)], [range(15, 20)], [range(20, 25)], [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]
        for x in win_comb:
            if all(y in player_move_hist[current_player] for y in x):
                return True
        return False

#Проверка ничьи
def is_draw(player_move_hist:dict):
    if len(get_board()) == 9:
        if len(player_move_hist[PLAYER_SYMB1]) + len(player_move_hist[PLAYER_SYMB2]) == 9:
            return True
        return False
    else:
        if len(player_move_hist[PLAYER_SYMB1]) + len(player_move_hist[PLAYER_SYMB2]) == 25:
            return True
        return False

# Один цикл игры за любого игрока
def one_game_iteration(current_player, board):
    player_move_hist = {PLAYER_SYMB1: [], PLAYER_SYMB2: []}
    variance = [EMPTY_CEIL for x in range(100)]
    while True:
        try:
            step = int(input(f"Игрок {current_player} введите номер ячейки: "))
        except ValueError:
            print("Не верные данные, повторите.")
            continue

        if len(get_board()) == 9:
            if not 1 < step < 9:
                print("Ячейка вне диапазона поля, повторите.")
                continue
            if variance[step - 1] != EMPTY_CEIL:
                print("Ячейка уже занята, выберите новую")
                continue
        #Определяем координату игрока и записываем в список
            variance[step - 1] = current_player
            player_move_hist[current_player].append(step)

        elif len(get_board()) == 25:
            if not 1 < step < 25:
                print("Ячейка вне диапазона поля, повторите.")
                continue
            if variance[step - 1] != EMPTY_CEIL:
                print("Ячейка уже занята, выберите новую")
                continue
            # Определяем координату игрока и записываем в список
            variance[step - 1] = current_player
            player_move_hist[current_player].append(step)

        #Проверка игрока на выигрыш
        if is_win(player_move_hist, current_player):
            print_board(variance)
            print(f"{current_player} выиграл! \n")
            return current_player

        # Проверка ничьи
        if is_draw(player_move_hist):
            print_board(variance)
            print("Ничья")
            break

        # Смена игроков
        if current_player == PLAYER_SYMB1:
            current_player = PLAYER_SYMB2
        else:
            current_player = PLAYER_SYMB1


def main():
    player1 = input("Игрок 1, введите имя:\n")
    player2 = input("Игрок 2, введите имя:\n")
    current_player = player1
    board = get_board()
    print_board(board)
    player_move_hist = {PLAYER_SYMB1: [], PLAYER_SYMB2: []}
    while True:
        try:
            choice_symbol = int(input(f"{player1}, выбирайте символ: \n если хотите играть {PLAYER_SYMB1}, нажмите 1 \n если хотите играть {PLAYER_SYMB2}, нажмите 2:    "))
        except ValueError:
            print("Неверно, повторить ввод.\n")
            continue

        if choice_symbol == 1:
            player_move_hist[PLAYER_SYMB1] = current_player
            if current_player == player1:
                player_move_hist[PLAYER_SYMB2] = player2
        else:
            player_move_hist[PLAYER_SYMB2] = current_player
            if current_player == player1:
                player_move_hist[PLAYER_SYMB1] = player2
        break
    return one_game_iteration(current_player, board)

if __name__ == "__main__":
    main()


