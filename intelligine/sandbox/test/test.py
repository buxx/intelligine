from os import getcwd
from intelligine.display.pygame.config import map_config
from intelligine.display.pygame.visualisation import get_standard_extract_from_map


simulations, visualisation = get_standard_extract_from_map(getcwd()+"/intelligine/sandbox/test/test.tmx",
                                                           map_config)
