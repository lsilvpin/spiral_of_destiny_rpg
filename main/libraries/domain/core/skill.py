
class Skill:

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        self.is_active = False

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def __eq__(self, other):
        return self.name == other.name and self.bonus == other.bonus
