"""Carregamento local e proveniência da base WineQT usada no projeto."""
from pathlib import Path

import pandas as pd

DATASET_FILENAME = "WineQT.csv"
DATASET_SOURCE = "Kaggle — YasserH, Wine Quality Dataset (arquivo WineQT.csv)"
DATASET_SOURCE_URL = "https://www.kaggle.com/datasets/yasserh/wine-quality-dataset"
UCI_REFERENCE_URL = "https://archive.ics.uci.edu/dataset/186/wine+quality"


def project_root() -> Path:
    """Retorna a raiz do projeto a partir deste arquivo em src/."""
    return Path(__file__).resolve().parents[1]


def load_wine_data(dataset_path: str | Path | None = None) -> pd.DataFrame:
    """Lê a cópia local do CSV; não baixa dados nem depende de caminho absoluto."""
    csv_path = Path(dataset_path) if dataset_path is not None else project_root() / "data" / DATASET_FILENAME
    if not csv_path.is_file():
        raise FileNotFoundError(
            f"Base não encontrada em: {csv_path}. "
            "Coloque WineQT.csv na pasta data/ do projeto. "
            f"Fonte: {DATASET_SOURCE_URL}"
        )
    return pd.read_csv(csv_path)
