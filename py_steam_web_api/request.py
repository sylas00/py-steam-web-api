import requests


class SteamAPIBaseRequest:
    def __init__(self):
        self.base_url = "http://api.steampowered.com"

    def request(self, r_method, path1: str, path2: str, version_id: int, **kwargs) -> dict:
        url = f"{self.base_url}/{path1}/{path2}/v000{str(version_id)}"
        params = {"format": "json"}
        params.update(kwargs)
        if r_method == "get":
            r = requests.get(url, params=params)
        elif r_method == "post":
            r = requests.post(url, data=params)
        else:
            raise ValueError(f"xxx")

        if r.status_code != 200:
            raise ValueError(f"{r.text}")
        return r.json()


steam_request = SteamAPIBaseRequest()
