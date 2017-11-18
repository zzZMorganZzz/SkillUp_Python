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
        self.__equalization_Ration_List(firstRatioList, secondRatioList)
        print self.__ratioList
        print other.__ratioList
        listResult = []
        for i in range(0, len(firstRatioList), 1):
            listResult.append(firstRatioList[i] + secondRatioList[i])
        return Polynomal(listResult)

    def __sub__(self, other):
        firstRatioList = copy.deepcopy(self.get_ratioList())
        secondRatioList = copy.deepcopy(other.get_ratioList())
        self.__equalization_Ration_List(firstRatioList, secondRatioList)
        print self.__ratioList
        print other.__ratioList
        listResult = []
        for i in range(0, len(firstRatioList), 1):
            listResult.append(firstRatioList[i] - secondRatioList[i])
        return Polynomal(listResult)


    def __equalization_Ration_List(self, firstList, secondList):
        isComplite = False
        while isComplite != True:
            if len(firstList) != len(secondList):
                if len(firstList) > len(secondList):
                    secondList.insert(0, 0)
                else:
                    firstList.insert(0, 0)

            else:
                isComplite = True


print(Polynomal([5, 2, 3, 4]) - Polynomal([1, 2,-1]))
