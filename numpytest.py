# import rwfile
import GenCompare

#
# sl = rwfile.stReadFile('txt/resulSet1.txt')
# # print(sl)
#
# filer = open('txt/result0614-1.txt', 'r', encoding='utf-8')
# # file2=open('command4.txt', 'r', encoding='utf-8')
# # cl = rwfile.readfile2()
# cl=rwfile.stReadFile('txt/set1-sentence-1.txt')
# print(cl)
# l1 = []
# l2 = []
# for line in filer.readlines():
#     curLine = line.strip().split(" ")
#     l2.append(list(map(int, curLine)))
#     # print(list(map(int,curLine)))
# print(l2)
# index = 0
# filetest = open(r'txt/com0614-set1-1.txt', 'w')
# filetest2 = open(r'txt/sim0614-1.txt', 'r')
#
# ll = []
# for line in filetest2.readlines():
#     curLine = line.strip().split(" ")
#     ll.append(list(map(float, curLine)))
#
# print(ll)
# llindex=0
# print(len(ll))
# for i in l2:
#     # print(cl[index])
#     filetest.write(cl[index])
#     filetest.write('\n')
#     # print(ll[llindex])
#     li=0
#     for j in i:
#         print(sl[j],ll[llindex][li])
#         filetest.write(sl[j])
#         filetest.write(' ')
#         filetest.write(str(ll[llindex][li])[:6])
#         filetest.write('\n')
#         li+=1
#     llindex+=1
#     print('\n')
#     filetest.write('\n')
#     index+=1
# #

# GenCompare.Gen('txt/resulSet1.txt','txt/result0614-1.txt','txt/set1-sentence-1.txt','txt/com0614-set1-1.txt','txt/sim0614-1.txt')
# GenCompare.Gen('txt/resulSet2.txt','txt/result0614-2.txt','txt/set1-sentence-2.txt','txt/com0614-set1-2.txt','txt/sim0614-2.txt')
# GenCompare.Gen('txt/resulSet3.txt','txt/result0614-3.txt','txt/set1-sentence-3.txt','txt/com0614-set1-3.txt','txt/sim0614-3.txt')
# GenCompare.Gen('txt/resulSet4.txt','txt/result0614-4.txt','txt/set1-sentence-4_if.txt','txt/com0614-set1-4_if.txt','txt/sim0614-4.txt')
# GenCompare.Gen('txt/resulSet4.txt','txt/result0614-4.txt','txt/set1-sentence-4_action.txt','txt/com0614-set1-4.txt','txt/sim0614-4_if.txt')

# GenCompare.Gen('txt/resulSet1.txt','txt/result-set2-0614-1.txt','txt/set2-sentence-1.txt','txt/com0614-set2-1.txt','txt/sim0614-set2-1.txt')
# GenCompare.Gen('txt/resulSet2.txt','txt/result-set2-0614-2.txt','txt/set2-sentence-2.txt','txt/com0614-set2-2.txt','txt/sim0614-set2-2.txt')
# GenCompare.Gen('txt/resulSet3.txt','txt/result-set2-0614-3.txt','txt/set2-sentence-3.txt','txt/com0614-set2-3.txt','txt/sim0614-set2-3.txt')
# GenCompare.Gen('txt/resulSet4.txt','txt/result-set2-0614-4.txt','txt/set2-sentence-4_if.txt','txt/com0614-set2-4_if.txt','txt/sim0614-set2-4.txt')
# GenCompare.Gen('txt/resulSet4.txt','txt/result-set2-0614-4.txt','txt/set2-sentence-4_action.txt','txt/com0614-set2-4.txt','txt/sim0614-set2-4.txt')


# GenCompare.Gen('txt/original-resultSet1.txt', 'txt/original-result-set1-0614-1.txt', 'txt/original-set1-sentence-1.txt',
#                'txt/original-com0614-set1-1.txt', 'txt/original-sim0614-set1-1.txt')
# GenCompare.Gen('txt/original-resultSet2.txt', 'txt/original-result-set1-0614-2.txt', 'txt/original-set1-sentence-2.txt',
#                'txt/original-com0614-set1-2.txt', 'txt/original-sim0614-set1-2.txt')
# GenCompare.Gen('txt/original-resultSet3.txt', 'txt/original-result-set1-0614-3.txt', 'txt/original-set1-sentence-3.txt',
#                'txt/original-com0614-set1-3.txt', 'txt/original-sim0614-set1-3.txt')
# GenCompare.Gen('txt/original-resultSet4.txt', 'txt/original-result-set1-0614-4.txt',
#                'txt/original-set1-sentence-4_if.txt', 'txt/original-com0614-set1-4_if.txt',
#                'txt/original-sim0614-set1-4.txt')


# GenCompare.Gen('txt/original-resultSet1.txt', 'txt/original-result-set2-0614-1.txt', 'txt/original-set2-sentence-1.txt',
#                'txt/original-com0614-set2-1.txt', 'txt/original-sim0614-set2-1.txt')
# GenCompare.Gen('txt/original-resultSet2.txt', 'txt/original-result-set2-0614-2.txt', 'txt/original-set2-sentence-2.txt',
#                'txt/original-com0614-set2-2.txt', 'txt/original-sim0614-set2-2.txt')
# GenCompare.Gen('txt/original-resultSet3.txt', 'txt/original-result-set2-0614-3.txt', 'txt/original-set2-sentence-3.txt',
#                'txt/original-com0614-set2-3.txt', 'txt/original-sim0614-set2-3.txt')
# GenCompare.Gen('txt/original-resultSet4.txt', 'txt/original-result-set2-0614-4.txt',
#                'txt/original-set2-sentence-4_if.txt', 'txt/original-com0614-set2-4_if.txt',
#                'txt/original-sim0614-set2-4.txt')

GenCompare.Gen('txt2/resultSet1-0701.txt', 'txt2/result0701-set1-1.txt', 'txt2/set1-sentence-1.txt',
               'txt2/com0701-set1-1.txt', 'txt2/sim0701-set1-1.txt')
GenCompare.Gen('txt2/resultSet2-0701.txt', 'txt2/result0701-set1-2.txt', 'txt2/set1-sentence-2.txt',
               'txt2/com0701-set1-2.txt', 'txt2/sim0701-set1-2.txt')
GenCompare.Gen('txt2/resultSet3-0701.txt', 'txt2/result0701-set1-3.txt', 'txt2/set1-sentence-3.txt',
               'txt2/com0701-set1-3.txt', 'txt2/sim0701-set1-3.txt')
GenCompare.Gen('txt2/resultSet4-0701.txt', 'txt2/result0701-set1_if.txt', 'txt2/set1-sentence-4_if.txt',
               'txt2/com0701-set1-4_if.txt', 'txt2/sim0701-set1-4.txt')

# GenCompare.Gen('txt2/resultSet1-0701.txt', 'txt2/result0701-set2-1.txt', 'txt2/set2-sentence-1.txt',
#                'txt2/com0701-set2-1.txt', 'txt2/sim0701-set2-1.txt')
# GenCompare.Gen('txt2/resultSet2-0701.txt', 'txt2/result0701-set2-2.txt', 'txt2/set2-sentence-2.txt',
#                'txt2/com0701-set2-2.txt', 'txt2/sim0701-set2-2.txt')
# GenCompare.Gen('txt2/resultSet3-0701.txt', 'txt2/result0701-set2-3.txt', 'txt2/set2-sentence-3.txt',
#                'txt2/com0701-set2-3.txt', 'txt2/sim0701-set2-3.txt')
# GenCompare.Gen('txt2/resultSet4-0701.txt', 'txt2/result0701-set2-4.txt', 'txt2/set2-sentence-4_if.txt',
#                'txt2/com0701-set2-4_if.txt', 'txt2/sim0701-set2-4.txt')