import random
from main.libraries.domain.core.character import Character
from main.libraries.domain.core.skill import Skill
from main.libraries.tools.core.log_tool import LogTool
from main.libraries.tools.core.settings_tool import SettingsTool


class MoveTool:

    characterAttribute: int = 0
    first1d6Roll: int = 0
    second1d6Roll: int = 0
    third1d6Roll: int = 0
    totalRoll: int = 0
    skillBonus: int = 0
    bestSkill: Skill = None
    modifier: int = 0
    attributeDelta: int = 0
    total: int = 0

    def __init__(self, logTool: LogTool):
        self.logTool = logTool

    def roll(
        self,
        character: Character = Character("Default"),
        characterAttribute: int = 10,
        modifier: int = 0,
        appliableSkills: list[str] = [],
    ) -> str:
        self.characterAttribute = characterAttribute
        self.modifier = modifier
        first1d6Roll = random.randint(1, 6)
        self.first1d6Roll = first1d6Roll
        self.logTool.info(f"First 1d6 roll: {first1d6Roll}")
        second1d6Roll = random.randint(1, 6)
        self.second1d6Roll = second1d6Roll
        self.logTool.info(f"Second 1d6 roll: {second1d6Roll}")
        third1d6Roll = random.randint(1, 6)
        self.third1d6Roll = third1d6Roll
        self.logTool.info(f"Third 1d6 roll: {third1d6Roll}")
        self.totalRoll = first1d6Roll + second1d6Roll + third1d6Roll
        self.logTool.info(f"Total roll: {self.totalRoll}")
        if self.totalRoll in [3, 4]:
            self.logTool.warn("Critical failure")
            return "Critical failure"
        if self.totalRoll in [17, 18]:
            self.logTool.warn("Critical success")
            return "Critical success"
        characterAppliableSkills = list(
            filter(lambda skill: skill.name in appliableSkills, character.skills)
        )
        bestSkill = max(characterAppliableSkills, key=lambda skill: skill.bonus)
        self.bestSkill = bestSkill
        self.skillBonus = bestSkill.bonus if bestSkill else 0
        assert 0 <= characterAttribute <= 20
        self.attributeDelta = (characterAttribute - 10) // 2
        self.total = self.totalRoll + self.attributeDelta + self.skillBonus + modifier
        assert 3 <= self.totalRoll <= 18
        assert -5 <= self.attributeDelta <= 5
        assert -2 <= self.skillBonus <= 3
        assert -5 <= modifier <= 5
        self.logTool.info(f"Roll: {self.totalRoll}")
        self.logTool.info(f"Attribute delta: {self.attributeDelta}")
        self.logTool.info(f"Skill bonus: {self.skillBonus}")
        self.logTool.info(f"Modifier: {modifier}")
        self.logTool.info(
            f"Total = {self.totalRoll} (roll) + {self.attributeDelta} (attribute delta) + {self.skillBonus} (skill bonus) + {modifier} (modifier) = {self.total}"
        )
        if self.total <= 7:
            self.logTool.info("Failure")
            return "Failure"
        if 8 <= self.total <= 13:
            self.logTool.info("Partial success")
            return "Partial success"
        if 14 <= self.total:
            self.logTool.info("Success")
            return "Success"
        raise Exception("Invalid roll result")
