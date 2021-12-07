SAMPLE_INPUT = "sample-input.txt"
REAL_INPUT = "input.txt"
with open(REAL_INPUT) as file:
    lines = file.readlines()
    size_of_file = len(lines)
    size_of_row = len(lines[0].strip())
    counts = [0] * size_of_row

    for line in lines:
        for i in range(size_of_row):
            counts[i] += int(line[i])

    halved_file_size = size_of_file / 2
    gamma = ""
    epsilon = ""
    for count in counts:
        if count > halved_file_size:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))
