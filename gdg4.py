from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=  ChatGoogleGenerativeAI(model='gemini-1.5-pro')

while True:
       inp= input("You:")

       response = model.invoke("user : "+inp)
       
       print("AI : " + response.content)