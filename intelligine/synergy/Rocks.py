from intelligine.synergy.event.smell.SmellAction import SmellAction
from synergine.synergy.collection.SynergyCollection import SynergyCollection


class Rocks(SynergyCollection):
    """
    TODO: Rename in Environment
    """

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [SmellAction]
