import rwfile
import simhash

sentenlist=rwfile.readfile()
# print(sentenlist)

sentenlist2=rwfile.readfile2("command4.txt")
# print(sentenlist2)


L2=[]
for i in sentenlist2:
    L1 = []
    for j in sentenlist:
        L1.append(simhash.run_simhash(i,j))
    L2.append(L1)
# print(L2)
for i in L2:
    print(i)


MinList=[]
for i in L2:
    Min=min(i)
    index=0
    for j in i:
        if j==Min:
            MinList.append(index)
            break
        index+=1
print(len(MinList))
print(MinList)

index=0
for i in MinList:
#
    print(sentenlist2[index])
    print(sentenlist[i])
    index+=1
    print()
#
#



