from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def scrape_reviews(url, output_file):
    # === Setup Chrome Driver ===
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment to run headless
    service = Service("chromedriver.exe")  # Make sure chromedriver.exe is accessible
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    # === Open URL ===
    driver.get(url)

    # === Close Initial Popup (if it appears) ===
    try:
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='تایید']")))
        confirm_button.click()
        print("✅ Popup closed")
    except:
        print("⚠️ Popup not found or already closed")

    # === Click the "اطلاعات و نظرات" (Info & Reviews) tab ===
    try:
        review_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='اطلاعات و نظرات']/..")))
        review_tab.click()
        print("✅ Review tab clicked")
    except Exception as e:
        print("❌ Couldn't click review tab:", e)
        driver.quit()
        return

    # === Wait for review container to load ===
    try:
        container = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class*='Comments__CommentsList']")
        ))
    except Exception as e:
        print("❌ Review container not found:", e)
        driver.quit()
        return

    # === Scroll the review section container to load all reviews ===
    scroll_pause_time = 2
    max_attempts = 6
    attempts = 0
    prev_count = 0

    while attempts < max_attempts:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)
        time.sleep(scroll_pause_time)

        reviews = container.find_elements(By.CSS_SELECTOR, "div[class*='Item__Container']")
        current_count = len(reviews)

        if current_count > prev_count:
            prev_count = current_count
            attempts = 0
        else:
            attempts += 1

    print(f"✅ {prev_count} reviews loaded.")

    # === Extract and Save Review Data ===
    data = []

    for review in reviews:
        try:
            name = review.find_element(By.CSS_SELECTOR, "p[class*='fnXEtS']").text.strip()
        except:
            name = ""

        try:
            date = review.find_element(By.CSS_SELECTOR, "div[class*='CommentInfo'] p:nth-child(2)").text.strip()
        except:
            date = ""

        try:
            rating = review.find_element(By.CSS_SELECTOR, "p[class*='Item__Rate']").text.strip()
        except:
            rating = ""

        try:
            comment = review.find_element(By.CSS_SELECTOR, "div[class*='CommentContent'] > p").text.strip()
        except:
            comment = ""

        try:
            tags = review.find_elements(By.CSS_SELECTOR, "div[class*='Item__Tag'] p")
            tag_text = ", ".join([t.text.strip() for t in tags])
        except:
            tag_text = ""

        data.append({
            "name": name,
            "date": date,
            "rating": rating,
            "comment": comment,
            "tags": tag_text
        })

    # === Save to CSV ===
    with open(output_file, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "rating", "comment", "tags"])
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Reviews saved to {output_file}")

    # === Done ===
    driver.quit()
