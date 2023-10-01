# Parser Project

Cкрипт для парсинга данных с  сайта https://adstransparency.google.com/

ВНИМАНИЕ! так как обьявления рекламодателей заблокированы на територии РФ советую использовать прокси или vpn на локальной машине. 


* Для запуска скрипта склонируйте репозиторий или скачайте Zip себе на локальную машину.
* Откройте проект в Pycharm.
* Для изменения рекламодателя нужно изменить переменную advertiser_id на ID нужного рекламодателя
* Так же в переменной chrome_driver_path в файле main указываем полный путь к файлу chromedriver.exe


* Установите вертуальное окружение 
Linux:
```bash
python3 -m venv venv 
```
Активировать виртуальное окружение
```bash
source venv/bin/activate
```
Windows:
```bash
virtualenv venv
```
Активировать виртуальное окружение
```bash
venv\Scripts\activate
```
Установить зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
Прейдите в консоли в папку p_parser командой
```bash
cd p_parser
```
Запустите скрипт командой:
```bash
python main.py
```
Следуйте инструкциям на экране:
1. Введите ключ региона: - здесь указываем страну на английском список всех страна находится в файле country_codes.json( если не вводить регион и нажать Enter применится дефолтное значение для всех регионов)
2. Введите период времени: - здесь указываем нужный период где:
    "30" - период показов за 30 дней
    "7" - период показов за 7 дней
    Anywhere" - - период показов за все время
    "Yesterday" - период показов за вчера
    "Today" - период показов за сегодня ( если не вводить период и нажать Enter применится дефолтное значение " За все время")


## Скачанные файлы сохранятся в папке в корне проекта с надванием ID рекламодателя (в данном случае папка будет называться AR07328800802254880769)
   

