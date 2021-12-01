SAMPLE_INPUT = "sample-part.txt"
REAL_INPUT = "part1-input.txt"
with open(REAL_INPUT) as file:
    lines = file.readlines()
    total_file_size = len(lines)
    total = 0
    for index, item in enumerate(lines):
        previous_index = index - 1
        next_index = index + 1
        next_next_index = next_index + 1

        if previous_index >= 0 and next_index < total_file_size and next_next_index < total_file_size:
            base = int(item) + int(lines[next_index])
            if base + int(lines[previous_index]) < base + int(lines[next_next_index]):
                total += 1

    print(total)



