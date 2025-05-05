import csv
import os

# CSV files
source_file = "wine-quality_dataset.csv"
destination_file = "wine_quality_dataset_raw.csv"

def clone_csv_data(source_file, destination_file):
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        if not reader:
            print("The source file is empty.")
            return

        header = reader[0]
        data_rows = reader[1:]

        with open(destination_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # If the destination file is empty, write the header
            if os.stat(destination_file).st_size == 0:
                writer.writerow(header)

            writer.writerows(data_rows)

    print(f"Cloned {len(data_rows)} rows from '{source_file}' to '{destination_file}'.")

# Run the function
clone_csv_data(source_file, destination_file)
