from synergine.synergy.event.Action import Action
from intelligine.synergy.event.transport.TakeableEvent import TakeableEvent
from random import randint


class TakeableAction(Action):

    _listen = TakeableEvent

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
        try:
            obj_transportable.set_carried_by(obj)
            obj.carry(obj_transportable)
        except ValueError: # Une NotCarriableError serais pus approprie
            # TODO: tmp? Si on as pas pu le porter c'est qu'il vient d'etre porte par une autre.
            pass
