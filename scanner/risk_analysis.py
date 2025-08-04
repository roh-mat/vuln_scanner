from fpdf import FPDF
from lxml import etree

def extract_top_findings(openvas_xml, top_n=5):
    tree = etree.parse(openvas_xml)
    results = []
    for result in tree.xpath("//result"):
        severity = float(result.findtext("severity", default="0"))
        name = result.findtext("name")
        description = result.findtext("description", default="No description")
        solution = result.findtext("solution", default="No solution")
        results.append((severity, name, description, solution))
    results.sort(reverse=True)  # Highest severity first
    return results[:top_n]

def generate_risk_report(xml_path, out_path="output/risk_analysis/top_5_findings.pdf"):
    findings = extract_top_findings(xml_path)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Top 5 Security Findings - Risk Report", ln=True)

    for i, (sev, name, desc, sol) in enumerate(findings, 1):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"{i}. {name} [Severity: {sev}]", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 10, f"Description: {desc}")
        pdf.multi_cell(0, 10, f"Remediation: {sol}")
        pdf.ln(5)

    pdf.output(out_path)
