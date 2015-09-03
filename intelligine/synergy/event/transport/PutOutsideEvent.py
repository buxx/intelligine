from synergine.core.exceptions import NotConcernedEvent
from synergine_xyz.cst import POSITION
from intelligine.cst import COL_PUT_OUTSIDE
from intelligine.simulation.object.brain.part.move.AntMoveBrainPart import AntMoveBrainPart
from intelligine.simulation.object.brain.part.transport.AntPutBrainPart import AntPutBrainPart
from intelligine.synergy.event.Event import Event


# TODO: NearEvent ?
class PutOutsideEvent(Event):

    _concern = COL_PUT_OUTSIDE

    def _prepare(self, object_id, context, parameters={}):
        # TODO: DEV code ailleurs (._)
        if AntMoveBrainPart._on_home_smell(context, object_id):
            raise NotConcernedEvent()

        current_position = context.metas.value.get(POSITION, object_id)
        around_positions = context.get_around_points_of(current_position)

        for around_position in around_positions:
            # TODO DEV: ... ._
            if AntPutBrainPart._position_have_free_space_around(context, around_position):
                if AntPutBrainPart._position_is_enought_place(context, around_position):
                    # TODO: Constant ?
                    parameters['position_to_put'] = around_position
                    return parameters

        raise NotConcernedEvent()
