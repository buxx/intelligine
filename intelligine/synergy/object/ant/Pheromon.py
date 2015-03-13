from xyzworld.SynergyObject import SynergyObject as XyzSynergyObject


class Pheromon(XyzSynergyObject):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        self._direction = None

    # TODO: direction ailleurs non ?
    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction