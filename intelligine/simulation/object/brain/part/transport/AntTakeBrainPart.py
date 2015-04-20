from intelligine.simulation.object.brain.part.transport.TakeBrainPart import TakeBrainPart
from intelligine.synergy.object.ressource.Ressource import Resource
from intelligine.cst import MOVE_MODE_EXPLO, MOVE_MODE, TYPE_RESOURCE_TRANSFORMABLE, \
    TYPE, MOVE_MODE_GOHOME, PHEROMON_DIR_EXPLO, MOVE_MODE_NURSE, TYPE_NURSERY


class AntTakeBrainPart(TakeBrainPart):

    # TODO: methode __nit_ pour la classe ? vt mieux surcharger !
    _mode_matches = {
        MOVE_MODE_EXPLO: [TYPE_RESOURCE_TRANSFORMABLE],
        MOVE_MODE_NURSE: [TYPE_NURSERY]
    }

    @classmethod
    def can_take(cls, context, object_id, object_to_take_id):
        # Pour le moment si le type de l'objet fait partie des types admis pour le mode courant du porteur, c'est bon.
        return cls._match_with_mode(context, object_id, object_to_take_id)

    def done(self, obj, take_object, context):
        # TODO: Ranger ca ? Truc plus dynamique/configurable ?
        if isinstance(take_object, Resource):
            obj.get_brain().switch_to_mode(MOVE_MODE_GOHOME)
            # TODO: set_last_pheromone_point ca devrait pas etre dans get_movement_pheromone_gland().appose() ?
            obj.set_last_pheromone_point(PHEROMON_DIR_EXPLO, obj.get_position())
            obj.get_movement_pheromone_gland().appose()