import glob
import pandas
import tabula

pdf_files = glob.glob('*.pdf')
pdf_tables = tabula.read_pdf(pdf_files[1])

