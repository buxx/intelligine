from synergine.synergy.event.Event import Event
from xyzworld.mechanism.ArroundMechanism import ArroundMechanism
from synergine.synergy.Simulation import Simulation
from intelligine.cst import ATTACKER, ATTACKABLE, COLONY, ALIVE


class NearAttackableEvent(Event):

    def concern(self, object_id, context):
        return context.metas.list.have(Simulation.STATE, object_id, ATTACKER) and \
               context.metas.list.have(Simulation.STATE, object_id, ALIVE)

    def __init__(self, actions):
        super().__init__(actions)
        self._mechanism = ArroundMechanism

    def _object_match(self, object_id, context, parameters={}):
        # TODO: nettoyer
        obj_colony_id = context.metas.value.get(COLONY, object_id)
        for obj_near_id in parameters['objects_ids_near']:
            if context.metas.list.have(Simulation.STATE, obj_near_id, ATTACKABLE):
                if obj_colony_id != context.metas.value.get(COLONY, obj_near_id):
                    if 'objects_ids_attackable' not in parameters:
                        parameters['objects_ids_attackable'] = []
                    parameters['objects_ids_attackable'].append(obj_near_id)
        if 'objects_ids_attackable' not in parameters:
            return False
        return True
