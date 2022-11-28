from random import randint

def draw_board(spots: dict[str]):
    board = f" {spots[1]} | {spots[2]} | {spots[3]} \n {spots[4]} | {spots[5]} | {spots[6]} \n {spots[7]} | {spots[8]} | {spots[9]} "
    
    print(board)


def check_turn(turn:int) -> str:
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def check_for_win(spots):
    if (spots[1] == spots [2] == spots [3]) or (spots[4] == spots [5] == spots [6]) or (spots[7] == spots [8] == spots [9]):
        return True
    if (spots[1] == spots [4] == spots [7]) or (spots[2] == spots [5] == spots [8]) or (spots[3] == spots [6] == spots [9]):
        return True
    if (spots[7] == spots [5] == spots [3]) or (spots[1] == spots [5] == spots [9]):
        return True
    else:
        return False

def ki_playing(turn: int) -> int:
    if check_turn(turn) == "X":
        return randint(1, 9)

