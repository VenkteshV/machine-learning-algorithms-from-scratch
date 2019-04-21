import random

class Generalizer(object):

    def __init__(self, weights_length):
        self._training_examples=[]
        self._training_example_values=[]
        self._weights=[]
        for i in range(weights_length):
            self._weights.append(random.random())

    """update weights based on training_samples and values of training_samples"""
    def LMS_weight_update_rule(self):
        learning_rate = .1

        for board,V_board in zip(self._training_examples, self._training_example_values):
            V_board_cap = board.calculate_target_value(self._weights)
            X = board.get_features()

            for i in range(len(self._weights)):
                self.weights[i] += learning_rate * (V_board - V_board_cap) * X[i]

    def get_weights(self):
        return self._weights

    def set_training_examples(self, training_examples):
        self._training_examples = training_examples


    def set_training_values(self, training_values):
        self.training_example_values = training_values