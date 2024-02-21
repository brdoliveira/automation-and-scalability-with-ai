from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        """
        Cabeçalho padrão de cada página.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def chapter_title(self, title):
        """
        Define o título de um capítulo.

        :param title: O título do capítulo.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)  # Adiciona uma quebra de linha após o título

    def chapter_cost(self, cost):
        """
        Exibe o custo estimado da requisição abaixo do título do capítulo.

        :param cost: O custo estimado da requisição.
        """
        self.set_font('Arial', '', 12)
        cost_text = f"Valor gasto pela requisição: ${cost:.4f}"
        self.cell(0, 10, cost_text, 0, 1, 'L')
        self.ln(5)  # Adiciona uma pequena quebra de linha após o custo

    def chapter_body(self, body):
        """
        Define o corpo de um capítulo.

        :param body: O texto do corpo do capítulo.
        """
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()  # Adiciona uma quebra de linha após o corpo

# Exemplo de como usar a classe PDF modificada:
if __name__ == "__main__":
    pdf = PDF()
    pdf.set_title("Exemplo de Título")
    pdf.add_page()
    pdf.chapter_title("Título do Capítulo")
    pdf.chapter_cost(0.0345)  # Exemplo de custo
    pdf.chapter_body("Este é o corpo do capítulo, onde o texto principal será inserido.")
    pdf.output("exemplo.pdf")