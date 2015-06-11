from synergine.synergy.Simulation import Simulation as BaseSimulation
from synergine_xyz.cst import POSITIONS
from intelligine.synergy.event.transport.PutableAction import PutableAction
from intelligine.synergy.event.transport.TakeableAction import TakeableAction
from intelligine.cst import COL_TRANSPORTER_CARRYING, COL_TRANSPORTER_NOT_CARRYING


class Simulation(BaseSimulation):

    def connect_actions_signals(self, Signals):
        Signals.signal(PutableAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_TRANSPORTER_NOT_CARRYING, COL_TRANSPORTER_CARRYING))
        Signals.signal(TakeableAction).connect(lambda obj, context: \
            context.metas.collections.add_remove(obj.get_id(), COL_TRANSPORTER_CARRYING, COL_TRANSPORTER_NOT_CARRYING))

    def end_cycle(self, context):
        if context.get_cycle() % 100 is 0:
            context.metas.list.clean(POSITIONS)
