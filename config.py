from intelligine.core.Context import Context
from intelligine.display.Pygame import Pygame
import argparse

parser = argparse.ArgumentParser(description='Select sandbox.')
parser.add_argument('sandbox', metavar='sandbox', type=str, nargs=1,
                    help='Name of sandbox: ' + ', '.join(['exploration', 'all']))

args = parser.parse_args()

if 'all' in args.sandbox:
    from intelligine.sandbox.all.all import simulations, visualisation as pygame_visualisation
elif 'exploration' in args.sandbox:
    from intelligine.sandbox.exploration.exploration import simulations, visualisation as pygame_visualisation
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
            'cycles': -1,
            'seed': 42
        }
    },
    'simulations': simulations,
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
        },
        'put': {
            'max_objects_at_same_position': 5
        }
    }
}
