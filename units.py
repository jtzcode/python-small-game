class GameUnit:
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None
    
    def info(self):
        """Information on the unit (overridden in subclasses)"""
        pass


class Knight(GameUnit):
    def __init__(self, name="Sir Eggy"):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        print("I  am an Eggy Knight!")

class OrcRider(GameUnit):
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")