import os
import json
import loguru
import yaml

def get_library() -> json:
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
