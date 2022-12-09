nilai_awal = int(input('nilai_awal:'))
nilai_akhir = int(input('nilai_akhir:'))
for i in range(nilai_awal,nilai_akhir):
    if i%3!=0 and i%6!=0 and i%2!=0:
        print (i,end="\t")
        i = i + 1