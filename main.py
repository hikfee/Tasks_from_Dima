def multiply():
    x = input("Введите первое число\n")
    while not x.isnumeric():
        x = input("Лох! Введи заного\n")
    x = float(x)

    y = input("Введите второе число\n")
    while not y.isnumeric():
        y = input("Лох! Введи заного\n")
    y = float(y)

    print("Результат перемножения = ", x * y)


def retry():
    again = str(input("Хотите ли повторить умножение? (да/нет)\n")).lower()
    while again != "да" and again != "нет":
        again = input("Лох! Введи заного\n").lower()
    if again == "да":
        multiply()
    elif again == "нет":
        print("хрш, бб")
        exit()


multiply()
while True:
    retry()
