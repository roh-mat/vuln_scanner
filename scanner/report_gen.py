from fpdf import FPDF

import os

def generate_combined_report(nmap_data_path, openvas_data_path):
    os.makedirs("output/reports", exist_ok=True)

    with open(nmap_data_path, "r") as f:
        nmap_data = f.read()

    with open(openvas_data_path, "r") as f:
        openvas_data = f.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Combined Nmap + OpenVAS Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Nmap Scan Output", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 8, nmap_data[:5000])  # Limit output size

    pdf.add_page()
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "OpenVAS Scan Output", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 8, openvas_data[:5000])

    pdf.output("output/reports/combined_scan_report.pdf")
