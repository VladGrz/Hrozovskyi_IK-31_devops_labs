# Lab_2: Автоматизація. Знайомство з CI/CD.  

****
## Хід роботи:  
1. Створив папку lab_2 з _README.md_ файлом;
2. За допомогою пакетного менеджера _PIP_ інсталював `pipenv` та створив ізольоване середовище для Python. Ознайомився з командою `pipenv -h`;
```
pip install pipenv
pipenv --python 3.8
pipenv shell
```
3. Встановив бібліотеку `requests` у моєму середовищі. Також встановив бібліотеку `ntplib`, яка працює з часом.
```
pipenv install requests
pipenv install ntplib
```
4. Створив файл `app.py`. Скопіював код програми із репозиторію до себе. Для кращого розуміння програми ознайомився з [Python tutorial](https://www.tutorialspoint.com/python/index.htm)
5. Переконався, що програма працює правильно.
```
$ python app.py
```
Результат виконання програми:
```
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  13:21:11 PM
Date is:  2021-09-30
success
```
6. Встановив бібліотеку pytest `pipenv install pytest`. Для кращого розуміння ознайомився з документацією pytest.
7. Запустив тести з папки _tests_ кандою `pytest tests/tests.py` та переконався, що вони виконались успішно.  
    Результат тестів:
```
$ pytest tests/tests.py
===================================================================================================== test session starts =====================================================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/vlad/Hrozovskyi_Labs_TPIS/Hrozovskyi_IK-31_devops_labs/lab_2
collected 5 items                                                                                                                                                                                                             

tests/tests.py .....                                                                                                                                                                                                    [100%]

====================================================================================================== 5 passed in 0.50s ======================================================================================================
```
8. У програмі дописую функцію яка буде перевіряти час доби АМ/РМ та відповідно друкувати: Доброго дня/ночі;  
```python
def home_work(t):
    # Ваш захист
    return {
        'PM' in t: "Доброї ночі",
        'AM' in t: "Доброго дня"
    }[True]
```
9. Написав тест, що буде перевіряти правильність виконання функції:
```python
def test_home_work(self):
    # захист
    self.assertEqual(home_work("22:37:31 PM"), "Доброї ночі")
    self.assertEqual(home_work("01:37:31 AM"), "Доброго дня")
```
10. За допомогою команд `pytest tests/tests.py > results.txt` та `python app.py >> results.txt` перенаправив результат виконання тестів, а також результат виконання програми, у файл _results.txt_.
11. Зробив коміт зі змінами до репозиторію.
12. Заповнюю _Makefile_ необхідними командами (bash) для повної автоматизації процесу СІ.
```bash
.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pip install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Starting tests."
	pipenv run pytest tests/tests.py > results.txt

run:
	@echo "Running Python app."
	pipenv run python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Lab_2: commiting by makefile"
	git push
```
13. Закомітив зміни в Makefile до репозиторію та перейшов на віртуальну машину Ubuntu;
14. Склонував git репозиторій на віртуальну машину Ubuntu. Перейшов у папку лабораторної роботи та запустив make командою `make`. В результаті виконання команди запустився скрипт, який створив віртуальне середовище, встановив необхідні бібліотеки, виконавтести та програму та перенапривив їх вивід в файл _results.txt_ і закомітив зміни до репозиторію.