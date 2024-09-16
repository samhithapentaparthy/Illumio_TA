# Update file to add more protocols
def convert_protocol(protocol_number):
    protocol_map = {
        '1': 'icmp',
        '4': 'ipv4',
        '6': 'tcp',
        '17': 'udp'

    }
    return protocol_map.get(protocol_number, 'unknown')