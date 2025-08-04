from fpdf import FPDF

def generate_report(nmap_data, openvas_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Scan Report", ln=True, align='C')

    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="--- Nmap Results ---\n" + nmap_data)

    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="--- OpenVAS Results ---\n" + openvas_data)

    pdf.output("output/final_report.pdf")
