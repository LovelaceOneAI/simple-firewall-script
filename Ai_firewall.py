import subprocess

# Simulated open port list – in the future, this can be dynamically generated
open_ports = [22, 80, 443]

# Flush rules and apply basic protections
subprocess.call(["iptables", "-F"])
subprocess.call(["iptables", "-P", "INPUT", "DROP"])
subprocess.call(["iptables", "-P", "FORWARD", "DROP"])
subprocess.call(["iptables", "-P", "OUTPUT", "ACCEPT"])
subprocess.call(["iptables", "-A", "INPUT", "-i", "lo", "-j", "ACCEPT"])
subprocess.call(["iptables", "-A", "INPUT", "-m", "conntrack", "--ctstate", "ESTABLISHED,RELATED", "-j", "ACCEPT"])

# Dynamically allow based on open_ports list
for port in open_ports:
    subprocess.call(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"])
