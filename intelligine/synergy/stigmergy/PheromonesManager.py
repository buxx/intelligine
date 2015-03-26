from intelligine.core.exceptions import BestPheromoneHere
from intelligine.cst import PHEROMON_INFOS
from intelligine.core.exceptions import NoPheromone


class PheromonesManager():

    def __init__(self, context):
        self._context = context

    def get_pheromones(self, position, prepare=[]):
        point_pheromones = self._context.metas.value.get(PHEROMON_INFOS,
                                                         position,
                                                         allow_empty=True,
                                                         empty_value={})
        current_check = point_pheromones
        for prepare_key in prepare:
            if prepare_key not in current_check:
                current_check[prepare_key] = {}
            current_check = current_check[prepare_key]

        return point_pheromones

    def set_pheromones(self, position, pheromones):
        self._context.metas.value.set(PHEROMON_INFOS, position, pheromones)

    def get_info(self, position, address, allow_empty=False, empty_value=None):
        pheromones = self.get_pheromones(position, address[:-1])

        pheromone = pheromones
        for key in address[:-1]:
            pheromone = pheromone[key]

        if address[-1] not in pheromone:
            if allow_empty:
                pheromone[address[-1]] = empty_value
            else:
                raise KeyError()

        return pheromone[address[-1]]

    def increment(self, position, address, distance, increment_value=1):
        pheromones = self.get_pheromones(position, address[:-1])

        pheromone = pheromones
        for key in address[:-1]:
            pheromone = pheromone[key]

        if address[-1] not in pheromone:
            pheromone[address[-1]] = (distance, 0)
        # On se retrouve avec un {} dans pheromone[address[-1]]. A cause de la recherche de pheromone avant (et main process)
        if not pheromone[address[-1]]:
            pheromone[address[-1]] = (distance, 0)

        pheromone_distance = pheromone[address[-1]][0]
        pheromone_intensity = pheromone[address[-1]][1]

        pheromone_intensity += increment_value

        if distance < pheromone_distance:
            pheromone_distance = distance

        pheromone[address[-1]] = (pheromone_distance, pheromone_intensity)
        self.set_pheromones(position, pheromones)

        if distance > pheromone_distance:
            raise BestPheromoneHere(pheromone_distance)