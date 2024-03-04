import pytest
from main.libraries.di_container import Container
from main.libraries.domain.core.character import Character
from main.libraries.domain.core.skill import Skill
from main.libraries.tools.core.move_tool import MoveTool


@pytest.fixture
def move_tool():
    container = Container()
    return container.move_tool()


def test_should_make_a_lot_of_rolls_and_print_all_results(move_tool):
    all_infos_to_print = []
    for i in range(0, 10):
        for skill_bonus in range(-2, 4):
            allResults = []
            for attribute in range(0, 21):
                for modifier in range(-5, 6):
                    character = Character(
                        "Fulano", skills=[Skill("Martelar", skill_bonus)]
                    )
                    result = move_tool.roll(
                        character, attribute, modifier, ["Martelar"]
                    )
                    allResults.append(move_tool.total)
                    assert result in [
                        "Critical failure",
                        "Critical success",
                        "Failure",
                        "Partial success",
                        "Success",
                    ]
                    print(
                        f"Attribute: {attribute}, Skill bonus: {skill_bonus}, Modifier: {modifier}, Result: {result}"
                    )
            all_infos_to_print.append(
                {
                    "skill_bonus": skill_bonus,
                    "number_of_rolls": len(allResults),
                    "number_of_successful_rolls": len(
                        [result for result in allResults if result >= 13]
                    ),
                    "number_of_partial_successful_rolls": len(
                        [result for result in allResults if 9 <= result <= 12]
                    ),
                    "number_of_failed_rolls": len(
                        [result for result in allResults if result <= 8]
                    ),
                }
            )
            assert -9 <= min(allResults)
            assert max(allResults) <= 31
    all_infos_to_print_ordered_by_skill_bonus = sorted(
        all_infos_to_print, key=lambda info_to_print: info_to_print["skill_bonus"]
    )
    for info_to_print in all_infos_to_print_ordered_by_skill_bonus:
        print(f"Skill bonus: {info_to_print['skill_bonus']}")
        print(f"Number of rolls: {info_to_print['number_of_rolls']}")
        print(
            f"Number of successful rolls: {info_to_print['number_of_successful_rolls']}, percentage: {info_to_print['number_of_successful_rolls']/info_to_print['number_of_rolls']}"
        )
        print(
            f"Number of partial successful rolls: {info_to_print['number_of_partial_successful_rolls']}, percentage: {info_to_print['number_of_partial_successful_rolls']/info_to_print['number_of_rolls']}"
        )
        print(
            f"Number of failed rolls: {info_to_print['number_of_failed_rolls']}, percentage: {info_to_print['number_of_failed_rolls']/info_to_print['number_of_rolls']}"
        )
