dict_1={
    "user_1":input("enter a name"),
    "age_1":input("enter a age")}
dict_2={
    "user_2":input("enter a name"),
    "age_2":input("enter a age")}
list1=[]
list1.append(dict_1)
list1.append(dict_2)
print(list1)
# print(list1[0]["user_1"])
# print(type(list1[0]))
name_tomatch=input("enter a name")
flag=0
for i in list1:
    for key,values in dict_1.items():
        for key,values in dict_2.items():
            if (dict_1["user_1"]==name_tomatch) or (dict_2["user_2"]==name_tomatch):
                flag=1
if flag==1:
    print("names are matching")
else:
    print("do not match")
# flag=0
# for i in list1:
#     for key,values in dict_1.items():
#         if dict_1["user_1"]==name_tomatch:
#             flag=1
#     if flag==1:
#         print(i)
#     else:
#         print("do not match")