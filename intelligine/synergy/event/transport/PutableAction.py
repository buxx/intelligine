from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.PutableEvent import PutableEvent
from intelligine.cst import CANT_CARRY_STILL


class PutableAction(Action):

    _listen = PutableEvent

    def __init__(self, object_id, parameters):
        super().__init__(object_id, parameters)

    def prepare(self, context):
        pass

    def run(self, obj, collection, context, synergy_manager):
        # TODO: TEST
        # TODO: Enlever le state de transportable a ce qui est transporte
        # ?! Comment gerer lorsque deux obj vont vouloir transporter le meme objet ? process !
        obj_id_transportable = self._parameters['objects_ids_transportable'][0]
        obj_transportable = synergy_manager.get_map().get_object(obj_id_transportable)
        # TODO: Doit etre du meme type que ce qui est transporte !
        obj_transported = obj.get_carried()
        obj_transported.set_carried_by(None)
        obj.put_carry(obj_transported)
        context.metas.value.set(CANT_CARRY_STILL, obj.get_id(), 5)
        # TODO: Il faut interdire cette action pendant un temps pour eviter que le fourmis deplace
        # les memes objets direct apres
        # Utiliser les metas pour ca ?
