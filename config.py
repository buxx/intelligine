from intelligine.core.Context import Context
from intelligine.synergy.Simulation import Simulation
from intelligine.display.Pygame import Pygame
from intelligine.display.pygame.visualisation import visualisation as pygame_visualisation
from intelligine.sandbox.colored.colors_colonys import collections

"""
 TODO:
 * AttackAction :: comment choisir entre les actions ?
 * TakeAction, PutAction, Object Egg
 * --> frameworkiser les usage de states, metas etc ?
 * Plusieurs objets au mm endroit; Cinq oeuf => dessein de cinq oeuf; etc (image dynamique (param max_supperposer ?)
 * 3d
 * Optimisation display pygame: ne pas tout reafficher; opt google
"""

config = {
    'app': {
        'name': 'StigEngine',
        'classes': {
          'Context': Context
        }
    },
    'engine': {
        'fpsmax': 25,
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