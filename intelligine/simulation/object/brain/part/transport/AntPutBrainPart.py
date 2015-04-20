from intelligine.core.exceptions import CantFindWhereToPut
from intelligine.cst import MOVE_MODE_EXPLO, TYPE_RESOURCE_TRANSFORMABLE, CARRIED
from intelligine.simulation.object.brain.part.transport.TransportBrainPart import TransportBrainPart
from intelligine.synergy.object.Food import Food
from xyzworld.cst import POSITION, POSITIONS


class AntPutBrainPart(TransportBrainPart):

    # TODO: methode __nit_ pour la classe ?
    _mode_matches = {
        MOVE_MODE_EXPLO: [TYPE_RESOURCE_TRANSFORMABLE],
    }

    @classmethod
    def can_put(cls, context, object_id, object_near_id):
        object_carried_id = context.metas.value.get(CARRIED, object_id)
        #  Pour le moment on considere qu'un objet peut-etre depose a cote d'un objet qui a un type identique
        return cls._objects_have_same_type(context, object_carried_id, object_near_id)

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
        # TODO: Pour le moment on ne regarde pas si ce sont tous des obj identique
        count_obj_here = len(context.metas.list.get(POSITIONS, position, allow_empty=True))
        # TODO: 5 est hardcode; de plus cette cntrainte (not brain) devrait dependre de l'objet, du contexte ...
        if count_obj_here <= 5 and (context.position_is_penetrable(position) or position == (0, 0, 0)):  # TODO TEST !!!
            return True
        return False

    def done(self, obj, puted_object, context):
        # TODO: Il faut refact/logique qqpart pour ca !! Genre Brain.done(PUT, ??)
        if isinstance(puted_object, Food):
            obj.get_brain().switch_to_mode(MOVE_MODE_EXPLO)
            # TODO: TEST Depose au -1 pour des raisons de test. Plus tard ce sera des tas comme un autre !
            puted_object.set_position((-1, 0, 0))

