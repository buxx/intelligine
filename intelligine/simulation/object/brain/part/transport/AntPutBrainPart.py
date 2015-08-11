from synergine.core.Core import Core
from intelligine.core.exceptions import CantFindWhereToPut
from intelligine.cst import MODE_EXPLO, TYPE_RESOURCE_EXPLOITABLE, CARRIED, MODE_NURSE, TYPE_NURSERY, \
    MODE_HOME, TYPE_RESOURCE_EATABLE, MODE_GOHOME
from intelligine.simulation.object.brain.part.transport.TransportBrainPart import TransportBrainPart
from synergine_xyz.cst import POSITION, POSITIONS


class AntPutBrainPart(TransportBrainPart):

    _mode_matches = TransportBrainPart._mode_matches.copy()
    _mode_matches.update({
        MODE_NURSE: [TYPE_NURSERY],
        MODE_HOME: [TYPE_RESOURCE_EATABLE],
        MODE_GOHOME: []
    })

    _types_matches = {
        TYPE_RESOURCE_EXPLOITABLE: [TYPE_RESOURCE_EATABLE],
        TYPE_NURSERY: [TYPE_NURSERY]
    }

    @classmethod
    def can_put(cls, context, object_id, object_near_id):
        # Si l'objet à coté fait partie des objets concernés par le mode du porteur
        if cls._match_with_mode(context, object_id, object_near_id):
            # Et si les objet sont rangeable enssemble:
            object_carried_id = context.metas.value.get(CARRIED, object_id)
            return cls._objects_types_match(context, object_carried_id, object_near_id)
        return False

    @classmethod
    def get_put_position(cls, context, object_id, object_near_id):
        """
        Maybe part "found available position arround" should be in other class.
        :param context:
        :param object_id:
        :param object_near_id:
        :return:
        """
        obj_near_position = context.metas.value.get(POSITION, object_near_id)
        if cls._is_available_position(context, obj_near_position):
            return obj_near_position

        obj_transporter_position = context.metas.value.get(POSITION, object_id)
        obj_transporter_around_positions = context.get_around_points_of_point(obj_transporter_position)
        obj_near_around_positions = context.get_around_points_of_point(obj_near_position)

        # For each position between target and current transporter
        for pos_around_target in obj_near_around_positions:
            if pos_around_target in obj_transporter_around_positions:
                if cls._is_available_position(context, pos_around_target):
                    return pos_around_target
        raise CantFindWhereToPut()

    @staticmethod
    def _is_available_position(context, position):
        if not context.position_is_penetrable(position):
            return False

        count_obj_here = len(context.metas.list.get(POSITIONS, position, allow_empty=True))
        if count_obj_here <= Core.get_configuration_manager().get('ant.put.max_objects_at_same_position', 5):
            return True
        return False

    def done(self, puted_object):
        # TODO: lancer le choix d'un nouveau mode dans le brain.
        self._host.get_brain().switch_to_mode(MODE_EXPLO)
