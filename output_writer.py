import csv

"""
Writes a dictionary to a CSV file.

data_dict -> data in dictionary format
output_file -> path to the output file
header -> header for the csv file (column names)
"""
def write_csv(data_dict, output_file, header):

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
        # Write data depending on the tuple or single key
        for key, value in data_dict.items():
            if isinstance(key, tuple):
                writer.writerow([*key, value])
            else:
                writer.writerow([key, value])
