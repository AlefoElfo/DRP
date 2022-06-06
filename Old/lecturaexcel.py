from excel import OpenExcel
import sys
import excel





f = OpenExcel('Definiciones2003.xls')
f.read()  # read all
#f.read('A')  # read 'A' row
#f.read(1)  # f.read('1'), read '1' column

m=f.read('A5')  # read 'A5' position

print (m)






