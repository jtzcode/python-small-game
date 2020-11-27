from game.units import OrcRider, Knight
class UnitFactory:
    units_dict = {
        'rider': OrcRider,
        'knight': Knight
    }

    @classmethod
    def create_unit(cls, unit_type):
        key = unit_type.lower()
        return cls.units_dict.get(key)()