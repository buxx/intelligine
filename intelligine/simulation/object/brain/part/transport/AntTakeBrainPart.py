from intelligine.simulation.object.brain.part.transport.TakeBrainPart import TakeBrainPart
from intelligine.synergy.object.ressource.Ressource import Resource
from intelligine.cst import MODE_EXPLO, TYPE_RESOURCE_EXPLOITABLE, \
    MODE_GOHOME, MODE_NURSE, TYPE_NURSERY, MODE_HOME


class AntTakeBrainPart(TakeBrainPart):

    # TODO: methode __init_ pour la classe ? Pour surcharger ici.
    _mode_matches = {
        MODE_EXPLO: [TYPE_RESOURCE_EXPLOITABLE],
        MODE_NURSE: [TYPE_NURSERY],
        MODE_GOHOME: []
    }

    def __init__(self, host_brain):
        super().__init__(host_brain)
        self._smell_target = None

    def get_smell_target(self):
        if not self._smell_target:
            raise Exception('No _smell_target')
        return self._smell_target

    @classmethod
    def can_take(cls, context, object_id, object_to_take_id):
        # Pour le moment si le type de l'objet fait partie des types admis pour le mode courant du porteur, c'est bon.
        return cls._match_with_mode(context, object_id, object_to_take_id)

    def done(self, take_object):
        # TODO: Ranger ca ? Truc plus dynamique/configurable ?
        # TODO: qqch plus generique ... (attention aux eggs)
        if isinstance(take_object, Resource):
            self._smell_target = self._host_brain.get_smell_for_object_taken(take_object)
            self._host.get_brain().switch_to_mode(MODE_GOHOME)
            self._host.get_movement_molecule_gland().appose()