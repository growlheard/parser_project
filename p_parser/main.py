import json
import os
from selenium import webdriver

from utils import download_previews, get_ad_previews


def main():
    advertiser_id = "AR07328800802254880769"

    chrome_driver_path = r'путь_к_\parser_project-master\p_parser\chromedriver.exe'
    service = Service(chrome_driver_path)

    # Создание экземпляра веб-драйвера Selenium
    driver = webdriver.Chrome(service=service)

    # Загрузка списка стран и их значений из файла country_codes.json
    with open("country_codes.json") as json_file:
        country_codes = json.load(json_file)

    with open("time_preset.json") as json_file:
        date = json.load(json_file)

    # Запрос ключа региона от пользователя
    region = None
    while region is None:
        country_key = input("Введите ключ региона: ").capitalize() or "Anywhere"

        # Получение значения региона из списка стран и их значений
        region = country_codes.get(country_key)

        # Проверка, что введенный ключ региона существует
        if region is None:
            print("Неверный ключ региона!")

    # Запрос ключа периода времени от пользователя
    time_period = None
    while time_period is None:
        time_key = input("Введите период времени: ").capitalize() or "Anywhere"

        # Получение значения периода времени из списка значений времени
        time_period = date.get(time_key)

        # Проверка, что введенный ключ периода времени существует
        if time_period is None:
            print("Неверный ключ периода времени!")

    url = f"https://adstransparency.google.com/advertiser/{advertiser_id}?region={region}&preset-date={time_period}"

    # Получение данных объявлений
    combined_data = get_ad_previews(driver, url, region, time_period, advertiser_id)

    
    # Вывод количества объявлений
    print(f"Получено {len(combined_data['ad_data'])} объявлений.")

    # Создание директории с именем advertiser_id
    os.makedirs(advertiser_id, exist_ok=True)

    # Скачивание превью объявлений
    download_previews(combined_data, advertiser_id)

    # Закрытие веб-драйвера
    driver.quit()


if __name__ == "__main__":
    main()
