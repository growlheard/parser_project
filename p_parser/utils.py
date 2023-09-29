import json
import os
import time
from urllib.parse import urljoin

import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def get_ad_previews(driver, url, region, time_period, advertiser_id):
    # Переход на страницу с объявлениями рекламодателя
    driver.get(url)

    # Прокрутка страницы
    max_scroll_time = 3  # Максимальное время прокрутки в секундах
    start_time = time.time()

    while time.time() - start_time < max_scroll_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)  # Ожидание 2 секунды после прокрутки страницы

    ad_elements = driver.find_elements(By.CSS_SELECTOR, "div.creative-bounding-box")

    # Создание списка для хранения пар ссылок на объявления и превью
    ad_data = []

    # Получение ссылок на объявления и превью и добавление их в список
    for ad_element in ad_elements:
        # Получение ссылки на объявление (относительная ссылка)
        href = ad_element.get_attribute("href")

        # Преобразование относительной ссылки в абсолютную URL-ссылку
        absolute_url = urljoin('https://adstransparency.google.com/advertiser/AR07328800802254880769/creative/',
                               href.split('?')[0])

        try:
            preview_element = ad_element.find_element(By.CSS_SELECTOR, "div.creative-bounding-box img")
            preview_url = preview_element.get_attribute("src")
        except NoSuchElementException as e:
            # Запись ошибки в лог
            print(f'Ошибка: {"Элемент не найден"}')
            preview_url = None

        # Добавление пары ссылок в список
        ad_data.append({"ad_link": absolute_url, "preview_link": preview_url, "region": region, "time_period": time_period})

    # Создание словаря с объединенными данными
    combined_data = {
        "ad_data": ad_data
    }
    return combined_data


def download_previews(combined_data, advertiser_id):
    # Создание директории для сохранения превью
    os.makedirs(f"{advertiser_id}", exist_ok=True)

    # Скачивание и сохранение превью объявлений
    for data in combined_data["ad_data"]:
        # Проверка наличия ссылки на превью объявления
        if "preview_link" not in data:
            continue

        # Запрос на скачивание превью
        response = requests.get(data["preview_link"])

        # Генерация имени файла
        file_name = f"{advertiser_id}/preview_{data['preview_link'].split('/')[-1]}.jpg"

        # Сохранение превью
        with open(file_name, "wb") as preview_file:
            preview_file.write(response.content)

        # Создание отдельного JSON файла для данных объявления
        ad_data_file_name = f"{advertiser_id}/data_{data['preview_link'].split('/')[-1]}.json"
        with open(ad_data_file_name, "w") as ad_data_file:
            json.dump(data, ad_data_file, indent=4)


def get_country_code(country):
    with open("country_codes.json", "r") as json_file:
        country_codes = json.load(json_file)

    return country_codes.get(country)


def get_time_preset(time):
    with open("time_preset.json", "r") as json_file:
        time_preset = json.load(json_file)

    return time_preset.get(time)