import copy

from GameBoard import GameBoard
from Experiment import Experiment
from Generalizer import Generalizer
from Critic import Critic


class PerformanceMeasure(object):

    def __init__(self, board, generalizer, critic, generator):
        self._board = board
        self._generalizer = generalizer
        self._critic = critic
        self._generator = generator


    def improve_system(self):

        ended = self._board.victor()
        while ended is None:

            weights = self._generalizer.get_weights()
            position = self._board.maximizer(weights)

            self._board._board[position] = 'O'

            self._critic.append_examples(copy.deepcopy(self._board), self._board.victor())

            learner_move = self._generator.next_trainer_move(self._board, weights)
            if learner_move is not None:
                  self._board._board[learner_move] = 'X'

            ended = self._board.victor()

        self._critic.append_examples(copy.deepcopy(self._board), ended)
        return ended