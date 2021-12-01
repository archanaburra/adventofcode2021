SAMPLE_INPUT = "sample-part.txt"
REAL_INPUT = "part1-input.txt"
with open(REAL_INPUT) as file:
    lines = file.readlines()
    total = 0
    for index, item in enumerate(lines):
        previous_index = index - 1
        if previous_index >= 0 and int(lines[previous_index]) < int(item):
            total += 1

    print(total)



