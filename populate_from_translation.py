import csv

# Percorsi file
SRC_PATH = r"C:/PakTest/estrazione dal tedesco/Game.locres_it.csv"
DST_PATH = r"C:/PakTest/estrazione dal tedesco/Game.locres.csv"

# Leggi il file delle traduzioni italiane
with open(SRC_PATH, encoding="utf-8") as f_in, open(DST_PATH, 'w', encoding="utf-8", newline='') as f_out:
    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        # Copia tutte le colonne, la colonna Translation è già popolata
        writer.writerow(row)

print(f"File Game.locres.csv popolato con le traduzioni italiane: {DST_PATH}")
