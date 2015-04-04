from intelligine.core.exceptions import DirectionException
from intelligine.simulation.object.brain.part.BrainPart import BrainPart
from intelligine.synergy.event.move.direction import directions_same_level, directions_slighty
from random import randint, choice, randrange
from xyzworld.cst import BLOCKED_SINCE, PREVIOUS_DIRECTION


class MoveBrainPart(BrainPart):

    @classmethod
    def get_direction(cls, context, object_id):
        try:
            return cls._get_slighty_direction(context, object_id)
        except DirectionException:
            return cls._get_random_direction(context, object_id)

    @classmethod
    def _get_slighty_direction(cls, context, object_id):
        # TODO: A terme le calcul de la direction devra prendre en compte les directions bloques
        blocked_since = context.metas.value.get(BLOCKED_SINCE, object_id, allow_empty=True, empty_value=0)
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
                return choice(directions_list)
            except KeyError:
                pass

        raise DirectionException()

    @classmethod
    def _get_random_direction(cls, context, object_id):
        return randint(directions_same_level[0], directions_same_level[-1])