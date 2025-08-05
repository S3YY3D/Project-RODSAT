import os
import csv

def fix_blank_ratings_in_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        data = list(reader)

    for row in data:
        if not row.get("rating") or row["rating"].strip() == "":
            row["rating"] = "1"

    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    with open(output_csv_path, "w", encoding="utf-8-sig", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)