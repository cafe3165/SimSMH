from stanfordcorenlp import StanfordCoreNLP
import rwfile

nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )


# sentence = 'open air purifier in the sitting room .'


# sentence='open air purifier in the sitting room .'
# print('Tokenize:', nlp.word_tokenize(sentence))
# print('Part of Speech:', nlp.pos_tag(sentence))
# print('Named Entities:', nlp.ner(sentence))
# print('Constituency Parsing:', nlp.parse(sentence))  # 语法树
# print('Dependency Parsing:', nlp.dependency_parse(sentence))  # 依存句法

# posList=[]
# for i in nlp.pos_tag(sentence):
#     posList.append(i)

# posList = []
# posList = nlp.pos_tag(sentence)
# print(posList)
# for i in posList:
#     print(i[0])

def jude(posList):
    # print(posList)
    if (posList[0][1] == 'IN'):
        return 4
    for i in posList:
        if (i[0] == 'if'):
            return 4
    if (posList[0][1] == 'VBZ' and posList[-1][0] == '?'):
        return 1
    if (posList[0][1] == 'VB' and posList[-1][0] == '.' or posList[0][1] == 'VBN' and posList[-1][0] == '.'):
        return 2
    if (posList[0][1] == 'WP'):
        return 3

    return 0


# print(jude(posList))


def cal(sentence):
    posList = nlp.pos_tag(sentence)
    # print(posList)


    return (jude(posList))


def deal(sentenceList):
    posResult = []
    for i in sentenceList:
        x = cal(i)
        posResult.append(x)
    nlp.close()  # Do not forget to close! The backend server will consume a lot memery
    return posResult

# print(nlp.pos_tag(sentence))
# posResult1 = []
# posResult2 = []
# posResult3 = []
#
# sentenceList1 = rwfile.readSet1()
# sentenceList2 = rwfile.readSet2()
# sentenceList3 = rwfile.readfile()
# # print(sentenceList)
# for i in sentenceList1:
#     x = cal(i)
#     # print(i, x)
#     posResult1.append(x)
# print(posResult1)
# for i in sentenceList2:
#     x = cal(i)
#     # print(i, x)
#     posResult2.append(x)
# print(posResult2)
# for i in sentenceList3:
#     x = cal(i)
#     # print(i, x)
#     posResult3.append(x)
# print(posResult3)

# 陈述句，一般疑问句，特殊疑问句和条件句
# 1VB开头+？一般疑问句
# 2VB开头+.陈述句
# 3特殊疑问词开头
# 4if...then...
def dealResulSet4(resulSet4):
    nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )
    resulSet4_if = []
    resulSet4_action = []

    for i in resulSet4:
        print(i)
        pl = nlp.pos_tag(i)
        index = 0
        for j in pl:
            if (j[0] == 'if'):
                break
            else:
                index += 1
        if (index > 0):
            ll = i.split(' if')
            If = 'if' + ll[1]
            resulSet4_if.append(If.replace('.', ''))
            Action = ll[0]
            resulSet4_action.append(Action.replace('.', ''))
        else:
            ll = i.split(',')
            If = ll[0]
            resulSet4_if.append(If.replace('.', ''))
            if(len(ll)>1):
                Action = ll[1]
            else:
                Action=""
            resulSet4_action.append(Action.replace('.', ''))

    nlp.close()
    Set4 = []
    Set4.append(resulSet4_if)
    Set4.append(resulSet4_action)

    return Set4