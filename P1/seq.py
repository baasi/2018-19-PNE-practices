class Seq:
    #A class for representing sequences
    def  __init__  (self, strbases):
        print("New sequence created!")

        self.strbases = strbases
    def len(self):
        return len(self.strbases)


class Gene(Seq):
    #this class is derived from the seq
    #all the objects of class Gene will inheritage the methods from seq Class
    pass


s1 = Gene("ATTCGATCC")
s2 = Seq("AAACCTTTGG")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

dic = {"A":"T", "T":"A", "C":"G", "G":"C"}
comp1 = [dic.get(n, n) for n in str1]
comp2 = [dic.get(n, n) for n in str2]

rev1 = ''.join(reversed(str1))
rev2 = ''.join(reversed(str2))

a1 = str1.count("A")
c1 = str1.count("C")
g1 = str1.count("G")
t1 = str1.count("T")
a2 = str2.count("A")
c2 = str2.count("C")
g2 = str2.count("G")
t2 = str2.count("T")

perca1 = round(a1 / l1, 2)
percc1 = round(c1 / l1, 2)
percg1 = round(g1 / l1, 2)
perct1 = round(t1 / l1, 2)
perca2 = round(a2 / l2, 2)
percc2 = round(c2 / l2, 2)
percg2 = round(g2 / l2, 2)
perct2 = round(t2 / l2, 2)

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))

print("length: {}".format(l1))
print("length: {}".format(l2))

print("The complementary of seq1 is: {}".format(comp1))
print("The complementary of seq2 is: {}".format(comp2))

print("The reverse of seq1 is {}".format(rev1))
print("The reverse of seq2 is {}".format(rev2))

print("The number of As in seq1 is  {}".format(a1))
print("The number of As in seq2 is  {}".format(a2))
print("The number of Cs in seq1 is  {}".format(c1))
print("The number of Cs in seq2 is  {}".format(c2))
print("The number of Ts in seq1 is  {}".format(t1))
print("The number of Ts in seq2 is  {}".format(t2))
print("The number of Gs in seq1 is  {}".format(g1))
print("The number of Gs in seq2 is  {}".format(g2))

print("The percentage of As in seq1 is {}".format(perca1))
print("The percentage of As in seq2 is {}".format(perca2))
print("The percentage of Cs in seq1 is {}".format(percc1))
print("The percentage of Cs in seq2 is {}".format(percc2))
print("The percentage of Ts in seq1 is {}".format(perct1))
print("The percentage of Ts in seq2 is {}".format(perct2))
print("The percentage of Gs in seq1 is {}".format(percg1))
print("The percentage of Gs in seq2 is {}".format(percg2))