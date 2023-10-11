import requests

def search_market_items(appid, query=" "):
    url = f"https://steamcommunity.com/market/search/render/?norender=1&country=BR&currency=7&start=0&count=100&appid={appid}&q={query}"
    
    response = requests.get(url)
    data = response.json()

    return data