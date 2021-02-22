from PyPDF2 import PdfFileReader, PdfFileWriter

path ='QA.pdf'
pdf =  PdfFileReader(path)

with open('QA.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)
        try:
            txt =  pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            f.write('Page: {0}'.format(page_num+1))
            f.write(txt)
    f.close()