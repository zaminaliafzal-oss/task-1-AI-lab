# ============================================================
# Lab 10 Task: Data Pre-Processing
# ============================================================
# Continues from Lab 9 (uses same titanic.csv)

import pandas as pd
import numpy as np

# ── 1. Read CSV ───────────────────────────────────────────────
data = pd.read_csv('titanic.csv')

print("=" * 50)
print("           DATA PRE-PROCESSING")
print("=" * 50)

# ── 2. Shape ──────────────────────────────────────────────────
print(f"\n[1] Rows: {data.shape[0]}  |  Columns: {data.shape[1]}")

# ── 3. Check null values ──────────────────────────────────────
print("\n[2] Null values before processing:")
print(np.sum(pd.isnull(data)))

# ── 4. Check unique values of important columns ───────────────
print("\n[3] Unique values in 'Sex'    :", data['Sex'].unique())
print("    Unique values in 'Embarked':", data['Embarked'].unique())

# ── 5. Fill null values with Mode ─────────────────────────────
for col in data.columns:
    if data[col].isnull().sum() > 0:
        fill_val = data[col].mode()[0]
        data[col] = data[col].fillna(fill_val)
        print(f"\n[4] Filled '{col}' nulls with mode: {fill_val}")

print("\n    Null values after filling:")
print(data.isnull().sum())

# ── 6. Drop unnecessary columns ───────────────────────────────
cols_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin']
data.drop(columns=[c for c in cols_to_drop if c in data.columns], inplace=True)
print(f"\n[5] Dropped columns: {cols_to_drop}")

# ── 7. Type conversion ────────────────────────────────────────
print("\n[6] Datatypes before conversion:")
print(data.dtypes)

# ── 8. Check datatypes ────────────────────────────────────────
cat_columns = data.select_dtypes(['object']).columns
print(f"\n[7] Object (categorical) columns: {list(cat_columns)}")

# ── 9. Split X and Y ──────────────────────────────────────────
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Convert object columns to int using factorize
cat_x_cols = x.select_dtypes(['object']).columns
x[cat_x_cols] = x[cat_x_cols].apply(lambda col: pd.factorize(col)[0])

print(f"\n[8] Feature matrix (X) shape: {x.shape}")
print(f"    Target vector (Y) shape  : {y.shape}")
print("\n    X dtypes after encoding:")
print(x.dtypes)

print("\n" + "=" * 50)
print("       Pre-Processing Complete!")
print("=" * 50)
