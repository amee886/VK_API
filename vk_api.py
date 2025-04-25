import requests
from urllib.parse import urlparse
from decouple import config


API_TOKEN = config("API_TOKEN")
API_VERSION = '5.131'
input_url = input("Введите URL: ")


def is_shorten_link(input_url):
    short_domains = ["vk.cc"]
    parsed_url = urlparse(input_url)
    if parsed_url.netloc in short_domains:
        return True


def shorten_link(API_TOKEN, input_url):
    url = f'https://api.vk.com/method/utils.getShortLink'
    params = {
        'access_token': API_TOKEN,
        'url': input_url,
        'v': API_VERSION
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    short_url = data['response']['short_url']
    return short_url


try:
    short_url = shorten_link(API_TOKEN, input_url)
    print(f"Сокращенная ссылка: {short_url}")
except requests.exceptions.HTTPError:
    print("Ошибка  в запросе")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Произошла ошибка: не удалось распознать JSON")


def count_clicks(API_TOKEN, short_url):
    parsed = urlparse(short_url)
    key = parsed.path[1:]
    url = f'https://api.vk.com/method/utils.getLinkStats'
    params = {
        'access_token': API_TOKEN,
        'key': key,
        'v': API_VERSION
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    clicks = data["response"]["stats"]
    return clicks


def main(input_url):
    if is_shorten_link(input_url):
        short_url = input_url
        clicks = count_clicks(API_TOKEN, short_url)
        print("Является короткой ссылкой.")
    else:
        short_url = shorten_link(API_TOKEN, input_url)
        clicks = count_clicks(API_TOKEN, short_url)
        print("Не является короткой ссылкой")
    return clicks


try:
    clicks = count_clicks(input_url)
    print(f"Количество кликов по ссылке: {clicks}")
except requests.exceptions.HTTPError:
    print("Ошибка в запросе")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Произошла ошибка: отстутсвуют клики")


if __name__ == '__main__':
    main(input_url)

