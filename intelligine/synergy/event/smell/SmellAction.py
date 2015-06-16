from intelligine.cst import POINT_SMELL, POINTS_SMELL
from intelligine.synergy.event.smell.SmellEvent import SmellEvent
from synergine.synergy.event.Action import Action


class SmellAction(Action):

    _listen = SmellEvent

    @classmethod
    def cycle_pre_run(cls, context, synergy_manager):
        smell_positions = context.metas.list.get(POINTS_SMELL, POINTS_SMELL, allow_empty=True)
        for smell_position in smell_positions:
            context.metas.value.unset(POINT_SMELL, smell_position)
        context.metas.list.unset(POINTS_SMELL, POINTS_SMELL, allow_empty=True)

    def run(self, obj, context, synergy_manager):

        points_distances = self._parameters['points_distances']
        smell_type = obj.get_smell()

        for smell_point in points_distances:

            where_to_put_smells = context.metas.value.get(POINT_SMELL, smell_point, allow_empty=True, empty_value={})
            current_point_smell = points_distances[smell_point]

            if smell_type not in where_to_put_smells:
                where_to_put_smells[smell_type] = current_point_smell
            else:
                where_to_put_smell = where_to_put_smells[smell_type]
                if current_point_smell < where_to_put_smell:
                    where_to_put_smells[smell_type] = where_to_put_smell

            context.metas.value.set(POINT_SMELL, smell_point, where_to_put_smells)
            context.metas.list.add(POINTS_SMELL, POINTS_SMELL, smell_point, assert_not_in=False)
