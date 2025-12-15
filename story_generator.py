from dotenv import load_dotenv
from google import genai
load_dotenv
import os

load_dotenv()


api_key=os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError('API akeey is not found')

client=genai.Client(api_key=api_key)

response=client.model.generate_content(
    model='gemini-2.5-pro',
    content='what is car explian in  300 words'

)

print(response.text)