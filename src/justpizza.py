import os
import csv

def keep_the_pizza(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        filtered_rows = [row for row in reader if "پیتزا" in row['tags']]

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

    print("✅ done with pizza!")