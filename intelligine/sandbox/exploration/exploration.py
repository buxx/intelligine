from os import getcwd
from intelligine.display.pygame.visualisation import get_standard_extract_from_map, map_config


simulations, visualisation = get_standard_extract_from_map(getcwd()+"/intelligine/sandbox/exploration/map.tmx",
                                                           map_config)
