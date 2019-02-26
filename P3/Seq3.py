class Seq:
    #A class for representing sequences
    def  __init__  (self, strbases):

        self.strbases = strbases
    def len(self):
        return len(self.strbases)

    def complement(self):
        word = ''
        for letter in self.strbases:
            self.strbases = self.strbases.upper()
            if letter == 'A':
                word += 'T'
            elif letter == 'C':
                word += 'G'
            elif letter == 'G':
                word += 'C'
            elif letter == 'T':
                word += 'A'
        c = Seq(word)
        return c

    def reversed(self):
        se = self.strbases[::-1]
        seq = Seq(se)
        return seq


    def counting(self, base):
        self.base = base
        count = self.strbases.count(base)
        return count

    def percentage(self, base):
        self.base = base
        per = round(100.0 * self.strbases.count(base) / len(self.strbases), 2)
        return per

