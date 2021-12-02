PART1_REAL_INPUT = "part1-input.txt"
PART1_SAMPLE_INPUT = "part1-sample-input.txt"


class Coordinate:
    def __init__(self, x_axis: int = 0, y_axis: int = 0, aim: int = 0):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.aim = aim

    def multiplied_coordinates(self):
        return self.x_axis * self.y_axis


def update(coordinate: Coordinate, x_amount: int = 0, y_amount: int = 0, aim_amount: int = 0):
    coordinate.x_axis += x_amount
    coordinate.y_axis += y_amount
    coordinate.aim += aim_amount


def forward(x, loc: Coordinate):
    update(loc, x_amount=x, y_amount=loc.aim * x)


def down(y, loc: Coordinate):
    update(loc, aim_amount=y)


def up(y, loc: Coordinate):
    update(loc, aim_amount=-y)


with open(PART1_SAMPLE_INPUT) as file:
    coordinate = Coordinate()
    line = file.readline()
    while line:
        (instruction, amount) = line.split(" ")
        eval(instruction)(int(amount), coordinate)
        line = file.readline()

print(coordinate.multiplied_coordinates())
