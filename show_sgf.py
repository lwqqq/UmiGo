from GoRule.gosgf import Sgf_game
from GoRule.goboard import GameState, Move
from GoRule.gotypes import Point
from GoRule.utils import print_board


# gf_content = "(;GM[1]FF[4]SZ[9];B[ee];W[ef];B[ff]" + ";W[df];B[fe];W[fc];B[ec];W[gd];B[fb])"
sgf_content = "(;GM[1]FF[4]SZ[9];B[ee]W[ef];B[ff]" + ";W[df];B[fe];W[fc];B[ec];W[gd];B[fb])"
sgf_game = Sgf_game.from_string(sgf_content)

game_state = GameState.new_game(19)

for item in sgf_game.main_sequence_iter():
    color, move_tuple = item.get_move()
    if color is not None and move_tuple is not None:
        row, col = move_tuple
        point = Point(row + 1, col + 1)
        move = Move.play(point)
        # 将读出的落子应用到棋盘上
        game_state = game_state.apply_move(move)
        print_board(game_state.board)

