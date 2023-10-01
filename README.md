# Parser Project

Cкрипт для парсинга данных с  сайта https://adstransparency.google.com/


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
Следуйте инструкциям на экране.

