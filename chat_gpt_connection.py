import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora, a chave da API é carregada a partir do arquivo .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def setup_openai():
    """Configura a biblioteca openai com a chave de API."""
    openai.api_key = OPENAI_API_KEY

def generate_response(prompt, model="text-davinci-003", temperature=0.7, max_tokens=150):
    """
    Gera uma resposta usando o Chat GPT (OpenAI).

    :param prompt: O prompt de texto para o Chat GPT.
    :param model: O modelo do Chat GPT a ser usado.
    :param temperature: Quão criativas as respostas devem ser.
    :param max_tokens: O número máximo de tokens na resposta.
    :return: A resposta gerada pelo Chat GPT.
    """
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    setup_openai()
    prompt = "Insira seu prompt aqui"
    response = generate_response(prompt)
    print("Resposta do GPT-3:", response)