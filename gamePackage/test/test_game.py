import unittest
from unittest import mock
from game.units import Knight, OrcRider, AbstractGameUnit
from game.hut import Hut
from game.utils import weighted_random_selection
from game.game_oo import GameOfThrones

class TestGame(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()
        self.enemy = OrcRider()
    
    def test_injured_unit_selection(self):
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight, self.enemy)
            self.assertIsInstance(injured_unit, AbstractGameUnit, "Injured unit must be an instance of AbstractGameUnit")

    def test_play(self):
        game = GameOfThrones()
        self.hut_selection_count = 0
        with mock.patch('builtins.input', new = self.user_input_processor):
            game.play()
            acquired_huts = [h.is_acquired for h in game.huts]
            if all(acquired_huts):
                self.assertTrue(game.player.health_meter > 0)
            else:
                self.assertFalse(game.player.health_meter > 0)
    
    def user_input_processor(self, prompt):
        if 'hut' in prompt.lower():
            self.hut_selection_count += 1
            assert self.hut_selection_count <= 5
            return self.hut_selection_count
        elif 'attack' in prompt.lower():
            return 'y'
        else:
            raise Exception("Unexpected prompt!", prompt)

if __name__ == '__main__':
    unittest.main()