from intelligine.simulation.object.pheromone.PheromoneGland import PheromoneGland


class MovementPheromoneGland(PheromoneGland):


    def get_movement_molecules(self):
        """
        :return: pheromone_type, distance_from_objective
        """
        return self._pheromone_type, self._host.get_brain().get_distance_from_objective()