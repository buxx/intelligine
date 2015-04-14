from intelligine.simulation.object.brain.part.BrainPart import BrainPart


class TakeBrainPart(BrainPart):

    _take = {}

    @classmethod
    def can_take(cls, context, object_to_take_id):
        return False
