import os
import numpy as np
from GoRule.gosgf import Sgf_game
from GoRule.goboard import GameState, Move
from GoRule.gotypes import Point
from GoRule.utils import print_board


def get_sgf(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sgf')]


def get_total_samples():
    total_sample = 0
    for index in sgf_path:
        f = open(index)
        sgf_content = f.read()
        f.close()
        sgf_game = Sgf_game.from_string(sgf_content)
        num_moves = 0
        first_move = False
        for item in sgf_game.main_sequence_iter():
            color, move_tuple = item.get_move()
            if color is not None and move_tuple is not None:
                if first_move:
                    num_moves += 1
                else:
                    first_move = True
        total_sample += num_moves
    return total_sample


if __name__ == '__main__':
    sgf_path = get_sgf('./data/sgf_record')
    total_samples = get_total_samples()
    print(total_samples)


