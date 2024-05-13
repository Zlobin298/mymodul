import time

print('Думай сам -_-')

time.sleep(3)

print('Я же сказал думай сам!')

time.sleep(4)

print('Ну раз не хочешь думать сам, я помогу тебе))')

time.sleep(4)

print('Только учти что мой калькулятор будет несколько странноват, но я думаю ты к нему привыкнешь)')

time.sleep(9)

while True:
    try:
        v = int(input('Выбери цифру от 1 до 4 чтобы начать решать \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))
        if 1 <= v <= 4:
            q1 = int(input('Введите число 1: '))
            q2 = int(input('Введите число 2: '))

            if v == 1:
                r = q1 + q2
                t = 'сложения'
            elif v == 2:
                r = q1 - q2
                t = 'вычитания'
            elif v == 3:
                r = float(q1) / float(q2)
                t = 'деления'
            else:
                r = q1 * q2
                t = 'умножения'
            break
        else:
            print("Я же сказал ввести число от 1 до 4")
    except ValueError:
        print("Я же сказал ввести число, а не букву")

print('Результат ', t, ' = ', r)

time.sleep(3)

print ('Ну как тебе помогла моя помощь)')

time.sleep(3)

while True:
    a = input("Ответь да или нет: ")
    b = a.capitalize()

    if b == "Да":
      print("Я знал, что смогу помочь)")
      break
    elif b == "Нет":
      print("Почему сам тогда не решал собака сутулая")
      break
    else:
      print("Я же сказал написать да либо нет")
