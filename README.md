# 🥡 Snappfood Review Scraper

This project scrapes customer reviews from restaurant pages on [Snappfood](https://snappfood.ir), Iran’s most popular food delivery platform.  
It uses **Selenium** to handle dynamic content and extract key data like reviewer name, date, rating, comment, and tags.

---

## 📁 Project Structure

.
your_project/
│
├── src/
│   ├── main.py
│   ├── scraper.py
│   ├── date_convertor.py
│   ├── date_sorter.py
│   ├── blanks.py
│   ├── justpizza.py
│   ├── daily_score.py
│
├── data/
│   ├── raw/
│   ├── sorted/
│   ├── daily/
│
├── requirements.txt
└── README.md

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
