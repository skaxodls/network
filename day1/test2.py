import ipaddress

def create_subnets(network, subnet_bits):
  net=ipaddress.IPv4Network(network)

  num_subnets=2**subnet_bits
  
  subnets=list(net.subnets(prefixlen_diff=subnet_bits))

  print(f"원본 네트워크: {net}")
  print(f"생성된 서브넷 수: {num_subnets}")

  for i, subnet in enumerate(subnets, 1):
    print(f"\n 서브넷 {i}: ")
    print(f" 네트워크 주소: {subnet.network_address}")
    print(f" 브로드캐스트 주소: {subnet.broadcast_address}")
    print(f" 사용 가능한 IP 주소 수: {subnet.num_addresses - 2}")  # -2 for network and broadcast addresses

create_subnets("192.168.1.0/24", 2)
