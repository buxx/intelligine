from intelligine.simulation.object.brain.part.take.TakeBrainPart import TakeBrainPart
from intelligine.synergy.object.ressource.Ressource import Resource
from intelligine.cst import MOVE_MODE_EXPLO, MOVE_MODE, TYPE_RESOURCE_TRANSFORMABLE, \
    TYPE, MOVE_MODE_GOHOME, PHEROMON_DIR_EXPLO


class AntTakeBrainPart(TakeBrainPart):

    # TODO: methode __nit_ pour la classe ?
    _take = {
        MOVE_MODE_EXPLO: [TYPE_RESOURCE_TRANSFORMABLE],
    }

    @classmethod
    def can_take(cls, context, object_id, object_to_take_id):
        if not cls._object_is_takable_type(context, object_id, object_to_take_id):
            return False
        return True

    @classmethod
    def _object_is_takable_type(cls, context, object_id, object_to_take_id):
        move_mode = context.metas.value.get(MOVE_MODE, object_id)
        for takable_type in cls._take[move_mode]:
            if context.metas.list.have(TYPE, takable_type, object_to_take_id, allow_empty=True):
                return True
        return False

    def done(self, obj, take_object, context):
        # TODO: Ranger ca ? Truc plus dynamique/configurable ?
        if isinstance(take_object, Resource):
            obj.get_brain().switch_to_mode(MOVE_MODE_GOHOME)
            # TODO: set_last_pheromone_point ca devrait pas etre dans get_movement_pheromone_gland().appose() ?
            obj.set_last_pheromone_point(PHEROMON_DIR_EXPLO, obj.get_position())
            obj.get_movement_pheromone_gland().appose()