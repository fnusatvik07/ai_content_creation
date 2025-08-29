from dotenv import load_dotenv
load_dotenv()

import os 
import json 
import requests
from datetime import datetime


# Step 1: Make Serp AI Call and Get Results


params = {
  "engine": "google",
  "q": "AI Agents in 2025",
  "location": "United States",
  "num": 30,
  "api_key": "ENTER YOUR API KEY"
}

response=requests.get("https://serpapi.com/search.json",params=params)
response.raise_for_status()

# Step 2: Load this JSON into Python

data=json.loads(response.text)


# Step 3: Extract Long Video from the JSON

video_titles=[]

for item in data["inline_videos"][:5]:
    title=item["title"]
    channel=item["channel"]
    video_titles.append(f"{title}-{channel}")


# Step 4: Extract Shorts from the JSON

short_videos = []
for item in data["short_videos"][:5]:
    short_videos.append(item["title"])



# Step 5: Top 5 Questions People are Searching

questions = []
for item in data["related_questions"][:5]:
    questions.append(item["question"])



# Step 6: Organic Results

snippets = []
for item in data["organic_results"][:5]:
    snippets.append(item["snippet"])

# Step 7- Combine Result to JSON

combine_data={
    "topic":"AI Agents in 2025",
    "video_titles":video_titles,
    "short_videos":short_videos,
    "questions":questions,
    "organic_results":snippets,
    "fetched_at":datetime.now().isoformat()
}

# Step 8: Save the Result to a JSON File

with open("content_idea.json","w") as f:
    json.dump(combine_data,f,indent=2)










