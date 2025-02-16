"""
This module manages the game library for the Game Grid project.

It provides functionality to retrieve the list of games from the static directory,
read their configuration files, and construct a list of game dictionaries.

Functions:
    get_library(): Retrieves the list of games from the static directory.

Usage:
    Import this module and call the get_library function to get the list of games.
"""
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
    for directory in os.listdir('static/games'):
        if os.path.isdir('static/games/' + directory):
            loguru.logger.info('Found Game at: ' + directory)
            try:
                with open(f'static/games/{directory}/config.yaml', 'r', encoding="utf-8") as file:
                    game_info = yaml.load(file, Loader=yaml.SafeLoader)
                    game_info['url'] = f'/static/games/{directory}/index.html'
                    game_info['image'] = f'/static/games/{directory}/{game_info["title_image"]}'
                    games.append(game_info)
            except FileNotFoundError:
                loguru.logger.error('Config file not found')
    return games
