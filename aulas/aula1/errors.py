a = "a"
b = 12

try:
    print(b / a)
except ZeroDivisionError:
    print("Você não pode realizar divisão por zero")
except TypeError:
    print("Para realizar a divisão informe apenas número")
