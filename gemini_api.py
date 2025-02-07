import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = '***********************'


genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

def format_text(text):
    formatted_text = text.replace('.', '  ./n')
    return formatted_text

def mainn(name):
    model = genai.GenerativeModel('gemini-pro')
    k = f"I wants to plant {name} in my land so give me the details  like which season this crop should we grow , how much expence it take to cultivate for one actare , how much water needed to cultivate this crop , Expalin the process of cultivating this crop ."
    response = model.generate_content(k)

    formatted_content = format_text(response.text)
    return formatted_content


