class BowlingGame:
    """
    A class to represent a bowling game and calculate the score.
    """
    
    def __init__(self):
        """
        Initialize a new game of bowling with an empty list of rolls.
        """
        self.rolls = []
    
    def roll(self, pins):
        """
        Record the number of pins knocked down in a roll.
        
        Args:
            pins (int): The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)
    
    def score(self):
        """
        Calculate the total score for the bowling game.
        
        Returns:
            int: The total score of the game.
        """
        total_score = 0
        roll_index = 0
        
        for frame in range(10):
            if self.is_strike(roll_index):  # Strike
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):  # Spare
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:  # Open frame
                total_score += self.sum_of_balls_in_frame(roll_index)
                roll_index += 2
                
        return total_score
    
    def is_strike(self, roll_index):
        """
        Determine if the current roll is a strike.
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[roll_index] == 10
    
    def is_spare(self, roll_index):
        """
        Determine if the current frame is a spare.
        
        Args:
            roll_index (int): The index of the first roll of the frame in the rolls list.
        
        Returns:
            bool: True if the frame is a spare, False otherwise.
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def strike_bonus(self, roll_index):
        """
        Calculate the strike bonus for the current roll.
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            int: The bonus points for the strike (next two rolls).
        """
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    def spare_bonus(self, roll_index):
        """
        Calculate the spare bonus for the current frame.
        
        Args:
            roll_index (int): The index of the first roll of the frame in the rolls list.
        
        Returns:
            int: The bonus points for the spare (next one roll).
        """
        return self.rolls[roll_index + 2]
    
    def sum_of_balls_in_frame(self, roll_index):
        """
        Sum the total number of pins knocked down in a frame.
        
        Args:
            roll_index (int): The index of the first roll of the frame in the rolls list.
        
        Returns:
            int: The sum of pins knocked down in the two rolls of the frame.
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
