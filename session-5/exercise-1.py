def count_bases(seq):
    #Counting the number of a's in the sequence
    #Counter for the As
    resA = 0
    resC = 0
    resT = 0
    resG = 0
    for i in seq:
        if i == "A":
            resA += 1
        elif i == "C":
            resC += 1
        elif i == "T":
            resT += 1

    #Return the result
    return result

#Main program
s = input("Type a sequence:  ")
na = count_a(s)
print("the number of As is: {}".format(na))

#Calculate the total sequence length
tl = len(s)

#Calculate the percentage of As in the sequence
if tl > 0:
    per = round(100.0 * na/ tl, 1)
else:
    per = 0

print("The total length is: {}".format(tl))
print("The percentage of As is: {}%".format(per))