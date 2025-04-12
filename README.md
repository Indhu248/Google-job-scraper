# 🔍 Google Job Scraper (with Direct Apply Links)

This project is a Python-based job scraper that uses **Google Jobs via SerpAPI** to fetch up to **50 recent job listings (within 3 days)** and stores them in a clean JSON format. Each job includes the **title, company, location, posted time, and a direct application link** to portals like LinkedIn, Glassdoor, etc.



---

## 📌 Features

- ✅ Scrapes job data from Google Jobs using SerpAPI
- ✅ Filters jobs posted within the last 3 days
- ✅ Limits the output to 50 results max
- ✅ Stores job listings in structured JSON format
- ✅ Includes direct job portal links for easy apply

---

## 🖥️ System Requirements

Before getting started, make sure your computer has the following:

### ✅ Software/Tools Required

| Tool             | Version Recommended | Required For         |
|------------------|---------------------|----------------------|
| Python           | 3.7 or above        | Running the script   |
| pip              | Latest              | Installing libraries |
| Text Editor      | VS Code / Sublime   | Editing code         |
| Git (optional)   | Latest              | Cloning the repo     |
| SerpAPI Account  | Free/Pro            | Google Job Scraping  |

---

## 🧱 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/google-job-scraper.git
cd google-job-scraper
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, create one with:

```text
serpapi
```

### 4. Get your SerpAPI key

- Sign up at [https://serpapi.com](https://serpapi.com)
- Go to your dashboard and copy your **API key**

### 5. Add your SerpAPI key in the script

Open `job_scraper.py` and replace:

```python
"api_key": "YOUR_API_KEY"
```

with your real key.

---

## 🚀 How to Use

1. Run the script:

```bash
python job_scraper.py
```

2. After a few seconds, it will create a file:

```
google_jobs_filtered.json
```

This file will contain job results like:

```json
[
  {
    "title": "React Developer",
    "company": "Awesome Tech",
    "location": "Remote",
    "via": "LinkedIn",
    "date": "2 days ago",
    "link": "https://www.linkedin.com/jobs/view/123456789"
  }
]
```

---

## 🔄 Customization

You can change these inside the script:

| Parameter   | Description                      | Example                          |
|-------------|----------------------------------|----------------------------------|
| `q`         | Keyword for job role             | `"web developer"`               |
| `location`  | Job location                     | `"India"`, `"Remote"`            |
| `max_results` | How many jobs to scrape       | `50`                             |
| `date_filter` | Filter jobs by posted time     | `"3 days ago"`                  |

---

Open `job_scraper.py` and modify these lines at the top:

```python
JOB_TITLE = "web developer"  # 🔁 Change this to any job title (e.g., "python developer")
LOCATION = "Remote"          # 🔁 Change this to any location (e.g., "Bangalore", "USA", etc.)
DAYS_POSTED = 3              # 🔁 Max age of job posts in days
MAX_RESULTS = 50             # 🔁 Number of job listings to scrape
```

✅ Save the file and run the script again — it’ll fetch results based on your new filters.

## 🧪 Troubleshooting

- If you get `0 jobs found`, try:
  - Updating your keyword or location
  - Checking your API quota
  - Using a different SerpAPI key

---

## 👨‍💻 Author

Built with 💻 by [Indu](https://github.com/your-username)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
```


