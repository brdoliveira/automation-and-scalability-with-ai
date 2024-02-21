import os
import re
import fitz
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Análise de Custos ChatGPT', 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def analisar_dados_e_gerar_pdf(diretorio, nome_arquivo='analise_custos.pdf'):
    padrao_nome_arquivo = re.compile(r'^Respostas_ChatGPT_.*\.pdf$')
    padrao_valor_gasto = re.compile(r'Valor gasto pela requisição: \$([0-9]+\.[0-9]+)')
    dados = []
    
    for arquivo in filter(padrao_nome_arquivo.match, os.listdir(diretorio)):
        caminho = os.path.join(diretorio, arquivo)
        valores = [float(v) for pagina in fitz.open(caminho) for v in padrao_valor_gasto.findall(pagina.get_text())]
        if valores:
            dados.append([arquivo, np.sum(valores), np.mean(valores), np.median(valores), np.std(valores), min(valores), max(valores), len(valores)])
    
    if dados:
        gerar_graficos(dados)
        gerar_pdf(dados, nome_arquivo)

def gerar_graficos(dados):
    for i, (titulo, func) in enumerate([('Total Gasto por Arquivo', np.sum), ('Gasto por Requisições', np.size)], start=1):
        valores = [func(d[1:]) for d in dados]
        plt.figure(figsize=(10, 6))
        if i == 1:
            plt.bar(range(len(dados)), valores, color='skyblue')
            plt.xticks(range(len(dados)), [d[0] for d in dados], rotation=45, ha="right")
        else:
            plt.scatter(range(len(dados)), valores, color='red')
            plt.xticks(range(len(dados)), [d[0] for d in dados], rotation=45, ha="right")
        plt.title(titulo)
        plt.tight_layout()
        plt.savefig(f'{titulo}.png')
        plt.close()

def gerar_pdf(dados, nome_arquivo):
    pdf = PDF()
    pdf.add_page()
    colunas = ['Arquivo', 'Total Gasto', 'Média Gasto', 'Mediana Gasto', 'Desvio Padrão', 'Mín Gasto', 'Máx Gasto', 'Total Requisições']
    larguras = [40, 30, 30, 30, 30, 30, 30, 30]
    pdf.set_fill_color(200, 220, 255)
    pdf.set_font('Arial', '', 12)
    
    for i, coluna in enumerate(colunas):
        pdf.cell(larguras[i], 10, coluna, 1, 0, 'C', 1)
    pdf.ln()
    
    for linha in dados:
        for i, valor in enumerate(linha):
            pdf.cell(larguras[i], 10, str(valor), 1)
        pdf.ln()
    
    for titulo in ['Total Gasto por Arquivo', 'Gasto por Requisições']:
        pdf.add_page()
        pdf.image(f'{titulo}.png', x=10, y=20, w=180)

    pdf.output(nome_arquivo)

# Exemplo de uso
analisar_dados_e_gerar_pdf('./pdfs')