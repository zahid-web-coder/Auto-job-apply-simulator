from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from dotenv import load_dotenv

# Load credentials
load_dotenv()
EMAIL = os.getenv("INTERNSHALA_EMAIL")
PASSWORD = os.getenv("INTERNSHALA_PASSWORD")

# Load cover letter and resume
RESUME_PATH = os.path.abspath("zahid_resume.pdf")
with open("cover_letter.txt", "r", encoding="utf-8") as f:
    COVER_LETTER = f.read()

# Keywords to search
keywords = [
    "android app development",
        "computer science",
        "cyber security",
        "front-end development",
        "full-stack development",
        "internet of things",
        "java development",
        "javascript development",
        "mobile app development",
        "python",
        "software development",
        "web development"
]
# Start browser
driver = webdriver.Chrome()
driver.get("https://internshala.com/login")
time.sleep(3)

# Login
driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)
time.sleep(5)

print("✅ Logged in as:", driver.title)

for keyword in keywords:
    url = f"https://internshala.com/internships/{keyword}-internship-in-bangalore/"
    driver.get(url)
    time.sleep(3)

    # Scroll down to load jobs
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    view_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'View details')]")
    total = len(view_buttons)
    print(f"🔍 Found {total} jobs for '{keyword.replace('+', ' ')}'")

    for i in range(min(2, total)):
        try:
            view_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'View details')]")
            view_buttons[i].click()
            time.sleep(4)

            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)

            apply_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Apply now')]"))
            )
            apply_button.click()
            time.sleep(3)

            resume_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "resume"))
            )
            resume_input.send_keys(RESUME_PATH)

            textarea = driver.find_element(By.TAG_NAME, "textarea")
            textarea.clear()
            textarea.send_keys(COVER_LETTER)

            submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
            submit.click()
            print(f"✅ Applied to: {keyword.replace('+', ' ')} #{i+1}")
            time.sleep(5)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ Error for '{keyword}' job #{i+1}: {e}")
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

driver.quit()
