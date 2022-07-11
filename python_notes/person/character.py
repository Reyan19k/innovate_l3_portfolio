

class Superhero():
    def __init__(self, real_name, alias):
        self.real = real_name
        self.alias = alias

    def set_power(self, powers):
        self.powers = powers

    def get_power(self):
        print(self.powers)

