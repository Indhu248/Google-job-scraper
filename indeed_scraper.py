from serpapi import GoogleSearch
import json

params = {
    "engine": "google_jobs",
    "q": "react developer remote" ,
    "location": "India",
    "hl": "en",
    "api_key": "b0002f12215924aa21f41e38a06970ddc20902ff7aa385b9c03e4fff68ff118d"  # Replace with your SerpAPI key
}

search = GoogleSearch(params)
results = search.get_dict()
jobs = results.get("jobs_results", [])

filtered_jobs = []

for job in jobs:
    posted_at = job.get("detected_extensions", {}).get("posted_at", "")
    job_link = job.get("apply_options", [{}])[0].get("link") or job.get("job_highlight_url") or job.get("job_id")

    # Filter by date
    if any(day in posted_at.lower() for day in ["hour", "1 day", "2 days", "3 days"]):
        job_data = {
            "title": job.get("title", "N/A"),
            "company": job.get("company_name", "N/A"),
            "location": job.get("location", "N/A"),
            "via": job.get("via", "N/A"),
            "date": posted_at,
            "link": job_link if job_link.startswith("http") else "https://www.google.com"  # fallback
        }
        filtered_jobs.append(job_data)

    if len(filtered_jobs) >= 50:
        break

# Save to JSON file
with open("google_jobs_filtered.json", "w", encoding="utf-8") as f:
    json.dump(filtered_jobs, f, ensure_ascii=False, indent=2)

print(f"✅ {len(filtered_jobs)} filtered jobs saved to google_jobs_filtered.json")
