from synergine.synergy.event.Action import Action
from intelligine.synergy.event.CycleEvent import CycleEvent
from intelligine.cst import CANT_CARRY_STILL, CANT_PUT_STILL


class CycleAction(Action):

    _listen = CycleEvent

    def run(self, obj, context, synergy_manager):
        cant_carry_still = context.metas.value.get(CANT_CARRY_STILL, obj.get_id(), allow_empty=True, empty_value=0)
        if cant_carry_still > 0:
            context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), cant_carry_still-1)

        cant_put_still = context.metas.value.get(CANT_PUT_STILL, obj.get_id(), allow_empty=True, empty_value=0)
        if cant_put_still > 0:
            context.metas.value.set(CANT_PUT_STILL, obj.get_id(), cant_put_still-1)
