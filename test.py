import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyBE7TdE-8DsnHiKfBsVnQnjsBtwroYFAm4'

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
     

def to_printResponse(response):
  print(response.text)


model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("I have a friend named Tamojit Roy likes boys instead of girls what is he?")

to_printResponse(response)