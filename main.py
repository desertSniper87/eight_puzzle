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

    initial_blocks = random_initial_blocks()
    # initial_blocks = [
    #     [3, 5, 2],
    #     [8, 0, 1],
    #     [6, 4, 7]]

    DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    initial = Board(initial_blocks)
    initial.print_elements()
    # TODO: Ask a question about object inference in mypy
    for direction in DIRECTIONS:
        if initial.is_move_possible(direction):
            new = initial.go(direction)
            new.print_elements()

        else:
            print(f'Moving in {direction} not possible.')

