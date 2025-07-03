# 🤖 Auto Job Apply Simulator – Internshala,Linkdin,Naukri Bot

A Python automation script that applies to Jobs and internships on Internshala, Linkedin and Naukri based on your preferences. Built using Selenium WebDriver, this bot simulates a user logging in, finding relevant jobs, and applying with a resume and custom cover letter.

## 🚀 Features

- ✅ Auto login using credentials from `.env` file
- ✅ Scrolls and loads dynamic job listings
- ✅ Filters jobs using keywords like `python`, `web`, `java`, `software`, etc.
- ✅ Clicks “View Details” → “Apply Now” on matching jobs
- ✅ Uploads your resume and fills out a cover letter
- ✅ Applies to up to 3 jobs per session (configurable)

---

## 🧰 Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (matching your browser version)
- Selenium
- python-dotenv

---

## 🛠 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/zahid-web-coder/Auto-job-apply-simulator.git
   cd Auto-job-apply-simulator
Install dependencies

pip install -r requirements.txt
Download ChromeDriver
Get ChromeDriver here
→ Place the file in the same folder as your script

Create your .env file

Copy .env.example and rename it to .env:


INTERNSHALA_EMAIL=your@email.com
INTERNSHALA_PASSWORD=yourpassword123
Add your resume and cover letter

resume.pdf → your resume

cover_letter.txt → your generic or custom message

▶️ Run the Script

python auto_apply_internshala.py
It will:

Log into Internshala

Search internships in Bengaluru

Apply to top matching jobs based on your keywords

💡 Example Keywords Used
You can customize the keyword list in the script:

python
Copy
Edit
keywords = ["web", "python", "software", "frontend", "java", "developer", "engineer"]
📁 Project Structure
vbnet
Copy
Edit
Auto-job-apply-simulator/
├── auto_apply_internshala.py
├── auto_apply_internshala_debug.py
├── .env.example
├── cover_letter.txt
├── resume.pdf
├── requirements.txt
└── README.md
⚠️ Disclaimer
This project is for educational purposes only.
Please use it responsibly and do not spam job applications.
Internshala's terms of service may prohibit automated activity.

✨ Author
Mohammed Zahid – aspiring developer with a passion for automation, Python, and building helpful tools.


