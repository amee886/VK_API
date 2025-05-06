import requests
from urllib.parse import urlparse
from decouple import config


API_VERSION = '5.131'


def is_shorten_link(api_token, input_url):
    parsed_url = urlparse(input_url)
    key = parsed_url.path[1:]
    url = f'https://api.vk.com/method/utils.getLinkStats'
    params = {
        'access_token': api_token,
        'key': key,
        'v': API_VERSION
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_data = response.json()
    return "response" in response_data and response_data["response"]


def shorten_link(api_token, input_url):
    url = f'https://api.vk.com/method/utils.getShortLink'
    params = {
        'access_token': api_token,
        'url': input_url,
        'v': API_VERSION
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_data = response.json()
    short_url = response_data['response']['short_url']
    return short_url


def count_clicks(api_token, short_url):
    parsed_url = urlparse(short_url)
    key = parsed_url.path[1:]
    url = f'https://api.vk.com/method/utils.getLinkStats'
    params = {
        'access_token': api_token,
        'key': key,
        'v': API_VERSION
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_data = response.json()

    if "response" in response_data and "stats" in response_data["response"] and len(response_data["response"]["stats"]) > 0:
        clicks = response_data["response"]["stats"][0]["views"]
        return clicks
    else:
        return 0


def main():
    api_token = config("API_TOKEN")
    input_url = input("Введите URL: ")
    try:
        if is_shorten_link(api_token, input_url):
            clicks = count_clicks(api_token, input_url)
            print("Является короткой ссылкой.")
        else:
            short_url = shorten_link(api_token, input_url)
            print(f"Сокращенная ссылка: {short_url}")
            clicks = count_clicks(api_token, short_url)
            print("Не является короткой ссылкой")
        print(f"Количество кликов по ссылке: {clicks}")

    except requests.exceptions.HTTPError:
        print("Ошибка в запросе")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
