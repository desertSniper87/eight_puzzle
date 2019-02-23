from typing import List

from solver import Board, CONST_DIM

import random

def random_initial_blocks() -> List[List[int]]:
    row_sample = []
    initial_blocks = []

    for i in random.sample(range(CONST_DIM ** 2), CONST_DIM ** 2):
        row_sample.append(i)
        if len(row_sample) == CONST_DIM:
            initial_blocks.append(row_sample)
            row_sample = []

    return initial_blocks


if __name__ == '__main__':

    # initial_blocks = random_initial_blocks()
    initial_blocks = [
        [8,  1,  3],
        [4,  0,  2],
        [7,  6,  5]
    ]

    DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    initial = Board(initial_blocks)
    initial.print_elements("Initial")
    print("initial.manhattan(): ", initial.manhattan())

    # TODO: Ask a question about object inference in mypy stackoverflow
    for direction in DIRECTIONS:
        possible_moves: List[Board] = []
        if initial.is_move_possible(direction):
            new = initial.go(direction)
            print(new.manhattan())
            possible_moves.append(new)

            recomended_move = min(possible_moves, key= lambda x: x.manhattan())
            recomended_move.print_elements('recomended')
            print('recomended_move.manhattan()', recomended_move.manhattan())
            # new.print_elements(direction)


        else:
            print(f'Moving in {direction} not possible.')

