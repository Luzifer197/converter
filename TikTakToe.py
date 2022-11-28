from Functionen_ttt import draw_board, check_turn, check_for_win, ki_playing
import os

spots:dict[str] = {1: "1", 2 : "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

playing = True
complete = False
turn = 0
prev_turn = -1
ki = input("vs Computer, vs player?     ").lower()
mode = input("normal, medium, hardcore ").lower()
ki    
mode
while playing:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("invalid spot selected, please pick another spot")
    prev_turn = turn

    if ki == "vs player":
        print(f"Player {str((turn%2) + 1)}\'s turn: Pick your spot or press q to quit:")
        choice = input("type you move:  ")
    elif ki == "vs computer":
        if check_turn(turn) == "X": 
            choice = ki_playing(spots, mode)
            print(f"Player {str((turn%2) + 1)}\'s pickt {choice}")
        
        elif check_turn(turn) == "O":
            print(f"Player {str((turn%2) + 1)}\'s turn: Pick your spot or press q to quit:")
            choice = input("type you move:  ")

    if choice == "q":
        playing = False
    elif str.isdigit(str(choice)) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:

            turn += 1
            spots[int(choice)] = check_turn(turn) 
                
    if check_for_win(spots):
        playing = False
        complete = True
    if turn > 8:
        playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete == True:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("No Winner")