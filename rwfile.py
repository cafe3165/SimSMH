import numpy as np


def readfile(vbd,vbc,ta,pathname):
    # pathname = "E:/sts_workspace/littletest/"
    # pathname = "D:/idea_workspace/littletest2/"
    # pathname = "txt/"

    pathname1 = pathname + vbd
    pathname2 = pathname + vbc
    pathname3 = pathname + ta
    file1 = open(pathname1, 'r', encoding='utf-8')
    file2 = open(pathname2, 'r', encoding='utf-8')
    file3 = open(pathname3, 'r', encoding='utf-8')
    sentencelist1 = []
    sentencelist2 = []
    sentencelist3 = []


    for line in file1.readlines():
        curLine = line.strip()
        sentencelist1.append(curLine)
    for line in file2.readlines():
        curLine = line.strip()
        sentencelist2.append(curLine)
    for line in file3.readlines():
        curLine = line.strip()
        sentencelist3.append(curLine)

    sentencelist = sentencelist1 + sentencelist2 + sentencelist3
    # print(sentencelist)
    return sentencelist


def readSet1():
    pathname = "txt/set1-0614.txt"
    file1 = open(pathname, 'r', encoding='utf-8')
    sentencelist = []
    for line in file1.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist
def readSet2():
    pathname = "txt/set2-0614.txt"
    file1 = open(pathname, 'r', encoding='utf-8')
    sentencelist = []
    for line in file1.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist

def readfile2(pathname):
    sentencelist = []
    file = open(pathname, 'r', encoding='utf-8')
    for line in file.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist


def writefile(sen2vec):
    file = open(r'sen2vec0614.txt', 'w')
    # print(sen2vec.tolist())
    # print(type(sen2vec))
    # print(type(sen2vec[0]))

    ff = []
    # print(len(sen2vec))
    for i in sen2vec:
        # print(len(i))

        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))

        ff.append(temp)
        # ff.append(round(f,5))

    # print(ff)
    for k in ff:
        print(k)
        file.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file.close()


def writefile2(noList,outputPathname1,outputPathname2):
    file = open(outputPathname1, 'w')
    file2 = open(outputPathname2, 'w')

    print(noList)
    for i in noList:
        file.write(str(list(i.keys())).replace('[', '').replace(']', '').replace(',', '') + "\n")
        file2.write(str(list(i.values())).replace('[', '').replace(']', '').replace(',', '') + "\n")


def mainWriteFile(sen2vec1,sen2vec2,sen2vec3,sen2vec4):
    file1 = open(r'txt2/sen2vec0701-1.txt', 'w')
    file2 = open(r'txt2/sen2vec0701-2.txt', 'w')
    file3 = open(r'txt2/sen2vec0701-3.txt', 'w')
    file4 = open(r'txt2/sen2vec0701-4.txt', 'w')
    ff = []
    for i in sen2vec1:
        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))
        ff.append(temp)
    for k in ff:
        print(k)
        file1.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file1.close()
    ff2 = []
    for i in sen2vec2:
        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))
        ff2.append(temp)
    for k in ff2:
        print(k)
        file2.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file2.close()
    ff3 = []
    for i in sen2vec3:
        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))
        ff3.append(temp)
    for k in ff3:
        print(k)
        file3.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file3.close()
    ff4 = []
    for i in sen2vec4:
        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))
        ff4.append(temp)
    for k in ff4:
        print(k)
        file4.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file4.close()

def mainWriteFile2(resulSet1,resulSet2,resulSet3,resulSet4):
    file1 = open(r'txt2/resultSet1-0701.txt', 'w')
    file2 = open(r'txt2/resultSet2-0701.txt', 'w')
    file3 = open(r'txt2/resultSet3-0701.txt', 'w')
    file4 = open(r'txt2/resultSet4-0701.txt', 'w')

    for i in resulSet1:
        file1.write(i+ "\n")
    for i in resulSet2:
        file2.write(i+ "\n")
    for i in resulSet3:
        file3.write(i+ "\n")
    for i in resulSet4:
        file4.write(i+ "\n")


def stReadFile(pathName):
    file = open(pathName, 'r')
    sentencelist = []

    for line in file.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist

def sentenceWriteFile(resulSet,pathname):
    file = open(pathname, 'w')


    for i in resulSet:
        file.write(i+ "\n")

