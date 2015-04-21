from intelligine.cst import MOVE_MODE, TYPE
from intelligine.simulation.object.brain.part.BrainPart import BrainPart


class TransportBrainPart(BrainPart):

    _mode_matches = {}

    @classmethod
    def _match_with_mode(cls, context, object_id, concerned_object_id):
        move_mode = context.metas.value.get(MOVE_MODE, object_id)
        for takable_type in cls._mode_matches[move_mode]:
            if context.metas.list.have(TYPE, concerned_object_id, takable_type, allow_empty=True):
                return True
        return False

    @classmethod
    def _objects_have_same_type(cls, context, object_carried_id, object_to_put_id):
        object_carried_types = context.metas.list.get(TYPE, object_carried_id)
        for object_carried_type in object_carried_types:
            if context.metas.list.have(TYPE, object_to_put_id, object_carried_type):
                return True
        return False