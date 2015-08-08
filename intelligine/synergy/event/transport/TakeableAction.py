from intelligine.synergy.event.move.MoveAction import MoveAction
from synergine.core.Core import Core
from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from intelligine.cst import CANT_PUT_STILL, BRAIN_PART_TAKE
from synergine.synergy.event.exception.ActionAborted import ActionAborted


class TakeableAction(Action):

    _listen = TakeableEvent
    _depend = [MoveAction]

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def run(self, obj, context, synergy_manager):
        obj_id_transportable = self._parameters[TakeableEvent.PARAM_TAKE]
        obj_transportable = synergy_manager.get_map().get_object(obj_id_transportable)

        if not obj_transportable.is_takable():
            raise ActionAborted()

        obj_carried = obj_transportable.get_what_carry()
        obj_carried.set_carried_by(obj)
        obj.carry(obj_carried)
        cant_put_still = Core.get_configuration_manager().get('ant.take.cant_put_still')
        context.metas.value.set(CANT_PUT_STILL, obj.get_id(), cant_put_still)
        obj.get_brain().get_part(BRAIN_PART_TAKE).done(obj_carried)
