import os
from PyPDF2 import PdfFileReader

f_path = 'Files/'

directory = os.fsencode(f_path)

files = []


for file in os.listdir(directory):
     filename = os.fsdecode(file)
     pdf = PdfFileReader(open(f_path + filename,'rb'))
     print (filename+', '+str(pdf.getNumPages()))
     files.append(filename+', '+str(pdf.getNumPages()))


f = open ("output.txt", "w")

for val in files:
    f.write (val+"\n")

f.close()
