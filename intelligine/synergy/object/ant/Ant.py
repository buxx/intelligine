from intelligine.synergy.object.Bug import Bug
from synergine.metas import metas
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER


class Ant(Bug):

    def __init__(self):
        super().__init__()
        metas.states.add_list(self.get_id(), [TRANSPORTER, ATTACKER])
        self._carried = []

    def put_carry(self, obj):
        self._carried.remove(obj)
        obj.set_position(self.get_position())
        metas.states.remove(self.get_id(), CARRYING)

    def get_carried(self):
        # TODO: cas ou plusieurs ?
        return self._carried[0]

    def carry(self, obj):
        self._carried.append(obj)
        metas.states.add(self.get_id(), CARRYING)

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
