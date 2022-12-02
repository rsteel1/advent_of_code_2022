from enum import Enum, auto


class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


shapes = {
    "A": Shape.ROCK,
    "X": Shape.ROCK,
    "B": Shape.PAPER,
    "Y": Shape.PAPER,
    "C": Shape.SCISSORS,
    "Z": Shape.SCISSORS
}

shape_scores = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3
}

win_scenarios = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER
}


def get_shape(shape_letter):
    return shapes[shape_letter]


def get_shape_score(shape: Shape):
    return shape_scores[shape]


def get_outcome_score(opp_shape: Shape, my_shape: Shape):
    if opp_shape == my_shape:
        return 3
    elif win_scenarios[my_shape] == opp_shape:
        return 6
    return 0


def get_round_score(opp_shape: Shape, my_shape: Shape):
    return get_shape_score(my_shape) + get_outcome_score(opp_shape, my_shape)


def calculate_part_1_score(rounds):
    total = 0
    for round in rounds:
        total += get_round_score(round[0], round[1])
    return total


def get_shape_for_desired_outcome(shape, outcome):
    if outcome == "X":
        return win_scenarios[shape]
    elif outcome == "Y":
        return shape
    else:
        return [k for k, v in win_scenarios.items() if v == shape][0]


def calculate_part_2_score(rounds):
    total = 0
    for round in rounds:
        shape, outcome = round
        desired_shape = get_shape_for_desired_outcome(shape, outcome)
        total += get_round_score(shape, desired_shape)
    return total


def process_input(file_path, is_part_2=False):
    with open(file_path, "r") as infile:
        rounds = []
        for round in infile.read().splitlines():
            round = round.split(" ")
            rounds.append([get_shape(round[0]), round[1] if is_part_2 else get_shape(round[1])])
        return rounds


if __name__ == "__main__":
    rounds = process_input("day2/input.txt")
    print(calculate_part_1_score(rounds))

    rounds = process_input("day2/input.txt", is_part_2=True)
    print(calculate_part_2_score(rounds))
