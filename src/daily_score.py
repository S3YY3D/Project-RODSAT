import os
import csv
from collections import defaultdict

def daily_average(input_csv_path, output_csv_path):
    all_dates = set()
    ratings_by_date = defaultdict(list)

    # Read the CSV and collect dates and ratings
    with open(input_csv_path, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            date = row['date']
            all_dates.add(date)

            rating_str = row['rating'].strip()
            if rating_str:
                try:
                    rating = float(rating_str)
                    ratings_by_date[date].append(rating)
                except ValueError:
                    pass  # Skip non-numeric ratings

    # Write the average rating per day to output CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['date', 'average_rating'])

        for date in sorted(all_dates):
            ratings = ratings_by_date.get(date, [])
            average = round(sum(ratings) / len(ratings), 2) if ratings else 0
            writer.writerow([date, average])

    print("✅ daily average calculated!")

def daily_sales(input_csv_path, output_csv_path):
    sales_by_date = defaultdict(int)

    # Read the CSV and count number of reviews per date
    with open(input_csv_path, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            date = row['date']
            sales_by_date[date] += 1

    # Write date and number of reviews (sales) to output CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['date', 'sales'])

        for date in sorted(sales_by_date):
            writer.writerow([date, sales_by_date[date]])

    print("✅ daily sales calculated!")
