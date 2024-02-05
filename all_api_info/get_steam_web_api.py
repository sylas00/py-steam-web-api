import requests

key = ""
r = requests.get("http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/")
with open("steam_web_api_list.json", "w") as f:
    f.write(r.text)

r = requests.get(f"http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key={key}")
with open("steam_web_apikey_list.json", "w") as f:
    f.write(r.text)
