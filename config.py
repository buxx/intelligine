from xyzworld.Context import Context as XyzContext
from socialintengine.synergy.Simulation import Simulation
from socialintengine.synergy.Colony import Colony
from socialintengine.synergy.ColonyConfiguration import ColonyConfiguration
from socialintengine.synergy.Rocks import Rocks
from socialintengine.synergy.RocksConfiguration import RocksConfiguration
from socialintengine.display.Pygame import Pygame
from socialintengine.display.pygame.visualisation import visualisation as pygame_visualisation


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
            'mainprocess': False,
            'cycles': -1
        }
    },
    'simulations' : [Simulation([Colony(ColonyConfiguration()), Rocks(RocksConfiguration())])],
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