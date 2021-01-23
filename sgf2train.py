import os
import numpy as np
from GoRule.gosgf import Sgf_game
from GoRule.goboard import GameState, Move
from GoRule.gotypes import Point
from GoRule.utils import print_board
from GoRule.encoder.oneplane import OnePlaneEncoder
from GoRule.encoder.base import get_encoder_by_name


def get_sgf(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sgf')]


def encode(game_state):
    board_matrix = np.zeros((19, 19, 1))
    next_player = game_state.next_player
    for r in range(19):
        for c in range(19):
            p = Point(row=r + 1, col=c + 1)
            go_string = game_state.board.get_go_string(p)
            if go_string is None:
                continue
            if go_string.color == next_player:
                board_matrix[r, c, 0] = 1
            else:
                board_matrix[r, c, 0] = -1
    return board_matrix


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


def get_train():
    counter = 0
    for index in sgf_path:
        f = open(index)
        sgf_content = f.read()
        f.close()
        sgf_game = Sgf_game.from_string(sgf_content)
        game_state = GameState.new_game(19)

        first_move = False
        for item in sgf_game.main_sequence_iter():
            color, move_tuple = item.get_move()
            point = Point
            if color is not None:
                if move_tuple is not None:
                    row, col = move_tuple
                    point = Point(row + 1, col + 1)
                    move = Move.play(point)
                else:
                    move = Move.pass_turn()
                if first_move and point is not None:
                    features[counter] = encode(game_state)
                    labels[counter] = (point.row - 1) * 19 + (point.col - 1)
                    counter += 1
                game_state = game_state.apply_move(move)
                first_move = True


if __name__ == '__main__':
    sgf_path = get_sgf('./data/sgf_record')
    total_samples = get_total_samples()
    print(total_samples)
    features = np.zeros((total_samples, 19, 19, 1))
    labels = np.zeros((total_samples, 1))
    get_train()
    feature_file_base = './data/features'
    label_file_base = './data/labels'
    np.save(feature_file_base, features)
    np.save(label_file_base, labels)

    # print(features[1])
