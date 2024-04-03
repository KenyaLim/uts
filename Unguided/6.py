def berurutan(kata):
    kata = kata.lower()
    k = ""
    for i in kata:
        if i not in k:
            k += i
    print(k)

berurutan("AAAAABBBBBBCCCCCEEEEEEEEEAAAAAAAAAAAAAA")