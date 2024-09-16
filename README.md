# Illumio_TA
Illumio Technical Assessment Code

# Assumptions
- The flow logs have consistent data and follow the guidelines listed in the AWS user guide <br>
- The **7th field** is considered as **destination port** and **8th field** is considered as **protocol** based on the AWS user guide <br>
- All lines in the input logs file are valid lines <br>

# File Structure
```
├── main.py                     
├── lookup_parser.py              
├── processor.py         
├── protocol_converter.py         
├── output_writer.py
├── README.md            
├── data/
│   ├── logs.txt         
│   └── lookup_table.csv          
└── output/
    ├── port_protocol_count.csv      
    └── tag_count.csv
```
main.py               -> Main script to run the program <br>
lookup_parser.py      -> Contains function for parsing the lookup table <br>
processor.py          -> Contains functions to process logs and get desired output <br>
protocol_converter.py -> Contains function to convert protocol numbers to names (update file to add more protocols) <br>
output_writer.py      -> Contains function for writing results to CSV files <br>

# Running the Code
## 1. Clone the Repository:
```
git clone https://github.com/samhithapentaparthy/Illumio_TA.git
```
## 2. Install Dependencies:
Ensure you have Python installed. No additional library dependencies
## 3. Input Files:
Place your flow logs file (logs.txt) and lookup table file (lookup_table.csv) into the data folder <br>
Ensure that lookup_table.csv is in a comma-separated format and logs.txt follows the expected log structure <br> <br>
Note: The sample files provided are present to run code directly <br>
## 4. Run the Code:
```
python main.py
```
## 5. Output:
The results will be saved in the output folder <br><br>
port_protocol_count.csv will contain the counts of port and protocol combinations <br>
tag_count.csv will contain the counts of tags <br>
## 6. Verify:
Open the generated CSV files in a text editor or spreadsheet application to verify the results

# Links
AWS User Guide https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html <br>
Protocol Numbers https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

