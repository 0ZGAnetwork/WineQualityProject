import csv
import os

# Pliki CSV
source_file = "wine-quality_Red_2.csv"
destination_file = "wine_quality_dataset_raw.csv"

def clone_csv_data(source_file, destination_file):
    if not os.path.exists(source_file):
        print(f"Błąd: Plik źródłowy '{source_file}' nie istnieje.")
        return

    with open(source_file, newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        if not reader:
            print("Plik źródłowy jest pusty.")
            return

        header = reader[0]
        data_rows = reader[1:]

        with open(destination_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Jeśli plik docelowy jest pusty, dopisz nagłówek
            if os.stat(destination_file).st_size == 0:
                writer.writerow(header)

            writer.writerows(data_rows)

    print(f"Sklonowano {len(data_rows)} wierszy z pliku '{source_file}' do '{destination_file}'.")

# Uruchomienie
clone_csv_data(source_file, destination_file)
