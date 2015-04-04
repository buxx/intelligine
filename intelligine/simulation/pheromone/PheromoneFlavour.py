from intelligine.core.exceptions import NoTypeInPheromone, NoCategoryInPheromone
from intelligine.simulation.pheromone.Pheromone import Pheromone


class PheromoneFlavour():

    @classmethod
    def new_from_raw_data(cls, raw_data):
        flavour = {}
        for category in raw_data:
            pheromones_by_category = raw_data[category]
            for type in pheromones_by_category:
                distance, intensity = pheromones_by_category[type]
                if category not in flavour:
                    flavour[category] = {}
                flavour[category][type] = Pheromone(category, type, distance, intensity)
        return cls(flavour)

    def get_raw_data(self):
        raw_data = {}
        for category in self._flavour:
            pheromones_by_category = self._flavour[category]
            for type in pheromones_by_category:
                pheromone = pheromones_by_category[type]
                if category not in raw_data:
                    raw_data[category] = {}
                raw_data[category][type] = (pheromone.get_distance(), pheromone.get_intensity())
        return raw_data

    def __init__(self, flavour):
        self._flavour = flavour

    def get_pheromone(self, category, type):
        types = self.get_types(category)
        if type not in types:
            raise NoTypeInPheromone()
        return types[type]

    def get_types(self, category):
        if category not in self._flavour:
            raise NoCategoryInPheromone()
        return self._flavour[category]

    def set_pheromone(self, pheromone):
        category = pheromone.get_category()
        type = pheromone.get_type()

        if category not in self._flavour:
            self._flavour[category] = {}

        self._flavour[category][type] = pheromone