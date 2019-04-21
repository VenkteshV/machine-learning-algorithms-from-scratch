"""
Task : tom-mitchell machine learning exercise 1 - tic-tac toe- playing  against humans

Experience by learning:program playing aginst self

perfomance: wins

Target function: v= w0 + w1*x1+..wn*xn

wi - weights

Learning: 
LMS weight update rule
"""
import math,random,copy

from GameBoard import GameBoard

from Experiment import Experiment
from Generalizer import Generalizer
from Critic import Critic
from PerformanceMeasure import PerformanceMeasure


NUMBER_OF_EXaMPLES=2000

BOARD_DIMENSION=9

def main():
    no_of_wins = 0; no_of_ties=0; no_of_losses=0 ;
    print(" algorithm gaining experience")

    game_generator = Experiment(BOARD_DIMENSION)
    generalizer = Generalizer(19) #19 because of 18 features + one constant w0

    critic = Critic(generalizer)
    for i in range(NUMBER_OF_EXaMPLES):
        board = game_generator.generate_board()

        performance_system = PerformanceMeasure(board, generalizer, critic, game_generator)
        result = performance_system.improve_system()

        examples, values = critic.fetch_training_examples()
        generalizer.set_training_examples(examples)
        generalizer.set_training_values(values)
        generalizer.LMS_weight_update_rule()

        if result == 100: no_of_wins += 1
        if result == -100: no_of_losses += 1
        if result == 0: no_of_ties += 1



    W = generalizer.get_weights()

    print(no_of_wins, no_of_ties, no_of_losses)

    """
        Playing against human...
    """

    while True:
        human_board = GameBoard(['-', '-', '-', '-', '-', '-', '-', '-', '-', ])

        vs_human = human_board.victor()
        while vs_human is None:
            x = int(input(" X coordinate: "))
            y = int(input(" Y coordinate: "))

            human_board._board[x*3 + y] = 'X'

            computer_position = human_board.maximizer(W)
            human_board._board[computer_position] = 'O'

            print(human_board)

            vs_human = human_board.victor()



main()