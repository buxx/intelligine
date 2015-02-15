from synergine.synergy.event.Event import Event
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.synergy.Simulation import Simulation
from intelligine.cst import TRANSPORTABLE, TRANSPORTER, ALIVE, CARRYING, CANT_CARRY_STILL


class TakeableEvent(Event):

    def concern(self, object_id, context):
        return context.metas.list.have(Simulation.STATE, object_id, TRANSPORTER) and \
               context.metas.list.have(Simulation.STATE, object_id, ALIVE) and \
               not context.metas.list.have(Simulation.STATE, object_id, CARRYING) and \
               not context.metas.value.get(CANT_CARRY_STILL, object_id, allow_empty=True)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        # TODO: Nettoyer (refact possible sur ces objets ont tel states, comme dans concern)
        for obj_near_id in parameters['objects_ids_near']:
            if context.metas.list.have(Simulation.STATE, obj_near_id, TRANSPORTABLE):
                if 'objects_ids_transportable' not in parameters:
                    parameters['objects_ids_transportable'] = []
                parameters['objects_ids_transportable'].append(obj_near_id)
        if 'objects_ids_transportable' not in parameters:
            return False
        return True