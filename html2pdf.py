import pdfkit

for i in range(16, 37):
    pdfkit.from_file(f'./output/30440345/1470968{i}.html', f'./output/{i-16}.pdf')