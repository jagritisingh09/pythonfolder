import google.generativeai as genai
import os

os.environ['GOOGLE_API_KEY']=''
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model=genai.GenerativeModel('gemini-1.5-flash')

prompt= "Why UP is the best state"
response= model.generate_content(prompt)

print(response.text)