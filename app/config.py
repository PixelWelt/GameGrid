"""
Configuration module for GameGrid application.

This module provides configuration settings for improved game engine support,
including cache durations, MIME types, and CORS settings.
"""

# Cache durations in seconds
CACHE_DURATIONS = {
    'images': 604800,      # 7 days for images
    'audio': 604800,       # 7 days for audio
    'video': 604800,       # 7 days for video
    'scripts': 3600,       # 1 hour for scripts and WASM
    'data': 3600,          # 1 hour for data files
    'default': 86400       # 1 day for everything else
}

# File extensions mapped to cache categories
CACHE_EXTENSIONS = {
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.ico'],
    'audio': ['.mp3', '.ogg', '.wav', '.m4a', '.aac'],
    'video': ['.webm', '.mp4', '.ogv'],
    'scripts': ['.js', '.wasm', '.mjs'],
    'data': ['.json', '.data', '.xml', '.yaml', '.yml']
}

# Additional MIME types for game engines
GAME_ENGINE_MIMETYPES = {
    # RPG Maker
    '.rpgmvp': 'application/octet-stream',  # RPG Maker MV encrypted images
    '.rpgmvo': 'application/octet-stream',  # RPG Maker MV encrypted audio
    '.rpgmvm': 'application/octet-stream',  # RPG Maker MV encrypted video
    '.rpgmvw': 'application/octet-stream',  # RPG Maker MV encrypted weba
    '.png_': 'application/octet-stream',    # RPG Maker MZ encrypted images
    '.ogg_': 'application/octet-stream',    # RPG Maker MZ encrypted audio

    # Unity
    '.unityweb': 'application/octet-stream',
    '.data': 'application/octet-stream',
    '.wasm': 'application/wasm',

    # Godot
    '.pck': 'application/octet-stream',
    '.wasm': 'application/wasm',

    # General web formats
    '.js': 'application/javascript',
    '.mjs': 'application/javascript',
    '.json': 'application/json',
    '.webmanifest': 'application/manifest+json',

    # Images
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',

    # Audio
    '.mp3': 'audio/mpeg',
    '.ogg': 'audio/ogg',
    '.wav': 'audio/wav',
    '.m4a': 'audio/mp4',

    # Video
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.ogv': 'video/ogg',
}


CORS_CONFIG = {
    'origins': ['http://localhost:*', 'http://127.0.0.1:*'],
    'methods': ['GET', 'OPTIONS', 'HEAD'],
    'allow_headers': ['Content-Type', 'Range', 'Accept', 'Accept-Encoding'],
    'expose_headers': ['Content-Length', 'Content-Range', 'Accept-Ranges'],
    'supports_credentials': False,
    'max_age': 3600
}

SECURITY_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'SAMEORIGIN',
}


DEBUG = False
HOST = '0.0.0.0'
PORT = 5000


GAMES_DIRECTORY = 'static/games'
CONFIG_FILENAME = 'config.yaml'
DEFAULT_INDEX = 'index.html'

