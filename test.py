import chess
import random

print("Babibot is starting")

board = chess.Board()

print(board)

while board.is_game_over() == False:

    human_move = None

    while not(human_move in board.legal_moves):
        print("YOUR MOVE: ")
        human_move_uci = input()
        try:
            human_move = chess.Move.from_uci(human_move_uci)
        except ValueError:
            human_move = None

    board.push(human_move)

    print(board)
    print("-----------------------------------------------")
    
    bot_move = random.choice(list(board.legal_moves))  

    print(bot_move)

    board.push(bot_move)

    print(board)
    print("-----------------------------------------------")