import PyPDF2
pdfFileObj = open('summer.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# returns  the amount of pages
pdfReader.numPages
# were selecting page # 1
pageObj = pdfReader.getPage(0)
# extraction of text
pageObj.extractText()
# closing the document.
pdfFileObj.close()

