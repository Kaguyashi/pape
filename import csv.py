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
                        # Append the split information to the current cell
                        row[i] = parts[j]
                        # Write the current row with the added information
                        writer.writerow(row)
                    # Update the current cell with the remaining part
                    row[i] = parts[-1]

            # Write the current row after all the splits
            writer.writerow(row)

# Input and output CSV file names
input_file = 'o.csv'
output_file = 'setembro1000.csv'

# Call the function to split the data and write the result to the new file
split_lines(input_file, output_file)

