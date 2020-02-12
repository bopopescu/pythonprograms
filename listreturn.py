# def l(li):
# #     f=li[0]
# #     l=li[-1]
# #     if f==l:
# #         return True
# #     else:
# #         return False
# # lis=[4,2,3,4]
# # print(l(lis))
def l(li):
    flag=0
    for i in li:
        if i % 5 == 0:
            print(i)
        else:
             print("not divisible")
lis = [10, 20,30,24,23,67]
l(lis)
