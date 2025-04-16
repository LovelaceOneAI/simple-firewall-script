# Simple Personal Firewall Script

A beginner-friendly personal firewall setup for both Linux and Windows. This repo contains basic scripts using `iptables` (Linux) and PowerShell (Windows Defender Firewall).

## 🛠 Features

- Flushes old rules and resets default policies
- Allows safe traffic (localhost, SSH, web)
- Blocks unwanted traffic
- Teaches foundational firewall concepts

---

## 🔧 Usage

### Linux (`linux_firewall.sh`)

**Run with sudo:**
```bash
chmod +x linux_firewall.sh
sudo ./linux_firewall.sh
