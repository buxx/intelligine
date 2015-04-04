from intelligine.cst import PHEROMON_DIRECTION
from intelligine.simulation.object.pheromone.PheromoneGland import PheromoneGland
from intelligine.simulation.pheromone.Pheromone import Pheromone


class MovementPheromoneGland(PheromoneGland):

    def get_pheromone(self):
        """
        :return: pheromone_type, distance_from_objective
        """
        return Pheromone(PHEROMON_DIRECTION, self._pheromone_type, self._host.get_brain().get_distance_from_objective(), 1)