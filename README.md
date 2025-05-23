Markdown

# URL Shortener with VK API

Этот проект представляет собой простое приложение на Python, которое позволяет сокращать ссылки с помощью API ВКонтакте и отслеживать количество кликов по сокращенным ссылкам.

## Описание

Программа принимает URL от пользователя и проверяет, является ли он уже сокращенной ссылкой. Если ссылка не сокращена, она будет сокращена с использованием метода utils.getShortLink API ВКонтакте. После этого программа отслеживает количество кликов по сокращенной ссылке с помощью метода utils.getLinkStats.

## Установка

1. **Клонируйте репозиторий:**

   
```bash
   git clone https://github.com/ваш_репозиторий.git   cd ваш_репозиторий
```   

2. **Установите необходимые библиотеки:**

   Убедитесь, что у вас установлен Python 3.6 или выше. Затем установите необходимые зависимости:

   
```bash
   python -m pip install -r requirements.txt
```   
3. **Получите токен доступа API ВКонтакте:**

   Вам нужно получить токен доступа для работы с API ВКонтакте. Это можно сделать через [VK Developer](https://vk.com/dev) и создать новое приложение.

4. **Настройте переменные окружения:**

   Создайте файл .env в корневом каталоге проекта и добавьте туда ваш токен:

   
   APITOKEN=ваштокен_доступа
   

## Использование

Запустите скрипт:

```bash
python ваш_скрипт.py
```
Введите URL, который вы хотите сократить, когда программа запросит это.

### Пример

Введите URL: https://example.com
Сокращенная ссылка: https://vk.cc/xxxxx
Количество кликов по ссылке: 10

## Функции

- **is_shorten_link(input_url)**: Проверяет, является ли введенный URL сокращенной ссылкой.
- **shorten_link(API_TOKEN, input_url)**: Сокращает введенный URL с использованием API ВКонтакте.
- **count_clicks(API_TOKEN, short_url)**: Получает количество кликов по сокращенной ссылке.
- **main(input_url)**: Основная логика программы, которая управляет процессом проверки и сокращения ссылки.

## Обработка ошибок

Программа включает обработку ошибок для различных случаев, таких как:

- Ошибки HTTP-запросов.
- Ошибки при распознавании JSON.
- Ошибки при получении статистики кликов.


▎Примечания

1. Замените ваш_репозиторий на фактический URL вашего репозитория.

2. Замените ваш_скрипт.py на имя вашего скрипта.

3. Вы можете добавить дополнительные разделы или изменить существующие в зависимости от ваших предпочтений или требований проекта.
