

import sys
from scipy.spatial import KDTree
from serial import Serial

def rmctocoords(line):
    p=line.split(",")
    lat=(int(p[3][:2])+float(p[3][2:])/60)
    lon=(int(p[5][:3])+float(p[5][3:])/60)
    if p[4]!="N": lat=-lat
    if p[6]!="E": lon=-lon
    return lat,lon

tree=KDTree(citycoords)
if len(sys.argv)==3:
    gps=Serial(sys.argv[2],4800)
    with open(sys.argv[1],"w") as f:
        while True:
            try:
                line=gps.readline().decode("utf-8",errors="ignore")
                if line.startswith("$GPRMC"):
                    lat,lon=rmctocoords(line)
                    closest=citynames[tree.query([lat,lon],p=2)[1]]
                    f.seek(0)
                    f.write(closest)
                    f.truncate()
                    f.flush()
            except:
                pass
else:
    sys.exit("GPS2City.exe outputFile serialPort")