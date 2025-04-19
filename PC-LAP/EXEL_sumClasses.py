import csv
import os
import sys

# Pliki CSV
source_file = "wine-quality_Red_1.csv"
destination_file = "wine-quality_Red_2.csv"

# Wybrane klasy do przeniesienia
selected_classes = {3, 4, 7, 8, 9}

def add_selected_classes(source_file, destination_file, selected_classes):
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

        with open(destination_file, mode='a', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Zapisz nagłówek, jeśli plik docelowy jest pusty
            if os.stat(destination_file).st_size == 0:
                writer.writerow(header)

            for row in data_rows:
                try:
                    quality = int(row[quality_index])
                except ValueError:
                    continue  # pomiń błędne dane

                if quality in selected_classes:
                    writer.writerow(row)
                    rows_added += 1

    print(f"Dodano {rows_added} wierszy z klasami {selected_classes} do pliku '{destination_file}'.")

# Uruchomienie
add_selected_classes(source_file, destination_file, selected_classes)
