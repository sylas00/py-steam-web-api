from .model import User, Game, Badge
from .request import steam_request


def generate_instance_list(class_name: str, result_list: list):
    instance_list = []
    for i in result_list:
        if class_name == 'User':
            instance = User()
        elif class_name == 'Game':
            instance = Game()
        elif class_name == "Badge":
            instance = Badge()
        else:
            raise Exception('Unknown_class_name')
        instance.__dict__.update(i)
        instance_list.append(instance)
    return instance_list


class _User:
    def __init__(self, key):
        self.key = key

    def get_friends(self, steamid: str) -> list[User]:
        users_dict = steam_request.request("get", "ISteamUser", "GetFriendList", 1, key=self.key, steamid=steamid,
                                           relationship="friend")
        users_dict_list = users_dict.get("friendslist", {}).get("friends", [])
        users = []
        for i in users_dict_list:
            u = self.get_user_info(i.get("steamid"))
            u.__dict__.update(i)
            users.append(u)
        return users

    def get_user_info(self, steamid: str) -> User:
        result_dict = steam_request.request("get", "ISteamUser", "GetPlayerSummaries", 2, key=self.key,
                                            steamids=steamid)
        user_list = result_dict.get("response", {}).get("players", [])
        return generate_instance_list("User", user_list)[0]

    def get_level(self, steamid) -> int:
        result_dict = steam_request.request("get", "IPlayerService", "GetSteamLevel", 1, key=self.key,
                                            steamid=steamid)
        level = result_dict.get("response", {}).get("player_level")

        return level

    def get_badges(self, steamid) -> list[Badge]:
        result_dict = steam_request.request("get", "IPlayerService", "GetBadges", 1, key=self.key,
                                            steamid=steamid)
        badge_list = result_dict.get("response", {}).get("badges")

        return generate_instance_list("Badge", badge_list)


class _Game:
    def __init__(self, key):
        self.key = key

    def get_recent_played_games(self, steamid: str) -> list[Game]:
        result_dict = steam_request.request("get", "IPlayerService", "GetRecentlyPlayedGames", 1, key=self.key,
                                            steamid=steamid, )
        game_list = result_dict.get("response", {}).get("games", [])
        return generate_instance_list("Game", game_list)

    def get_owned_games(self, steamid: str, include_appinfo=True) -> list[Game]:
        result_dict = steam_request.request("get", "IPlayerService", "GetOwnedGames", 1, key=self.key,
                                            steamid=steamid, include_appinfo=include_appinfo)
        game_list = result_dict.get("response", {}).get("games", [])
        return generate_instance_list("Game", game_list)

    def get_game_list(self, max_results=10000) -> list[Game]:
        result_dict = steam_request.request("get", "IStoreService", "GetAppList", 1, key=self.key,
                                            max_results=max_results)
        game_list = result_dict.get("response", {}).get("apps", [])
        return generate_instance_list("Game", game_list)


class _UserStats:
    def __init__(self, key):
        self.key = key

    def get_global_achievement_percentages_for_app(self, gameid: int) -> list:
        games = steam_request.request("get", "ISteamUserStats", "GetGlobalAchievementPercentagesForApp", 2,
                                      gameid=gameid)
        print(games)

    # def get_global_stats_for_game(self, appid: int, ) -> list:
    #     games = steam_request.request("get", "ISteamUserStats", "GetGlobalStatsForGame", 1,
    #                                   appid=appid)
    #
    #     print(games)

    def get_number_of_current_players(self, appid: int) -> dict:
        result_dict = steam_request.request("get", "ISteamUserStats", "GetNumberOfCurrentPlayers", 1,
                                            appid=appid)
        return result_dict.get("response", {}).get("player_count")

    def get_player_achievements(self, appid: int, steamid: int) -> dict:
        result_dict = steam_request.request("get", "ISteamUserStats", "GetPlayerAchievements", 1, key=self.key,
                                            appid=appid, steamid=steamid)
        return result_dict

    def get_schema_for_game(self, appid: int) -> dict:
        result_dict = steam_request.request("get", "ISteamUserStats", "GetSchemaForGame", 2, key=self.key,
                                            appid=appid)
        return result_dict

    def get_user_stats_for_game(self, appid: int, steamid: int) -> dict:
        result_dict = steam_request.request("get", "ISteamUserStats", "GetUserStatsForGame", 2, key=self.key,
                                            appid=appid, steamid=steamid)
        return result_dict
