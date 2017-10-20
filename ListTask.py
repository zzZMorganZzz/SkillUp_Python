# coding=utf-8
"""

"""


List = [1, 8, 2, 3, 4]
newItems = input()
lastindex = 0
if (List.count(newItems) == 0):
    List.append(newItems)
    print (len(List) - 1)
else:
    for i in range(0, len(List), 1):
        if List[i] == newItems:
            lastindex = i
    List.insert(lastindex + 1, newItems)
    print lastindex + 1
