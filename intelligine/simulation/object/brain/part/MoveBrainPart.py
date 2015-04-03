from intelligine.simulation.object.brain.part.BrainPart import BrainPart
from intelligine.synergy.event.move.direction import directions_same_level, directions_slighty
from random import randint, choice, randrange
from intelligine.cst import BLOCKED_SINCE, PREVIOUS_DIRECTION


class MoveBrainPart(BrainPart):

    @classmethod
    def get_direction(cls, context, object_id):
        return cls._get_random_direction(context, object_id)

    @classmethod
    def _get_random_direction(cls, context, object_id):
        try:
            blocked_since = context.metas.value.get(BLOCKED_SINCE, object_id)
        except KeyError:
            blocked_since = 0
        direction_name = None
        if blocked_since <= 3:  #TODO: config
            try:
                previous_direction = context.metas.value.get(PREVIOUS_DIRECTION, object_id)
                # TODO: Faut mettre ca en plus propre (proba d'aller tou droit, config, etc)
                if randrange(100) < 75:  # 75% de change d'aller tout droit
                    # Dans le futur: les fourmis vont moins tout droit quand elle se croient et se touche
                    return previous_direction

                directions_list = directions_slighty[previous_direction]
                # TODO: TMP tant que 1 niveau (z)
                directions_list = [direction for direction in directions_list if 9 < direction < 19]
                direction_name = choice(directions_list)
            except KeyError:
                pass

        if not direction_name:
            direction_name = randint(directions_same_level)

        return direction_name