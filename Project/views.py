from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure API key
GOOGLE_API_KEY = 'AIzaSyBE7TdE-8DsnHiKfBsVnQnjsBtwroYFAm4'
genai.configure(api_key=GOOGLE_API_KEY)

# Load the generative model
model = genai.GenerativeModel('gemini-pro')

def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        response = model.generate_content(prompt)
        return JsonResponse({'response': response.text})

    return render(request, 'index.html')
