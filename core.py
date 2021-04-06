import logging
import chess
import random

logger = logging.getLogger(__name__)

def getBestMove(board: chess.Board) -> chess.Move:

    for candidate_move in list(board.legal_moves):

        board.push(candidate_move)
        if board.is_checkmate():
            logging.info(f"{candidate_move} will checkmate, this is the best move")
            return candidate_move
        else:
            board.pop()


    return random.choice(list(board.legal_moves))
