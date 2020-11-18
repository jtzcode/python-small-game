from game.units import Knight
from game.hut import Hut
import unittest

class TestHut(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()
    
    def test_acquire_hut(self):
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)

if __name__ == '__main__':
    unittest.main()