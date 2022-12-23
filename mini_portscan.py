import socket

def get_open_ports(ip_address):
    open_ports = []
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            print(f"port: {port}")
            s.connect((ip_address, port))
            open_ports.append(port)
            s.shutdown(1)
            s.close()
        except Exception:
            pass

    return open_ports

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except Exception:
        return "unknown"

ip_address = input("IP adresini girin: ")
open_ports = get_open_ports(ip_address)
closed_ports = set(range(1, 65535)) - set(open_ports)

print("Açık portlar:")
for port in open_ports:
    service_name = get_service_name(port)
    print("Port: {}, Service: {}".format(port, service_name))

print("\nKapalı portlar:")
for port in closed_ports:
    print("Port: {}".format(port))
