import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define risky patterns and messages
vulnerabilities = {
    "eval(": "High Risk: eval() can lead to code injection.",
    "exec(": "High Risk: exec() can execute arbitrary code.",
    "pickle.load(": "Medium Risk: pickle.load() can execute untrusted objects.",
    "input(": "Low Risk: raw input may be unsafe if not sanitized."
}

def scan_file(file_path):
    print(f"\nScanning file: {file_path}")
    issues_found = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, start=1):
                for pattern, message in vulnerabilities.items():
                    if pattern in line:
                        issues_found = True
                        print(
                            f"{Fore.RED}[!] Line {i} - {message}{Style.RESET_ALL}\n"
                            f"    >>> {line.strip()}"
                        )
    except Exception as e:
        print(f"{Fore.YELLOW}Could not open file: {file_path} | Reason: {e}{Style.RESET_ALL}")

    if not issues_found:
        print(f"{Fore.GREEN}[✓] No vulnerabilities found in this file.{Style.RESET_ALL}")

def secure_code_review(path):
    if os.path.isfile(path):
        scan_file(path)
    elif os.path.isdir(path):
        print(f"Scanning all Python files in directory: {path}")
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    scan_file(os.path.join(root, file))
    else:
        print(f"{Fore.YELLOW}Invalid path: {path}{Style.RESET_ALL}")
