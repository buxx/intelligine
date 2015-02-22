from synergine.synergy.event.Event import Event
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.cst import TRANSPORTABLE, CANT_CARRY_STILL, COL_TRANSPORTER_NOT_CARRYING


class TakeableEvent(Event):

    concern = COL_TRANSPORTER_NOT_CARRYING

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        if context.metas.value.get(CANT_CARRY_STILL, object_id, allow_empty=True):
            return False
        # TODO: Nettoyer (refact possible sur ces objets ont tel states, comme dans concern)
        for obj_near_id in parameters['objects_ids_near']:
            if context.metas.states.have(obj_near_id, TRANSPORTABLE):
                if 'objects_ids_transportable' not in parameters:
                    parameters['objects_ids_transportable'] = []
                parameters['objects_ids_transportable'].append(obj_near_id)
        if 'objects_ids_transportable' not in parameters:
            return False
        return True