import unittest

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """Registers a roll in the game."""
        self.rolls.append(pins)

    def score(self):
        """Calculates the total score for the game."""
        score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):  # Strike
                score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):  # Spare
                score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:  # Open frame
                score += self.sum_of_balls_in_frame(roll_index)
                roll_index += 2
        return score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def sum_of_balls_in_frame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """Create a new BowlingGame for each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Rolls the ball `n` times with `pins` pins knocked down."""
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down (all gutter balls)."""
        self.roll_many(20, 0)  # 20 rolls with 0 pins (gutter game)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        """Test a game where 1 pin is knocked down each roll."""
        self.roll_many(20, 1)  # 20 rolls with 1 pin each
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        """Test a game with one spare and a subsequent roll."""
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.roll_many(17, 0)  # Fill the remaining rolls with gutter balls
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        """Test a game with one strike and subsequent rolls."""
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)  # Fill the remaining rolls with gutter balls
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        """Test a perfect game with 12 strikes."""
        self.roll_many(12, 10)  # 12 strikes
        self.assertEqual(self.game.score(), 300)


if __name__ == '__main__':
    unittest.main()
