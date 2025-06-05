import requests

def fetch_news(api_key, keyword):
    url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={keyword}&language=en'
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        return [article['title'] for article in data['results'][:10]]
    else:
        print("Error fetching news:", data)
        return []
]