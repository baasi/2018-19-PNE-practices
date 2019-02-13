def count_bases(seq):

    result = {"A": 0, "C": 0, "G": 0, "T":0}
    for key in result:
        result[key] = seq.count(key)

    return result