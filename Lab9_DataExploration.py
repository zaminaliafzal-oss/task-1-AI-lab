# ============================================================
# Lab 9 Task: Data Loading & Exploration (Titanic Dataset)
# ============================================================
# Dataset: Titanic - https://www.kaggle.com/datasets/yasserh/titanic-dataset
# Download and place 'titanic.csv' in the same folder before running.

import pandas as pd
import numpy as np

# ── 1. Read CSV ───────────────────────────────────────────────
dataset = pd.read_csv('titanic.csv')

print("=" * 50)
print("         DATA LOADING & EXPLORATION")
print("=" * 50)

# ── 2. Top 5 rows ─────────────────────────────────────────────
print("\n[1] Top 5 rows:")
print(dataset.head())

# ── 3. Bottom 5 rows ──────────────────────────────────────────
print("\n[2] Bottom 5 rows:")
print(dataset.tail())

# ── 4. Number of Rows & Columns ───────────────────────────────
print("\n[3] Shape of Dataset:")
print(f"    Rows    : {dataset.shape[0]}")
print(f"    Columns : {dataset.shape[1]}")

# ── 5. All Null Columns ───────────────────────────────────────
print("\n[4] Null values per column:")
print(dataset.isnull().sum())

# ── 6. Fill null values using Mode ────────────────────────────
print("\n[5] Filling null values using Mode...")
dataset = dataset.fillna(dataset.mode().iloc[0])
print("    Null values after filling:")
print(dataset.isnull().sum())

# ── 7. Datatype of each column ────────────────────────────────
print("\n[6] Datatype of each column:")
print(dataset.dtypes)

print("\n" + "=" * 50)
print("        Exploration Complete!")
print("=" * 50)
