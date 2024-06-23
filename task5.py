import socket
import struct
import textwrap
import signal
import sys

# Function to unpack Ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# Function to format MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

# Function to unpack IPv4 packets
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

# Function to format IPv4 address
def ipv4(addr):
    return '.'.join(map(str, addr))

# Function to unpack ICMP packets
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

# Function to unpack TCP segments
def tcp_segment(data):
    src_port, dest_port, sequence, acknowledgement, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flags = offset_reserved_flags & 0x1FF
    return src_port, dest_port, sequence, acknowledgement, flags, data[offset:]

# Function to unpack UDP segments
def udp_segment(data):
    src_port, dest_port, length = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, length, data[8:]

# Main packet sniffer function
def packet_sniffer():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    print("Packet sniffer started. Press Ctrl+C to stop.")

    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            print('\nEthernet Frame:')
            print(f'Destination MAC: {dest_mac}, Source MAC: {src_mac}, Protocol: {eth_proto}')

            # IPv4
            if eth_proto == 8:
                (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
                print('IPv4 Packet:')
                print(f'Version: {version}, Header Length: {header_length}, TTL: {ttl}')
                print(f'Protocol: {proto}, Source: {src}, Target: {target}')

                # ICMP
                if proto == 1:
                    icmp_type, code, checksum, data = icmp_packet(data)
                    print('ICMP Packet:')
                    print(f'Type: {icmp_type}, Code: {code}, Checksum: {checksum}')
                    print('Data:')
                    print(format_multi_line_data(data))

                # TCP
                elif proto == 6:
                    src_port, dest_port, sequence, acknowledgement, flags, data = tcp_segment(data)
                    print('TCP Segment:')
                    print(f'Source Port: {src_port}, Destination Port: {dest_port}')
                    print(f'Sequence: {sequence}, Acknowledgement: {acknowledgement}')
                    print('Flags:')
                    print(f'URG: {bool(flags & 0x20)}, ACK: {bool(flags & 0x10)}, PSH: {bool(flags & 0x08)}, RST: {bool(flags & 0x04)}, SYN: {bool(flags & 0x02)}, FIN: {bool(flags & 0x01)}')
                    print('Data:')
                    print(format_multi_line_data(data))

                # UDP
                elif proto == 17:
                    src_port, dest_port, length, data = udp_segment(data)
                    print('UDP Segment:')
                    print(f'Source Port: {src_port}, Destination Port: {dest_port}, Length: {length}')
                    print('Data:')
                    print(format_multi_line_data(data))

                # Other IPv4
                else:
                    print('Other IPv4 Data:')
                    print(format_multi_line_data(data))

            else:
                print('Ethernet Data:')
                print(format_multi_line_data(data))

    except KeyboardInterrupt:
        print("\nPacket sniffer stopped by user.")
        sys.exit(0)

# Function to format multi-line data
def format_multi_line_data(data):
    return '\n'.join(textwrap.wrap(textwrap.fill(data.hex(), width=80), width=80))

# Run the packet sniffer
if __name__ == '__main__':
    packet_sniffer()