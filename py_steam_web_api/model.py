class User:
    def __init__(self):
        self.steamid: int = 0
        self.communityvisibilitystate: int = 0
        self.profilestate: int = 0
        self.personaname: str = ""
        self.profileurl: str = ""
        self.avatar: str = ""
        self.avatarmedium: str = ""
        self.avatarfull: str = ""
        self.avatarhash: str = ""
        self.lastlogoff: int = 0
        self.personastate: int = 0
        self.primaryclanid: str = ""
        self.timecreated: int = 0
        self.personastateflags: int = 0


class Game:
    def __init__(self):
        self.appid: int = 0
        self.playtime_forever: int = 0
        self.img_icon_url: str = ""
        self.last_modified: int = 0
        self.price_change_number: int = 0


class Badge:
    def __init__(self):
        self.badgeid: int = 0
        self.level: int = 0
        self.scarcity: int = 0
        self.completion_time: int = 0
        self.xp: int = 0
