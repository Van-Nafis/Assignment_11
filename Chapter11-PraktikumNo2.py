from datetime import *
myfile=open("D:/PythonProjects/Data Peminjaman.txt","w")

def addMember(kodeM,namaM,jdlBuku,tglPinjam,tglMaks):
    myfile.write(kodeM)
    myfile.write("|")
    myfile.write(namaM)
    myfile.write("|")
    myfile.write(jdlBuku)
    myfile.write("|")
    myfile.write(str(tglPinjam))
    myfile.write("|")
    myfile.write(str(tglMaks))
    myfile.write("\n")


while True:
    print("Masukan Kode Member\t  : ",end="")
    kodeM=input()
    
    print("Masukan Nama Member\t  : ",end="")
    namaM=input()
    
    print("Masukan Judul Buku\t  : ",end="")
    jdlBuku=input()

    tglPinjam=datetime.date(datetime.now())
    tglMaks=tglPinjam+timedelta(days=7)

    addMember(kodeM,namaM,jdlBuku,tglPinjam,tglMaks)

    print("")
    print("Ulangi lagi (y/n) : ",end="")
    tanya=input()
    print("")
    if tanya=="n":
        break

myfile.close()

