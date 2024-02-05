## Description

---
This project is entirely based on the [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API#JSON). You can find all the API information in the "all_api_info" folder, which includes both the APIs that require an API key and the ones that can be called without an API key. However, to ensure smooth usage, it is recommended that you [apply for an API key](https://steamcommunity.com/dev/apikey). Currently, the project has only implemented a portion of the API functionalities that I deemed useful.

## Get start
```shell
pip install py-steam-web-api
```
---
### basic
```python
from py_steam_web_api.api import SteamApi

s = SteamApi(key="xxxxxxxxxxxxxxxxxxxx")
```
### get user info 
```python
u = s.user.get_user_info(steamid=76561198155349454)
print(u.steamid, u.personaname)

# 76561198155349454 nike
```

### get friends
```python
# def get_friends(self, steamid: str) -> list[User]
u = s.user.get_friends(steamid=76561198155349454)
for i in u:
    print(i.steamid, i.personaname)

# 76561198098262862 nike
# 76561198400723672 aplay
# 76561198417914571 Π
```

### get level
```python

# def get_level(self, steamid: int) -> int:
a = s.user.get_level(steamid=76561198155349454)
print(a)

# 45
```

### get recent played games 
```python
#def get_recent_played_games(self, steamid: int) -> list[Game]:
a = s.game.get_recent_played_games(steamid=76561198155349454)
for i in a:
    print(i.appid)

# 271590
# 1260320
# 436150
# 322330
```

### all
```python
#user
def get_user_info(self, steamid: int) -> User:
def get_friends(self, steamid: int) -> list[User]:
def get_badges(self, steamid: int) -> list[Badge]:
def get_level(self, steamid: int) -> int:

#game
def get_recent_played_games(self, steamid: int) -> list[Game]:
def get_owned_games(self, steamid: int, include_appinfo=True) -> list[Game]:
def get_game_list(self, max_results=10000) -> list[Game]:

#stats
def get_number_of_current_players(self, appid: int) -> dict:
def get_player_achievements(self, appid: int, steamid: int) -> dict:
def get_schema_for_game(self, appid: int) -> dict:
def get_user_stats_for_game(self, appid: int, steamid: int) -> dict:


```
