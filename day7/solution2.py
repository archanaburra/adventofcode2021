import math

import numpy as np

SAMPLE_INPUT = "sample-input.txt"
REAL_INPUT = "input.txt"


def find_sum_to_n(n):
    return n * (n + 1) / 2  # thx gauss <3

# part 2
with open(REAL_INPUT) as file:
    input = [int(c) for c in file.readlines()[0].split(",")]
    # note sometimes the ceil works better but can't figure out a good way to round deterministically :(
    mean1 = math.floor(np.mean(input))
    mean2 = math.ceil(np.mean(input))
    fuel_sum1 = sum([find_sum_to_n(abs(mean1 - i)) for i in input])
    fuel_sum2 = sum([find_sum_to_n(abs(mean2 - i)) for i in input])
    print(min(fuel_sum1, fuel_sum2))
