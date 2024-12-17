log_data = """192.168.1.1:80
192.168.1.2:80
192.168.1.1:8080
192.168.1.3:80"""

port_ips = {}

for line in log_data.splitlines():
    ip, port = line.split(":")
    port_ips.setdefault(port,set()).add(ip)

port_ips = {port:list(ip) for port, ip in port_ips.items()}
print(port_ips)

