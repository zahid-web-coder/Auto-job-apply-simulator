from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
RESUME_PATH = os.path.abspath("resume.pdf")
COVER_LETTER = open("cover_letter.txt", 'r', encoding='utf-8').read()

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(3)

driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)
time.sleep(5)

keywords = ["Python Developer", "Frontend Developer", "Software Engineer", "Java Developer"]

for kw in keywords:
    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={kw.replace(' ', '%20')}&location=Bengaluru%2C%20Karnataka")
    time.sleep(5)

    jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")
    for i in range(min(2, len(jobs))):
        try:
            jobs[i].click()
            time.sleep(2)

            easy_apply = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Easy Apply')]"))
            )
            easy_apply.click()
            time.sleep(2)

            # Upload resume
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(RESUME_PATH)
            time.sleep(1)

            # Enter cover letter if available
            try:
                cover_field = driver.find_element(By.XPATH, "//textarea")
                cover_field.clear()
                cover_field.send_keys(COVER_LETTER)
            except:
                pass

            # Submit/Next
            submit_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Submit application') or contains(@aria-label,'Next')]")
            submit_btn.click()
            time.sleep(2)

            print(f"✅ Easy Applied on LinkedIn for '{kw}' #{i+1}")
            # Close modal
            driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']").click()
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ LinkedIn apply error for '{kw}' #{i+1}: {e}")
            time.sleep(2)

driver.quit()
