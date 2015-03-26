class PheromoneGland():

    def __init__(self, host):
        self._pheromone_type = None
        self._host = host

    def set_pheromone_type(self, pheromone_type):
        self._pheromone_type = pheromone_type

    def get_pheromone_type(self):
        if self._pheromone_type is None:
            raise Exception("pheromone_type not specified")
        return self._pheromone_type