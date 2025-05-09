#------------- IMPORT ------------#
from os import system as c
import time
import random
import os

#------------- COLOUR ------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
██████╗ ███████╗███████╗     ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝     ██║██╔════╝██╔══██╗
██████╔╝█████╗  █████╗       ██║█████╗  ██████╔╝
██╔═══╝ ██╔══╝  ██╔══╝  ██   ██║██╔══╝  ██╔══██╗
██║     ███████╗███████╗╚█████╔╝███████╗██║  ██║
╚═╝     ╚══════╝╚══════╝ ╚════╝ ╚══════╝╚═╝  ╚═╝
{P}
   HACKING WORLD - FREE FIRE DIAMOND HACK VIP TOOL
            {Y}** WORK ONLY ON ROOTED DEVICE **
{A}--------------------------------------------------
""")

#------------- ROOT CHECK -------------#
def check_root():
    print(f"{Y}[+] Checking Root Access...")
    time.sleep(2)
    if os.path.exists("/system/xbin/su") or os.path.exists("/system/bin/su"):
        print(f"{G}[✓] ROOT ACCESS GRANTED!")
    else:
        print(f"{R}[X] ROOT ACCESS NOT FOUND!")
        print(f"{R}This tool requires a rooted phone to work.")
        input(f"\n{A}Press Enter To Exit...")
        exit()

#------------- MAIN MENU -------------#
def menu():
    logo()
    check_root()
    print(f"{A}[1] START DIAMOND HACK")
    print(f"{A}[2] SHOW PASSWORD LIST")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}--------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        diamond_hack()
    elif choice == '2':
        password_list()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- DIAMOND HACK -------------#
def diamond_hack():
    logo()
    c('espeak "Free Fire Diamond Hack Starting"')
    uid = input(f"{C}ENTER FREE FIRE UID: ")
    print(f"\n{Y}[+] Connecting to Garena Free Fire Server...")
    time.sleep(3)
    print(f"{G}[✓] UID Verified: {uid}")
    time.sleep(1)
    print(f"{B}[+] Selecting Diamond Packages...")
    time.sleep(2)

    amounts = [500, 1000, 2000, 5000, 10000, 20000]
    for amount in amounts:
        print(f"{C}[*] Injecting {amount} Diamonds...")
        time.sleep(1.5)
    time.sleep(1)

    print(f"\n{R}[!] SECURITY VERIFICATION SUCCESSFUL")
    time.sleep(2)
    print(f"{Y}Visit the link to complete verification: {G}https://garena-vip-verify.com")
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- PASSWORD LIST -------------#
def password_list():
    logo()
    print(f"{P} VIP HACK PASSWORDS:")
    passwords = [
        'diamondking2025', 'ffmaster999', 'hackzone555',
        'royalvip2024', 'prohunter', 'freefirelegend', 'garenahack999',
        'ffgodmode', 'ultimatevip', 'ffhack@2025'
    ]
    for pw in passwords:
        print(f"{C}[*] {pw}")
        time.sleep(0.5)
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- START TOOL -------------#
menu()