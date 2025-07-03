from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
RESUME_PATH = os.path.abspath("resume.pdf")
COVER_LETTER = open("cover_letter.txt", 'r', encoding='utf-8').read()

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
time.sleep(3)

driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
driver.find_element(By.ID, "passwordField").send_keys(PASSWORD + Keys.RETURN)
time.sleep(5)

keywords = ["Python Developer", "Frontend Developer", "Software Engineer", "Java Developer"]

for kw in keywords:
    driver.get(f"https://www.naukri.com/{kw.replace(' ', '-')}-jobs-in-bangalore")
    time.sleep(5)

    job_cards = driver.find_elements(By.CSS_SELECTOR, ".jobTuple a.title")
    for i in range(min(2, len(job_cards))):
        try:
            job_cards[i].click()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)

            apply_btn = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
            )
            apply_btn.click()
            time.sleep(3)

            resume_upload = WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            resume_upload.send_keys(RESUME_PATH)

            textarea = driver.find_element(By.TAG_NAME, "textarea")
            textarea.clear()
            textarea.send_keys(COVER_LETTER)

            submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
            submit.click()
            print(f"✅ Applied on Naukri for '{kw}' #{i+1}")
            time.sleep(5)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ Naukri apply error for '{kw}' #{i+1}: {e}")
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            time.sleep(10)

driver.quit()
