import math,copy
class GameBoard(object):
    def __init__(self,board):
        self._board = board
        self._size = int(math.sqrt(len(board)))

    """ this function returns the victor of the game

    100 - winner is player who starts(X)

    -100 - X loses i.e O wins

    0 - tie"""

    def victor(self):
        board_str = ''.join(self._board)
        board_copy = copy.deepcopy(self._board)

        # check columns
        for i in range(self._size):
            if board_str[i::self._size].count('O') == self._size:
                return -100
            if board_str[i::self._size].count('X') == self._size:
                return 100
        #check rows
        for i in range(0,self._size**2, self._size):
            board_copy[i:i+self._size] = reversed(board_copy[i:i+self._size])

            if (board_str[i:i+self._size]).count('O') == self._size:
                return -100

            
            if (board_str[i:i+self._size]).count('O') == self._size:
                return 100

        #  now check diagonals too

        if self._size == board_str[::self._size+1].count('O'):
            return -100
        if self._size == board_str[::self._size+1].count('X'):
            return 100

        if self._size == board_copy[::self._size+1].count('O'):
            return -100

        if self._size == board_copy[::self._size+1].count('X'):
            return 100
        if 0 == self._board.count('-'):
            return 0
        return None
    def __str__(self):
        board_string=""
        for i in range(self._size):
            for j in range(self._size):
                board_string += self._board[i * self._size + j]
            board_string += '/n'
        return board_string
    

    def get_features(self):
        x1 = self._board[0].count('X')
        x2 = self._board[0].count('O')
        x3 = self._board[2].count('X')
        x4 = self._board[2].count('O')
        x5 = self._board[4].count('X')
        x6 = self._board[4].count('O')
        x7 = self._board[6].count('X')
        x8 = self._board[6].count('O')
        x9 = self._board[8].count('X')
        x10 = self._board[8].count('O')
        x11 = self._board[1].count('X')
        x12 = self._board[1].count('O')
        x13 = self._board[3].count('X')
        x14 = self._board[3].count('O')
        x15 = self._board[5].count('X')
        x16 = self._board[5].count('O')
        x17 = self._board[7].count('X')
        x18 = self._board[7].count('O')
        return [1,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18]
    def get_possible_positions(self):
        possible_positions = []
        for i in range(self._size**2):
            if '-' == self._board[i]:
                possible_positions.append(i)

        return possible_positions


    def calculate_target_value(self, W):
        X = self.get_features()
        target_value = 0
        for i in range(len(X)):
            target_value += X[i] * W[i]

        return target_value

    def maximizer(self, weights):
        max_target_value = 0
        learner_position = None

        for i in self.get_possible_positions():
            self._board[i] = 'O'
            current_utility = self.calculate_target_value(weights)
            if max_target_value is None or current_utility > max_target_value:
                max_target_value = current_utility
                learner_position = i
            self._board[i] = '-'

        return learner_position