#!/usr/bin/env python3

import sys

try:
    gzje = int(float(sys.argv[1]))
except:
    print("Parameter Error")
    
ynssdr = gzje - 3500
if ynssdr > 80000:
    ynse = ynssdr * 0.45 -13505
elif ynssdr > 55000:
    ynse = ynssdr * 0.35 - 5505
elif ynssdr > 35000:
    ynse = ynssdr * 0.30 -2755
elif ynssdr > 9000:
    ynse = ynssdr * 0.25 -1005
elif ynssdr > 4500:
    ynse = ynssdr * 0.20 -555
elif ynssdr > 1500:
    ynse = ynssdr * 0.10 -105
elif ynssdr > 0:
    ynse = ynssdr * 0.03
else:
    ynse = 0
print('{:.2f}'.format(ynse))
