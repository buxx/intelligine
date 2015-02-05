from synergine.synergy.event.Event import Event
from xyzworld.mechanism.PositionedArroundMechanism import PositionedArroundMechanism


class MoveEvent(Event):

    def concern(self, object_id, context):
        return True

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = PositionedArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
      return True