seq = input("Type a dna sequence: ")
seql = seq.lower()
if seql.isalpha():
    for i in seql:
        if not (i=="a" or i=="c" or i=="t" or i=="g"):
            seql = seql.replace(i, "")
        else:
            print("only A, C, T, G are valid")
    cnt = len(seql)
    a = seql.count("a")
    c = seql.count("c")
    g = seql.count("g")
    t = seql.count("t")
    print("Total length is", cnt)
    print("A:", a)
    print("C:", c)
    print("T:", t)
    print("G:", g)
else:
    print(("not valid, type only letters please"))

