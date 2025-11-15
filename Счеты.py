from tkinter import filedialog as fd
import string
import random
import json
import time
from ctypes import *
print('*' * 50)
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)
def colorLine(c, s):
    for i in range(2):
        print()
    color(c)
    print('*' * (len(s) + 2))
    print(' ' + s)
    print('*' * (len(s) + 2))

def loadMoney():
    try:
        f = open('money.txt', 'r')
        m = int(f.readline())
        f.close()
        
    except FileNotFoundError:
        print(f'Файл не найден! Признавайся, твоих рук дело!')
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open('money.txt', 'w')
        f.write(str(moneyToSave))
        f.close()
    except:
        print('Errrrroooorrrrr 000000000000000000000')
        quit(0)

def main():
    count = 0
    right = 0
    lowDiapazon = 10
    highDiapazon = 500
    sign = 0
    money = loadMoney()
    playGame = True
    while (playGame):
        colorLine(3, f'Ваш баланс: {money} $')
        
        print('-' * 50)

        sign = random.randint(0, 3)
    #Сложение
        if (sign == 0):
            z = random.randint(lowDiapazon, highDiapazon)
            x = random.randint(lowDiapazon , z)
            y = z - x
            if (random.randint(0, 1) == 0):
                print(f'{x} + {y} = ?')
            else:
                print(f'{y} + {x} = ?')
        #Вычитание
        elif (sign == 1):
            x = random.randint(lowDiapazon, highDiapazon)
            y = random.randint(0, x - lowDiapazon)
            z = x - y
            print(f'{x} - {y} = ?')
        elif (sign == 2):
            x = random.randint(1,(highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
            y = random.randint(lowDiapazon, highDiapazon) // x
            z = x * y
            print(f'{x} * {y} = ?')
        elif (sign == 3):
            x = random.randint(1, (highDiapazon - lowDiapazon) //
                               random.randint(1, highDiapazon // 10) + 1)
            y = random.randint(lowDiapazon, highDiapazon) // x
            if (y == 0):
                y = 1
            x = x * y
            z = x // y
            print(f'{x} : {y} = ?')
        
        user = ""
        while (not user.isdigit()
               and user.upper() != 'STOP'
               and user.upper() != 'S'
               and user.upper() != 'Ы'
               and user.upper() != 'ЫЕЩЗ'):
            user = input('Ваш ответ: ')
            if (user.upper() == "HELP"
                    or user =='?'
                    or user == ','
                    or user.upper() == 'РУДЗ' and money >= 10):
                if (z > 9):
                    print(f'Последняя цифра ответа {z % 10}')
                    money -= 10
                elif (money < 10):
                    print(f'Вам нечем платить за подсказку')
                else:
                    print("Ответ состоит из одной цифры! У тебя всё хорошо?")
                
            elif (user.upper() == 'STOP'
                  or user.upper() == 'Ы'
                  or user.upper() == 'ЫЕЩЗ'):
                
                print('*' * 50)
                print('Статистика игры:')
                color(7)
                print(f'\tОбработано задач: {count}')
                print(f'\tРешено верно: {right}')
                print(f'\tРешено неверно: {count - right}')
                
                if (right >= count - right):
                    color(10)
                    print(f'\tПроцент верных ответов: {int(right / count * 100)}%')
                    print('\tХорошая работа! Будем видеть рады вас ещё!')
                elif (right < (count-right)):
                    color(12)
                    print(f'\tАх, ты бездарь! Что из тебя выйдет! Ты решил правильно {right}  из {count}')
                    print("\tНу нечего, на выходных займёмся физикой, глядишь, ты поумнеешь!")
                else:
                    print('\tВы ничего не решали. Эх, жаль! Возвращайтесь!')
                color(15)
                
                input('Нажмите Enter, чтобы продолжить')
                playGame = False
            else:
                time.sleep(random.randint(1, 2))
                try:
                    count += 1
                    if (int(user) == z):
                        color(2)
                        print('\nИ это, правильный ответ!\n')
                        if (sign == 0 or sign == 1):
                            money += 75
                        elif (sign == 2 or sign == 3):
                            money += 100
                
                        right += 1
                    
                    else:
                        color(4)
                        print(f'Ответ неверный. Правильно: {z}')
                        color(15)
                        print(f'\nВы можите ввести команду HELP или ?, чтобы увидеть последнюю цифру ответа (-10 $)\n')
                        money -= 0
                except:
                    print('Введите число')
        saveMoney(money)
        
main()

