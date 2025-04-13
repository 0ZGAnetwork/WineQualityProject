import csv
import os
import sys

source_file = "wine-quality.csv"
destination_file = "wine-quality_dataset.csv"

def copy_csv_content(source_file, destination_file):
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"Error: Cannot open source file '{source_file}'. File does not exist.")
        sys.exit(1)

    try:
        with open(source_file, mode='r', newline='', encoding='utf-8') as src:
            reader = csv.reader(src)
            rows = list(reader)

        with open(destination_file, mode='a', newline='', encoding='utf-8') as dest:
            writer = csv.writer(dest)
            writer.writerows(rows)

        print(f"Content successfully copied to '{destination_file}'.")

    except Exception as e:
        print(f"Error during copying: {e}")
        sys.exit(1)

# Run the function
copy_csv_content(source_file, destination_file)
