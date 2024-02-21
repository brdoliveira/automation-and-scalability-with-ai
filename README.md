# Gerador de Respostas PDF com OpenAI ChatGPT

Este projeto permite a geração automática de respostas do ChatGPT da OpenAI para uma lista de prompts fornecida pelo usuário. Cada prompt é processado, e a resposta correspondente é salva em um arquivo PDF, com o prompt servindo como título da seção e a resposta da OpenAI como conteúdo.

## Estrutura do Projeto

O projeto é dividido em três arquivos principais:

- `openai_chat_gpt.py`: Contém a classe `OpenAIChatGPT`, responsável por encapsular a lógica de interação com a API do ChatGPT da OpenAI.
- `pdf_generator.py`: Define a classe `PDF`, uma extensão da classe `FPDF` para a criação de arquivos PDF. Esta classe formata o documento, adicionando títulos e o corpo do texto com as respostas do ChatGPT.
- `main.py`: Arquivo principal que orquestra a leitura dos prompts de um arquivo `.txt`, utiliza a classe `OpenAIChatGPT` para obter respostas para cada prompt e, em seguida, usa a classe `PDF` para gerar um documento PDF com essas informações.

## Como Usar

Para utilizar este projeto, siga os passos abaixo:

1. **Instalação de Dependências**: Certifique-se de instalar todas as dependências necessárias executando:

   ```bash
   pip install openai python-dotenv fpdf
   ```

2. **Configuração da API Key**: Adicione sua chave da API da OpenAI a um arquivo `.env` na raiz do projeto da seguinte forma:

   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```

3. **Adicionando Prompts**: Coloque os prompts que você deseja processar em um arquivo `prompts.txt`, com cada prompt em sua própria linha.

4. **Execução**: Execute o script principal com o comando:

   ```bash
   python main.py
   ```

## Impactos de Criar Múltiplas Requisições

Cada prompt processado resulta em uma requisição à API do ChatGPT da OpenAI. É importante ter em mente que:

- **Limites de Uso e Custos**: Dependendo do seu plano com a OpenAI, pode haver limites de uso e custos associados ao número de requisições. É aconselhável revisar o seu plano e entender os custos potenciais.
- **Desempenho e Latência**: Fazer múltiplas requisições em sequência pode levar a um aumento na latência, especialmente se estiver processando uma grande lista de prompts. Considere implementar lógicas de retry ou backoff exponencial em caso de falhas ou atrasos nas respostas.
- **Responsabilidade de Uso**: Ao utilizar a API, você é responsável pelo conteúdo gerado e por garantir que o uso está em conformidade com as políticas da OpenAI. Evite gerar conteúdo que possa ser considerado abusivo, discriminatório ou que viole diretrizes de uso.

## Contribuições

Contribuições para o projeto são bem-vindas! Se você tem sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para criar uma issue ou pull request.
