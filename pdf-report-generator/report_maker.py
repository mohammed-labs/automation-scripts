import pandas as pd
from fpdf import FPDF

df = pd.read_csv('sales.csv')

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Sales Report", ln=1, align='C')

for i, row in df.iterrows():
    pdf.cell(200, 10, txt=f"{row['Date']} - ${row['Amount']}", ln=1)

pdf.output("report.pdf")
