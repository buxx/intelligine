from synergine.synergy.collection.SynergyCollection import SynergyCollection
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.event.attack.NearAttackableAction import NearAttackableAction
from intelligine.synergy.event.transport.TakeableAction import TakeableAction


class Colony(SynergyCollection):


    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MoveAction, NearAttackableAction, TakeableAction]