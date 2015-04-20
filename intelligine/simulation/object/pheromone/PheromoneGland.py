from intelligine.core.exceptions import BestPheromoneHere, PheromoneGlandDisabled
from intelligine.simulation.pheromone.DirectionPheromone import DirectionPheromone

class PheromoneGland():

    def __init__(self, host, context):
        self._pheromone_type = None
        self._host = host
        self._context = context
        self._enabled = False

    def set_pheromone_type(self, pheromone_type):
        self._pheromone_type = pheromone_type

    def get_pheromone_type(self):
        if self._pheromone_type is None:
            raise Exception("pheromone_type not specified")
        return self._pheromone_type

    def get_pheromone(self):
        raise NotImplementedError()

    def appose(self):
        if not self._enabled:
            raise PheromoneGlandDisabled()

        try:
            DirectionPheromone.appose(self._context,
                                      self._host.get_position(),
                                      self.get_pheromone())
        except BestPheromoneHere as best_pheromone_here:
            self._host.get_brain().set_distance_from_objective(best_pheromone_here.get_best_distance())

    def disable(self):
        self._enabled = False

    def enable(self):
        self._enabled = True

    def is_enabled(self):
        return self._enabled