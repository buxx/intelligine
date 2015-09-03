from intelligine.core.exceptions import NearNothingFound, CantFindWhereToPut
from intelligine.shorcut.brain import get_brain_part
from intelligine.synergy.event.src.NearEvent import NearEvent
from synergine.core.exceptions import NotConcernedEvent
from intelligine.cst import CANT_PUT_STILL, COL_TRANSPORTER_CARRYING, TRANSPORTABLE, BRAIN_SCHEMA, BRAIN_PART_PUT
from synergine_xyz.mechanism.AroundMechanism import AroundMechanism


class PutableEvent(NearEvent):
    """
    TODO: Refactorise with TakableEvent
    """

    PARAM_PUT = 'put'
    PARAM_PUT_TO = 'put_to'
    PARAM_HOME_FAIL = 'home_fail'
    _mechanism = AroundMechanism
    _concern = COL_TRANSPORTER_CARRYING
    _near_name = 'objects_ids_putable'
    _near_map = lambda self, near_object_id, context: context.metas.states.have(near_object_id, TRANSPORTABLE)

    def _prepare(self, object_id, context, parameters={}):
        if not self._can_put(object_id, context):
            raise NotConcernedEvent()

        try:
            self.map(context, parameters, stop_at_first=False)
        except NearNothingFound:
            raise NotConcernedEvent()

        brain_part = get_brain_part(context, object_id, BRAIN_PART_PUT)
        parameters[self.PARAM_PUT] = []
        parameters[self.PARAM_PUT_TO] = []

        for object_near_id in parameters[self._near_name]:
            if brain_part.can_put(context, object_id, object_near_id):
                try:
                    put_position = brain_part.get_put_position(context, object_id, object_near_id)
                    parameters[self.PARAM_PUT].append(object_near_id)
                    parameters[self.PARAM_PUT_TO].append(put_position)
                    parameters[self.PARAM_HOME_FAIL] = False
                    return parameters  # Si a terme on veut tous les calculer a l'avance, ne pas retourner ici
                except CantFindWhereToPut:
                    pass  # On continu la booucle

        # Si a terme on veut tous les calculer a l'avance, raise que si rien trouve
        parameters[self.PARAM_HOME_FAIL] = True
        return parameters

    @staticmethod
    def _can_put(object_id, context):
        return not context.metas.value.get(CANT_PUT_STILL, object_id, allow_empty=True)

    @classmethod
    def _object_can_put(cls, object_id, context, object_to_put_id):
        object_take_brain_part = get_brain_part(context, object_id, BRAIN_PART_PUT)
        return object_take_brain_part.can_put(context, object_id, object_to_put_id)
