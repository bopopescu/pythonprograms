result_str=""
for row in range(0,5):
    for column in range(0,5):
        if (column == 0 or column == 4) or ((row == 0 or row == 4) and (column > 0 and column < 4)):
            # print(((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5)),end=" ")
            # print("row {}".format(row),end=" ")
            # print("column {}".format(column))
            # print("*",end=" ")
            result_str+="*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)



