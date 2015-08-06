from synergine.test.TestSimulation import TestSimulation
from os import getcwd
from intelligine.display.pygame.visualisation import get_standard_extract_from_map, map_config


class SimpleTestWorld1Simulation(TestSimulation):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        simulations, visualisation = get_standard_extract_from_map(
            getcwd()+"/intelligine/tests/src/simulation/SimpleTestWorld1.tmx",
            map_config
        )
        self._simulations = simulations

    def _get_set_up_simulations(self):
        return self._simulations
