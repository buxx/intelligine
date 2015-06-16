from synergine_xyz.mechanism.DistanceFromMechanism import DistanceFromMechanism


class TraversableDistanceFromMechanism(DistanceFromMechanism):
    """
    Prepare list of traversable points around synergy object position. These point are associated with distance
    of synergy object position.
    """

    def _get_maximum_distance(self, object_id, context):
        # TODO (ds surcharge) Maintenir un rayon (calculé en fonction de la taille de la colonie + ratio en
        #  fonction de ce qui est smelling)
        # pour le moment ...valeur hardcode
        return 6

    def _point_is_computable(self, context, point):
        return context.position_can_be_odorus(point)
