import PyPDF2
pdfFile = open('nombreArchivo.pdf')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfReader.numPages

pageObj = pdfReader.getPage(0)

pageObj.extract_text()

pdfFile.close()