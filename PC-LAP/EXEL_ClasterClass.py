import csv
import os
import sys

# Pliki CSV
source_file = "wine-quality_dataset_5class.csv"
destination_file = "wine-quality_dataset.csv"

# Dozwolone klasy (po modyfikacji)
allowed_classes = {4, 5, 6, 7, 8}

# Mapowanie: które klasy zmieniamy (3 → 4, 9 → 8)
class_mapping = {
    3: 4,
    9: 8
}

def add_transformed_classes(source_file, destination_file, allowed_classes, class_mapping):
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        sys.exit(1)

    rows_added = 0

    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        header = reader[0]
        data_rows = reader[1:]

        if 'quality' not in header:
            print("Error: Column 'quality' not found in source file.")
            sys.exit(1)

        quality_index = header.index('quality')

        # Nadpisz plik docelowy i zapisz nagłówek
        with open(destination_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            for row in data_rows:
                try:
                    quality = int(row[quality_index])
                except ValueError:
                    continue  # pomiń błędne dane

                # Przekształć jakość, jeśli jest w mapowaniu
                if quality in class_mapping:
                    new_quality = class_mapping[quality]
                    if new_quality in allowed_classes:
                        row[quality_index] = str(new_quality)
                        writer.writerow(row)
                        rows_added += 1

                # Lub zapisz bez zmian, jeśli klasa jest dozwolona
                elif quality in allowed_classes:
                    writer.writerow(row)
                    rows_added += 1

    print(f"Nadpisano plik '{destination_file}' ({rows_added} wierszy, klasy: {sorted(allowed_classes)} + przekształcenia {class_mapping}).")

# Uruchomienie
add_transformed_classes(source_file, destination_file, allowed_classes, class_mapping)
