# Membersihkan Terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Membuat Dictionary Kosong
data_buku = {}

# Membuka File Text dengan kondisi with
with open('Open_Library.txt', 'r') as f:
    for i in f: #iterasi file open_library (perbaris )yang sudah di simplifikasi menjadi variabel f
        line_list = i.split() #memasukan i kedalam list agar mempermudah untuk memasukan f ke dictionary
        buku = data_buku[line_list[0]] = {} #membuat Subdictionary di dalam key ISBN
        # value dari key ISBN
        buku['Jumlah Buku'] = line_list[1]
        buku['Total Peminjaman'] = (int(line_list[2]) + int(line_list[3]) + int(line_list[4]) 
                                   + int(line_list[5]) + int(line_list[6]) +int(line_list[7]))

# Membuat Fungsi buku favorit yang diukur dari total peminjaman terbanyak
def favorit(n):
    # membuat list kosong untuk ISBN dan Total Peminjaman
    key_list = []
    value_list = []
    # Iterasi file n dengan lalu dimasukan pada list kosong sesuai dengan fungsinya
    for k, v in n.items():
        key_list.append(k)
        value_list.append((v['Total Peminjaman'])) 
    maks = int(max(value_list)) # menghitung nilai maksimal dari value["Total Peminjaman"] file n
    buku_maks = key_list[value_list.index(maks)] # mencari ISBN yang memiliki total peminjaman terbanyak dari index value_list
    print("Buku yang paling banyak dipinjam dalam satu minggu adalah buku dengan ISBN",buku_maks,"dengan total",maks,"peminjaman") #Output  

# Membuat fungsi untuk mencari buku dengan total peminjaman sama dengan jumlah stoknya
def laporan_stok(n):
    print("Buku dengan total peminjaman dalam satu minggu sama dengan jumlah stoknya:")
    # Iterasi file n
    for k,v in n.items():
        # Membuat pengkondisian dimana jika total peminjaman sama dengan jumlah buku maka eksekusi output di line-38
        if int(v["Total Peminjaman"]) == int(v["Jumlah Buku"]):
            print("- ISBN:",k,"  Stok Buku:",v["Jumlah Buku"])

# Pemanggilan fungsi dan output dari dictionary
print("\n============================== DICTIONARY ==============================")
print(data_buku)
print("\n===========================  BUKU TERFAVORIT ==============================")
favorit(data_buku)
print("\n============================= LAPORAN STOK ==============================")
laporan_stok(data_buku)
print()