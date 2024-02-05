from .common import _User, _Game, _UserStats


class SteamApi:
    def __init__(self, key):
        self.key = key
        self.user = _User(self.key)
        self.game = _Game(self.key)
        self.stats = _UserStats(self.key)
