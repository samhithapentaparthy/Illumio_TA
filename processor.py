from collections import defaultdict
from protocol_converter import convert_protocol

"""
Function to count tags in the flow logs

flow_log_file -> path to input file
lookup_dict -> lookup table in dictionary format

Returns dictionary with tag as key and count as value
"""
def count_tags(flow_log_file, lookup_dict):
    tag_count = defaultdict(int)
    
    with open(flow_log_file, mode='r') as file:
        for line in file:
            fields = line.split()
            dst_port = fields[5]  
            protocol_number = fields[7]  

            protocol = convert_protocol(protocol_number).lower()

            tags = lookup_dict.get((dst_port, protocol), ["Untagged"])
            for tag in tags:
                tag_count[tag] += 1

    return tag_count

"""
Function to count port and protocol combinations in the flow logs

flow_log_file -> path to input file

Returns dictionary with (port, protocol) as key and count as value
"""
def count_port_protocol_combinations(flow_log_file):
    port_protocol_count = defaultdict(int)
    
    with open(flow_log_file, mode='r') as file:
        for line in file:
            fields = line.split()
            dst_port = fields[5]  
            protocol_number = fields[7]  

            protocol = convert_protocol(protocol_number).lower()

            port_protocol_count[(dst_port, protocol)] += 1

    return port_protocol_count
