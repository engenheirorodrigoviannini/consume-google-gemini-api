import google.generativeai as genai
import json

# Lê a chave da API do arquivo de configuração
with open('config') as config_file:
    config_data = json.load(config_file)
    google_api_key = config_data.get('google_api_key')

genai.configure(api_key=google_api_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

bem_vindo = "# Bem Vindo ao Assistente com Gemini AI #"
print(len(bem_vindo) * "#")
print(bem_vindo)
print(len(bem_vindo) * "#")
print("###   Digite 'sair' para encerrar    ###")
print("")

while True:
    texto = input("Escreva sua mensagem: ")

    if texto == "sair":
        break

    response = chat.send_message(texto)
    print("Gemini:", response.text, "\n")

print("Encerrando Chat")
