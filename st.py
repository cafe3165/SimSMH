import Similar
import rwfile


def returnSimilarSentence(sentence, filepath, rank, type):
    vecs = []
    file = open(filepath, 'r', encoding='utf-8')

    for line in file.readlines():
        curLine = line.strip().split(" ")
        vecs.append(curLine[:])
    v1 = Similar.calculate("txt/50d.txt", sentence).tolist()
    # print(v1)
    result = []
    for i in vecs:
        c = list(map(float, i))
        result.append(Similar.cos_sim(v1, c))
    sentenDict = {}
    # ii=0
    # for i in result:
    #     print(i,ii)
    # ii+=1
    for i in range(len(result)):
        sentenDict[i] = result[i]
        # print(sentenDict[i])

    sentenSortedSet = sorted(list(set(sentenDict.values())))
    if (type == 1):
        sentenceList = rwfile.stReadFile('txt/resulSet1.txt')
    elif (type == 2):
        sentenceList = rwfile.stReadFile('txt/resulSet2.txt')
    elif (type == 3):
        sentenceList = rwfile.stReadFile('txt/resulSet3.txt')
    elif (type == 4):
        sentenceList = rwfile.stReadFile('txt/resulSet4.txt')

    returnDict = {}
    # print(sentenSortedSet)
    # print(sentenSortedSet[-3:])
    for i in sentenSortedSet[rank:]:
        for j in range(len(sentenDict)):
            if i == sentenDict[j]:
                print(sentenceList[j], round(i, 4), j)
                returnDict[j] = i
                break
    return returnDict


def compare(pathname, sentenceList, outputPathname1, outputPathname2, type):
    orderList = []
    mapList = []
    print(sentenceList)
    for i in sentenceList:
        L = returnSimilarSentence(i, pathname, -5, type)
        print(list(L.keys()))
        orderList.append(list(L.keys()))
        mapList.append(L)

    print(orderList)
    rwfile.writefile2(mapList, outputPathname1, outputPathname2)
