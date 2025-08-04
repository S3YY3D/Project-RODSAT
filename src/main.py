import os
from scraper import scrape_reviews

if __name__ == "__main__":
    url = "https://snappfood.ir/restaurant/menu/%DA%AF%D9%88%DA%AF%DB%8C_%D8%A8%D8%B1%DA%AF%D8%B1-r-0jmzvr/"
    output_dir = "data/raw"
    output_file = os.path.join(output_dir, "snappfood_reviews.csv")
    scrape_reviews(url, output_file)
