import socket

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 126:
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:
        return "Class C", "255.255.255.0"
    elif 224 <= first_octet <= 239:
        return "Class D", None  # Class D doesn't have a subnet mask
    elif 240 <= first_octet <= 254:
        return "Class E", None  # Class E doesn't have a subnet mask
    else:
        return None, None

def calculate_network_and_broadcast(ip, mask):
    ip_parts = [int(part) for part in ip.split('.')]
    mask_parts = [int(part) for part in mask.split('.')]

    network_address = []
    broadcast_address = []

    for i in range(4):
        network_address.append(ip_parts[i] & mask_parts[i])
        broadcast_address.append(network_address[-1] | (mask_parts[i] ^ 255))

    return '.'.join(map(str, network_address)), '.'.join(map(str, broadcast_address))

def main():
    ip = input("ENTER IP: ")
    ip_class, mask = get_ip_class(ip)

    if ip_class is None:
        print("Invalid IP address.")
        return

    print(f"{ip_class} IP Address")

    if mask:
        print(f"SUBNET MASK: {mask}")

        network_address, broadcast_address = calculate_network_and_broadcast(ip, mask)
        print(f"First IP of block: {network_address}")
        print(f"Last IP of block: {broadcast_address}")
    else:
        print("This class does not use a subnet mask.")

if __name__ == "__main__":
    main()
