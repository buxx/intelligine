from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject


# TODO: ne doit plus exister. Il est la pour le display uniquement. (pheromones ne sont pas des entites)
class Pheromon(XyzSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._direction = None

    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction