import numpy as np

SAMPLE_INPUT = "sample-input.txt"
REAL_INPUT = "input.txt"

# part 1
with open(REAL_INPUT) as file:
    input = [int(c) for c in file.readlines()[0].split(",")]
    median = np.median(input)
    fuel_sum = sum([abs(median - i) for i in input])
    print(fuel_sum)



