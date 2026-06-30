import os
import subprocess
import pyfiglet
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

def print_banner():
    """عرض شعار غرير العسل واسم الأداة"""
    os.system('clear')
    badger = rf"""
    {Fore.LIGHTBLACK_EX}          .---.               
    {Fore.LIGHTBLACK_EX}         / ( ) \              
    {Fore.CYAN}       __{Fore.LIGHTBLACK_EX}\_`---'_{Fore.CYAN}__           
    {Fore.CYAN}      /   {Fore.WHITE}'-----'{Fore.CYAN}   \          
    {Fore.CYAN}     / {Fore.WHITE}|           |{Fore.CYAN} \         
    {Fore.CYAN}    / {Fore.WHITE}|  (\     /)  |{Fore.CYAN} \        
    {Fore.RED}    \ {Fore.WHITE}____{Fore.RED}'V'{Fore.WHITE}____/ {Fore.RED} /        
    {Fore.RED}     \___________/            
    """
    print(badger)
    print(Fore.RED + Style.BRIGHT + pyfiglet.figlet_format("HoneyBadger Net", font='slant'))
    print(Fore.CYAN + "="*65)
    print(Fore.YELLOW + " [!] LAB EDITION | AUTHORIZED USE ONLY")
    print(Fore.CYAN + "="*65 + "\n")

def get_interfaces():
    """جلب قائمة كروت الشبكة المتاحة"""
    return os.listdir('/sys/class/net/')

def set_monitor_mode(interface):
    """تحويل الكرت إلى وضع المراقبة"""
    print(f"{Fore.BLUE}[*] Attempting to set {interface} to Monitor Mode...")
    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        # قتل العمليات التي قد تعيق وضع المراقبة
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["sudo", "iwconfig", interface, "mode", "monitor"], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"{Fore.GREEN}[+] {interface} is now ready in Monitor Mode.")
        return True
    except Exception as e:
        print(f"{Fore.RED}[-] Failed to set monitor mode: {e}")
        return False