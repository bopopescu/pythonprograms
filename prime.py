# start = int(input("enter starting range"))
# end = int(input("enter ending  range"))

for val in range(1,20):
    if val > 1:                                     # If num is divisible by any number
        for n in range(2, val):                # between 2 and val, it is not prime
            if (val % n) == 0:
                break
        else:
            print(val)


