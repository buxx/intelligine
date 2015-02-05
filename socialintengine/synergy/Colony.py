from synergine.synergy.collection.SynergyCollection import SynergyCollection
from socialintengine.synergy.event.move.MoveAction import MoveAction


class Colony(SynergyCollection):


    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MoveAction]