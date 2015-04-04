from intelligine.core.exceptions import BestPheromoneHere, NoPheromone
from intelligine.cst import PHEROMON_INFOS
from intelligine.simulation.pheromone.PheromoneFlavour import PheromoneFlavour
from intelligine.simulation.pheromone.Pheromone import Pheromone


class PheromonesManager():

    def __init__(self, context):
        self._context = context

    def get_flavour(self, position):
        point_pheromones = self._context.metas.value.get(PHEROMON_INFOS,
                                                         position,
                                                         allow_empty=True,
                                                         empty_value={})
        return PheromoneFlavour.new_from_raw_data(point_pheromones)

    def set_flavour(self, position, flavour):
        self._context.metas.value.set(PHEROMON_INFOS, position, flavour.get_raw_data())

    def get_pheromone(self, position, category, type, allow_empty=False):
        flavour = self.get_flavour(position)
        try:
            return flavour.get_pheromone(category, type)
        except NoPheromone:
            if allow_empty:
                return Pheromone()
            raise

    def increment_with_pheromone(self, position, apposed_pheromone):
        flavour = self.get_flavour(position)
        try:
            position_pheromone = flavour.get_pheromone(apposed_pheromone.get_category(), apposed_pheromone.get_type())
        except NoPheromone:
            position_pheromone = Pheromone(apposed_pheromone.get_category(),
                                           apposed_pheromone.get_type(),
                                           distance=apposed_pheromone.get_distance())

        position_pheromone.increment_intensity(apposed_pheromone.get_intensity())

        if apposed_pheromone.get_distance() < position_pheromone.get_distance():
            position_pheromone.set_distance(apposed_pheromone.get_distance())

        flavour.set_pheromone(position_pheromone)
        self.set_flavour(position, flavour)

        if apposed_pheromone.get_distance() > position_pheromone.get_distance():
            raise BestPheromoneHere(position_pheromone.get_distance())