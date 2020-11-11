from units import Knight, OrcRider
from hut import Hut
from utils import print_bold
import random


class AttackOfTheOrcs:
    def __init__(self):
        self.huts = []
        self.player = None
    
    def _occupy_nuts(self):
        for i in range(5):
            choices = ['enemy', 'friend', None]
            computer_choice = random.choice(choices)
            if computer_choice == 'enemy':
                name =  'enemy-' + str(i + 1)
                self.huts.append(Hut(i+1, OrcRider(name)))
    
    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")
    
    def play(self):
        self.player = Knight()
        self._occupy_nuts()
        acquired_hut_counter = 0
