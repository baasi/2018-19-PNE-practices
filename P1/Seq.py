class sequence:
    #A class for representing sequences
    def  __init__  (self, strbases):
        print("New sequence created!")

        self.strbases = strbases
    def len(self):
        return len(self.strbases)

    def complement(self):
        new = ''
        for i in self.strbases:
            self.strbases = self.strbases.upper()
            if i == 'A':
                new += 'T'
            elif i == 'C':
                new += 'G'
            elif i == 'G':
                new += 'C'
            elif i == 'T':
                new += 'A'
        final = Seq(new)
        return final

    def reversed(self):
        reversed = self.strbases[::-1]
        seq = Seq(reversed)
        return seq


    def counting(self, base):
        self.base = base
        count = self.strbases.count(base)
        return count

    def percentage(self, base):
        self.base = base
        per = round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
        return per


def complement(self):
    dic = {"A": "T", "T": "A", "C": "G", "G": "C"}


lol = [dic.get(n, n) for n in strbases]
return lol
