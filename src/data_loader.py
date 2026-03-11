import os
import zipfile
from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATASET_REF = "benjaminawd/new-york-times-articles-comments-2020"


def download_dataset():
    cmd = f"kaggle datasets download -d {DATASET_REF} -p {DATA_DIR} --force"
    exit_code = os.system(cmd)
    if exit_code != 0:
        raise RuntimeError("Dataset download failed. Check Kaggle credentials.")

    zip_files = list(DATA_DIR.glob("*.zip"))
    if not zip_files:
        raise FileNotFoundError("No zip file found after download.")

    for zip_path in zip_files:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(DATA_DIR)


def find_csv_files():
    return list(DATA_DIR.rglob("*.csv"))


def load_first_csv():
    csv_files = find_csv_files()
    if not csv_files:
        raise FileNotFoundError("No CSV files found in data directory.")
    return pd.read_csv(csv_files[0])


def load_dataset():
    download_dataset()
    return load_first_csv()
