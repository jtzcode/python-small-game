from game.utils import print_bold

class Hut:
    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("GOOD JOB! Hut %d acquired" % self.number)

    def get_occupant_type(self):
        if self.is_acquired:
            type = 'ACQUIRED'
        elif self.occupant is None:
            type = 'unoccupied'
        else:
            type = self.occupant.unit_type
        
        return type
