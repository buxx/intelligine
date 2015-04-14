from intelligine.core.exceptions import NearNothingFound
from synergine.core.exceptions import NotConcernedEvent
from intelligine.synergy.event.src.NearEvent import NearEvent
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from intelligine.cst import ATTACKABLE, COLONY, COL_FIGHTER


class NearAttackableEvent(NearEvent):

    concern = COL_FIGHTER
    _near_name = 'objects_ids_attackable'
    _near_map = lambda self, near_object_id, context: context.metas.states.have(near_object_id, ATTACKABLE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _prepare(self, object_id, context, parameters={}):
        obj_colony_id = context.metas.value.get(COLONY, object_id)
        filter = lambda near_object_id, context: obj_colony_id != context.metas.value.get(COLONY, near_object_id)

        try:
            self.map(context, parameters, stop_at_first=True, filter=filter)
        except NearNothingFound:
            raise NotConcernedEvent()

        return parameters
