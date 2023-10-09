import requests

def search_market_items(appid, query="%20"):
    url = f"https://steamcommunity.com/market/search/render/?query={query}&appid={appid}&norender=1&county=BR&currency=7&l=portuguese&start=0&count=100"
    
    response = requests.get(url)
    data = response.json()

    return data