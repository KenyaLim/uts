matkul = int(input("Masukkan berapa mata kuliah :"))
tot_sks = 0
tot_ipk = 0

for i in range(matkul):
    nilai = input(f"Nilai MK kuliah {i+1} :")
    sks = 3

    if nilai == "A":
        ipk = 4 * sks
    elif nilai == "B":
        ipk = 3 * sks
    elif nilai == "C":
        ipk = 2 * sks
    elif nilai == "D":
        ipk = 1 * sks
    else:
        print("SALAH")

    tot_ipk += ipk
    tot_sks += sks

rata = tot_ipk / tot_sks
print(f"Nilai ips anda semester ini :{rata:.2f}")
