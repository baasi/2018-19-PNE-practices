from Seq import Seq

seq1 = Seq("ACTGAATTCTTGC")
seq2 = Seq("CCTGA")
seq3 = str(Seq.complement(seq1))
seq4 = Seq.reversed(seq3)

# Print one by one
# First
print("Sequence is: {}".format(seq1))
print("Length is: {}".format(len(seq1)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(seq1.counting("A"), seq1.counting("C"), seq1.counting("T"), seq1.counting("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(seq1.percentage("A"), seq1.percentage("C"), seq1.percentage("T"), seq1.percentage("G")))

# Second
print("Sequence is: {}".format(seq2))
print("Length is: {}".format(len(seq2)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(seq2.counting("A"), seq2.counting("C"), seq2.counting("T"), seq2.counting("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(seq2.percentage("A"), seq1.percentage("C"), seq2.percentage("T"), seq2.percentage("G")))

# Third
print("Sequence is: {}".format(seq3))
print("Length is: {}".format(len(seq3)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(seq3.counting("A"), seq3.counting("C"), seq3.counting("T"), seq3.counting("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(seq3.percentage("A"), seq3.percentage("C"), seq3.percentage("T"), seq3.percentage("G")))

# Fourth
print("Sequence is: {}".format(seq4))
print("Length is: {}".format(len(seq4)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(seq4.counting("A"), seq4.counting("C"), seq4.counting("T"), seq4.counting("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(seq4.percentage("A"), seq4.percentage("C"), seq4.percentage("T"), seq4.percentage("G")))
