from intelligine.core.Context import Context
from intelligine.synergy.Simulation import Simulation
from intelligine.display.Pygame import Pygame
from intelligine.display.pygame.visualisation import visualisation as pygame_visualisation
#from intelligine.sandbox.colored.colors_colonys import collections
# TODO: influencer avec argument python
from intelligine.sandbox.exploration.collections import collections

"""
 TODO:
 * AttackAction :: comment choisir entre les actions ?

 * pheromones:
   cf. doc papier
   + Pour le "pt de ressource": Poser un objet qui, lorsque on applique la position:
     L'objet doit pouvoir occuper plusieurs positions (gros objet)
     Il a donc * une position de reference
               * une liste de positions occupe
               * dans les metas cette liste de position contient la reference de l'objet
               *

"""

config = {
    'app': {
        'name': 'StigEngine',
        'classes': {
          'Context': Context
        }
    },
    'engine': {
        'fpsmax': 2555,
        'debug': {
            'mainprocess': True,
            'cycles': -1
        }
    },
    'simulations' : [Simulation(collections)],
    'connections': [Pygame],
    'terminal': {
      'pygame': {
            'visualisation': pygame_visualisation,
            'window_size': (800, 600),
            'app': {
                'name': 'SocialIntengine'
            },
            'display': {
                'grid': {
                    'size': 20
                }
            },
            'font': {
                'name': 'arial',
                'size': 13
            },
            'background': {
              'color': (125, 125, 125)
            }
        }
    }
}