# Lab_4: Робота з Docker.

****

## Хід роботи:
1. Для ознайомлення з Docker'ом звернувся до [документації](https://docs.docker.com/);
2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустив перевірку версії, виведення допомоги та тестовий імедж:
    ```
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    - Перенаправив вивід цих команд у файл `my_work.log` та закомітив його.
3. Docker працює з Імеджами та Контейнерами. Ознайомився з [документацією](https://docs.docker.com/engine/reference/builder/)
4. Для знайомства з Docker створив імедж із Django сайтом зробленим у попередній роботі.
    - Оскільки мій проект на Python то і базовий імедж також вибираю відповідний. Всі імеджі можна знайти на [Python Docker Hub](https://hub.docker.com/_/python). Використаємо команду щоб завантажити базовий імедж з репозиторію:
    ```
    docker pull python:3.8.12-slim
    docker images
    REPOSITORY        TAG           IMAGE ID       CREATED       SIZE
    python            3.8.12-slim   214d62795dbb   6 days ago    122MB
    hello-world       latest        feb5d9fea6a5   5 weeks ago   13.3kB
    docker/whalesay   latest        6b362a9f73eb   6 years ago   247MB
    docker inspect python:3.8.12-slim
    ```
   - Створив файл з іменем Dockerfile скопіював туди вміст такого ж файлу з репозиторію викладача;
   - Ознайомився із коментарями та постарався зрозуміти структуру написання Dockerfile;
   - Замінив посилання на власний Git репозиторій із веб-сайтом та закомітив даний Dockerfile;