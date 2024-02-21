import openai
from dotenv import load_dotenv
import os
from openai_models import OpenAIModels

class OpenAIChatGPT:
    # Custo hipotético por 1000 tokens para cada modelo. Atualize com os valores reais.
    COST_PER_THOUSAND_TOKENS = {
        OpenAIModels.DAVINCI: 0.02,  # Exemplo: $0.02 por 1000 tokens
        OpenAIModels.CURIE: 0.006,   # Exemplo: $0.006 por 1000 tokens
        # Adicione os custos para outros modelos conforme necessário
    }

    def __init__(self, model=OpenAIModels.DAVINCI):
        """
        Inicializa a instância com a chave da API e o modelo desejado.
        """
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = model.value  # Utiliza o valor do enum
        openai.api_key = self.api_key

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
        :return: A resposta gerada pelo Chat GPT e o custo estimado da requisição.
        """
        try:
            response = openai.Completion.create(
                engine=self.model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            # Calcula o custo estimado da requisição
            # A quantidade de tokens usados é a soma do prompt e da resposta
            prompt_tokens = len(prompt.split())  # Estimativa simplificada
            response_tokens = len(response['choices'][0]['text'].strip().split())  # Estimativa simplificada
            total_tokens = prompt_tokens + response_tokens
            cost = self.calculate_cost(total_tokens)
            
            return response['choices'][0]['text'].strip(), cost
        except Exception as e:
            return f"Ocorreu um erro ao processar sua solicitação: {str(e)}", 0

    def calculate_cost(self, total_tokens):
        """
        Calcula o custo de uma requisição com base na quantidade total de tokens.

        :param total_tokens: A quantidade total de tokens usados na requisição.
        :return: O custo estimado da requisição.
        """
        cost_per_token = self.COST_PER_THOUSAND_TOKENS[self.model] / 1000
        return total_tokens * cost_per_token

# Exemplo de uso
if __name__ == "__main__":
    # Instancia a classe OpenAIChatGPT com o modelo de sua escolha
    chat_gpt = OpenAIChatGPT(model=OpenAIModels.DAVINCI)
    
    # Define o prompt
    prompt = "Qual é o significado da vida, do universo e tudo mais?"
    
    # Gera e imprime a resposta e o custo
    response, cost = chat_gpt.generate_response(prompt)
    print("Resposta do GPT-3:", response)
    print(f"Custo estimado da requisição: ${cost:.4f}")