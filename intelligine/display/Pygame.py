from intelligine.core.exceptions import NoPheromone
from synergine_xyz.display.Pygame import Pygame as XyzPygame
import pygame
from intelligine.cst import PHEROMON_DIRECTION, PHEROMON_DIR_HOME, PHEROMON_DIR_EXPLO, PHEROMON_POSITIONS, POINTS_SMELL, \
    POINT_SMELL, SMELL_EGG, SMELL_FOOD
from intelligine.display.pygame.visualisation import SURFACE_PHEROMONE_EXPLORATION, SURFACE_PHEROMONE_HOME, \
    SURFACE_SMELL_EGG, SURFACE_SMELL_FOOD


class Pygame(XyzPygame):

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)
        self._is_display_pheromones = False
        self._is_display_smells = False

    def receive(self, actions_done):
        super().receive(actions_done)

        if self._is_display_pheromones:
            pheromones_positions = self._context.metas.list.get(PHEROMON_POSITIONS,
                                                                PHEROMON_POSITIONS,
                                                                allow_empty=True)
            self._display_pheromones(pheromones_positions, self._context)

        if self._is_display_smells:
            smell_positions = self._context.metas.list.get(POINTS_SMELL,
                                                           POINTS_SMELL,
                                                           allow_empty=True)
            self._display_smells(smell_positions, self._context)

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

    def _display_smells(self, smell_positions, context):
        smell_egg_surface = self._object_visualizer.get_surface(SURFACE_SMELL_EGG)
        smell_food_surface = self._object_visualizer.get_surface(SURFACE_SMELL_FOOD)

        for point in smell_positions:
            point_flavour = context.metas.value.get(POINT_SMELL, point, allow_empty=True, empty_value={})
            if SMELL_EGG in point_flavour:
                self.draw_surface(point, smell_egg_surface)
            if SMELL_FOOD in point_flavour:
                self.draw_surface(point, smell_food_surface)

    def _key_pressed(self, key):
        self._is_display_pheromones = key == pygame.K_p
        self._is_display_smells = key == pygame.K_s
