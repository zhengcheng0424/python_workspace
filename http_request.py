import requests


def fetch_url_data(url):
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    url = 'http://httpbin.org'
    data = fetch_url_data(url)
    print(data)
