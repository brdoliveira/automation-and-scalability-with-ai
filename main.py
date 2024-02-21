import os
from dotenv import load_dotenv
from openai_chat_gpt import OpenAIChatGPT  # Certifique-se de que este é o nome correto do arquivo onde a classe está definida
from pdf_generator import PDF

# Carrega as variáveis de ambiente
load_dotenv()

def main():
    # Instancia a classe OpenAIChatGPT
    chat_gpt = OpenAIChatGPT(model="text-davinci-003")
    
    # Cria um objeto PDF
    pdf = PDF()
    pdf.set_title("Respostas do ChatGPT")
    
    # Abre o arquivo .txt e lê linha por linha
    with open('prompts.txt', 'r') as file:
        for line in file:
            prompt = line.strip()
            if prompt:  # Verifica se a linha não está vazia
                print(f"Processando: {prompt}")
                response = chat_gpt.generate_response(prompt)
                pdf.add_page()
                pdf.chapter_title(prompt)
                pdf.chapter_body(response)
    
    # Salva o PDF
    pdf.output('Respostas_ChatGPT.pdf')
    print("PDF gerado com sucesso.")

if __name__ == "__main__":
    main()