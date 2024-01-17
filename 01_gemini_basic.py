import google.generativeai as genai
import json

# Lê a chave da API do arquivo de configuração
with open('config') as config_file:
    config_data = json.load(config_file)
    google_api_key = config_data.get('google_api_key')

# Configura a chave da API
genai.configure(api_key=google_api_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Quais os estados brasileiros?")

print(response.text)
