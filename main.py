from lookup_parser import parse_lookup_table
from processor import count_tags, count_port_protocol_combinations
from output_writer import write_csv

def main():
    lookup_file = 'data/lookup_table.csv'
    logs_file = 'data/logs.txt'

    lookup_dict = parse_lookup_table(lookup_file)
    tag_count = count_tags(logs_file, lookup_dict)
    port_protocol_count = count_port_protocol_combinations(logs_file)

    write_csv(tag_count, 'output/tag_count.csv', ['Tag', 'Count'])
    write_csv(port_protocol_count, 'output/port_protocol_count.csv', ['Port', 'Protocol', 'Count'])

if __name__ == '__main__':
    main()
