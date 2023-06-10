import requests
import logging

from http import HTTPStatus


class CustomRequestsException(Exception):
    pass


class NotOkHTTPCodeException(Exception):
    pass


def make_get_query():
    try:
        logging.info("Начинаю")
        r = requests.get('https://httpbin.org/aslklas/').json()
        if r.status_code != HTTPStatus.OK:
            raise NotOkHTTPCodeException("...")
    except requests.JSONDecodeError as error:
        raise CustomRequestsException("Some error on https://httpbin.org") from error
    else:
        logging.info("Запрос выполнен удачно")
    return r


def make_get_other_query():
    try:
        r = requests.get('http://ya.ru')
        if r.status_code != HTTPStatus.OK:
            raise NotOkHTTPCodeException("...")
    except requests.RequestException as error:
        raise CustomRequestsException("Some error on https://ya.ru")
    return r


def main():
    try:
        print(make_get_query())
    except NotOkHTTPCodeException as error:
        logging.error(error)
        # send_message(error)
    except CustomRequestsException as error:
        logging.error(f"Что-то пошло не так - {error}")
    except Exception:
        logging.error("...")
    else:
        print("Все ок!")
    finally:
        print("Я выполняюсь всегда")


if __name__ == '__main__':
    main()

# DRY


