import ipaddress
def analyze_ipv6(ip_address):
  ip=ipaddress.IPv6Address(ip_address)

  print(f"IPv6 주소: {ip}")
  print(f"축약형: {ip.compressed}")
  print(f"확장형: {ip.exploded}")
  print(f"범위: {'Global' if ip.is_global else 'Local'}")
  
analyze_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
