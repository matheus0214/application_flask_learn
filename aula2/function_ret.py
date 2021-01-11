def sum_numbers(a: int, b: int) -> int:
    return a + b


def header(f):
    def wrapper(*args, **kwargs):
        print(f"########### HEADER ###########")
        f(*args, **kwargs)

    return wrapper


def footer(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print("\nCopyright © 2020")

    return wrapper


@header
@footer
def message(name) -> None:
    print(f"Olá você está aqui")


message("Matheus")
