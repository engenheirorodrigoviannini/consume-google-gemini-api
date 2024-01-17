import google.generativeai as genai
import PIL.Image
import json

# Lê a chave da API do arquivo de configuração
with open('config') as config_file:
    config_data = json.load(config_file)
    google_api_key = config_data.get('google_api_key')

genai.configure(api_key=google_api_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('files/images/mapa_brasil.PNG')

response = model.generate_content(img)

print("Resposta 1:", response.text)

response = model.generate_content(["Descreva a imagem?", img])
response.resolve()

print("Resposta da pergunta", response.text)
