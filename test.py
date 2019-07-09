#!/usr/bin/python3
import numpy as np

print("Hello, World!")
# data = []
# for line in open("words.txt","r"): #设置文件对象并读取每一行文件
#     data.append(line.strip('\n').split(','))               #将每一行文件加入到list中
# print(data[0])
# # list1=[]
# # with open('words.txt', 'r') as f1:
# #     list1 = f1.readlines()
# # for i in range(0, len(list1)):
# #     list1[i] = list1[i].rstrip('\n')
# # list11=[]
# # print(list1)
# #
# # for i in list1:
# #     list11.append(i.strip(' ').split(','))
# # print(list11)
# # list12=[]
# #
# # for i in list11:
# #     print(i)
#
#
#
#
# # data2=[]
# data2= np.loadtxt("words.txt")   #将文件中数据加载到data数组里
# print(data2)
# with open("50d.txt","r",encoding= 'utf-8') as file:
#     result=[]
#     for line in file.readlines():
#         result.append(list(map(str,line.strip().split(','))))
#
#
# #
#     words=[]
#     file1 = open('50dd.txt', 'w',encoding= 'utf-8')
#     for i in result:
#         for j in i:
#             k=j[j.find(" ")+1:]
#             words.append(j[:j.find(" ")+1])
#             # print(k)
#             file1.write(k + '\n')
#     file1.close()
#     # print(words)
#
#     file2 = open('50dd.txt', 'r',encoding= 'utf-8')
#     dataMat = []
#     labelMat = []
#     for line in file2.readlines():
#         curLine = line.strip().split(" ")
#         floatLine = list(map(float, curLine))  # 这里使用的是map函数直接把数据转化成为float类型
#         dataMat.append(floatLine[:])
#     p=0.0
#     for i in dataMat:
#         # print(i)
#         for j in i:
#             # print(j)
#             p=p+j;
#         print(p)

file2 = open('50d.txt', 'r',encoding='utf-8')

dataMat = []
pp=[]
#     labelMat = []
for line in file2.readlines():
    curLine = line.strip().split(" ")
        # floatLine = list(map(float, curLine))  # 这里使用的是map函数直接把数据转化成为float类型
    dataMat.append(curLine[:])

# print(dataMat)
words=[]
for i in dataMat:
    p=0.0
    words.append(i[0])
    k=map(float,i[1:])
    kk=list(k)
    pp.append(kk)
    for j in kk:
        p=p+j

# sentence1="turn on the light"
# sentence2="what is the temperature in the living room"
sentence1="turn up the air conditioner in sitting room"
sentence2="what is the status of the smart light"
ss1=sentence1.split(" ")
ss2=sentence2.split(" ")
# print(ss1)
index1=[]
for i in ss1 :
    count=0
    for j in words:
        count=count+1
        if i==j:
            print(j)
            print(count)
            index1.append(count)

index1.sort()
print(index1)


x=[]
for i in range(50):
    x.append(0.0)
y=np.array(x)
for i in index1:
    y = y + np.array(pp[i-1])
    print(np.array(pp[i-1]),"------")
    print(y)

print(y)



