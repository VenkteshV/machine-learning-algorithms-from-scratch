import random

from GameBoard import GameBoard

class Experiment(object):

    def __init__(self, length):
        self._board_length = length


    """
        Generates new board for training.
    """
    def generate_board(self):
        initial_position = random.randint(0, self._board_length - 1)
        initial_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        initial_board[initial_position] = 'X'

        return GameBoard(initial_board)


    """
        It receives instance of Board class and returns index of position.
        If there's not possible positions it returns None.
    """
    def next_trainer_move(self, board, weights):
        possible_moves = board.get_possible_positions()

        if len(possible_moves) > 0:

            max_target_value = 0
            move = None

            for i in possible_moves:
                board._board[i] = 'X'
                current_utility = board.calculate_target_value(weights)
                if current_utility > max_target_value or max_target_value is None:
                    max_target_value = current_utility
                    move = i
                board._board[i] = '-'

            return move

        return None