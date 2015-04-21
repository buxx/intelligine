from intelligine.simulation.object.brain.part.BrainPart import BrainPart


class AttackBrainPart(BrainPart):

    @classmethod
    def can_attack(cls, context, object_id, concerned_object_id):
        # Pour le moment on ne passe ici que si c'est un object ATTACKABLE d'une colonie differente. On attaque
        # toujours. On codera dans ce brain part la decision d'attaquer.
        return True