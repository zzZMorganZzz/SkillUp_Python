import copy


class Polynomal:
    __ratioList = []

    def get_ratioList(self):
        return self.__ratioList

    def __init__(self, ratio_list):
        self.__ratioList = ratio_list

    def __str__(self):
        scope = 0
        result = ''
        for i in self.__ratioList[::-1]:
            if i != 0:
                if scope == 0:
                    result = ('+' if i > 0 else '') + str(i) + result
                else:
                    result = ('+' if i > 0 else '') + '{0}x^{1}'.format(str(i), str(scope)) + result
            scope += 1
        result += '=0'
        return result if result[0] == '-' else result[1:]

    def __add__(self, other):
        firstRatioList = copy.deepcopy(self.get_ratioList())
        secondRatioList = copy.deepcopy(other.get_ratioList())
        self.__equalization_ration_list(firstRatioList, secondRatioList)
        listResult = []
        for i in range(0, len(firstRatioList), 1):
            listResult.append(firstRatioList[i] + secondRatioList[i])
        return Polynomal(listResult)

    def __sub__(self, other):
        firstRatioList = copy.deepcopy(self.get_ratioList())
        secondRatioList = copy.deepcopy(other.get_ratioList())
        self.__equalization_ration_list(firstRatioList, secondRatioList)
        listResult = []
        for i in range(0, len(firstRatioList), 1):
            listResult.append(firstRatioList[i] - secondRatioList[i])
        return Polynomal(listResult)

    def __equalization_ration_list(self, firstList, secondList):
        isComplite = False
        while not isComplite:
            if len(firstList) != len(secondList):
                if len(firstList) > len(secondList):
                    secondList.insert(0, 0)
                else:
                    firstList.insert(0, 0)
            else:
                isComplite = True

    def __mul__(self, other):
        collectionItems = []
        firstRatioList = copy.deepcopy(self.get_ratioList())
        secondRatioList = copy.deepcopy(other.get_ratioList())
        resultLen = len(firstRatioList) + len(secondRatioList) - 1
        slip = 0
        resultList = []
        for i in range(0, len(firstRatioList), 1):
            listItem = []
            self.__correct_slip(listItem, slip)
            for j in range(0, len(secondRatioList), 1):
                listItem.append(firstRatioList[i] * secondRatioList[j])
            slip += 1
            self.__add_items(listItem, resultLen)
            collectionItems.append(listItem)

        for i in range(0,len(collectionItems[0]),1):
            item = 0
            for j in range(0,len(collectionItems),1):
                item += collectionItems[j][i]
            resultList.append(item)
        return Polynomal(resultList)

    def __add_items(self, ListItem, lenList):
        while len(ListItem)!= lenList:
            ListItem.append(0)

    def __correct_slip(self,ListItem, slip):
        for i in range(0,slip,1):
            ListItem.append(0)


first = Polynomal([5, 2, 3, 4])
second = Polynomal([1, 2, -1])
print(first)
print(second)
print(first * second)
print(first - second)
print(first + second)
