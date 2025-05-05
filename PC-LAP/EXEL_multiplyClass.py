import csv
import os
import sys

# Pliki źródłowy i docelowy
source_file = "wine_quality_dataset_raw.csv"
destination_file = "wine_quality_dataset_raw.csv"

# Mapa klas i ich współczynników powielania
duplication_map = {
    3: 15,  # klasa 3 → 15 razy
    4: 2,   # klasa 4 → 2 razy
    8: 2,   # klasa 8 → 2 razy
    9: 60   # klasa 9 → 60 razy
}

def duplicate_rows_by_class(source_file, destination_file, duplication_map):
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        sys.exit(1)

    # Wczytaj wszystkie dane z pliku źródłowego
    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        header = reader[0]
        data_rows = reader[1:]

    if 'quality' not in header:
        print("Error: Column 'quality' not found in source file.")
        sys.exit(1)

    quality_index = header.index('quality')

    # Sprawdź, czy plik docelowy istnieje
    file_exists = os.path.exists(destination_file)
    rows_added = 0

    # Otwórz plik docelowy w trybie dopisywania
    with open(destination_file, mode='a', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Jeśli plik nie istnieje lub jest pusty, zapisz nagłówek
        if not file_exists or os.stat(destination_file).st_size == 0:
            writer.writerow(header)

        # Iteracja i powielanie odpowiednich klas
        for row in data_rows:
            try:
                quality = int(row[quality_index])
            except ValueError:
                continue  # pomiń błędne dane

            if quality in duplication_map:
                for _ in range(duplication_map[quality]):
                    writer.writerow(row)
                    rows_added += 1

    print(f"{rows_added} rows duplicated for classes {list(duplication_map.keys())} and added to '{destination_file}'.")

# Uruchomienie funkcji
duplicate_rows_by_class(source_file, destination_file, duplication_map)
