from xyzworld.display.Pygame import Pygame as XyzPygame
import pygame
from intelligine.cst import PHEROMON_INFOS, PHEROMON_DIRECTION, PHEROMON_DIR_EXPLO, PHEROMON_POSITIONS
from intelligine.synergy.object.ant.Pheromon import Pheromon


class Pygame(XyzPygame):

    def __init__(self, config, context):
        super().__init__(config, context)
        self._is_display_pheromones = False


    def receive(self, synergy_object_manager, context):
        super().receive(synergy_object_manager, context)
        if self._is_display_pheromones:
            self._display_pheromones(context.metas.list.get(PHEROMON_POSITIONS, PHEROMON_POSITIONS, allow_empty=True), context)

    def _display_pheromones(self, pheromones_positions, context):
        for point in pheromones_positions:
            exploration_info = context.pheromones().get_info(point,
                                                             [PHEROMON_DIRECTION,
                                                              PHEROMON_DIR_EXPLO],
                                                             allow_empty=True,
                                                             empty_value={})

            for direction in exploration_info:
                intensity = exploration_info[direction]
                # TODO: ne pas avoir a creer d'objet, voir comment dans display
                pheromon = Pheromon(object(), context)
                pheromon.set_direction(direction)
                self._draw_objects_with_decal(point, [pheromon])

    def _key_pressed(self, key):
        if key == pygame.K_p:
            if self._is_display_pheromones:
                self._is_display_pheromones = False
            else:
                self._is_display_pheromones = True