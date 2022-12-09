batas=int(input("masukkan pembatas:"))
larang=int(input("masukkan angka yang dilarang"))
for i in range(batas):
    if i == larang:
        continue
    print(i, end=' ')