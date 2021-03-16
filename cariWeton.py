from datetime import date

patokan = date(1900, 1, 1) #tanggal patokan untuk kalender jawa

hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

weton = ['Pahing', 'Pon', 'Wage', 'Kliwon', 'Legi'] 

tgl = input("Masukkan tanggal lahir anda: ")
bln = input("Masukkan bulan lahir anda: ")
thn = input("Masukkan tahun lahir anda: ")

lahir = date(int(thn), int(bln), int(tgl))

selisih = lahir - patokan

index_hari = selisih.days % 7
index_weton = selisih.days % 5

hari_lahir = hari[index_hari]
weton_lahir = weton[index_weton]

print("")
print("Anda lahir pada hari: " + str(hari_lahir) , (weton_lahir))
print("")
