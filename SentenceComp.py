import rwfile
import st
import datetime
import nlptest
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )

sentenceList = []
# pathname1 = "txt/set2-0614.txt"
# pathname1 = "txt/command4.txt"
pathname1 = "txt2/SET2-0701.txt"

pathname2_1 = "txt2/sen2vec0701-1.txt"
pathname2_2 = "txt2/sen2vec0701-2.txt"
pathname2_3 = "txt2/sen2vec0701-3.txt"
pathname2_4 = "txt2/sen2vec0701-4.txt"

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime)
sentenceList = rwfile.readfile2(pathname1)

posResult = []

posResult = nlptest.deal(sentenceList)
# print(posResult)
resulSet1 = []
resulSet2 = []
resulSet3 = []
resulSet4 = []
resulSet4_if = []
resulSet4_action = []

index = 0
for i in range(len(sentenceList)):
    if (posResult[index] == 1):
        resulSet1.append(sentenceList[index])
        index += 1
        continue
    elif (posResult[index] == 2):
        resulSet2.append(sentenceList[index])
        index += 1
        continue
    elif (posResult[index] == 3 or posResult[index] == 0):
        resulSet3.append(sentenceList[index])
        index += 1
        continue
    elif (posResult[index] == 4):
        resulSet4.append(sentenceList[index])
        index += 1
        continue

Set4 = nlptest.dealResulSet4(resulSet4)
# print(Set4[0])
# print(Set4[1])
for i in Set4[0]:
    resulSet4_if.append(i)
for i in Set4[1]:
    resulSet4_action.append(i)
    resulSet2.append(str(i).strip())
# orderList = []
# # mapList = []
# # print(sentenceList)
# # for i in sentenceList:
# #     L = st.returnSimilarSentence(i, pathname2, -5)
# #     print(list(L.keys()))
# #     orderList.append(list(L.keys()))
# #     mapList.append(L)
# #
# # print(orderList)
# # rwfile.writefile2(mapList)

print(resulSet1)
print(resulSet2)
print(resulSet3)
print(resulSet4)
print(resulSet4_if)
print(resulSet4_action)

# rwfile.sentenceWriteFile(resulSet1,'txt2/set2-sentence-1.txt')
# rwfile.sentenceWriteFile(resulSet2,'txt2/set2-sentence-2.txt')
# rwfile.sentenceWriteFile(resulSet3,'txt2/set2-sentence-3.txt')
# rwfile.sentenceWriteFile(resulSet4_if,'txt2/set2-sentence-4_if.txt')
# rwfile.sentenceWriteFile(resulSet4_action,'txt2/set2-sentence-4_action.txt')
# rwfile.sentenceWriteFile(resulSet4,'txt2/set2-sentence-4.txt')


# rwfile.sentenceWriteFile(resulSet1,'txt/set2-sentence-1.txt')
# rwfile.sentenceWriteFile(resulSet2,'txt/set2-sentence-2.txt')
# rwfile.sentenceWriteFile(resulSet3,'txt/set2-sentence-3.txt')
# rwfile.sentenceWriteFile(resulSet4_if,'txt/set2-sentence-4_if.txt')
# rwfile.sentenceWriteFile(resulSet4_action,'txt/set2-sentence-4_action.txt')
# rwfile.sentenceWriteFile(resulSet4,'txt/set2-sentence-4.txt')

# rwfile.sentenceWriteFile(resulSet1,'txt/original-set1-sentence-1.txt')
# rwfile.sentenceWriteFile(resulSet2,'txt/original-set1-sentence-2.txt')
# rwfile.sentenceWriteFile(resulSet3,'txt/original-set1-sentence-3.txt')
# rwfile.sentenceWriteFile(resulSet4_if,'txt/original-set1-sentence-4_if.txt')
# rwfile.sentenceWriteFile(resulSet4_action,'txt/original-set1-sentence-4_action.txt')
# rwfile.sentenceWriteFile(resulSet4,'txt/original-set1-sentence-4.txt')

# rwfile.sentenceWriteFile(resulSet1, 'txt/original-set2-sentence-1.txt')
# rwfile.sentenceWriteFile(resulSet2, 'txt/original-set2-sentence-2.txt')
# rwfile.sentenceWriteFile(resulSet3, 'txt/original-set2-sentence-3.txt')
# rwfile.sentenceWriteFile(resulSet4_if, 'txt/original-set2-sentence-4_if.txt')
# rwfile.sentenceWriteFile(resulSet4_action, 'txt/original-set2-sentence-4_action.txt')
# rwfile.sentenceWriteFile(resulSet4, 'txt/original-set2-sentence-4.txt')

st.compare(pathname2_1,resulSet1,'txt2/result0701-set2-1.txt','txt2/sim0701-set2-1.txt',1)
st.compare(pathname2_2,resulSet2,'txt2/result0701-set2-2.txt','txt2/sim0701-set2-2.txt',2)
st.compare(pathname2_3,resulSet3,'txt2/result0701-set2-3.txt','txt2/sim0701-set2-3.txt',3)
st.compare(pathname2_4,resulSet4_if,'txt2/result0701-set2-4.txt','txt2/sim0701-set2-4_if.txt',4)

# st.compare(pathname2_1,resulSet1,'txt2/result0701-set1-1.txt','txt2/sim0701-set2-1.txt',1)
# st.compare(pathname2_2,resulSet2,'txt2/result0701-set1-2.txt','txt2/sim0701-set2-2.txt',2)
# st.compare(pathname2_3,resulSet3,'txt2/result0701-set1-3.txt','txt2/sim0701-set2-3.txt',3)
# st.compare(pathname2_4,resulSet4_if,'txt2/result0701-set1_if.txt','txt2/sim0701-set2-4_if.txt',4)

# st.compare(pathname2_1,resulSet1,'txt/result-set2-0614-1.txt','txt/sim0614-set2-1.txt',1)
# st.compare(pathname2_2,resulSet2,'txt/result-set2-0614-2.txt','txt/sim0614-set2-2.txt',2)
# st.compare(pathname2_3,resulSet3,'txt/result-set2-0614-3.txt','txt/sim0614-set2-3.txt',3)
# st.compare(pathname2_4,resulSet4_if,'txt/result-set2-0614-4.txt','txt/sim0614-set2-4.txt',4)

# st.compare(pathname2_1,resulSet1,'txt/original-result-set1-0614-1.txt','txt/original-sim0614-set1-1.txt',1)
# st.compare(pathname2_2,resulSet2,'txt/original-result-set1-0614-2.txt','txt/original-sim0614-set1-2.txt',2)
# st.compare(pathname2_3,resulSet3,'txt/original-result-set1-0614-3.txt','txt/original-sim0614-set1-3.txt',3)
# st.compare(pathname2_4,resulSet4_if,'txt/original-result-set1-0614-4.txt','txt/original-sim0614-set1-4.txt',4)

# st.compare(pathname2_1, resulSet1, 'txt/original-result-set2-0614-1.txt', 'txt/original-sim0614-set2-1.txt', 1)
# st.compare(pathname2_2, resulSet2, 'txt/original-result-set2-0614-2.txt', 'txt/original-sim0614-set2-2.txt', 2)
# st.compare(pathname2_3, resulSet3, 'txt/original-result-set2-0614-3.txt', 'txt/original-sim0614-set2-3.txt', 3)
# st.compare(pathname2_4, resulSet4_if, 'txt/original-result-set2-0614-4.txt', 'txt/original-sim0614-set2-4.txt', 4)

#
nowTime2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime2)
