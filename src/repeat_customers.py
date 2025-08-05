import csv
from collections import defaultdict
from datetime import datetime

def parse_month(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m')

def monthly_repeat_customers(input_csv_path, output_csv_path):
    customer_visits = defaultdict(list)  # {customer: [dates]}
    monthly_customers = defaultdict(set)  # {month: set(customers)}

    # Step 1: Read input and collect customer visit data
    with open(input_csv_path, 'r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row['name'].strip()
            date = row['date'].strip()

            try:
                visit_date = datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                continue  # Skip invalid date formats

            month = visit_date.strftime('%Y-%m')
            customer_visits[name].append(visit_date)
            monthly_customers[month].add(name)

    # Step 2: Sort visits for each customer
    for visits in customer_visits.values():
        visits.sort()

    # Step 3: Track cumulative and monthly stats
    all_months = sorted(monthly_customers.keys())
    seen_customers = set()
    seen_repeaters = set()

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([
            'month',
            'total_customers_till_now',
            'repeat_customers_till_now',
            'repeat_rate_till_now',
            'total_customers_this_month',
            'repeat_customers_this_month',
            'repeat_rate_this_month'
        ])

        for month in sorted(all_months):
            customers_this_month = monthly_customers[month]
            repeaters_this_month = set()

            for customer in customers_this_month:
                visits = customer_visits[customer]
                # Check if this is a repeat customer as of this month
                if len(visits) >= 2:
                    second_visit = visits[1]
                    if second_visit.strftime('%Y-%m') == month:
                        repeaters_this_month.add(customer)

            seen_customers.update(customers_this_month)
            seen_repeaters.update(repeaters_this_month)

            total_till_now = len(seen_customers)
            repeat_till_now = len(seen_repeaters)
            rate_till_now = round((repeat_till_now / total_till_now) * 100, 2) if total_till_now else 0

            total_this_month = len(customers_this_month)
            repeat_this_month = len(repeaters_this_month)
            rate_this_month = round((repeat_this_month / total_this_month) * 100, 2) if total_this_month else 0

            writer.writerow([
                month + '-01',
                total_till_now,
                repeat_till_now,
                rate_till_now,
                total_this_month,
                repeat_this_month,
                rate_this_month
            ])

    print("✅ Monthly repeat customer analysis saved!")
