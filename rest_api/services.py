import os
import requests

STEAM_KEY = os.getenv("STEAM_API_KEY")

# Obtener detalle de juego en particular de steam
def get_steam_app_details(app_id: int, country: str = "cl"):
    url = "https://store.steampowered.com/api/appdetails"
    params = {
        "appids": app_id,
        "cc": country,
        "key": STEAM_KEY
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json().get(str(app_id), {})
    return data.get("data") if data.get("success") else {}

# Obtener top vendidos de steam
def get_steam_top_sellers(limit: int = 10, country: str = "cl", language: str = "es"):
    url = "https://store.steampowered.com/api/featuredcategories"
    params = {
        "cc": country,   
        "l": language    
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    sellers = data.get("top_sellers", {}).get("items", [])
    return [{"appid": item["id"], "name": item["name"]} for item in sellers[:limit]]