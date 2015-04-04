from intelligine.core.exceptions import NoTypeInPheromone, NoCategoryInPheromone
from intelligine.simulation.pheromone.Pheromone import Pheromone


class PheromoneFlavour():

    def __init__(self, point_data):
        self._point_data = point_data

    def get_pheromone(self, category, type):
        types = self.get_types(category)
        if type not in types:
            raise NoTypeInPheromone()
        distance, intensity = types[type]
        return Pheromone(category, type, distance, intensity)

    def get_types(self, category):
        if category not in self._point_data:
            raise NoCategoryInPheromone()
        return self._point_data[category]

    def update_pheromone(self, pheromone):
        category = pheromone.get_category()
        type = pheromone.get_type()

        if category not in self._point_data:
            self._point_data[category] = {}

        self._point_data[category][type] = (pheromone.get_distance(), pheromone.get_intensity())

    def get_raw_data(self):
        return self._point_data