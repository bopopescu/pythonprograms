list=[1,2,3,4,1,1,3,7,8,9,2,3]
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)