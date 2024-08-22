# number_1 = 4
# number_2 = 5
# def sum(a, b):
#     return a + b
# print(sum(15,5))


# def difference(*args):
#     difference = 0
#     for i in args:
#         difference -=i
#     return difference
# print(difference(32,15,2,5,5))


# def summ (sheets,cost = 100, work=1000):
#     summ = sheets*cost+work
#     print(summ)

# summ(10)
# summ(10,200,2000)

# def min(*args):
#     i = 999999
#     for m in args:
#         if i > m:
#             i = m
#     return i
# print(min(321,321,32,142,421,3213,21,3,21,1))


def get_number():
    a = int(input('Введи первое число'))
    b = int(input('Введи второе число'))
    return a,b

def get_operation(a,b):
    c = input('Какую операцию ты хочешь +,-,/,*')
    if c == '-':
        return a - b
    elif c == '+':
        return a + b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    else:
        print('Ошибка')

get_operation(get_number())

# Не знаю как правильно вытащить 2 аргумента с первой функции 