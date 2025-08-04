import subprocess
import os

def run_nmap(target):
    os.makedirs("output/logs", exist_ok=True)
    output_file = "output/logs/nmap_raw.xml"
    print("[+] Running Nmap scan...")
    subprocess.run(["nmap", "-sV", "-O", "-oX", output_file, target], check=True)
    return output_file
