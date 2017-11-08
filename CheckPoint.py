# coding=utf-8


"""Дан файл с каким-то математическим выражением, которое содержит скобки разных типов “{[()]}” в любом порядке.
   Проверить сбалансированны ли скобки.
   В случае сбалансированности вывести результат вычисления выражения, иначе указать позицию скобки,
   которая нарушает баланс."""


def get_Revers_Bracked(bracked):
    return_value = ''
    if bracked == '{':
        return_value = '}'
    if bracked == '[':
        return_value = ']'
    if bracked == '(':
        return_value = ')'
    return return_value


def check_Bracked(example):
    is_result = True
    open_symbol_collection = []
    close_symbol = None
    for item in example:
        if item in ['{', '[', '(']:
            open_symbol_collection.append(item)
            close_symbol = get_Revers_Bracked(item)
        if item in ['}', ']', ')']:
            if close_symbol == item:
                open_symbol_collection.pop()
                close_symbol = None
                if len(open_symbol_collection) != 0:
                    close_symbol = get_Revers_Bracked(open_symbol_collection[len(open_symbol_collection) - 1])
            else:
                is_result = False
                break
    if len(open_symbol_collection) != 0:
        is_result = False
    return is_result


pathToFile = input('Specify the path to the file:')

try:
    file = open(pathToFile, 'r')
except IOError as Error:
    print (Error.strerror)
else:
    task = file.readline().replace(' ', '')
    if check_Bracked(task):
        task = task.replace('[', '(').replace(']', ')')
        task = task.replace('{', '(').replace('}', ')')
        try:
            result = eval(task)
            print('Task: {0}'.format(task))
            print('Result: {0}'.format(result))
        except SyntaxError as Error:
            print (Error.msg)
        except NameError as Error:
            print (Error.message)
    else:
        print ('Incorrect brackets')
    file.close()
