import argparse
from scanner.nmap_scan import run_nmap
from scanner.openvas_scan import run_openvas
from scanner.report_gen import generate_combined_report
from scanner.risk_analysis import generate_risk_report

def read_file(path):
    with open(path) as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Nmap + OpenVAS Vulnerability Scanner")
    parser.add_argument('--target', required=True, help="Target IP address or domain")
    parser.add_argument('--output', choices=['pdf', 'txt', 'json'], default='pdf', help="Output report type")

    args = parser.parse_args()
    target = args.target
    output_type = args.output

    print(f"[+] Scanning target: {target}")

    # Step 1: Run Nmap
    nmap_xml_path = run_nmap(target)

    # Step 2: Run OpenVAS
    openvas_xml_path = run_openvas(target)

    # Step 3: Generate final report(s)
    if output_type == "pdf":
        print("[+] Generating combined PDF report...")
        generate_combined_report(nmap_xml_path, openvas_xml_path)
        generate_risk_report(openvas_xml_path)
        print("[+] PDF reports saved in /output/reports and /output/risk_analysis/")
    elif output_type == "txt":
        print("[+] TODO: Add TXT output support")
    elif output_type == "json":
        print("[+] TODO: Add JSON output support")

if __name__ == "__main__":
    main()
