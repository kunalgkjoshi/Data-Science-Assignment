def string_features(S1, S2):
    S1_words = set(S1.split(" "))
    S2_words = set(S2.split(" "))

    a = len(S1_words.intersection(S2_words))
    b = list(S1_words - S2_words)
    c = list(S2_words - S1_words)

    return a, b, c


S1 = "the first column F will contain only 5 uniques values"
S2 = "the second column S will contain only 3 uniques values"

a, b, c = string_features(S1, S2)
print(a)
print(b)
print(c)