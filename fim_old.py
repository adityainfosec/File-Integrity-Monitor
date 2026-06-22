import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def banner():
    os.system("clear")

    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + "              FILE INTEGRITY MONITOR (FIM)")
    print(Fore.YELLOW + "      SHA-256 Based File Integrity Monitoring Tool")
    print(Fore.CYAN + "=" * 70)
    print(Fore.WHITE + "        Developed for Cybersecurity Learning")
    print(Fore.CYAN + "=" * 70)
    print()


def main():
    banner()

    print(Fore.GREEN + "[+] Application Started Successfully")
    print(Fore.YELLOW + "[+] Ready to Create File Baseline")


if __name__ == "__main__":
    main()
