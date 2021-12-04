#!/usr/bin/env python3
import time

import requests
import json
import logging

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        logging.error("Сайт не доступний!")
    else:
        data = json.loads(r.content)
        logging.info(f"Сервер доступний. Дата на сервері: {data['date']['year']}.{data['date']['month']}.{data['date']['day']}. Час: {data['date']['time']}")
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            if isinstance(data[key], dict):
                result = ''
                for i in data[key].keys():
                    result+=f"{i}:{data[key][i]}, "
                logging.info(f"Ключ: {key}, Значення: {result}")
            else:
                logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    while(True):
        main("http://localhost:8000/health")
        time.sleep(60)
