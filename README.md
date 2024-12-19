# Django Weather Forecast Project

## Описание проекта
Приложение написаное в рамках учебного проекта.
Это веб-приложение на Django для прогноза погоды. Оно позволяет пользователям вводить название города, чтобы узнать текущую погоду в этом городе. Приложение использует шаблоны Django для рендеринга интерфейса и взаимодействует с API [OpenWeatherMap](https://openweathermap.org/) для получения данных о погоде. Введенные города сохраняются в модели `City` и отображаются при обновлении страницы.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git@github.com:MikhailSavenko/forecast.git
    cd forecast
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте базу данных:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Создайте суперпользователя:
    ```sh
    python manage.py createsuperuser
    ```

5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Настройки

1. Получите API ключ от [OpenWeatherMap](https://openweathermap.org/).
2. Добавьте его в файл .env(создайте в корне проекта)
    ```
    API_KEY = 'ваш_api_ключ'
    ```

## Использование

1. Перейдите на домашнюю страницу приложения.
2. Введите название города в форму и нажмите "Отправить".
3. Приложение отобразит текущую погоду для введенного города, включая:
    - Название города
    - Температуру
    - Иконку погоды

## Модель данных

Проект использует модель `City` для хранения введенных пользователями городов и выводит их при каждом обновлении.
