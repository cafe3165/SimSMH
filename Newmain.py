import Similar
import rwfile
import datetime
import nlptest

nowTime1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime1)
sentencelist = rwfile.readfile("vbd0701.txt","vbc0701.txt","ta0701.txt","txt2/")
print(sentencelist)
print(len(sentencelist))

dname = "txt/50d.txt"

posResult = []

posResult = nlptest.deal(sentencelist)
print(posResult)

resulSet1 = []
resulSet2 = []
resulSet3 = []
resulSet4 = []

index = 0
for i in range(len(sentencelist)):
    if (posResult[index] == 1):
        resulSet1.append(sentencelist[index])
        index += 1
        continue
    elif (posResult[index] == 2):
        resulSet2.append(sentencelist[index])
        index += 1
        continue
    elif (posResult[index] == 3):
        resulSet3.append(sentencelist[index])
        index += 1
        continue
    elif (posResult[index] == 4):
        resulSet4.append(sentencelist[index])
        index += 1
        continue
        # ///////////////////////////////////////////
print(resulSet1)
print(resulSet2)
print(resulSet3)
print(resulSet4)
print(len(resulSet1), len(resulSet2), len(resulSet3), len(resulSet4), len(sentencelist))
sen2vec1 = []
sen2vec2 = []
sen2vec3 = []
sen2vec4 = []

for sentence in resulSet1:
    v1 = Similar.calculate(dname, sentence)
    sen2vec1.append(v1)
for sentence in resulSet2:
    v1 = Similar.calculate(dname, sentence)
    sen2vec2.append(v1)
for sentence in resulSet3:
    v1 = Similar.calculate(dname, sentence)
    sen2vec3.append(v1)
for sentence in resulSet4:
    v1 = Similar.calculate(dname, sentence)
    sen2vec4.append(v1)
# rwfile.mainWriteFile(sen2vec1, sen2vec2, sen2vec3, sen2vec4)
rwfile.mainWriteFile2(resulSet1,resulSet2,resulSet3,resulSet4)

nowTime2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime2)
