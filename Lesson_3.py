# coding=utf-8
"""
Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере.
Пример входного файла:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Пример выходного файла:
Input file contains:
108 letters
20 words
4 lines
"""

path = input("Set path to file:")

try:
    var = open(path) #("/home/krypton/PycharmProjects/SkillUp_Python/Test_pr_1")
    fileText = var.read()
    print (fileText.replace('\n', " "))
    print ('Count lines:{count}'.format(count=str(len(fileText.split('\n')))))
    print ('Count words:{count}'.format(count=str(len(fileText.replace('\n'," ").split(' ')))))
    print ('Count letters:{count}'.format(count=str(len(fileText.replace('\n'," ").replace(' ','').replace('.','')))))
    var.close()

except IOError:
    print ("No such file or directory ({0})".format(path))