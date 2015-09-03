from intelligine.cst import CANT_CARRY_STILL, BRAIN_PART_PUT, COL_PUT_OUTSIDE, MODE_EXPLO
from intelligine.synergy.event.transport.PutOutsideEvent import PutOutsideEvent
from intelligine.synergy.event.transport.PutableAction import PutableAction


class PutOutsideAction(PutableAction):
    _listen = PutOutsideEvent

    def run(self, obj, context, synergy_manager):
        # TODO: Refact avec pare,t
        obj_transported = obj.get_carried()
        obj_transported.set_carried_by(None)
        obj.put_carry(obj_transported, self._parameters['position_to_put'])
        context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), 5)
        obj.reinit_put_fail_count()

        #  obj.get_brain().get_part(BRAIN_PART_PUT).done(obj_transported)
        obj._remove_col(COL_PUT_OUTSIDE)
        obj.get_brain().switch_to_mode(MODE_EXPLO)  # TODO: dans le brain.done
