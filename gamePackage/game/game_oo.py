from game.units import Knight, OrcRider
from game.hut import Hut
from game.factory import UnitFactory
from game.utils import print_bold
import random


class GameOfThrones:
    factory = UnitFactory
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
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))
    
    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")
    
    def get_occupants(self):
        return [x.get_occupant_type() for x in self.huts]


    def _process_user_choice(self):
        verifying_choice = True
        index = 0
        print("Current Occupant: %s" % self.get_occupants())

        while verifying_choice:
            msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
            user_choice = input("\n" + msg)
            try:
                index = int(user_choice)
            except ValueError as e:
                print_bold("Invalid input args: %s\n" % e.args)
                continue

            try:
                if self.huts[index - 1].is_acquired:
                    print("You have already acquired this hut. Try again."
                        "<INFO: You can NOT get healed in already acquired hut.>")
                else:
                    verifying_choice = False
            except IndexError:
                print('Invalid input: ', index)
                print_bold('Number should be in the range of 1-5. Try again.')
                continue
            
        return index
    
    def setup_game_scenario(self):
        self.player = type(self).factory.create_unit('knight')
        self._occupy_nuts()

        self.show_game_mission()
        self.player.show_health(bold=True)

    def play(self):
        self.setup_game_scenario()
        acquired_hut_counter = 0
        while acquired_hut_counter < 5:
            index = self._process_user_choice()
            self.player.acquire_hut(self.huts[index-1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break

            if self.huts[index-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")

if __name__ == '__main__':
    game = GameOfThrones()
    game.play()
