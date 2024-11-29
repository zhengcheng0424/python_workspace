import requests


def fetch_url_data(url):
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    url = 'https://api.example.com/data'
    data = fetch_url_data(url)
    print(data)
