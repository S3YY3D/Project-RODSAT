# 🥡 Snappfood Review Scraper

This project scrapes customer reviews from restaurant pages on [Snappfood](https://snappfood.ir), Iran’s most popular food delivery platform.  
It uses **Selenium** to handle dynamic content and extract key data like reviewer name, date, rating, comment, and tags.

---

## 📁 Project Structure

.
├── data/
│ └── raw/
│ └── snappfood_reviews.csv # Scraped reviews saved here
├── scraper.py # Scraping logic (as a function)
├── main.py # Entry point to run the scraper
└── README.md # Project documentation

---

## 🚀 How It Works

- `main.py`: Specifies the restaurant URL and desired output file name, and calls the scraping function.
- `scraper.py`: Contains `scrape_reviews(url, output_file)` which:
  - Loads the restaurant page
  - Closes any popup
  - Clicks the review tab ("اطلاعات و نظرات")
  - Scrolls to load all available reviews
  - Extracts and saves the review data as CSV

---

## 🛠️ Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (matching your browser version)

---

### Install dependencies:

```bash
pip install selenium
