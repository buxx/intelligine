from intelligine.core.exceptions import NoMolecule
from intelligine.synergy.object.ant.Ant import Ant
from synergine_xyz.display.Pygame import Pygame as XyzPygame
import pygame
from intelligine.cst import PHEROMON_DIR_EXPLO, MOLECULES, SMELL_EGG, SMELL_FOOD, MOLECULES_DIRECTION, \
    MOVE_BYBASS_MEMORY
from intelligine.display.pygame.visualisation import SURFACE_PHEROMONE_EXPLORATION, SURFACE_PHEROMONE_HOME, \
    SURFACE_SMELL_EGG, SURFACE_SMELL_FOOD


class Pygame(XyzPygame):

    def __init__(self, config, context, synergy_manager):
        super().__init__(config, context, synergy_manager)
        self._is_display_molecules = False
        self._is_display_smells = False
        self._draw_callbacks = []

    def receive(self, actions_done):
        super().receive(actions_done)

        if self._is_display_molecules:
            molecules_positions = self._context.metas.list.get(MOLECULES,
                                                               MOLECULES,
                                                               allow_empty=True)
            self._display_molecules(molecules_positions, self._context)

    def _display_molecules(self, molecules_positions, context):
        molecule_exploration_surface = self._object_visualizer.get_surface(SURFACE_PHEROMONE_EXPLORATION)
        molecule_home_surface = self._object_visualizer.get_surface(SURFACE_PHEROMONE_HOME)
        smell_egg_surface = self._object_visualizer.get_surface(SURFACE_SMELL_EGG)
        smell_food_surface = self._object_visualizer.get_surface(SURFACE_SMELL_FOOD)

        for point in molecules_positions:
            point_flavour = context.molecules().get_flavour(point)
            try:
                molecule = point_flavour.get_molecule(category=MOLECULES_DIRECTION, type=PHEROMON_DIR_EXPLO)
                self.draw_surface(point, molecule_exploration_surface)

                adapted_point = self._get_real_pixel_position_of_position(point)
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(str(molecule.get_distance()), 1, (128,255,128))
                self._screen.blit(label, adapted_point)

            except NoMolecule:
                pass # No molecule here

            try:
                molecule = point_flavour.get_molecule(category=MOLECULES_DIRECTION, type=SMELL_FOOD)
                self.draw_surface(point, smell_food_surface)

                adapted_point = self._get_real_pixel_position_of_position(point)
                adapted_point = (adapted_point[0]+10, adapted_point[1]+10)
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(str(molecule.get_distance()), 1, (255,255,0))
                self._screen.blit(label, adapted_point)

            except NoMolecule:
                pass # No molecule here

            try:
                molecule = point_flavour.get_molecule(category=MOLECULES_DIRECTION, type=SMELL_EGG)
                self.draw_surface(point, smell_food_surface)

                adapted_point = self._get_real_pixel_position_of_position(point)
                adapted_point = (adapted_point[0]+10, adapted_point[1]+10)
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(str(molecule.get_distance()), 1, (255,255,0))
                self._screen.blit(label, adapted_point)

            except NoMolecule:
                pass # No molecule here

            try:
                point_flavour.get_molecule(category=MOLECULES_DIRECTION, type=SMELL_EGG)
                self.draw_surface(point, smell_egg_surface)
            except NoMolecule:
                pass # No molecule here

    def _key_pressed(self, key):

        if key == pygame.K_m:
            if self._is_display_molecules:
                self._is_display_molecules = False
            else:
                self._is_display_molecules = True

    def draw_object(self, obj, point):
        super().draw_object(obj, point)
        # TODO: DEBUG
        if isinstance(obj, Ant):
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render(str(obj.get_id()), 1, (255,255,0))
            self._draw_callbacks.append(lambda: self._screen.blit(label, point))
            label2 = myfont.render(',', 1, (0,0,0))

            ant_mem = self._context.metas.value.get(MOVE_BYBASS_MEMORY, obj.get_id(), allow_empty=True,
                                                             empty_value=[])

            def print_mem(points):
                for m in points:
                    real_point = self._get_real_pixel_position_of_position((0, m[0], m[1]))
                    self._screen.blit(label2, real_point)

            self._draw_callbacks.append(lambda: print_mem(ant_mem) )

    def start_of_cycle(self):
        super().start_of_cycle()
        self._draw_callbacks = []

    def end_of_cycle(self):
        for draw_callback in self._draw_callbacks:
            draw_callback()
        super().end_of_cycle()