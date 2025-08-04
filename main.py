from scanner.nmap_scan import run_nmap
from scanner.openvas_scan import run_openvas
from scanner.report_gen import generate_report

def read_file(path):
    with open(path) as f:
        return f.read()

def main():
    target = "192.168.1.10"
    nmap_file = run_nmap(target)
    run_openvas(target)

    nmap_data = read_file(nmap_file)
    openvas_data = read_file("output/openvas_report.xml")  # Or converted text

    generate_report(nmap_data, openvas_data)
    print("Scan complete. Report saved to output/final_report.pdf")

if __name__ == "__main__":
    main()
