from fpdf import FPDF

# Sample data file
file_path = "data.txt"

# Read and analyze
with open(file_path, 'r') as f:
    lines = f.readlines()
    word_count = sum(len(line.split()) for line in lines)
    line_count = len(lines)

# Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Text File Report", ln=True, align='C')
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Lines: {line_count}", ln=True)
pdf.cell(200, 10, txt=f"Total Words: {word_count}", ln=True)
pdf.output("report.pdf")