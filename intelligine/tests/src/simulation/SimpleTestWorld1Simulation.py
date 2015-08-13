from intelligine.display.map import get_map_connector
from intelligine.display.pygame.config import map_config
from synergine.test.TestSimulation import TestSimulation
from os import getcwd


class SimpleTestWorld1Simulation(TestSimulation):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        map_connector = get_map_connector(
            getcwd()+"/intelligine/tests/src/simulation/SimpleTestWorld1.tmx",
            map_config
        )
        self._simulations = map_connector.create_simulations()

    def _get_set_up_simulations(self):
        return self._simulations
