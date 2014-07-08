"""
Package docstring
"""
import random

from character import errors


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
        self.potential_psychic_energy = PPE(kwargs.get('ppe', 0))

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


class PPE(object):
    current = 0
    max = 0

    def __init__(self, max=0):
        self.max = max
        self.current = max

    def __str__(self):
        return "{}/{}".format(self.current, self.max)

    def use_ppe(self, amount):
        """
        This function attempts to reduce the PPE value. If the result is less
        than zero, it throws an exception.

        :param amount: Amount of PPE being used
        :type amount: int
        :return: Returns the remaining total PPE after expenditure
        :rtype: int
        :exception: :class:`~character.errors.NotEnoughPpeException` is raised
            if there is not enough PPE left to satisfy the amount requested.
        :exception: :class:`~character.errors.CharacterNotPowerfulEnough` is
            raised if the character could NOT have enough PPE.
        """

        if amount > self.max:
            raise errors.CharacterNotPowerfulEnough
        elif self.current - amount < 0:
            raise errors.NotEnoughPpeException
        self.current -= amount
        return self.current

    def reclaim_ppe(self, amount):
        """
        This function attempts to increase the PPE value. If the result is
        than the max, it sets to max and throws exception.

        :param amount: Amount of PPE being returned
        :type amount: int
        :return: Returns the new amount of PPE after addition
        :rtype: int
        :exception: :class:`~character.errors.PpeOverload` is raised if the
            character is already at max or would add above max
        """
        new_amount = self.current + amount
        if new_amount > self.max:
            self.current = self.max
            raise errors.PpeOverload
        self.current = min(new_amount, self.max)
        return self.current
