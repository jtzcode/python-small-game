from game.utils import print_bold, weighted_random_selection
from abc import ABCMeta, abstractmethod
from game.exceptions import GameUnitException
import random

class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None
    
    @abstractmethod
    def info(self):
        """Information on the unit (overridden in subclasses)"""
        pass

    def show_health(self, bold=False, end='\n'):
        # TODO: what if there is no enemy?
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
    
    def attack(self, enemy):
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end='  ')
        enemy.show_health(end='  ')



class Knight(AbstractGameUnit):
    def __init__(self, name="Sir Eggy"):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        print("I  am an Eggy Knight!")
    
    def run_away(self):
        print_bold("RUNNING AWAY...")
        self.enemy = None
    
    def heal(self, heal_by=2, full_healing=True):
        if self.health_meter == self.max_hp:
            return
        
        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter = max(self.max_hp, self.health_meter + heal_by)
        
        if self.health_meter > self.max_hp:
            raise GameUnitException("Health meter greater than maximum value %d" % self.max_hp, 100)

        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def acquire_hut(self, hut):
        print_bold("Entering hut %d..." % hut.number, end=' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit) and hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'
        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')

            while continue_attack:
                continue_attack = input(".......continue attack? (y/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break
                self.attack(hut.occupant)
                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() == 'unoccupied':
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            hut.acquire(self)
            self.heal()

class OrcRider(AbstractGameUnit):
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("Grrrr..I am the Night King. Don't mess with me.")