from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.PutableEvent import PutableEvent
from intelligine.cst import CANT_CARRY_STILL
from xyzworld.cst import POSITIONS
from synergine.synergy.event.exception.ActionAborted import ActionAborted


class PutableAction(Action):

    _listen = PutableEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def prepare(self, context):
        pass

    def run(self, obj, collection, context, synergy_manager):
        # TODO: DEV
        obj_id_transportable = self._parameters['objects_ids_transportable'][0]
        obj_transportable = synergy_manager.get_map().get_object(obj_id_transportable)
        # TODO: Cette logique de calcul cote process!
        position_to_put = self._get_position_to_put(context, obj, obj_transportable)
        # TODO: Doit etre du meme type que ce qui est transporte !
        obj_transported = obj.get_carried()
        obj_transported.set_carried_by(None)
        obj.put_carry(obj_transported, position_to_put)
        context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), 5)

    def _get_position_to_put(self, context, obj, obj_transportable):
        obj_transportable_pos = obj_transportable.get_position()
        if self._is_available_position(context, obj_transportable_pos):
            return obj_transportable_pos
        poss_arround_target = context.get_arround_points_of_point(obj_transportable_pos)
        poss_arround_obj = context.get_arround_points_of_point(obj.get_position())
        # For each position between target and current transporter
        for pos_arround_target in poss_arround_target:
            if pos_arround_target in poss_arround_obj:
                if self._is_available_position(context, pos_arround_target):
                    return pos_arround_target
        raise ActionAborted()

    def _is_available_position(self, context, position):
        # TODO: Pour le moment on ne regarde pas si ce sont tous des oeufs
        count_obj_here = len(context.metas.list.get(POSITIONS, position, allow_empty=True))
        if count_obj_here <= 5 and context.position_is_penetrable(position):
            return True
        return False