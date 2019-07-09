import numpy as np


def calculateVec(sentence, words, d, Vecs):
    s = sentence.split(" ")
    index = []
    for i in s:
        count = 0
        for j in words:
            count = count + 1
            if i == j:
                index.append(count)
    index.sort()
    x = []

    for i in range(d):
        x.append(0.0)
    y = np.array(x)
    for i in index:
        y = y + Vecs[i - 1]
    # print(y)
    return y / len(s)


def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


vecfile = open('txt/50d.txt', 'r', encoding='utf-8')

vecMat = []
Vecs = []
for line in vecfile.readlines():
    curLine = line.strip().split(" ")
    vecMat.append(curLine[:])

words = []
for i in vecMat:
    tempVec = 0.0
    words.append(i[0])
    # vec单个向量
    vec = map(float, i[1:])
    vecs = list(vec)
    Vecs.append(vecs)
# sentence1="if temperature of sitting room is below 18 degrees"
# sentence2="if the temperature in the sitting room is higher than x"
# sentence3="if the temperature in the sitting room is below x"

# sentence1="if the temperature in the sitting room is under x"
# sentence2="if the temperature in the sitting room is below x"
# sentence3="if the temperature in the sitting room is less than x"
# sentence4="if the temperature in the sitting room is lower than x"
# sentence5="if the temperature in the sitting room is above x"
# sentence6="if the temperature in the sitting room is higher than x"

# sentence1="If the sitting room is brighter than x"
# sentence2="if the brightness in the sitting room is below x"
# sentence3="if the brightness in the sitting room is less than x"
# sentence4="if the brightness of the sitting room is lower than x"
# sentence5="if the brightness in the sitting room is above x"
# sentence6="if the brightness in the sitting room is higher than x"
# sentence7="if the brightness in the sitting room is more than x"
# sentence8="if the brightness in the sitting room is between x and y"

# sentence1="turn up the brightness of sitting room ."
# sentence2="monitor the brightness of sitting room ."
# sentence3="increase the brightness of sitting room ."
# sentence4="assign the brightness of sitting room ."
# sentence5="reduce the brightness of sitting room ."
# sentence6="set the brightness of the smart light in the sitting room to x ."
# sentence7="turn on the smart light in the sitting room ."


# sentence1="is the air purifier working ?"
# sentence2="is the air purifier on ?"
# sentence3="is the air purifier off ?"
# sentence4="is the air conditioner on ?"
# sentence5="is the air conditioner off ?"

# sentence1="is the air cleaner on ?"
#
# sentence2="is the air conditioner on ?"
# sentence3="is the air conditioner off ?"
# sentence4="is the air purifier on ?"
# sentence5="is the air purifier off ?"


# sentence1="if the brightness in the sitting room is between 23 and 30 "
# sentence2="if the brightness in the sitting room is below x"
# sentence3="if the brightness in the sitting room is above x"
# sentence4="if the brightness in the sitting room is more than x"
# sentence5="if the brightness in the sitting room is higher than x"
# sentence6="if the brightness in the sitting room is lower than x"




# s = "shut down the air detector in the sitting room .shut down the pm2.5 monitor in the sitting room . turn off the air conditioner in the sitting room . turn on the air conditioner in the sitting room . shut down the air conditioner in the sitting room . shut down the air purifier in the sitting room ."
# s="turn up the air-conditioning of living room .turn the pm2.5 of the pm2.5 monitor in the sitting room to x . shut down the smart light in the sitting room . turn on the smart light in the sitting room . monitor the pm2.5 of sitting room . reduce the pm2.5 of sitting room . "
# s="open the air conditioner in the sitting room .shut down the air conditioner in the sitting room .turn off the air conditioner in the sitting room . turn on the air conditioner in the sitting room . open the air purifier in the sitting room . open the air conditioner in the sitting room . "
# s= "turn down the brightness of sitting room .set the brightness of sitting room to x . monitor the brightness of sitting room . increase the brightness of sitting room . turn the brightness of the smart light in the sitting room to x . "
# s=" assign the brightness of sitting room .increase the brightness of sitting room . reduce the brightness of sitting room . assign the temperature of sitting room . monitor the brightness of sitting room . assign the brightness of sitting room . "
# s="turn the pm2.5 of the air purifier in the sitting room to 12 . turn on the air conditioner in the sitting room .turn off the air purifier in the sitting room . set the pm2.5 of the air purifier in the sitting room to x .turn the pm2.5 of the air purifier in the sitting room to x .turn on the air purifier in the sitting room ."
# s="How many degrees centigrade in the living room ? what is the status of the air conditioner ? what is the pm2.5 in the sitting room ? what is the temperature of the air conditioner ? what is the brightness in the sitting room ? what is the temperature in the sitting room ? "
s="turn up the brightness of sitting room .set the brightness of sitting room to x .monitor the brightness of sitting room .turn the brightness of the smart light in the sitting room to x .increase the brightness of sitting room . reduce the brightness of sitting room . "
# 0.988119208521711
# 0.988673399725523
# 0.9889678673895722
# 0.9890827630495018
# 0.9565488516391015
# 操作6不太正常，7正常


sl=[]
d="."
sl=s.split(d)

print(sl)
sentence1 = sl[0]+d
sentence2 = sl[1]+d
sentence3 = sl[2]+d
sentence4 = sl[3]+d
sentence5 = sl[4]+d
sentence6 = sl[5]+d
v1 = calculateVec(sentence1, words, len(vecMat[0]) - 1, Vecs)
v2 = calculateVec(sentence2, words, len(vecMat[0]) - 1, Vecs)
v3 = calculateVec(sentence3, words, len(vecMat[0]) - 1, Vecs)
v4 = calculateVec(sentence4, words, len(vecMat[0]) - 1, Vecs)
v5 = calculateVec(sentence5, words, len(vecMat[0]) - 1, Vecs)
v6 = calculateVec(sentence6, words, len(vecMat[0]) - 1, Vecs)
# v7 = calculateVec(sentence7, words, len(vecMat[0]) - 1, Vecs)
# v8 = calculateVec(sentence8, words, len(vecMat[0]) - 1, Vecs)

# print(v1)
# print(v2)

print(cos_sim(v1, v2))
print(cos_sim(v1, v3))
print(cos_sim(v1, v4))
print(cos_sim(v1, v5))
print(cos_sim(v1, v6))
# print(cos_sim(v1, v7))
# print(cos_sim(v1, v8))
