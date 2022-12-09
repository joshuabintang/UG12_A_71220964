masukkan_sebuah_kalimat = input("masukkan nama:")
muncul=0
for i in range(len(masukkan_sebuah_kalimat)):
    muncul +=1
    print(masukkan_sebuah_kalimat[:muncul])
for i in range(len(masukkan_sebuah_kalimat)):
    muncul -=1
    print(masukkan_sebuah_kalimat[:muncul])