import json
import os

import loguru
import yaml


def get_library() -> json:
    """Retrieve the list of games from the static directory.

    This function scans the 'static/games' directory for subdirectories, each representing a game.
    It reads the 'config.yaml' file in each subdirectory to gather game information and constructs
    a list of game dictionaries.

    Returns:
        json: A list of dictionaries, each containing information about a game.

    Raises:
        FileNotFoundError: If the 'config.yaml' file is not found in a game's directory.
    """
    games = []
    for dir in os.listdir('static/games'):
        if os.path.isdir('static/games/' + dir):
            loguru.logger.info('Found Game at: ' + dir)
            try:
                with open(f'static/games/{dir}/config.yaml', 'r') as file:
                    game_info = yaml.load(file, Loader=yaml.SafeLoader)
                    game_info['url'] = f'/static/games/{dir}/index.html'
                    game_info['image'] = f'/static/games/{dir}/{game_info["title_image"]}'
                    games.append(game_info)
            except FileNotFoundError:
                loguru.logger.error('Config file not found')
    return games
