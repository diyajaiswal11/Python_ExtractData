import PyPDF2 as p2

pdffile=open('AGK.pdf','rb')
pdfread=p2.PdfFileReader(pdffile)

#TO EXTRACT SINGLE PAGE DATA
"""
x=pdfread.getPage(10)
print(x.extractText())
"""


#TO EXTRACT ENTIRE PDF'S DATA

i=0
while i<pdfread.getNumPages():
    pginfo=pdfread.getPage(i)
    print(pginfo.extractText())
    i=i+1
