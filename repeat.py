# def last2(str):
#   return len([i for i in range(len(str) - 2) if str[i:i+2] == str[-2:]])
# x=last2("jasna is jasna")
# print(x)


def count_sub(substr, string):
pos = string.find(substr)
if pos == -1:
return 0
return 1+count_sub(substr, string[pos+len(substr):])