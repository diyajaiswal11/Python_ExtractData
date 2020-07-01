print("Hiii")
import PyPDF2 as p2
PDFfile=open('AGK.pdf','rb')
pdfread=p2.PdfFileReader(PDFfile)
x=pdfread.getPage(2)
print(x.extractText())