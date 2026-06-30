# 🍯 HoneyBadger-Net

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Security-Educational-red.svg" alt="Security Level">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

**HoneyBadger-Net** is a powerful, modular Python-based toolkit designed for network monitoring, wireless security analysis, and laboratory testing. It allows users to interact with network interfaces, scan for wireless access points, and perform controlled security assessments in isolated environments.

---

## 🚀 Features / المميزات
* **Interface Management:** Seamlessly switch network adapters to Monitor Mode.
* **Network Discovery:** Scan and identify available WiFi access points (BSSID, SSID, Channel).
* **Security Testing:** Perform controlled Deauthentication attacks for testing purposes.
* **Identity Masking:** Includes MAC address spoofing capabilities to simulate network conditions.
* **Modular Architecture:** Clean, separated code structure for easy maintenance and expansion.

---

## 🛠️ Prerequisites / المتطلبات
To run this tool, ensure you have the following installed on your Linux system:
* **Python 3.x**
* **Aircrack-ng suite** (for monitor mode management)
* **Root/Sudo privileges**

---

## 📦 Installation / التثبيت

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Lionalashwel/HoneyBadger-Net.git](https://github.com/Lionalashwel/HoneyBadger-Net.git)
   cd HoneyBadger-Net



   Install dependencies:

Bash
pip install -r requirements.txt



Run the tool:

Bash
sudo python3 main.py



⚠️ Disclaimer / إخلاء مسؤولية
Educational Purposes Only. This tool is intended for use in authorized penetration testing and educational scenarios within controlled laboratory environments. The developer is not responsible for any misuse, illegal activities, or damage caused by this software. Use it responsibly and respect privacy.

📄 License / الترخيص
This project is licensed under the MIT License.

💡 How it works
The tool operates by leveraging Scapy to inject specific 802.11 management frames. It automates the transition of your network hardware into monitoring mode, allowing the capture of beacon frames, and subsequently facilitates the spoofing of hardware addresses.

Developed with 🍯 by Lionalashwel


