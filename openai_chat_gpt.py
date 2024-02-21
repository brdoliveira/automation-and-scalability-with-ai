import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class OpenAIChatGPT:
    def __init__(self, model="text-davinci-003"):
        """
        Inicializa a instância com a chave da API e o modelo desejado.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.setup_openai()

    def setup_openai(self):
        """
        Configura a biblioteca openai com a chave de API.
        """
        if not self.api_key:
            raise ValueError("API Key não encontrada. Certifique-se de que está definida no arquivo .env.")
        openai.api_key = self.api_key

    def generate_response(self, prompt, temperature=0.7, max_tokens=150):
        """
        Gera uma resposta usando o Chat GPT.

        :param prompt: O prompt de texto para o Chat GPT.
        :param temperature: Quão criativas as respostas devem ser.
        :param max_tokens: O número máximo de tokens na resposta.
        :return: A resposta gerada pelo Chat GPT.
        """
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

# Exemplo de uso
if __name__ == "__main__":
    # Instancia a classe OpenAIChatGPT com o modelo de sua escolha
    chat_gpt = OpenAIChatGPT(model="text-davinci-003")
    
    # Define o prompt
    prompt = "Insira seu prompt aqui"
    
    # Gera e imprime a resposta
    response = chat_gpt.generate_response(prompt)
    print("Resposta do GPT-3:", response)