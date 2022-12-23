import socket

def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
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
start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip_address, port))
        print("Taranan port: {}, Durum: Açık, Servis: {}".format(port, get_service_name(port)))
        s.shutdown(1)
        s.close()
    except Exception:
        print("Taranan port: {}, Durum: Kapalı".format(port))
#Teşekkürler.
