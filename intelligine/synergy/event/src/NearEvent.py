from intelligine.core.exceptions import NearNothingFound
from intelligine.synergy.event.Event import Event
from synergine_xyz.mechanism.AroundMechanism import AroundMechanism


class NearEvent(Event):

    _mechanism = AroundMechanism
    _near_name = None
    _near_map = lambda self, near_object_id, context: False

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