from dotenv import load_dotenv
load_dotenv()

import json
from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

OPENAI_API_KEY = "ENTER YOUR API KEY"

with open("content_idea.json",'r') as f:
    content=json.load(f)

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=OPENAI_API_KEY  
)


prompt = PromptTemplate.from_template("""
You are a YouTube strategist.

Using the following research, generate a 4-week content calendar (2 videos/week).
Each video must include:
- title
- format (Short, Long, Tutorial, Explainer)
- level (Beginner, Intermediate, Advanced)
- tags (list of 2–5 keywords)

Respond with a valid JSON structure:

{{
  "week_1": [
    {{"title": "...", "format": "...", "level": "...", "tags": ["...", "..."]}},
    ...
  ],
  "week_2": [...],
  "week_3": [...],
  "week_4": [...]
}}

Here is the research data:
{content}

""")


formatted_prompt = prompt.format(
    content=json.dumps(content, indent=2)
)

parser = JsonOutputParser()

response = llm.invoke(formatted_prompt)
structured_plan = parser.parse(response.content)

print(structured_plan)

filename = f"youtube_calendar_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(structured_plan, f, indent=2)

print(f"✅ YouTube Content Calendar saved to: {filename}")

