from synergine.lib.eint import IncrementedNamedInt

ALIVE = IncrementedNamedInt.get('intelligine.alive')
WALKER = IncrementedNamedInt.get('intelligine.walker')
IMPENETRABLE = IncrementedNamedInt.get('intelligine.impenetrable')
ATTACKABLE = IncrementedNamedInt.get('intelligine.attackable')
ATTACKER = IncrementedNamedInt.get('intelligine.attacker')
COLONY = IncrementedNamedInt.get('intelligine.colony')
TRANSPORTABLE = IncrementedNamedInt.get('intelligine.transportable')
TRANSPORTER = IncrementedNamedInt.get('intelligine.transporter')
CARRYING = IncrementedNamedInt.get('intelligine.carrying')
CARRIED = IncrementedNamedInt.get('intelligine.carried')
CANT_CARRY_STILL = IncrementedNamedInt.get('intelligine.cantcarry.still')
CANT_PUT_STILL = IncrementedNamedInt.get('intelligine.cantput.still')
ACTION_DIE = IncrementedNamedInt.get('intelligine.basebug.action.die')
PHEROMONE_SEARCHING = IncrementedNamedInt.get('intelligine.pheromone_searching')

MOVE_MODE = IncrementedNamedInt.get('intelligine.basebug.move.mode')
MOVE_MODE_EXPLO = IncrementedNamedInt.get('intelligine.basebug.move.mode.explo')
MOVE_MODE_GOHOME = IncrementedNamedInt.get('intelligine.basebug.move.mode.gohome')

TYPE = IncrementedNamedInt.get('intelligine.object.type')
TYPE_RESOURCE_TRANSFORMABLE = IncrementedNamedInt.get('intelligine.object.type.resource.transformable')

LAST_PHERMONES_POINTS = IncrementedNamedInt.get('intelligine.last_pheromones_points')

PHEROMON_POSITIONS = IncrementedNamedInt.get('intelligine.phero.positions')
PHEROMON_INFOS = IncrementedNamedInt.get('intelligine.phero.infos')
PHEROMON_DIRECTION = IncrementedNamedInt.get('intelligine.phero.direction')
PHEROMON_DIR_EXPLO = IncrementedNamedInt.get('intelligine.phero.direction.explo')
PHEROMON_DIR_HOME = IncrementedNamedInt.get('intelligine.phero.direction.home')

COL_ALIVE = IncrementedNamedInt.get('intelligine.col.alive')
COL_WALKER = IncrementedNamedInt.get('intelligine.col.walker')
COL_FIGHTER = IncrementedNamedInt.get('intelligine.col.walker')
COL_TRANSPORTER = IncrementedNamedInt.get('intelligine.col.transporter')
COL_TRANSPORTER_CARRYING = IncrementedNamedInt.get('intelligine.col.transporter_carrying')
COL_TRANSPORTER_NOT_CARRYING = IncrementedNamedInt.get('intelligine.col.transporter_not_carrying')

BRAIN_SCHEMA = IncrementedNamedInt.get('intelligine.brain_schema')
BRAIN_PART_MOVE = IncrementedNamedInt.get('intelligine.brain.part.move')
BRAIN_PART_TAKE = IncrementedNamedInt.get('intelligine.brain.part.take')
BRAIN_PART_PUT = IncrementedNamedInt.get('intelligine.brain.part.put')
BRAIN_PART_ATTACK = IncrementedNamedInt.get('intelligine.brain.part.attack')