from intelligine.synergy.event.move.MoveAction import MoveAction
from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.PutableEvent import PutableEvent
from intelligine.cst import CANT_CARRY_STILL, BRAIN_PART_PUT


class PutableAction(Action):

    _listen = PutableEvent
    _depend = [MoveAction]

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def run(self, obj, context, synergy_manager):
        position_to_put = self._parameters[PutableEvent.PARAM_PUT_TO]
        obj_transported = obj.get_carried()

        obj_transported.set_carried_by(None)
        #  TODO: re controle de si posable ? (5 max etc)
        obj.put_carry(obj_transported, position_to_put)
        context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), 5)

        obj.get_brain().get_part(BRAIN_PART_PUT).done(obj_transported)
