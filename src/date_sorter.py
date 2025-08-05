import csv
from datetime import datetime
import os

def sort_reviews_by_date(input_csv_path, output_csv_path):
    with open(input_csv_path, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        data = list(reader)

    # Sort by 'date' field (assumes format YYYY-MM-DD), handle empty dates by putting them at the end
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except Exception:
            return datetime.max

    data.sort(key=lambda x: parse_date(x.get('date', '')))

    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

    with open(output_csv_path, "w", encoding="utf-8-sig", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ All steps completed. Sorted data saved to: {output_csv_path}")
