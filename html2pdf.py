import pdfkit
from PyPDF2 import PdfMerger

# for i in range(16, 37):
#     pdfkit.from_file(f'./output/30440345/1470968{i}.html', f'./output/{i-16}.pdf')

pdfs = [f'./output/{i}.pdf' for i in range(0, 21)]
file_merger = PdfMerger()
for pdf in pdfs:
    file_merger.append(pdf)

file_merger.write('./output/total.pdf')