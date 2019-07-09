#!/usr/bin/python3
import numpy as np


def calculateVec(sentence, words, d, vecs):
    s = sentence.split(" ")
    index = []
    for i in s:
        count = 0
        for j in words:
            count +=1
            if i == j:
                index.append(count)
    index.sort()
    print(index)
    # for i in index:
    #     print(words[i-1])
    x = []

    for i in range(d):
        x.append(0.0)
    y = np.array(x)
    for i in index:
        # print(y)
        # print(vecs[i-1])
        y = y + vecs[i - 1]
    # print(y)
    return y


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

def calculate(dname,sentence):
    vecfile = open(dname, 'r', encoding='utf-8')
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

    # for i in Vecs:
    #     print(i)
    # print(words)
    # print(len(vecMat[0]) - 1)
    v=calculateVec(sentence, words, len(vecMat[0]) - 1, Vecs)
    return v




