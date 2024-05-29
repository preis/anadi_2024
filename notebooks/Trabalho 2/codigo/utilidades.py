import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use(
    "style/estilo.mplstyle")  # Garantir que se utiliza um estilo definido centralmente e comum a todos os gráficos.
sns.set(style="whitegrid")


def titulo(texto: str):
    print(f"\033[21;30;44m{texto}\033[0m")


def etiqueta_e_valor(etiqueta: str, valor: str = ""):
    print(f"\033[0;94m{etiqueta}: \033[1;94m{valor}\033[0m")


def texto(texto: str, cor="94"):
    print(f"\033[0;{cor}m{texto}\033[0m")


def undersplit(texto):
    return " ".join(texto.split("_"))


def histograma(
        dados: pd.Series,
        grupos: int = 20,
        kde: bool = True,
        size_x: int = 4,
        size_y: int = 4,
        titulo: str = "",
        etiqueta_x: str = "",
        etiqueta_y: str = "",
        color: str = "skyblue",
        edgecolor: str = "black",
):
    """Gera um histograma de forma isolada.

    A dimensão final do gráfico é controlada pela relação entre os valores size_x e size_y.
    """
    hist_fig, hist_axes = plt.subplots(figsize=(size_x, size_y))
    sns.histplot(dados, bins=grupos, kde=kde, color=color, edgecolor=edgecolor)
    hist_axes.set_title(titulo)
    hist_axes.set_xlabel(etiqueta_x)
    hist_axes.set_ylabel(etiqueta_y)
    plt.tight_layout()


def tarte(
        dados: pd.Series,
        size_x: int = 4,
        size_y: int = 4,
        autopct="%.2f%%",
        titulo: str = "",
        **kwargs,
):
    pie_fig, pie_axes = plt.subplots(figsize=(size_x, size_y))
    pie_axes.pie(
        dados,
        autopct=autopct,
        **kwargs
    )
    pie_fig.suptitle(titulo)
    return pie_fig, pie_axes


def tabela_1_coluna(dados_coluna, texto_titulo: str):
    titulo(texto_titulo)
    for item in dados_coluna:
        texto(item)
