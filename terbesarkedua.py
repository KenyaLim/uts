def angka_terbesar_kedua(list_angka):
    if len(list_angka) < 2:
        return "List harus memiliki setidaknya dua angka"
    
    max1 = max2 = float('-inf')
    for num in list_angka:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
            
    if max2 == float('-inf'):
        return "Tidak ada angka terbesar kedua"
    else:
        return max2

# Contoh penggunaan:
angka = [1, 3, 4, 5, 6, 7]
print(angka_terbesar_kedua(angka))
