from datetime import *
def diffDate(x):
    z=x.split("-")
    skrg=datetime.now()
    thn=skrg.year-int(z[0])
    bln=abs(skrg.month-int(z[1]))
    hari=abs(skrg.day-int(z[2]))
    selisih=(thn*365)+(bln*30)+(hari)
    print("Selisihnya : ",selisih,"Hari")
    

print("Masukan Tanggal (YYYY-MM-DD) : ",end="")
j=input()
y=str(j)

diffDate(y)
