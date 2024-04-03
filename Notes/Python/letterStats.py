
def test():
    text = input("Type something in ")
    print(text)

    counts = dict()

    for c in text:
        counts[c] = counts.getkey(c) + 1
    print(counts)
