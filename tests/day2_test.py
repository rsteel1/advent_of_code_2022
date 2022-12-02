import unittest
from day2.day2 import *

class TestGetShape(unittest.TestCase):
    def test_get_shape(self):
        self.assertEquals(get_shape("A"), Shape.ROCK)
        self.assertEquals(get_shape("X"), Shape.ROCK)
        self.assertEquals(get_shape("B"), Shape.PAPER)
        self.assertEquals(get_shape("Y"), Shape.PAPER)
        self.assertEquals(get_shape("C"), Shape.SCISSORS)
        self.assertEquals(get_shape("Z"), Shape.SCISSORS)

    def test_get_shape_for_desired_outcome(self):
        self.assertEquals(get_shape_for_desired_outcome(Shape.ROCK, "X"), Shape.SCISSORS)
        self.assertEquals(get_shape_for_desired_outcome(Shape.ROCK, "Y"), Shape.ROCK)
        self.assertEquals(get_shape_for_desired_outcome(Shape.ROCK, "Z"), Shape.PAPER)
        self.assertEquals(get_shape_for_desired_outcome(Shape.PAPER, "X"), Shape.ROCK)
        self.assertEquals(get_shape_for_desired_outcome(Shape.PAPER, "Y"), Shape.PAPER)
        self.assertEquals(get_shape_for_desired_outcome(Shape.PAPER, "Z"), Shape.SCISSORS)
        self.assertEquals(get_shape_for_desired_outcome(Shape.SCISSORS, "X"), Shape.PAPER)
        self.assertEquals(get_shape_for_desired_outcome(Shape.SCISSORS, "Y"), Shape.SCISSORS)
        self.assertEquals(get_shape_for_desired_outcome(Shape.SCISSORS, "Z"), Shape.ROCK)


class TestScores(unittest.TestCase):
    def test_shape_score(self):
        self.assertEquals(get_shape_score(Shape.ROCK), 1)
        self.assertEquals(get_shape_score(Shape.PAPER), 2)
        self.assertEquals(get_shape_score(Shape.SCISSORS), 3)

    def test_outcome_score(self):
        self.assertEquals(get_outcome_score(Shape.ROCK, Shape.PAPER), 6)
        self.assertEquals(get_outcome_score(Shape.PAPER, Shape.SCISSORS), 6)
        self.assertEquals(get_outcome_score(Shape.SCISSORS, Shape.ROCK), 6)
        self.assertEquals(get_outcome_score(Shape.ROCK, Shape.ROCK), 3)
        self.assertEquals(get_outcome_score(Shape.PAPER, Shape.PAPER), 3)
        self.assertEquals(get_outcome_score(Shape.SCISSORS, Shape.SCISSORS), 3)
        self.assertEquals(get_outcome_score(Shape.PAPER, Shape.ROCK), 0)
        self.assertEquals(get_outcome_score(Shape.SCISSORS, Shape.PAPER), 0)
        self.assertEquals(get_outcome_score(Shape.ROCK, Shape.SCISSORS), 0)

    def test_round_score(self):
        self.assertEquals(get_round_score(Shape.ROCK, Shape.PAPER), 8)
        self.assertEquals(get_round_score(Shape.PAPER, Shape.SCISSORS), 9)
        self.assertEquals(get_round_score(Shape.SCISSORS, Shape.ROCK), 7)
        self.assertEquals(get_round_score(Shape.ROCK, Shape.ROCK), 4)
        self.assertEquals(get_round_score(Shape.PAPER, Shape.PAPER), 5)
        self.assertEquals(get_round_score(Shape.SCISSORS, Shape.SCISSORS), 6)
        self.assertEquals(get_round_score(Shape.PAPER, Shape.ROCK), 1)
        self.assertEquals(get_round_score(Shape.SCISSORS, Shape.PAPER), 2)
        self.assertEquals(get_round_score(Shape.ROCK, Shape.SCISSORS), 3)

    def test_part_1_score(self):
        rounds = process_input("tests/day2/test_input.txt")
        self.assertEquals(calculate_part_1_score(rounds), 45)

    def test_part_2_score(self):
        rounds = process_input("tests/day2/test_input_short.txt", is_part_2=True)
        self.assertEquals(calculate_part_2_score(rounds), 3)


class TestInputProcessing(unittest.TestCase):
    def test_process_input(self):
        expected = [
            [Shape.ROCK, Shape.ROCK], 
            [Shape.ROCK, Shape.PAPER], 
            [Shape.ROCK, Shape.SCISSORS],
            [Shape.PAPER, Shape.ROCK],
            [Shape.PAPER, Shape.PAPER],
            [Shape.PAPER, Shape.SCISSORS],
            [Shape.SCISSORS, Shape.ROCK],
            [Shape.SCISSORS, Shape.PAPER],
            [Shape.SCISSORS, Shape.SCISSORS]
        ]
        self.assertEquals(process_input("tests/day2/test_input.txt"), expected)

    def test_process_input_part_2(self):
        expected = [
            [Shape.ROCK, "X"], 
            [Shape.ROCK, "Y"], 
            [Shape.ROCK, "Z"],
            [Shape.PAPER, "X"],
            [Shape.PAPER, "Y"],
            [Shape.PAPER, "Z"],
            [Shape.SCISSORS, "X"],
            [Shape.SCISSORS, "Y"],
            [Shape.SCISSORS, "Z"]
        ]
        self.assertEquals(process_input("tests/day2/test_input.txt", is_part_2=True), expected)