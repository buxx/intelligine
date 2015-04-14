from intelligine.core.exceptions import NearFound, NearNothingFound
from synergine.synergy.event.Event import Event
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism


class NearEvent(Event):

    _near_name = None
    _near_map = lambda self, near_object_id, context: False

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    # TODO: parameters en entre/sortie c pas bon ca
    def map(self, context, parameters, stop_at_first=False, filter=lambda near_object_id, context: True):
        for near_object_id in parameters['objects_ids_near']:
            if self._near_map(near_object_id, context) and filter(near_object_id, context):
                if self._near_name not in parameters:
                    parameters[self._near_name] = []
                parameters[self._near_name].append(near_object_id)
                if stop_at_first:
                    return
        raise NearNothingFound()