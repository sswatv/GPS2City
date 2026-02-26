smdbfile="uscities.csv"
c2cfile="GPS2City.py"

from csv import reader
coords=[]
names=[]
with open(smdbfile,"r",encoding="utf-8",errors="ignore") as f:
    v=reader(f)
    next(v)
    for r in v:
        coords.append(f"[{r[9]},{r[10]}]")
        names.append(f'"{r[1]}, {r[3]}"')
citycoords="citycoords=["+",".join(coords)+"]"
citynames="citynames=["+",".join(names)+"]"

with open(c2cfile,"r") as f:
    orig=f.read()

with open(c2cfile,"w") as f:
    f.write(citycoords+"\n")
    f.write(citynames+"\n")
    f.write(orig)