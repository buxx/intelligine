from synergine.synergy.event.Action import Action
from intelligine.synergy.event.attack.NearAttackableEvent import NearAttackableEvent
from random import randint


class NearAttackableAction(Action):

    _listen = NearAttackableEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def prepare(self, context):
        pass

    def run(self, obj, context, synergy_manager):
        # TODO: reprendre ?
        for obj_id_attackable in self._parameters['objects_ids_attackable']:
            obj_attackable = synergy_manager.get_map().get_object(obj_id_attackable)
            obj_attackable.hurted(randint(0, 2))
