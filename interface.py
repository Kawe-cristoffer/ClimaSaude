import tkinter as tk
from tkinter import messagebox

from clima import obter_clima
from alertas import analisar_riscos


class ClimaSaudeApp:

    def __init__(self, janela):

        self.janela = janela

        self.janela.title("ClimaSaúde - Alertas Preventivos")
        self.janela.geometry("650x650")
        self.janela.resizable(False, False)

        titulo = tk.Label(
            janela,
            text="ClimaSaúde",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(20, 0))

        subtitulo = tk.Label(
            janela,
            text="Alertas Preventivos",
            font=("Arial", 14)
        )
        subtitulo.pack()

        local = tk.Label(
            janela,
            text="📍 Curitiba - Paraná",
            font=("Arial", 12)
        )
        local.pack(pady=10)

        self.informacoes = tk.Label(
            janela,
            text="Clique em 'Atualizar clima' para consultar os dados.",
            font=("Arial", 13),
            justify="left"
        )
        self.informacoes.pack(pady=15)

        tk.Frame(
            janela,
            height=2,
            bg="gray"
        ).pack(fill="x", padx=30, pady=10)

        titulo_alertas = tk.Label(
            janela,
            text="⚠️ Alertas Preventivos",
            font=("Arial", 18, "bold")
        )
        titulo_alertas.pack(pady=10)

        self.alertas = tk.Label(
            janela,
            text="Nenhuma consulta realizada.",
            font=("Arial", 12),
            justify="left",
            wraplength=550
        )
        self.alertas.pack(pady=5)

        titulo_recomendacoes = tk.Label(
            janela,
            text="💡 Recomendações",
            font=("Arial", 18, "bold")
        )
        titulo_recomendacoes.pack(pady=10)

        self.recomendacoes = tk.Label(
            janela,
            text="As recomendações aparecerão aqui.",
            font=("Arial", 12),
            justify="left",
            wraplength=550
        )
        self.recomendacoes.pack(pady=5)

        botao = tk.Button(
            janela,
            text="🔄 Atualizar clima",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10,
            command=self.atualizar
        )
        botao.pack(pady=25)

        rodape = tk.Label(
            janela,
            text="ClimaSaúde - Projeto Extensionista",
            font=("Arial", 9)
        )
        rodape.pack(side="bottom", pady=10)

    def atualizar(self):

        dados = obter_clima()

        if dados is None:
            messagebox.showerror(
                "Erro",
                "Não foi possível obter os dados climáticos.\n"
                "Verifique sua conexão com a internet."
            )
            return

        temperatura = dados["temperatura"]
        umidade = dados["umidade"]
        sensacao = dados["sensacao"]
        vento = dados["vento"]

        texto_informacoes = (
            f"🌡️ Temperatura: {temperatura:.1f} °C\n"
            f"💧 Umidade do ar: {umidade:.0f}%\n"
            f"🌡️ Sensação térmica: {sensacao:.1f} °C\n"
            f"💨 Velocidade do vento: {vento:.1f} km/h\n"
            f"🕐 Atualizado em: {dados['horario']}"
        )

        self.informacoes.config(
            text=texto_informacoes
        )

        alertas, recomendacoes = analisar_riscos(
            temperatura,
            umidade,
            vento
        )

        texto_alertas = "\n\n".join(
            f"⚠️ {alerta}" for alerta in alertas
        )

        texto_recomendacoes = "\n\n".join(
            f"• {recomendacao}" for recomendacao in recomendacoes
        )

        self.alertas.config(
            text=texto_alertas
        )

        self.recomendacoes.config(
            text=texto_recomendacoes
        )