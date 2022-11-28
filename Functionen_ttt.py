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

def ki_playing(spots, mode) -> int:

    if mode == "leicht":
        return randint(1, 9)
    
    elif mode == "medium":
        
        #horizontal
        if (spots[4] == spots[5]) and (spots[6] != "O"):
            return 6
        if (spots[4] == spots[6]) and (spots[5] != "O"):
            return 5
        if (spots[5] == spots[6]) and (spots[3] != "O"):
            return 4
        
        #diagonal  
        if (spots[7] == spots[5]) and (spots[3] != "O"):
            return 3
        if (spots[3] == spots[7]) and (spots[3] != "O"):
            return 5
        if (spots[3] == spots[5]) and (spots[7] != "O"):
            return 7

        #perpendicular

        if (spots[2] == spots[5]) and (spots[8] != "O"):
            return 8
        if (spots[2] == spots[8]) and (spots[5] != "O"):
            return 5
        if (spots[5] == spots[8]) and (spots[7] != "O"):
            return 2
        
        return randint(1, 9)

    elif mode == "hardcore":

        #horizontal
        if (spots[1] == spots[2]) and (spots[3] != "O"):
            return 3
        if (spots[1] == spots[3]) and (spots[2] != "O"):
            return 2
        if (spots[3] == spots[2]) and (spots[1] != "O"):
            return 1

        if (spots[4] == spots[5]) and (spots[6] != "O"):
            return 6
        if (spots[4] == spots[6]) and (spots[5] != "O"):
            return 5
        if (spots[5] == spots[6]) and (spots[4] != "O"):
            return 4

        if (spots[7] == spots[8]) and (spots[9] != "O"):
            return 9
        if (spots[7] == spots[9]) and (spots[8] != "O"):
            return 8
        if (spots[8] == spots[9]) and (spots[7] != "O"):
            return 7

        #diagonal
        if (spots[7] == spots[5]) and (spots[3] != "O"):
            return 3
        if (spots[3] == spots[7]) and (spots[5] != "O"):
            return 5
        if (spots[3] == spots[5]) and (spots[7] != "O"):    
            return 7

        if (spots[9] == spots[5]) and (spots[1] != "O"):
            return 1
        if (spots[1] == spots[9]) and (spots[5] != "O"):
            return 5
        if (spots[5] == spots[1]) and (spots[9] != "O"):
            return 9

        #perpendicular        
        if (spots[1] == spots[4]) and (spots[7] != "O"):
            return 7
        if (spots[1] == spots[7]) and (spots[4] != "O"):
            return 4
        if (spots[4] == spots[7]) and (spots[1] != "O"):
            return 1

        if (spots[2] == spots[5]) and (spots[8] != "O"):
            return 8
        if (spots[2] == spots[8]) and (spots[5] != "O"):
            return 5
        if (spots[5] == spots[8]) and (spots[2] != "O"):
            return 2

        if (spots[6] == spots[3]) and (spots[9] != "O"):
            return 9
        if (spots[3] == spots[9]) and (spots[6] != "O"):
            return 6
        if (spots[6] == spots[9]) and (spots[3] != "O"):
            return 3

        return randint(1, 9)
