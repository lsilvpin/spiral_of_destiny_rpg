class DiceProbabilities:
    """
    A class representing the probabilities of rolling different sums with two six-sided dice.

    Attributes:
        values (dict): A dictionary mapping the sum of two dice rolls to its probability.
    """

    values = {
        3: 1 / 216,   # 0.46%
        4: 3 / 216,   # 1.39%
        5: 6 / 216,   # 2.78%
        6: 10 / 216,  # 4.63%
        7: 15 / 216,  # 6.94%
        8: 21 / 216,  # 9.72%
        9: 25 / 216,  # 11.57%
        10: 27 / 216, # 12.50%
        11: 27 / 216, # 12.50%
        12: 25 / 216, # 11.57%
        13: 21 / 216, # 9.72%
        14: 15 / 216, # 6.94%
        15: 10 / 216, # 4.63%
        16: 6 / 216,  # 2.78%
        17: 3 / 216,  # 1.39%
        18: 1 / 216,  # 0.46%
    }

    def probability_of(self, value: int) -> float:
        """
        Calculates the probability of rolling a value with three six-sided dice.

        Args:
            value (int): The desired sum of the three dice rolls. Must be between 2 and 12 (inclusive).

        Returns:
            float: The probability of rolling the given value.
        """
        assert 3 <= value <= 18
        return self.values[value]

    def acumulated_probability(self, value: int) -> float:
        """
        Calculates the accumulated probability of rolling a value with three six-sided dice.

        Args:
            value (int): The desired sum of the three dice rolls. Must be between 3 and 18 (inclusive).

        Returns:
            float: The accumulated probability of rolling the given value.
        """
        assert 3 <= value <= 18
        return sum([self.values[i] for i in range(3, value + 1)])

    def print_all_acumulated_probabilities(self):
        """
        Prints the accumulated probabilities of rolling each possible value with three six-sided dice.
        """
        for i in range(3, 19):
            print(
                f"Acumulated probability of rolling {i}: {self.acumulated_probability(i)}"
            )
