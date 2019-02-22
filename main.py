from typing import List

from solver import Board, CONST_DIM

import random
from pprint import pprint

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
    # initial_blocks = [[8, 0, 1],
    #                   [3, 5, 2],
    #                   [6, 4, 7]]



    # pprint(initial_blocks)

    initial = Board(initial_blocks)

    # print(initial.manhattan())
    # print(initial.hamming())

    # print(initial.is_goal())

    print(initial.row_containing_blank_piece())
    print(initial.column_containing_blank_piece())


