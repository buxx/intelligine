from intelligine.synergy.object.Bug import Bug
from synergine.metas import metas
from intelligine.synergy.Simulation import Simulation
from intelligine.cst import CARRYING, TRANSPORTER, ATTACKER


class Ant(Bug):

    def __init__(self):
        super().__init__()
        metas.list.add(Simulation.STATE, self.get_id(), TRANSPORTER)
        metas.list.add(Simulation.STATE, self.get_id(), ATTACKER)
        self._carried = []

    def carry(self, obj):
        self._carried.append(obj)
        metas.list.add(Simulation.STATE, self.get_id(), CARRYING)

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
