class Seq:
    #A class for representing sequences
    def  __init__  (self, strbases):

        self.strbases = strbases
    def len(self):
        return len(self.strbases)

    def complement(self):
        dic = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comple = [dic.get(n, n) for n in self.strbases]
        return comple

    def reversed(self):
        reverse = self.strbases[::-1]
        seq = Seq(reverse)
        return seq


    def counting(self, base):
        self.base = base
        count = self.strbases.count(base)
        return count

    def percentage(self, base):
        self.base = base
        per = round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
        return per


