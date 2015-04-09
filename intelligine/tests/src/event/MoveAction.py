from intelligine.synergy.event.move.MoveAction import MoveAction as BaseMoveAction
from intelligine.tests.src.event.MoveEvent import MoveEvent


class MoveAction(BaseMoveAction):

    @classmethod
    def set_move_event(cls, force_direction_function, event=MoveEvent):
        event.force_direction = force_direction_function
        cls._listen = event