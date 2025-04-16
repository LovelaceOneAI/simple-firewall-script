# AI-Generated Firewall Script

This branch explores how AI and automation can assist with building dynamic firewall rules.

## What it does:
- Uses Python to simulate detection of open ports
- Automatically generates `iptables` rules based on those ports
- Provides a foundation for more intelligent firewalls that respond to environment changes

## Future ideas:
- Connect to log analyzers or `nmap` to detect actual open ports
- Let LLMs suggest or explain rule changes
- Adapt in real-time based on usage or threat profiles

## Run it (Linux):
```bash
sudo python3 ai_firewall.py
