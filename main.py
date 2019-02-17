from solver import Board, CONST_DIM

import random


if __name__ == '__main__':
    row_sample = []
    initial_blocks = []
    for i in random.sample(range(CONST_DIM**2), CONST_DIM**2):
        row_sample.append(i)
        if len(row_sample) == CONST_DIM:
            initial_blocks.append(row_sample)
            row_sample = []

    print(initial_blocks)


    initial = Board(initial_blocks)

    print(initial.is_goal())


