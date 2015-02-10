from xyzworld.Context import Context as XyzContext
from intelligine.synergy.Simulation import Simulation
from intelligine.display.Pygame import Pygame
from intelligine.display.pygame.visualisation import visualisation as pygame_visualisation
from intelligine.sandbox.redblue.red_blue_colonys import collections

config = {
    'app': {
        'name': 'StigEngine',
        'classes': {
          'Context': XyzContext
        }
    },
    'engine': {
        'fpsmax': 5,
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