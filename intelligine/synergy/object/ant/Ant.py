from intelligine.synergy.object.Bug import Bug
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER, \
   COL_TRANSPORTER, COL_TRANSPORTER_NOT_CARRYING, COL_FIGHTER


class Ant(Bug):

    def __init__(self, collection, context):
        super().__init__(collection, context)
        context.metas.states.add_list(self.get_id(), [TRANSPORTER, ATTACKER])
        context.metas.collections.add_list(self.get_id(), [COL_TRANSPORTER,
                                                           COL_TRANSPORTER_NOT_CARRYING,
                                                           COL_FIGHTER])
        self._carried = []

    def put_carry(self, obj, position=None):
        if position is None:
            position = self._get_position()
        self._carried.remove(obj)
        obj.set_position(position)
        self._context.metas.states.remove(self.get_id(), CARRYING)

    def get_carried(self):
        # TODO: cas ou plusieurs ?
        return self._carried[0]

    def carry(self, obj):
        self._carried.append(obj)
        self._context.metas.states.add(self.get_id(), CARRYING)

    def is_carrying(self):
        if len(self._carried):
            return True
        return False

    # TODO: Est-ce ici que doit etre ce code ?
    def set_position(self, position):
        super().set_position(position)
        if self.is_carrying():
            for obj_carried in self._carried:
                obj_carried.set_position(position)
