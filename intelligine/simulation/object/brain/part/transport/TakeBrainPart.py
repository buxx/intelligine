from intelligine.simulation.object.brain.part.transport.TransportBrainPart import TransportBrainPart


class TakeBrainPart(TransportBrainPart):

    @classmethod
    def can_take(cls, context, object_to_take_id):
        raise NotImplementedError()
