from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.synergy.Simulation import Simulation
from intelligine.cst import TRANSPORTER, ALIVE, CARRYING, CANT_PUT_STILL


class PutableEvent(TakeableEvent):

    def concern(self, object_id, context):
        return context.metas.list.have(Simulation.STATE, object_id, TRANSPORTER) and \
               context.metas.list.have(Simulation.STATE, object_id, ALIVE) and \
               context.metas.list.have(Simulation.STATE, object_id, CARRYING) and \
               not context.metas.value.get(CANT_PUT_STILL, object_id, allow_empty=True)