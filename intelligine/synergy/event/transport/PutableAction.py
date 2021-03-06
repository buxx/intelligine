from synergine.synergy.event.exception.ActionAborted import ActionAborted
from intelligine.synergy.event.move.MoveAction import MoveAction
from intelligine.synergy.object.Food import Food
from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.PutableEvent import PutableEvent
from intelligine.cst import CANT_CARRY_STILL, BRAIN_PART_PUT


class PutableAction(Action):

    _listen = PutableEvent
    _depend = [MoveAction]

    def run(self, obj, context, synergy_manager):
        obj_transported = obj.get_carried()

        if not self._parameters[PutableEvent.PARAM_PUT_TO]:
            if self._parameters[PutableEvent.PARAM_HOME_FAIL]:
                obj.increment_put_fail_count()
            raise ActionAborted()

        for position_to_put in self._parameters[PutableEvent.PARAM_PUT_TO]:

            #  TODO: re controle de si posable ? La position a été calculé
            #  dans le process. Ce qui fait que la situation peut avoir changer.
            # Soit: Recalculer d'office BrainPut.cant_put_at.. Soit le recalculer que si le hash
            # de ce qu'il y a la a changer ?

            obj_transported.set_carried_by(None)
            obj.put_carry(obj_transported, position_to_put)
            context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), 5)
            obj.reinit_put_fail_count()

            obj.get_brain().get_part(BRAIN_PART_PUT).done(obj_transported)

            # TODO: DEV
            if isinstance(obj_transported, Food):
                #obj_transported.set_position((-1, 0, 0))
                obj_transported.transform_to_stocked()
