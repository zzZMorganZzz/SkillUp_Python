# coding=utf-8


"""Дан файл с каким-то математическим выражением, которое содержит скобки разных типов “{[()]}” в любом порядке.
   Проверить сбалансированны ли скобки.
   В случае сбалансированности вывести результат вычисления выражения, иначе указать позицию скобки,
   которая нарушает баланс."""

_file = open("Task.txt")
task = _file.readline().replace(' ', '')


def getReversBracked(bracked):
    resultValue = ''
    if bracked == '{':
        resultValue = '}'
    if bracked == '[':
        resultValue = ']'
    if bracked == '(':
        resultValue = ')'
    return resultValue


def checkBracked(example):
    isResult = True
    openSymbolCollection = []
    closeSymbol = None
    for item in example:
        if item in ['{', '[', '(']:
            openSymbolCollection.append(item)
            closeSymbol = getReversBracked(item)
        if item in ['}', ']', ')']:
            if closeSymbol == item:
                openSymbolCollection.pop()
                if len(openSymbolCollection) != 0:
                    closeSymbol = getReversBracked(openSymbolCollection[len(openSymbolCollection) - 1])
            else:
                isResult = False
                break
    return isResult

print (checkBracked(task))

task = task.replace('[', '(').replace(']', ')')
task = task.replace('{', '(').replace('}', ')')
print (task)

print(eval(task))

_file.close()
