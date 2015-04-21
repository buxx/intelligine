from synergine.synergy.event.Event import Event as BaseEvent
from intelligine.cst import BRAIN_SCHEMA


class Event(BaseEvent):

    @classmethod
    def _get_brain_part(cls, context, object_id, brain_part_name):
        object_brain_schema = context.metas.value.get(BRAIN_SCHEMA, object_id)
        return object_brain_schema[brain_part_name]