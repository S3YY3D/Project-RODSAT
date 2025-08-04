import csv
import jdatetime

# Map Persian month names to month numbers
PERSIAN_MONTHS = {
    "فروردین": 1,
    "اردیبهشت": 2,
    "خرداد": 3,
    "تیر": 4,
    "مرداد": 5,
    "شهریور": 6,
    "مهر": 7,
    "آبان": 8,
    "آذر": 9,
    "دی": 10,
    "بهمن": 11,
    "اسفند": 12,
}

def persian_digits_to_english(s):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    translation_table = str.maketrans(''.join(persian_digits), ''.join(english_digits))
    return s.translate(translation_table)

def jalali_to_gregorian(jalali_date_str):
    # Example input: "۱۱ مرداد ۱۴۰۴"
    try:
        parts = jalali_date_str.strip().split()
        if len(parts) != 3:
            return jalali_date_str  # Can't parse, return as is

        day_persian, month_persian, year_persian = parts

        day = int(persian_digits_to_english(day_persian))
        year = int(persian_digits_to_english(year_persian))
        month = PERSIAN_MONTHS.get(month_persian)

        if month is None:
            return jalali_date_str  # Unknown month, return original

        jalali_date = jdatetime.date(year, month, day)
        gregorian_date = jalali_date.togregorian()
        return gregorian_date.strftime("%Y-%m-%d")
    except Exception:
        return jalali_date_str  # fallback if conversion fails

def convert_jalali_dates_in_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, "r", encoding="utf-8-sig") as infile, \
         open(output_csv_path, "w", encoding="utf-8-sig", newline="") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if 'date' in row and row['date'].strip():
                row['date'] = jalali_to_gregorian(row['date'])
            writer.writerow(row)
