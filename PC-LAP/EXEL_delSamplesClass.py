import csv
import os
import sys
import random

# Source and destination file paths
source_file = "wine-quality_dataset.csv"
destination_file = "wine-quality_bufor.csv"

# Class map with the number of samples to remove (undersampling)
removal_map = {
    5: 300,
    6: 1000,
}

def undersample_rows_by_class(source_file, destination_file, removal_map):
    if not os.path.exists(source_file):
        print(f" Error: Source file '{source_file}' does not exist.")
        sys.exit(1)

    # Load data
    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        header = reader[0]
        data_rows = reader[1:]

    if 'quality' not in header:
        print(" Error: Column 'quality' not found in the source file.")
        sys.exit(1)

    quality_index = header.index('quality')

    # Group data by class
    class_groups = {}
    for row in data_rows:
        try:
            quality = int(row[quality_index])
        except ValueError:
            continue
        class_groups.setdefault(quality, []).append(row)

    # Undersampling – randomly remove specified number of samples
    balanced_rows = []
    total_removed = 0

    for quality, rows in class_groups.items():
        remove_n = removal_map.get(quality, 0)
        if remove_n > 0 and remove_n < len(rows):
            indices_to_remove = set(random.sample(range(len(rows)), remove_n))
            filtered = [row for i, row in enumerate(rows) if i not in indices_to_remove]
            total_removed += remove_n
        else:
            filtered = rows  # Do not remove if not needed or too few examples

        balanced_rows.extend(filtered)

    # Write the balanced data to the destination file
    with open(destination_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(balanced_rows)

    print(f" Removed {total_removed} rows from classes: {list(removal_map.keys())} ➜ data saved to '{destination_file}'.")

# Run the function
undersample_rows_by_class(source_file, destination_file, removal_map)
