import csv

# Function to split data into rows with information before and after "|"
def split_lines(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as outputcsv:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(outputcsv, delimiter=';')

        for row in reader:

            for i, cell in enumerate(row):
                parts = cell.split('|')
                if len(parts) > 1:
                    for j in range(len(parts) - 1):
                        new_row = row.copy()  # Create a copy of the original row
                        new_row[i] = parts[j]  # Update the cell in the copy with the split part
                        new_rows.append(new_row)  # Add the new row to the temporary list

                    # Update the cell in the original row with the remaining part
                    row[i] = parts[-1]

            # Write the new rows generated during splitting
            for new_row in new_rows:
                writer.writerow(new_row)

            # Write the original row after all the splits
            writer.writerow(row)

# Input and output CSV file names
input_file = '1.csv'
output_file = 'september1000.csv'

# Call the function to split the data and write the result to the new file
split_lines(input_file, output_file)
