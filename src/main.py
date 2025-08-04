import os
from scraper import scrape_reviews
from date_convertor import convert_jalali_dates_in_csv

if __name__ == "__main__":

    url = "https://snappfood.ir/restaurant/menu/%DA%AF%D9%88%DA%AF%DB%8C_%D8%A8%D8%B1%DA%AF%D8%B1-r-0jmzvr/"
    output_raw_directory = "data/raw"

    raw_file = os.path.join(output_raw_directory, "snappfood_reviews.csv")
    jalali_date_converted_file = os.path.join(output_raw_directory, "snappfood_reviews_gregoriandate.csv")

    # Step 1: Scrape the data and save raw CSV
    scrape_reviews(url, raw_file)

    # Step 2: Convert Jalali dates to Gregorian and save new CSV
    convert_jalali_dates_in_csv(raw_file, jalali_date_converted_file)
