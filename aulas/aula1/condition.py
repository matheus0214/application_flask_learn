online = False


def printBGDanger(string):
    print("\x1b[0;37;41m" + string + "\x1b[0m")


if online:
    printBGDanger("Você pode requisitar")
else:
    printBGDanger("Você precisa realizar o login")


print("Olá estou online 😍" if not online else "Não to ON 😭")
