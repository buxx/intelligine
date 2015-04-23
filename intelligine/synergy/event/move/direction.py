"""
Directions identifiers 3D, central position is 14.
niv -1:  1   2  3
         4   5  6
         7   8  9

niv 0:   10 11 12
         13 14 15
         16 17 18

niv 1:   19 20 21
         22 23 24
         25 26 27
"""

directions = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
directions_under_level = (1, 2, 3, 4, 5, 6, 7, 8, 9)
directions_same_level = (10, 11, 12, 13, 15, 16, 17, 18)
directions_upper_level = (19, 20, 21, 22, 23, 24, 25, 26, 27)
directions_modifiers = {
    # (z, x, y)
    1: (-1, -1, -1),
    2: (-1, 0, -1),
    3: (-1, 1, -1),
    4: (-1, -1, 0),
    5: (-1, 0, 0),
    6: (-1, 1, 0),
    7: (-1, -1, 1),
    8: (-1, 0, 1),
    9: (-1, 1, 1),
    #  (z, x, y)
    10: (0, -1, -1),
    11: (0, 0, -1),
    12: (0, 1, -1),
    13: (0, -1, 0),
    14: (0, 0, 0),
    15: (0, 1, 0),
    16: (0, -1, 1),
    17: (0, 0, 1),
    18: (0, 1, 1),
    #  (z, x, y)
    19: (1, -1, -1),
    20: (1, 0, -1),
    21: (1, 1, -1),
    22: (1, -1, 0),
    23: (1, 0, 0),
    24: (1, 1, 0),
    25: (1, -1, 1),
    26: (1, 0, 1),
    27: (1, 1, 1),
}

NORTH = 11
NORTH_EST = 12
EST = 15
SOUTH_EST = 18
SOUTH = 17
SOUTH_WEST = 16
WEST = 13
NORTH_WEST = 10

CENTER = 14

"""
Directions identifiers 3D, central position is 14.
niv -1:  1   2  3
         4   5  6
         7   8  9

niv 0:   10 11 12
         13 14 15
         16 17 18

niv 1:   19 20 21
         22 23 24
         25 26 27
"""

directions_slighty = {
    1: (1, 2, 4, 13, 10, 11),
    2: (1, 2, 3, 10, 11, 12),
    3: (2, 3, 6, 11, 12, 15),
    4: (1, 4, 7, 10, 13, 16),
    5: (1, 2, 3, 4, 5, 6, 7, 8, 9),
    6: (2, 3, 6, 12, 15, 18),
    7: (4, 7, 8, 13, 16, 17),
    8: (7, 8, 9, 16, 17, 18),
    9: (6, 9, 8, 15, 18, 17),
    # (z, x, y)
    10: (13, 10, 11),
    11: (10, 11, 12),
    12: (11, 12, 15),
    13: (10, 13, 16),
    14: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27),
    15: (12, 15, 18),
    16: (13, 16, 17),
    17: (16, 17, 18),
    18: (15, 18, 17),
    #  (z, x, y)
    19: (22, 19, 20, 13, 10, 11),
    20: (19, 20, 21, 10, 11, 12),
    21: (20, 21, 24, 11, 12, 15),
    22: (19, 22, 25, 10, 13, 16),
    23: (19, 20, 21, 22, 23, 24, 25, 26, 27),
    24: (21, 24, 27, 12, 15, 18),
    25: (22, 25, 26, 13, 16, 17),
    26: (25, 26, 27, 16, 17, 18),
    27: (24, 27, 26, 15, 18, 17),
}

directions_degrees = {
    (0, 22.5): 11,
    (22.5, 67): 12,
    (67, 112.5): 15,
    (112.5, 157.5): 18,
    (157.5, 202.5): 17,
    (202.5, 247.5): 16,
    (247.5, 292.5): 13,
    (292.5, 337.5): 10,
    (337.5, 0): 11
}


def get_direction_for_degrees(degrees):
    if degrees < 0:
        degrees = 360 - abs(degrees)
    for plage in directions_degrees:
        if plage[0] <= degrees <= plage[1]:
            return directions_degrees[plage]
    raise Exception("Unknow plage for degree \"" + degrees + '"')


"""
niv 0:   10 11 12
         13 14 15
         16 17 18
"""

directions_opposites = {
    10: 18,
    11: 17,
    12: 16,
    13: 15,
    15: 13,
    16: 12,
    17: 11,
    18: 10
}


def get_direction_opposite(direction):
    return directions_opposites[direction]


def get_position_with_direction_decal(direction=CENTER, point=(0, 0, 0)):
    z, x, y = point
    directions_modifier = directions_modifiers[direction]
    return z + directions_modifier[0], x + directions_modifier[1], y + directions_modifier[2]