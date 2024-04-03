#soal 1
k1 = (input("Masukan kata 1 ="))#.lower()
k2 = (input("Masukan kata 2 ="))#.lower()
x = sorted(k1)
y = sorted(k2)
if x == y :
    print("Ini anagram")
else:
    print("bukan anagram")