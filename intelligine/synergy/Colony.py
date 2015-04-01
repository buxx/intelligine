from synergine.synergy.collection.SynergyCollection import SynergyCollection
from intelligine.synergy.event.move.PheromoneMoveAction import PheromoneMoveAction
from intelligine.synergy.event.attack.NearAttackableAction import NearAttackableAction
from intelligine.synergy.event.transport.TakeableAction import TakeableAction
from intelligine.synergy.event.transport.PutableAction import PutableAction
from intelligine.synergy.event.CycleAction import CycleAction


class Colony(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [PheromoneMoveAction, NearAttackableAction, TakeableAction, PutableAction,
                         CycleAction]
        self._start_position = configuration.get_start_position()

    def get_start_position(self):
        return self._start_position