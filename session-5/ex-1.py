def count_a(seq):
    #Counting the number of a's in the sequence
    #Counter for the As
    result = 0
    for i in seq:
        if i == "A":
            result += 1

    #Return the result
    return result

#Main program
s = "AGTACGATCGA"
na = count_a(s)
print("the number of As is: {}".format(na))

#Calculate the total sequence length
tl = len(s)

#Calculate the percentage of As in the sequence
per = round(100.0 * na/ tl, 1)

print("The total length is: {}".format(tl))
print("The percentage of As is: {}%".format(per))