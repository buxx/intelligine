from intelligine.cst import PHEROMON_INFOS


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
                raise IndexError()

        return pheromone[address[-1]]

    def increment(self, position, address, increment_value):
        pheromones = self.get_pheromones(position, address[:-1])

        pheromone = pheromones
        for key in address[:-1]:
            pheromone = pheromone[key]

        if address[-1] not in pheromone:
            pheromone[address[-1]] = 0
        pheromone[address[-1]] += increment_value
        self.set_pheromones(position, pheromones)