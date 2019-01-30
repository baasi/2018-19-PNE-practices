l = []

with open("CPLX2.txt", 'r') as f:
    for i in f:
        if not (i == 'A' or i == 'T' or i == 'G' or i=='C'):
            i2 = i.replace(i, "")
    for line in i2:
        l.append(line)
    str1 = "".join(l)
    str2 = str1.strip("\n").replace('"', '').split(",")


    a = str2.count("A")
    c = str2.count("C")
    t = str2.count("T")
    g = str2.count("G")
    print(a, t, c, g)




