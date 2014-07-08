"""
Collection of all mutable stats for a character.
"""
from character import errors


class Mutable(object):
    current = 0
    max = 0

    def __init__(self, max=0):
        self.max = max
        self.current = max

    def __str__(self):
        return "{}/{}".format(self.current, self.max)

    def use(self, amount):
        """
        This function attempts to reduce the PPE value. If the result is less
        than zero, it throws an exception.

        :param amount: Amount of PPE being used
        :type amount: int
        :return: Returns the remaining total PPE after expenditure
        :rtype: int
        :exception: :class:`~character.errors.NotEnoughMutablesException` is raised
            if there is not enough PPE left to satisfy the amount requested.
        :exception: :class:`~character.errors.CharacterNotPowerfulEnough` is
            raised if the character could NOT have enough PPE.
        """

        if amount > self.max:
            raise errors.CharacterNotPowerfulEnough
        elif self.current - amount < 0:
            raise errors.NotEnoughMutablesException
        self.current -= amount
        return self.current

    def reclaim(self, amount):
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
            raise errors.MutableOverload
        self.current = min(new_amount, self.max)
        return self.current


class ISP(Mutable):
    pass


class PPE(Mutable):
    pass


class HitPoints(Mutable):

    def use(self, amount):
        pass

    def reclaim(self, amount):
        pass


class StructuralDamageCapacity(Mutable):

    def use(self, amount):
        pass

    def reclaim(self, amount):
        pass


class MegaDamageCapacity(Mutable):

    def use(self, amount):
        pass

    def reclaim(self, amount):
        pass





