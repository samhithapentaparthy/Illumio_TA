# Illumio_TA
Illumio Technical Assessment Code

# Assumptions
The flow logs have consistent data and follow the guidelines listed in the AWS user guide
The 6th field is considered as destination port and 8th field is considered as protocol based on the provided sample flows
All lines in the input log file are valid lines

# Code Structure
│
├── main.py                     
├── lookup_parser.py              
├── processor.py         
├── protocol_converter.py         
├── output_writer.py              
├── data/
│   ├── logs.txt         
│   └── lookup_table.csv          
└── output/
    ├── port_protocol_count.csv      
    └── tag_count.csv

main.py               -> Main script to run the program
lookup_parser.py      -> Contains function for parsing the lookup table
processor.py          -> Contains functions to process logs and get desired output
protocol_converter.py -> Contains function to convert protocol numbers to names (update file to add more protocols)
output_writer.py      -> Contains function for writing results to CSV files

