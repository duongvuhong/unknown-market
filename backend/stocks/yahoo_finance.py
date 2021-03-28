import requests


headers = {
    'x-rapidapi-key': "5e9ea9d024mshb58004c3da36dadp11b056jsn2942a6bab769",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

def get_market_summary():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"

    querystring = {"region":"US"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(f'Market summary: {response.text}')

    return response
