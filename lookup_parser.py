import csv
from collections import defaultdict

def parse_lookup_table(lookup_file):
    lookup_dict = defaultdict(list)
    with open(lookup_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            port = row['dstport']
            protocol = row['protocol'].lower()  # To handle case-insensitive
            tag = row['tag']
            lookup_dict[(port, protocol)].append(tag)
    return lookup_dict