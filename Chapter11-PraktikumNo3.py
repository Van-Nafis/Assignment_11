myfile=open("d:/PythonProjects/Data Peminjaman.txt","r")
from datetime import *
teks=myfile.readlines()
dataMem={}
i=0
for j in teks:
    text=teks[i].split("|")
    x=text[4].split("\n")
    tglMaks=x[0]
    kode=text[0]
    akhir=text[1:4]
    akhir.append(tglMaks)
    i=i+1
    dataMem[kode]=akhir

def diffDate(x):
    z=x.split("-")
    skrg=datetime.now()
    thn=skrg.year-int(z[0])
    bln=abs(skrg.month-int(z[1]))
    hari=abs(skrg.day-int(z[2]))
    selisih=(thn*365)+(bln*30)+(hari)
    return selisih

s=datetime.date(datetime.now())

print("Selamat datang")
print("")
print("Masukan Kode Member\t: ",end="")
kode=input()
print("")
print("Data Peminjaman Buku")
print("Kode Member\t\t: ",end="")
print(kode)
print("Nama Member\t\t: ",end="")
print(dataMem[kode][0])
print("Judul Buku\t\t: ",end="")
print(dataMem[kode][1])
print("Tanggal Pinjam\t\t: ",end="")
print(dataMem[kode][2])
print("Tanggal Maks Pinjam\t: ",end="")
print(dataMem[kode][3])
print("Tanggal Pengembalian\t: ",end="")
print(datetime.date(datetime.now()))
print("Terlambat\t\t: ",end="")
print(diffDate(str(s)))
print("Denda\t\t\t: Rp ",end="")
print(diffDate(str(datetime.date(datetime.now())))*2000)
          
    




