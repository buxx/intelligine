from synergine_xyz.tmx.TileMapConnector import TileMapConnector


def get_map_connector(map_file_path, map_config):
    return TileMapConnector.from_file(map_file_path, dict(map_config))
