# Classificação da qualidade de vinhos — Fase 2

Projeto acadêmico de análise exploratória e classificação binária da qualidade de vinhos, com foco em comunicar os resultados em linguagem de negócio. A nota original foi convertida em duas classes: **alta qualidade (nota ≥ 7)** e **baixa/média qualidade (nota < 7)**.

## Estrutura

```text
wine-quality-classification/
├── data/
│   ├── WineQT.csv
│   └── README.md
├── notebooks/
│   └── wine_quality_classification.ipynb
├── src/
│   ├── __init__.py
│   └── data_loader.py
├── results/
│   ├── dashboard_eda.png
│   ├── matrizes_confusao.png
│   ├── coeficientes_regressao_logistica.png
│   ├── metricas_modelos.csv
│   └── README.md
├── output/
│   ├── assets/
│   │   └── capa_vinho_fase2.png
│   ├── Apresentacao_Executiva_Fase_2_Wine_Quality.pptx
│   └── Guia_Python_e_Roteiro_Fase_2.docx
├── .gitignore
├── requirements.txt
└── README.md
```

Os gráficos e o CSV de métricas em `results/` são gerados/atualizados ao executar todas as células do notebook. A pasta `output/` guarda os materiais de apresentação produzidos para a entrega.

## Origem da base de dados

O arquivo utilizado no projeto é **WineQT.csv**, disponibilizado por YasserH no Kaggle: [Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset). Ele contém 1.143 registros e inclui características físico-químicas, a nota de qualidade e uma coluna identificadora.

A fonte também está registrada no carregador em `src/data_loader.py` e na primeira célula explicativa do notebook.

## O que foi analisado

- Distribuição das classes e variáveis físico-químicas;
- Associações entre as características e a classe de alta qualidade;
- Sinais de valores extremos pelo intervalo interquartil (IQR);
- Comparação entre Regressão Logística e SVM linear, com divisão estratificada entre treino e teste.

Na amostra analisada, 159 de 1.143 vinhos (13,9%) receberam nota ≥ 7. Os modelos foram avaliados em uma amostra de teste de 229 registros; a acurácia ficou próxima de 78%–79%, enquanto a precisão da classe de alta qualidade ficou próxima de 36%. Por isso, a acurácia isolada não deve ser interpretada como desempenho suficiente para uso operacional. Os resultados são exploratórios e não constituem uma previsão de vendas, preço ou aceitação de mercado.

## Como executar

1. Tenha Python instalado e abra um terminal na pasta do projeto.
2. (Recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

   No Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instale as bibliotecas:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o Jupyter e abra o notebook:

   ```bash
   jupyter notebook notebooks/wine_quality_classification.ipynb
   ```

5. Execute as células na ordem. O notebook lê o CSV local em `data/` e grava os gráficos e as métricas em `results/`.

Também é possível abrir `notebooks/wine_quality_classification.ipynb` no VS Code e selecionar um kernel Python que tenha as dependências instaladas.

## Limitações importantes

A base não contém marca, preço, custos, região de venda ou resultados de mercado. A nota é uma avaliação sensorial, e as relações observadas não provam causalidade. Antes de apoiar decisões comerciais, seria necessário validar o modelo com dados independentes e medir o custo de falsos positivos e falsos negativos.