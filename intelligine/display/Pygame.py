from intelligine.core.exceptions import NoPheromone
from synergine_xyz.display.Pygame import Pygame as XyzPygame
import pygame
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_HOME, PHEROMON_DIR_EXPLO, PHEROMON_POSITIONS
from intelligine.display.pygame.visualisation import SURFACE_PHEROMONE_EXPLORATION, SURFACE_PHEROMONE_HOME


class Pygame(XyzPygame):

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)
        self._is_display_pheromones = False

    def receive(self, actions_done):
        super().receive(actions_done)
        if self._is_display_pheromones:
            pheromones_positions = self._context.metas.list.get(PHEROMON_POSITIONS,
                                                                PHEROMON_POSITIONS,
                                                                allow_empty=True)
            self._display_pheromones(pheromones_positions, self._context)

    def _display_pheromones(self, pheromones_positions, context):
        pheromone_exploration_surface = self._object_visualizer.get_surface(SURFACE_PHEROMONE_EXPLORATION)
        pheromone_home_surface = self._object_visualizer.get_surface(SURFACE_PHEROMONE_HOME)

        for point in pheromones_positions:
            point_flavour = context.pheromones().get_flavour(point)
            try:
                point_flavour.get_pheromone(category=PHEROMON_DIRECTION, type=PHEROMON_DIR_HOME)
                self.draw_surface(point, pheromone_home_surface)
            except NoPheromone:
                pass # No pheromone here

            try:
                point_flavour.get_pheromone(category=PHEROMON_DIRECTION, type=PHEROMON_DIR_EXPLO)
                self.draw_surface(point, pheromone_exploration_surface)
            except NoPheromone:
                pass # No pheromone here

    def _key_pressed(self, key):
        if key == pygame.K_p:
            if self._is_display_pheromones:
                self._is_display_pheromones = False
            else:
                self._is_display_pheromones = True