from synergine.synergy.Simulation import Simulation as BaseSimulation
from xyzworld.cst import POSITION, POSITIONS
#from intelligine.synergy.event.attack.NearAttackableAction import NearAttackableAction
from intelligine.synergy.event.transport.PutableAction import PutableAction
from intelligine.synergy.event.transport.TakeableAction import TakeableAction
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.event.CycleAction import CycleAction
from intelligine.cst import COL_TRANSPORTER_CARRYING, COL_TRANSPORTER_NOT_CARRYING, \
    COL_WALKER, ACTION_DIE, COL_ALIVE, ALIVE, ATTACKABLE

# TODO: Mettre ailleurs ?
def bug_die(bug, context):
    context.metas.collections.remove_list(bug.get_id(),
                                          [COL_TRANSPORTER_CARRYING, \
                                           COL_TRANSPORTER_NOT_CARRYING, \
                                           COL_WALKER, \
                                           COL_ALIVE],
                                          allow_not_in=True)
    context.metas.states.remove_list(bug.get_id(), [ALIVE, ATTACKABLE], allow_not_in=True)

class Simulation(BaseSimulation):

    def connect_actions_signals(self, Signals):
        Signals.signal(PutableAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING))
        Signals.signal(TakeableAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_TRANSPORTER_CARRYING, COL_TRANSPORTER_NOT_CARRYING))
        Signals.signal(ACTION_DIE).connect(lambda obj, context: bug_die(obj, context))

    def end_cycle(self, context):
        if context.get_cycle() % 100 is 0:
            context.metas.list.clean(POSITIONS)
