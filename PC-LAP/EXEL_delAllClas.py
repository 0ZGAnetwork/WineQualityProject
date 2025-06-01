import csv
import os
import sys
import random

# Source and destination file paths
source_file = "wine-quality_dataset — kopia.csv"
destination_file = "wine-quality_bufor.csv"

# Class map – specify number to remove, or 'all' to remove the entire class
removal_map = {
    3: "all",  # This will remove *all* rows with class 4
    5: 1294,
    6: 2035,
    7: 717,
    8: 12,
    9: "all"  # This will remove *all* rows with class 6
}

def undersample_rows_by_class(source_file, destination_file, removal_map):
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        sys.exit(1)

    # Load data
    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        header = reader[0]
        data_rows = reader[1:]

    if 'quality' not in header:
        print("Error: Column 'quality' not found in the source file.")
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

    # Apply undersampling or full removal
    balanced_rows = []
    total_removed = 0

    for quality, rows in class_groups.items():
        if quality in removal_map:
            remove_n = removal_map[quality]
            if remove_n == "all":
                total_removed += len(rows)
                continue  # Skip adding any rows for this class
            elif isinstance(remove_n, int) and remove_n < len(rows):
                indices_to_remove = set(random.sample(range(len(rows)), remove_n))
                filtered = [row for i, row in enumerate(rows) if i not in indices_to_remove]
                total_removed += remove_n
            else:
                filtered = rows  # Not enough rows to remove or invalid number
        else:
            filtered = rows  # Keep class untouched

        balanced_rows.extend(filtered)

    # Write the balanced data to the destination file
    with open(destination_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(balanced_rows)

    print(f"Removed {total_removed} rows from classes: {list(removal_map.keys())} ➜ data saved to '{destination_file}'.")

# Run the function
undersample_rows_by_class(source_file, destination_file, removal_map)
