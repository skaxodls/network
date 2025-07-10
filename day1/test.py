import ipaddress
def analyze_ip(ip_address, subnet_mask):
  network= ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}",strict=False)

  print(f"IP 주소: {ip_address}")
  print(f"서브넷 마스크: {subnet_mask}")
  print(f"네트워크 주소: {network.network_address}")
  print(f"브로드캐스트 주소: {network.broadcast_address}")
  print(f"사용 가능한 IP 주소 수: {network.num_addresses - 2}")  # -2 for network and broadcast addresses

analyze_ip("192.168.1.100","255.255.255.0")

