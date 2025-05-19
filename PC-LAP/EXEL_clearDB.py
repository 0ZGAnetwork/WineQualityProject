import os

# Plik docelowy
destination_file = "wine-quality_dataset.csv"

def clear_file(destination_file):
    if not os.path.exists(destination_file):
        print(f"Error: The file '{destination_file}' does not exist.")
        return

    # Wyczyść zawartość pliku
    with open(destination_file, mode='w', encoding='utf-8') as outfile:
        # Zapisanie pustego pliku (usunięcie zawartości)
        pass

    print(f"The file '{destination_file}' has been cleared.")

# Uruchomienie
clear_file(destination_file)
