SAMPLE_INPUT = "sample-input.txt"
REAL_INPUT = "input.txt"


def bit_active(line, i):
    int_value = int(line, 2)
    bit_active_at_i = 2 ** i
    return int(bin(int_value & bit_active_at_i), 2) >= 1


def get_counts(lines):
    counts = [0] * size_of_row

    for line in lines:
        for i in range(size_of_row):
            counts[i] += int(line[i])
    return counts


def get_max(counts, i, size_of_file):
    return 1 if counts[i] * 2 >= size_of_file else 0


def get_min(counts, i, size_of_file):
    return 0 if counts[i] * 2 >= size_of_file else 1


def get_remaining_lines(lines, i, instruction):
    counts = get_counts(lines)
    size_of_file = len(lines)
    oxygen_bit = instruction(counts, i, size_of_file)

    offset = size_of_row - 1 - i
    if oxygen_bit:
        lines = [line for line in lines if bit_active(line, offset)]
    else:
        lines = [line for line in lines if not bit_active(line, offset)]

    if len(lines) > 1:
        return get_remaining_lines(lines, i + 1, instruction)
    else:
        return lines


with open(REAL_INPUT) as file:
    lines = file.readlines()
    size_of_row = len(lines[0].strip())

    oxy_lines = get_remaining_lines(lines[:], 0, get_max)
    carbon_lines = get_remaining_lines(lines[:], 0, get_min)

    print(int(oxy_lines[0], 2) * int(carbon_lines[0], 2))
