from synergine.synergy.collection.SynergyCollection import SynergyCollection
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.event.attack.NearAttackableAction import NearAttackableAction
from intelligine.synergy.event.transport.PutOutsideAction import PutOutsideAction
from intelligine.synergy.event.transport.TakeableAction import TakeableAction
from intelligine.synergy.event.transport.PutableAction import PutableAction
from intelligine.synergy.event.CycleAction import CycleAction


class Colony(SynergyCollection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self._actions = [MoveAction, NearAttackableAction, TakeableAction, PutableAction,
                         CycleAction, PutOutsideAction]
        self._start_position = configuration.get_start_position()

    def get_start_position(self):
        return self._start_position