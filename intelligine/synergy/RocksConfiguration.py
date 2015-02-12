from synergine.synergy.collection.Configuration import Configuration
from intelligine.synergy.object.Rock import Rock


class RocksConfiguration(Configuration):

    def get_start_objects(self, collection):

      rocks = []
      rocks_positions = []

      for i in range(100):
          rocks_positions.append((0, 0+i, 0))
          if i is not 75:
              rocks_positions.append((0, 0+i, 50))
          rocks_positions.append((0, 0+i, 100))

      for i in range(50):
          rocks_positions.append((0, 0, 0+i))
          if i is not 25:
              rocks_positions.append((0, 50, 0+i))
          rocks_positions.append((0, 100, 50+i))
          rocks_positions.append((0, 0, 50+i))
          rocks_positions.append((0, 50, 50+i))
          rocks_positions.append((0, 100, 0+i))

      rocks_positions.append((0, 50, 50))
      rocks_positions.append((0, 100, 50))
      rocks_positions.append((0, 100, 100))

      for rock_position in rocks_positions:
          rock = Rock()
          rock.set_position(rock_position)
          rocks.append(rock)

      return rocks