import os
from scraper import scrape_reviews
from date_convertor import convert_jalali_dates_in_csv
from date_sorter import sort_reviews_by_date
from blanks import fix_blank_ratings_in_csv


if __name__ == "__main__":

    url = "https://snappfood.ir/restaurant/menu/%DA%AF%D9%88%DA%AF%DB%8C_%D8%A8%D8%B1%DA%AF%D8%B1-r-0jmzvr/"
    raw_dir = "data/raw"
    sorted_dir = "data/sorted"

    raw_file = os.path.join(raw_dir, "snappfood_reviews.csv")
    gregorian_date_file = os.path.join(raw_dir, "snappfood_reviews_gregoriandate.csv")
    fixed_rating_file = os.path.join(raw_dir, "snappfood_reviews_fixedrating.csv")
    sorted_file = os.path.join(sorted_dir, "snappfood_reviews_sorted.csv")

    # Step 1: Scrape the data and save raw CSV
    scrape_reviews(url, raw_file)

    # Step 2: Convert Jalali dates to Gregorian and save new CSV
    convert_jalali_dates_in_csv(raw_file, gregorian_date_file)

    # Step 3: Fix blank ratings in the converted CSV
    fix_blank_ratings_in_csv(gregorian_date_file, fixed_rating_file)

    # Step 4: Sort reviews by Gregorian date
    sort_reviews_by_date(fixed_rating_file, sorted_file)

    print(f"✅ All steps completed. Sorted data saved to: {sorted_file}")