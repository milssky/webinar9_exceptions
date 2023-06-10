class CustomExceptions(Exception):
    pass


def raise_exceptions():
    raise CustomExceptions("Message")


def raise_other_exception():
    try:
        raise_exceptions()
    except Exception as error:
        raise ValueError from error

# raise
# raise ... from ...


def main():
    try:
        raise_other_exception()
    except Exception as e:
        print(e.__context__)
        print(e.__cause__)



if __name__ == '__main__':
    main()
