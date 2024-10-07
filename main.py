from scapy.all import ARP, Ether, srp
import socket

def scan_network(network_prefix, timeout=1, retries=3):
    # ARP packet construction
    arp_request = ARP(pdst=f"{network_prefix}.1/50") # Checks the number of devices <50>
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request

    devices = []
    
    # Repeat scanning to increase the chance of finding devices
    for _ in range(retries):
        result = srp(packet, timeout=timeout, verbose=0)[0]

        for sent, received in result:
            device_info = {'ip': received.psrc, 'mac': received.hwsrc}
            # Get hostname through IP address
            try:
                hostname = socket.gethostbyaddr(received.psrc)[0]
                device_info['hostname'] = hostname
            except socket.herror:
                # If the device does not respond to DNS, its name will not be determined
                device_info['hostname'] = 'Unknown'
            
            # Avoid adding duplicate devices
            if device_info not in devices:
                devices.append(device_info)

    return devices


network_prefix = "192.168.1"    #  For example in the network

devices = scan_network(network_prefix, timeout=2, retries=3)

# Print all device information
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")
