"""
Package docstring
"""
import random

from character import errors
from character.mutables import Mutable


class Character(object):
    intellectual_quotient = 0
    mental_endurance = 0
    mental_affinity = 0
    physical_strength = 0
    physical_prowess = 0
    physical_endurance = 0
    speed = 0
    potential_psychic_energy = None

    def __init__(self, **kwargs):
        self.intellectual_quotient = kwargs.get(
            'iq', self._random_human_stat()
        )
        self.mental_endurance = kwargs.get('me', self._random_human_stat())
        self.mental_affinity = kwargs.get('ma', self._random_human_stat())
        self.physical_strength = kwargs.get('ps', self._random_human_stat())
        self.physical_prowess = kwargs.get('pp', self._random_human_stat())
        self.physical_endurance = kwargs.get('pe', self._random_human_stat())
        self.speed = kwargs.get('spd', self._random_human_stat())
        self.potential_psychic_energy = Mutable(kwargs.get('ppe', 0))

    def __str__(self):
        abbreviation_table = {
            'intellectual_quotient': 'IQ',
            'mental_endurance': 'ME',
            'mental_affinity': 'MA',
            'physical_strength': 'PS',
            'physical_prowess': 'PP',
            'physical_endurance': 'PE',
            'speed': 'SPD',
            'potential_psychic_energy': 'PPE',
        }
        return "\n".join(
            [
                "{}: {}".format(
                    abbreviation_table.get(attr), getattr(self, attr)
                )
                for attr in self.__dict__.keys()
            ]
        )

    @property
    def yards_per_melee(self):
        return 20.0 * self.speed

    def _random_human_stat(self):
        return random.randint(8, 10)


