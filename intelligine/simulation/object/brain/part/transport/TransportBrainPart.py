from intelligine.cst import MOVE_MODE, TYPE
from intelligine.simulation.object.brain.part.BrainPart import BrainPart


class TransportBrainPart(BrainPart):

    _mode_matches = {}
    _types_matches = {}

    @classmethod
    def _match_with_mode(cls, context, object_id, concerned_object_id):
        move_mode = context.metas.value.get(MOVE_MODE, object_id)
        for takable_type in cls._mode_matches[move_mode]:
            if context.metas.list.have(TYPE, concerned_object_id, takable_type, allow_empty=True):
                return True
        return False

    @classmethod
    def _objects_types_match(cls, context, object_a_id, object_b_id):
        """

        Retourne vrai si un des type de l'objet b se trouve dans la lise de type définis dans _types_matches pour
        l'un des types de l'objet a.

        :param context:
        :param object_a_id:
        :param object_b_id:
        :return: bool
        """
        object_a_types = context.metas.list.get(TYPE, object_a_id)
        object_b_types = context.metas.list.get(TYPE, object_b_id)

        for object_a_type in object_a_types:
            if object_a_type in cls._types_matches:
                wanted_types = cls._types_matches[object_a_type]
                for object_b_type in object_b_types:
                    if object_b_type in wanted_types:
                        return True

        return False
