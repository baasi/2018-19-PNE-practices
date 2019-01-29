def sumn(n):
    tot = 0
    for elem in range(n):
        tot = tot + 1 + n
    return tot


num = int(input("Type a number:"))
total = sumn(num)
print("total num is {}".format(total))