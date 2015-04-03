from intelligine.core.exceptions import BestPheromoneHere
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone

class PheromoneGland():

    def __init__(self, host, context):
        self._pheromone_type = None
        self._host = host
        self._context = context

    def set_pheromone_type(self, pheromone_type):
        self._pheromone_type = pheromone_type

    def get_pheromone_type(self):
        if self._pheromone_type is None:
            raise Exception("pheromone_type not specified")
        return self._pheromone_type

    def appose(self):
        try:
            DirectionPheromone.appose(self._context,
                                      self._host.get_position(),
                                      self._host.get_movement_pheromone_gland().get_movement_molecules())
        except BestPheromoneHere as best_pheromone_here:
            self._host.get_brain().set_distance_from_objective(best_pheromone_here.get_best_distance())