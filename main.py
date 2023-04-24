#  функция расчета мат.операций
def math_act(x1, x2, act):
    if act == '+':
        return x1 + x2
    elif act == '-':
        return x1 - x2
    elif act == '/':
        return x1 / x2
    elif act == '*':
        return x1 * x2


# функция возвращает индекс первого элемента в списке х со значением b, если такого элемента нет возвращает -1

def x_in(x, b):
    if b not in x:
        return -1
    else:
        return int(x.index(b))


a = input('Введите пример для решения: ')
placeholder = ""
math_actions = []
numbers = []
result = 0

# флаговая переменная деления на 0 - проверяется в момент выполнения операции деления
mistake = False

# распиливаем строку и извлекаем из неё числа и мат-операции

for i in range(len(a)):
    if a[i] == '+' or a[i] == '*' or a[i] == '-' or a[i] == '/':
        math_actions.append(a[i])
        numbers.append(int(placeholder))
        placeholder = ""
    elif a[i] != '+' or a[i] != '*' or a[i] != '-' or a[i] != '/':
        placeholder = placeholder + a[i]
numbers.append(int(placeholder))
print(math_actions)
print(numbers)

# Решение уравнения - действия будут выполняться до тех пор,
# пока контейнер мат-операций не станет пустым. Вначале определяется наличие
# приорететных операций (умножение\деление) затем выполняются операции сложения и вычитания

while len(math_actions) > 0 and mistake is False:
    # вначале выполняем все имеющиеся действия умножения и деления, в порядке их положения в уравнении
    if mistake is False:
        while ('*' in math_actions) or ('/' in math_actions):
            if ((x_in(math_actions, '*') >= 0 and x_in(math_actions, '/') >= 0)
                and x_in(math_actions, '*') < x_in(math_actions, '/')) \
                    or (x_in(math_actions, '*') >= 0 > x_in(math_actions, '/')):
                result = math_act(numbers[x_in(math_actions, '*')], numbers[x_in(math_actions, '*') + 1], '*')
                print('result *****', result)
                # удаляем число b в операции a*b, и присваем a
                # значение результата мат.операции
                numbers[x_in(math_actions, '*')] = result
                numbers.pop(x_in(math_actions, '*') + 1)
                # удаляем отработанную мат.операцию из списка
                math_actions.remove('*')
                print(math_actions)  # флаговый вывод для контроля работы программы
                print(numbers)  # флаговый вывод для контроля работы программы
            elif ((x_in(math_actions, '*') >= 0 and x_in(math_actions, '/') >= 0)
                  and x_in(math_actions, '*') > x_in(math_actions, '/')) \
                    or (x_in(math_actions, '*') < 0 <= x_in(math_actions, '/')):
                if numbers[x_in(math_actions, '/') + 1] == 0:
                    print('Ошибка! Делить на 0 нельзя!')
                    mistake = True  # флаговая переменная для отработки ошибки деления на 0
                    break
                result = math_act(numbers[x_in(math_actions, '/')], numbers[x_in(math_actions, '/') + 1], '/')
                numbers[x_in(math_actions, '/')] = result
                numbers.pop(x_in(math_actions, '/') + 1)
                math_actions.remove('/')
                print(math_actions)  # флаговый вывод для контроля работы программы
                print(numbers)  # флаговый вывод для контроля работы программы
    else:
        break
    if mistake is False:
        # по аналогии с умножением и делением выполняем действия мложения и вычитания
        while ('+' in math_actions) or ('-' in math_actions):
            if ((x_in(math_actions, '+') >= 0 and x_in(math_actions, '-') >= 0)
                and (x_in(math_actions, '+') < x_in(math_actions, '-'))) \
                    or (x_in(math_actions, '+') >= 0 > x_in(math_actions, '-')):
                result = math_act(numbers[x_in(math_actions, '+')], numbers[x_in(math_actions, '+') + 1], '+')
                numbers[x_in(math_actions, '+')] = result
                numbers.pop(x_in(math_actions, '+') + 1)
                math_actions.remove('+')
                print(math_actions)  # флаговый вывод для контроля работы программы
                print(numbers)  # флаговый вывод для контроля работы программы
            elif ((x_in(math_actions, '+') >= 0 and x_in(math_actions, '-') >= 0)
                  and x_in(math_actions, '+') > x_in(math_actions, '-')) \
                    or (x_in(math_actions, '+') < 0 <= x_in(math_actions, '-')):
                result = math_act(numbers[x_in(math_actions, '-')], numbers[x_in(math_actions, '-') + 1], '-')
                numbers[x_in(math_actions, '-')] = result
                numbers.pop(x_in(math_actions, '-') + 1)
                math_actions.remove('-')
                print(math_actions)  # флаговый вывод для контроля работы программы
                print(numbers)  # флаговый вывод для контроля работы программы
    else:
        break

if mistake is not True:
    print('result = ', numbers[0])
