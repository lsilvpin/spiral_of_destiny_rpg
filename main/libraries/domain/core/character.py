
class Character:
    def __init__(self, name: str, traces: list = [], skills: list = []):
        self.name = name
        self.intelligence = 10
        self.dexterity = 10
        self.strength = 10
        self.vitality = 10
        self.hp = self.calculate_hp()
        self.fp = self.calculate_fp()
        self.sp = 0
        self.supply = 0
        self.traces = traces
        self.skills = skills

    def calculate_hp(self):
        return self.strength + self.vitality

    def calculate_fp(self):
        return self.strength