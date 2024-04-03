#soal 2
def ganjil (bawah,atas):
    print(f"bawah = {bawah}, atas = {atas}. Maka hasilnya =")
    if bawah < atas:
        for i in range(bawah, atas+1):
            if i % 2 != 0:
                print(i,end=",")
    else:
        for i in range(bawah, atas-1,-1):
            if i % 2 != 0:
                print(i,end=",")

ganjil(10,30)
ganjil(97,82)