from pypdf import PdfReader
import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import pandas as pd

load_dotenv()

SYSTEM_PROMPT="""Extract these fields from the pdf: (invoice_number, seller, buyer, date, due_date, total).
Reply with JSON only, no extra text.
Use exactly these field names as keys."""

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract(pdf):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=pdf,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json", #smh makes ai respond json shit properly
        ),
    )
    return json.loads(response.text)


rows =[]
for file in os.listdir("invoices"):
    if not file.endswith(".pdf"):
        continue
    try:    
        reader = PdfReader(f"invoices/{file}")
        page = reader.pages[0]  
        text = page.extract_text()
        r = extract(text)
        rows.append(r)
    except Exception as e:
        print("Failed on", file, e)

df = pd.DataFrame(rows)
df.to_excel("invoices.xlsx",index = False)