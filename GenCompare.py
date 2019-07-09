import rwfile


# sl = rwfile.stReadFile('txt/resulSet1.txt')
# filer = open('txt/result0614-1.txt', 'r', encoding='utf-8')


def Gen(SystemSenFile, testSetNoFile, testSetSenFile, outPutFile, similarValueFile):
    sl = rwfile.stReadFile(SystemSenFile)

    filer = open(testSetNoFile, 'r', encoding='utf-8')
    cl = rwfile.stReadFile(testSetSenFile)
    # print(len(cl), cl)
    l1 = []
    l2 = []
    for line in filer.readlines():
        curLine = line.strip().split(" ")
        # print(len(curLine)>1)
        if(len(curLine)>1):
            l2.append(list(map(int, curLine)))
    # print(len(l2), l2)
    index = 0
    filetest = open(outPutFile, 'w')
    filetest2 = open(similarValueFile, 'r')
    ll = []
    for line in filetest2.readlines():
        curLine = line.strip().split(" ")
        # print(len(curLine))

        if (len(curLine) > 1):
            ll.append(list(map(float, curLine)))

    # print(len(ll), ll)
    llindex = 0
    num=1
    for i in l2:
        filetest.write(str(num)+". ")
        filetest.write(cl[index])
        num+=1
        filetest.write('\n')
        li = 0
        for j in i:
            # print(llindex)
            # print(sl[j], ll[llindex][li])
            filetest.write(sl[j])
            filetest.write(' ')
            filetest.write(str(ll[llindex][li])[:6])
            filetest.write('\n')
            li += 1
        llindex += 1
        # print('\n')
        filetest.write('\n')
        index += 1
