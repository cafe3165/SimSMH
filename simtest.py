#!/usr/bin/python3
import numpy as np
import numpytest


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

# sentence1 = "turn on the light"
# # sentence2="what is the temperature in the living room"
# # sentence2="turn on the light"
# # sentence2="turn on the air conditioner"
# # sentence2="open the light"
# sentence2 = "shut the light down"
sentence1="if the brightness in the sitting room is between 23 and 30 "
sentence2="if the brightness in the sitting room is lower than x"
sentence3="if the brightness in the sitting room is between x and y"

v1 = calculateVec(sentence1, words, len(vecMat[0]) - 1, Vecs)
v2 = calculateVec(sentence2, words, len(vecMat[0]) - 1, Vecs)
v3 = calculateVec(sentence3, words, len(vecMat[0]) - 1, Vecs)

print(v1)
print(v2)

print(cos_sim(v1, v2))
print(cos_sim(v1, v3))
