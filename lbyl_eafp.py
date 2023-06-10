# LBYL - Look before you leap
# EAFP - Easy to Ask for Forgivenes than Permission

class EmptyFieldError(ValueError):
    pass

def lbyl_open():
    import os

    if os.path.exists("1.txt"):
        f = open("1.txt")
    else:
        print("Файла нет")


def eafp_open():
    try:
        f = open("1.txt")
    except (FileNotFoundError, ValueError):
        pass


eafp_open()
lbyl_open()

raise Exception()