from synergine.synergy.event.Action import Action
from intelligine.synergy.event.attack.NearAttackableEvent import NearAttackableEvent
from random import randint
from intelligine.synergy.Simulation import Simulation
from intelligine.cst import ALIVE, ATTACKABLE


class NearAttackableAction(Action):

    _listen = NearAttackableEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def prepare(self, context):
        pass

    def run(self, obj, collection, context, synergy_manager):
        # TODO: TEST
        for obj_id_attackable in self._parameters['objects_ids_attackable']:
            obj_attackable = synergy_manager.get_map().get_object(obj_id_attackable)
            obj_attackable.hurted(randint(0, 2))
            if obj_attackable.get_life_points() <= 0:
                try:
                    context.metas.list.remove(Simulation.STATE, obj_id_attackable, ALIVE)
                    context.metas.list.remove(Simulation.STATE, obj_id_attackable, ATTACKABLE)
                except ValueError:  # Ant maybed killed by other ant at same turn
                    pass
