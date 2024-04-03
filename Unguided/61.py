def huruf_angka(kalimat):
    kalimat = str(kalimat).lower()
    kalimat_split = kalimat.split()

    for i in range(len(kalimat_split)):
        for j in kalimat_split[i]:
            if j.isdigit():
                print(kalimat_split[i])  

huruf_angka("test1 test2 test")