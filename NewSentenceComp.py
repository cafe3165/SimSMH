import rwfile
import st
import datetime
import nlptest
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )

sentenceList = []

# pathname1 = "txt3/SET1-0709.txt"
pathname1="txt3/test1.txt"

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

for i in Set4[0]:
    resulSet4_if.append(i)
for i in Set4[1]:
    resulSet4_action.append(i)
    resulSet2.append(str(i).strip())
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

setName="result0709-set1"
isTest="-test"
st.compare(pathname2_1,resulSet1,'txt3/'+setName+isTest+'-1.txt','txt3/'+setName+isTest+'-1.txt',1)
st.compare(pathname2_2,resulSet2,'txt3/'+setName+isTest+'-2.txt','txt3/'+setName+isTest+'-2.txt',2)
st.compare(pathname2_3,resulSet3,'txt3/'+setName+isTest+'-3.txt','txt3/'+setName+isTest+'-3.txt',3)
st.compare(pathname2_4,resulSet4_if,'txt3/'+setName+isTest+'-4_if.txt','txt3/'+setName+isTest+'-4_if.txt',4)

nowTime2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
print(nowTime2)
