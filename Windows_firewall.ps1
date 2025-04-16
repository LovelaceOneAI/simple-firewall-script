# Block port 4444
New-NetFirewallRule -DisplayName "Block Port 4444" -Direction Inbound -LocalPort 4444 -Protocol TCP -Action Block

# Allow HTTP and HTTPS
New-NetFirewallRule -DisplayName "Allow HTTP/HTTPS" -Direction Inbound -LocalPort 80,443 -Protocol TCP -Action Allow
