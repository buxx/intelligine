from intelligine.synergy.event.move.MoveAction import MoveAction
from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from intelligine.cst import CANT_PUT_STILL, BRAIN_SCHEMA, BRAIN_PART_TAKE
from synergine.synergy.event.exception.ActionAborted import ActionAborted


class TakeableAction(Action):
    """
    TODO: Prendre le premier prenable, interrompre la recherche si trouve
          si au run de l'action objet non prenable, tant pis. ActionAborted.
    """
    _listen = TakeableEvent
    _depend = [MoveAction]

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def prepare(self, context):
        # TODO: C l'event qui doit preparer les donnees
        pass

    def run(self, obj, context, synergy_manager):
        obj_id_transportable = self._parameters[TakeableEvent.PARAM_TAKE]
        obj_transportable = synergy_manager.get_map().get_object(obj_id_transportable)
        if obj_transportable.is_carried():  # TODO: is_takable
            raise ActionAborted()
        try:
            obj_carried = obj_transportable.get_what_carry()
            obj_carried.set_carried_by(obj)
            obj.carry(obj_carried)
            context.metas.value.set(CANT_PUT_STILL, obj.get_id(), 5)
            obj.get_brain().get_part(BRAIN_PART_TAKE).done(obj, obj_carried, context)
        except ValueError: # Une NotCarriableError serais pus approprie
            # TODO: tmp? Si on as pas pu le porter c'est qu'il vient d'etre porte par une autre.
            pass
