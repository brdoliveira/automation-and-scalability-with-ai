import os
import datetime
from dotenv import load_dotenv
from openai_chat_gpt import OpenAIChatGPT  # Supondo que esta seja a classe que acabamos de refatorar
from pdf_generator import PDF  # Supondo que esta classe permite adicionar páginas, títulos e corpos de texto
from openai_models import OpenAIModels

# Carrega as variáveis de ambiente
load_dotenv()

def main():
    # Instancia a classe OpenAIChatGPT com o modelo de sua escolha
    chat_gpt = OpenAIChatGPT(model=OpenAIModels.DAVINCI)
    
    # Cria um objeto PDF
    pdf = PDF()
    pdf.set_title("Respostas do ChatGPT")
    
    # Abre o arquivo .txt e lê linha por linha
    with open('prompts.txt', 'r') as file:
        for line in file:
            prompt = line.strip()
            if prompt:  # Verifica se a linha não está vazia
                print(f"Processando: {prompt}")
                response, cost = chat_gpt.generate_response(prompt)
                pdf.add_page()
                pdf.chapter_title(prompt)
                # Adiciona o valor gasto logo abaixo do título
                pdf.chapter_body(f"Valor gasto pela requisição: ${cost:.4f}\n\n{response}")
    
    # Gera um nome de arquivo único com base no horário atual
    now = datetime.datetime.now()
    unique_pdf_name = now.strftime("Respostas_ChatGPT_%Y-%m-%d_%H-%M-%S.pdf")
    
    # Salva o PDF com o nome único
    pdf.output(unique_pdf_name)
    print(f"PDF gerado com sucesso: {unique_pdf_name}.")

if __name__ == "__main__":
    main()