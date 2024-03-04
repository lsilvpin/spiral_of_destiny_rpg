import pytest

from main.libraries.utils.constants.dice_probabilities import DiceProbabilities


@pytest.fixture
def dice_probabilities():
    return DiceProbabilities()


def test_should_test_individual_probabilities(dice_probabilities):
    expected_values = [
        1 / 216,  # 0.46% (3)
        3 / 216,  # 1.39% (4)
        6 / 216,  # 2.78% (5)
        10 / 216,  # 4.63% (6)
        15 / 216,  # 6.94% (7)
        21 / 216,  # 9.72% (8)
        25 / 216,  # 11.57% (9)
        27 / 216,  # 12.50% (10)
        27 / 216,  # 12.50% (11)
        25 / 216,  # 11.57% (12)
        21 / 216,  # 9.72% (13)
        15 / 216,  # 6.94% (14)
        10 / 216,  # 4.63% (15)
        6 / 216,  # 2.78% (16)
        3 / 216,  # 1.39% (17)
        1 / 216,  # 0.46% (18)
    ]
    for i in range(3, 19):
        assert dice_probabilities.probability_of(i) == expected_values[i - 3]


def test_acumulated_probability(dice_probabilities):
    expected_values = [
        1 / 216,  # 0.46% (<=3)
        4 / 216,  # 1.85% (<=4) -> Critical Failure/Success threshold
        10 / 216,  # 4.63% (<=5)
        20 / 216,  # 9.26% (<=6)
        35 / 216,  # 16.20% (<=7) -> (16.20%-1.85%) = 14.35% Failure/Success threshold
        56 / 216,  # 25.93% (<=8)
        81 / 216,  # 37.50% (<=9)
        108 / 216,  # 50.00% (<=10)
        135 / 216,  # 62.50% (<=11)
        160 / 216,  # 74.07% (<=12)
        181 / 216,  # 83.80% (<=13) -> (83.80%-16.20%) = 67.60% Parcial Success threshold
        196 / 216,  # 90.74% (<=14)
        206 / 216,  # 95.37% (<=15)
        212 / 216,  # 98.15% (<=16)
        215 / 216,  # 99.54% (<=17)
        216 / 216,  # 100.00% (<=18)
    ]
    for i in range(3, 19):
        # On assertion compare just the first 6 decimal places
        assert round(dice_probabilities.acumulated_probability(i), 6) == round(
            expected_values[i - 3], 6
        )


def test_should_print_all_acumulated_probabilities(capsys, dice_probabilities):
    dice_probabilities.print_all_acumulated_probabilities()
    captured = capsys.readouterr()
    expected_output = "\n".join(
        [
            f"Acumulated probability of rolling {i}: {dice_probabilities.acumulated_probability(i)}"
            for i in range(3, 19)
        ]
    )
    assert captured.out.strip() == expected_output
    print(captured.out.strip())
