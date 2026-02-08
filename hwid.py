#!/usr/bin/env python3

import platform
import hashlib
import sys

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD_GREEN = '\033[1;92m'
    BOLD_YELLOW = '\033[1;93m'
    BOLD_CYAN = '\033[1;96m'
    BOLD_WHITE = '\033[1;97m'

def get_hwid():
    try:
        machine_id = platform.node()
        processor = platform.processor()
        system = platform.system()
        machine = platform.machine()
        
        hwid_string = f"{machine_id}-{processor}-{system}-{machine}"
        hwid_hash = hashlib.sha256(hwid_string.encode()).hexdigest()
        
        return hwid_hash
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")
        return None

def main():
    
    hwid = get_hwid()
    
    if hwid:
        print(f"{Colors.YELLOW}HWID Anda:{Colors.RESET}")
        print(f"{Colors.BOLD_GREEN}{hwid}{Colors.RESET}\n")
        
        try:
            with open("my_hwid.txt", "w") as f:
                f.write(f"{hwid}\n")
        except:
            pass
        
        print(f"\n{Colors.YELLOW}Kirim HWID di atas ke seller untuk mendapatkan license key{Colors.RESET}")
    else:
        print(f"{Colors.RED}Gagal generate HWID{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Dibatalkan{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.RESET}")
        sys.exit(1)
