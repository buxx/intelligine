from intelligine.simulation.object.brain.part.transport.TransportBrainPart import TransportBrainPart


class PutBrainPart(TransportBrainPart):

    @classmethod
    def can_put(cls, context, object_to_take_id):
        raise NotImplementedError()
