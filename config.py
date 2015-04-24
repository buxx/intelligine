from intelligine.core.Context import Context
from intelligine.synergy.Simulation import Simulation
from intelligine.display.Pygame import Pygame
from intelligine.display.pygame.visualisation import visualisation as pygame_visualisation
import argparse

parser = argparse.ArgumentParser(description='Select sandbox.')
parser.add_argument('sandbox', metavar='sandbox', type=str, nargs=1,
                    help='Name of sandbox: ' + ', '.join(['exploration', 'multi']))

args = parser.parse_args()

if 'multi' in args.sandbox:
    from intelligine.sandbox.colored.colors_colonys import collections
elif 'exploration' in args.sandbox:
    from intelligine.sandbox.exploration.collections import collections
else:
    parser.parse_args(['-h'])

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
    },
    'ant': {
        'take': {
            'cant_put_still': 5
        }
    }
}