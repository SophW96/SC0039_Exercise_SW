#import required libraries
import csv
import os

# define file name of the CSV file to be opened
file_name = 'brca_cnvs_tcga-1.csv'

#change working directory to the location of the current python script
os.chdir(os.path.dirname(__file__))

#retrieve current directory
current_directory = os.getcwd()

# Construct the full path to the CSV file
file_path_complete = os.path.abspath(file_name)
#print(file_path_complete) #check that the correct file path is displayed


# Open the CSV file for appending in binary mode (to avoid newline issues)
with open(file_path_complete,'r', newline='') as read_obj: #open file to read
    with open('brca_cnvs_tcga-1_updated.csv', 'w', newline='') as write_obj: #open file to write
        csv_reader = csv.reader(read_obj)
        csv_writer = csv.writer(write_obj)

    # Read the header row and add the 'seq_length' column header
        header = next(csv_reader)
        header.append('seq_length')
        csv_writer.writerow(header) # Write the header to the new file


    # Process each row and calculate the seq_length value
        for row in csv_reader:
            col3 = int(row[2])  # Assuming column 2 contains integer values
            col4 = int(row[3])  # Assuming column 3 contains integer values
            seq_length = col4 - col3
            row.append(seq_length)
            csv_writer.writerow(row) # Write the updated row to the new file

        
print(f"Data appended to {current_directory} with a new column '{'seq_length'}' successfully.")

