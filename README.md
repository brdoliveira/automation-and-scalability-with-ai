# Gerador de Respostas PDF com OpenAI ChatGPT

Este projeto automatiza a geração de respostas do ChatGPT da OpenAI para uma lista de prompts fornecida pelo usuário. Para cada prompt, a resposta obtida e o custo estimado da requisição são formatados e incluídos em um arquivo PDF. Este arquivo destaca tanto o prompt (como título da seção) quanto a resposta da OpenAI, com o custo estimado da requisição detalhado abaixo do título.

## Recursos Atualizados

- **Cálculo do Custo Estimado**: Implementação de uma funcionalidade para calcular o custo estimado de cada requisição, baseando-se no número de tokens processados.
- **Inclusão do Custo no PDF**: O custo estimado de cada requisição é agora exibido no documento PDF, logo abaixo do título correspondente ao prompt.
- **Flexibilidade com Modelos da OpenAI**: Uso da enumeração `OpenAIModels` para facilitar a seleção e o gerenciamento dos modelos da OpenAI utilizados para gerar respostas.
- **Geração de Gráficos de Análise de Custos**: Novo código permite a análise de custos das requisições e a geração de gráficos que visualizam essas análises, incorporando-os ao documento PDF.

## Componentes do Projeto

O projeto é estruturado em cinco componentes principais:

- `openai_chat_gpt.py`: Contém a classe `OpenAIChatGPT`, que encapsula a interação com a API do ChatGPT da OpenAI, incluindo o cálculo do custo estimado para cada requisição.
- `openai_models.py`: Define a enumeração `OpenAIModels`, que lista os modelos da OpenAI disponíveis, facilitando a seleção do modelo desejado.
- `pdf_generator.py`: Define a classe `PDF`, uma extensão da classe `FPDF`, atualizada para incluir tanto os prompts e respostas quanto os custos estimados no documento PDF gerado.
- `cost_analysis.py`: Script responsável pela análise de custos das requisições, geração de gráficos de análise e incorporação desses gráficos ao PDF.
- `main.py`: Arquivo principal que orquestra a leitura dos prompts de um arquivo `.txt`, utiliza a classe `OpenAIChatGPT` para obter respostas para cada prompt e, em seguida, usa a classe `PDF` para gerar um documento PDF com essas informações, incluindo análises de custos e gráficos.

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
