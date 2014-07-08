#!/usr/bin/env python

import webapp2

from character import Character
from character import errors

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Entry Point.')

if __name__ == "__main__":


    stats = {
        'iq': 21, 'me': 12, 'ma': 15, 'ps': 19, 'pp': 15, 'pe': 13, 'pb': 10,
        'spd': 8, 'ppe': 5
    }
    x = Character(**stats)
    print x
    try:
        x.potential_psychic_energy.use_ppe(1000)
        print "\n\n\n\nCurrent PPE: {}".format(x.potential_psychic_energy)
        x.potential_psychic_energy.reclaim_ppe(5)
        print "\n\n\n\nCurrent PPE: {}".format(x.potential_psychic_energy)
    except errors.CharacterNotPowerfulEnough:
        print (
            "Character isn't powerful enough, you only have "
            "maximum of {} PPE.".format(x.potential_psychic_energy.max)
        )

