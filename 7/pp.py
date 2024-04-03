k = input("Masukkan kalimat = ")
k1 = k.split() # split the input into a list of words

# initialize the shortest and longest words with the first word
p = k1[0]
pp = k1[0]

# iterate over each word in the list
for x in k1:
    # update the shortest and longest words if a shorter or longer word is found
    if len(x) < len(p):
        p = x
    elif len(x) > len(pp):
        pp = x

# print the result
print(f"{p} = terpendek dan {pp} = terpanjang")